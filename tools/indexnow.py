#!/usr/bin/env python3
"""IndexNow 색인 통보 — 빙(Bing)·네이버·얀덱스 등 IndexNow 참여 검색엔진에 URL을 즉시 통보.

외부 패키지가 필요 없습니다(표준 라이브러리만 사용).

사용법:
  python3 tools/indexnow.py                       # sitemap.xml 의 모든 URL 통보
  python3 tools/indexnow.py <URL> [<URL> ...]     # 특정 URL만 통보 (글 새로 올렸을 때)

예) 매거진 새 글 발행 후:
  python3 build.py
  python3 tools/indexnow.py https://bundang-aroma-massage.pages.dev/magazine/new-post/

키 파일(/{INDEXNOW_KEY}.txt)은 build.py 가 사이트 루트에 자동 생성합니다.
배포(Cloudflare Pages 등) 후 키 파일이 실제로 열리는지 먼저 확인하세요.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

BASE = BASE_URL.rstrip("/")
HOST = urllib.parse.urlparse(BASE).netloc
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

# IndexNow 는 한 엔드포인트에 보내면 참여 검색엔진끼리 공유하지만,
# 네이버 도달을 확실히 하기 위해 공용 + 네이버 엔드포인트에 함께 보낸다.
ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://www.bing.com/indexnow",
]


def read_sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def submit(urls):
    payload = json.dumps(
        {
            "host": HOST,
            "key": INDEXNOW_KEY,
            "keyLocation": KEY_LOCATION,
            "urlList": urls,
        }
    ).encode("utf-8")
    for ep in ENDPOINTS:
        req = urllib.request.Request(
            ep, data=payload,
            headers={"Content-Type": "application/json; charset=utf-8"},
        )
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                print(f"[{r.status}] {ep}  ({len(urls)} URLs)")
        except urllib.error.HTTPError as e:
            # 200/202 외에도 일부 엔드포인트는 4xx 로 정책 안내를 주기도 한다.
            print(f"[{e.code}] {ep}  {e.read()[:200]!r}")
        except Exception as e:  # noqa: BLE001
            print(f"[ERR] {ep}  {e}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    urls = args if args else read_sitemap_urls()
    if not urls:
        sys.exit("통보할 URL이 없습니다.")
    if "example" in HOST:
        print("주의: BASE_URL 이 아직 예시 도메인입니다. content/site.py 를 확인하세요.")
    print(f"host={HOST}  key={INDEXNOW_KEY[:8]}…  urls={len(urls)}")
    submit(urls)
