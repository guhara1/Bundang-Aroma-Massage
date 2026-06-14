#!/usr/bin/env python3
"""구글 Indexing API 색인 통보.

구글은 IndexNow 에 참여하지 않으므로, 즉시 통보가 필요하면 Indexing API 를 쓴다.

준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성 설정 → 사용자/권한에 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests

사용법:
  GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json \
    python3 tools/google_indexing.py <URL> [<URL> ...]
  # 인자가 없으면 sitemap.xml 전체를 URL_UPDATED 로 통보

주의: 구글 Indexing API 의 공식 지원 콘텐츠 타입은 JobPosting / BroadcastEvent 입니다.
일반 페이지 통보는 비공식적으로 동작할 수 있으나 색인을 보장하지 않습니다.
가장 확실한 방법은 Search Console 에 sitemap.xml 제출 + 우선 페이지는 URL 검사 도구로
'색인 요청' 입니다. 이 스크립트는 보조 수단입니다.
"""
import os
import re
import sys

try:
    import google.auth.transport.requests
    import requests
    from google.oauth2 import service_account
except ImportError:
    sys.exit("의존성이 필요합니다:  pip install google-auth requests")

SCOPES = ["https://www.googleapis.com/auth/indexing"]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"


def get_credentials():
    path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not path or not os.path.exists(path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 에 서비스 계정 JSON 경로를 지정하세요.")
    creds = service_account.Credentials.from_service_account_file(path, scopes=SCOPES)
    creds.refresh(google.auth.transport.requests.Request())
    return creds


def read_sitemap_urls():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 python3 build.py 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def main():
    urls = [a for a in sys.argv[1:] if not a.startswith("-")] or read_sitemap_urls()
    creds = get_credentials()
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json",
    }
    ok = 0
    for u in urls:
        r = requests.post(
            ENDPOINT, headers=headers,
            json={"url": u, "type": "URL_UPDATED"}, timeout=20,
        )
        flag = "OK" if r.status_code == 200 else "!!"
        if r.status_code == 200:
            ok += 1
        print(f"[{r.status_code}] {flag} {u}")
        if r.status_code != 200:
            print(f"      {r.text[:200]}")
    print(f"\n{ok}/{len(urls)} 통보 성공")


if __name__ == "__main__":
    main()
