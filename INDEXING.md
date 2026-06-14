# 색인(인덱싱) 가이드 — 네이버·구글·빙 빠르게 노출시키기

이 사이트는 색인 속도를 높이기 위한 요소가 빌드에 모두 포함되어 있습니다.

| 요소 | 위치 | 역할 |
|------|------|------|
| `sitemap.xml` | `/sitemap.xml` | 색인 페이지 목록 + `lastmod`(신선도 신호) |
| RSS 피드 | `/feed.xml` | 매거진 신규 글 발견 속도 향상 (네이버·구글) |
| `robots.txt` | `/robots.txt` | 전체 허용 + sitemap 위치 고지 |
| IndexNow 키 | `/{KEY}.txt` | 빙·네이버에 소유권 증명 (즉시 통보용) |
| 네이버 인증 | 메인 `<head>` | 네이버 서치어드바이저 사이트 등록 |
| RSS 자동 발견 | 전 페이지 `<head>` | `<link rel="alternate" type="application/rss+xml">` |

빌드하면 위 파일이 모두 자동 생성됩니다.

```bash
python3 build.py
```

> **도메인**: `content/site.py` 의 `BASE_URL` 이 실제 배포 도메인이어야 sitemap·canonical·
> IndexNow keyLocation 이 맞습니다. 현재 값: `https://bundang-aroma-massage.pages.dev`
> (커스텀 도메인 연결 시 이 값을 바꾸고 재빌드 → 재배포)

---

## 1. 최초 1회 — 검색엔진에 사이트 등록

### 네이버 서치어드바이저 (https://searchadvisor.naver.com)
1. 사이트 등록 → 도메인 입력
2. 소유 확인: **HTML 태그** 방식 선택 → 이미 메인 `<head>` 에 인증 메타가 들어 있으므로 바로 확인됨
   (`<meta name="naver-site-verification" content="772…" />`)
3. 요청 → 사이트맵 제출 → `sitemap.xml`
4. 요청 → RSS 제출 → `feed.xml`

### 구글 Search Console (https://search.google.com/search-console)
1. 속성 추가 → URL 접두어 → 도메인 입력
2. 소유 확인(HTML 파일 또는 DNS). Cloudflare Pages면 DNS(TXT)가 편함
3. Sitemaps → `sitemap.xml` 제출
4. 우선 노출할 페이지는 **URL 검사 → 색인 생성 요청**

### 빙 웹마스터도구 (https://www.bing.com/webmasters)
- 구글 Search Console 연동으로 한 번에 가져오기 가능. IndexNow가 자동 연결됩니다.

---

## 2. 글 올릴 때마다 — 즉시 색인 통보 (IndexNow)

빙·네이버·얀덱스는 **IndexNow** 로 즉시 통보를 받습니다. 외부 패키지 불필요.

```bash
# 1) 빌드 (sitemap·feed·키파일 갱신)
python3 build.py

# 2) 새 글 URL만 통보 (권장)
python3 tools/indexnow.py https://bundang-aroma-massage.pages.dev/magazine/new-post/

# 또는 sitemap 전체 통보 (인자 없이)
python3 tools/indexnow.py
```

`tools/indexnow.py` 는 공용 엔드포인트 + 네이버 + 빙에 동시에 보냅니다.
**키 파일(`/{KEY}.txt`)이 실제 도메인에서 열려야** 통보가 수락됩니다 — 배포 후 실행하세요.

---

## 3. (선택) 구글 즉시 통보 — Indexing API

구글은 IndexNow 미참여라 즉시 통보가 필요하면 Indexing API를 씁니다.

```bash
pip install google-auth requests
GOOGLE_APPLICATION_CREDENTIALS=/path/service-account.json \
  python3 tools/google_indexing.py https://bundang-aroma-massage.pages.dev/magazine/new-post/
```

준비: Cloud 프로젝트에서 Indexing API 사용 설정 → 서비스 계정 JSON 발급 →
Search Console 속성에 서비스 계정 이메일을 **소유자**로 추가.

> 참고: 구글 Indexing API의 공식 지원 타입은 JobPosting/BroadcastEvent입니다. 일반 페이지
> 통보도 동작하는 경우가 많지만 색인을 보장하진 않습니다. **가장 확실한 건 Search Console
> sitemap 제출 + URL 검사 색인 요청**이고, 이 API는 보조 수단입니다.

---

## 4. sitemap ping은 왜 안 쓰나요?

`google.com/ping?sitemap=` / 빙 sitemap ping 엔드포인트는 **2023년에 모두 폐지**되었습니다.
지금은 효과가 없으므로 이 저장소에는 넣지 않았습니다. 대신:

- 빙·네이버 → **IndexNow** (`tools/indexnow.py`)
- 구글 → **Search Console sitemap 제출 + URL 검사**(필요 시 Indexing API)

가 현재 가장 빠른 정공법입니다.

---

## 5. 배포 후 체크리스트

- [ ] `https://<도메인>/{KEY}.txt` 가 열리고 내용이 키와 동일한가
- [ ] `https://<도메인>/sitemap.xml`, `/feed.xml`, `/robots.txt` 가 정상 노출되는가
- [ ] 네이버·구글에 sitemap 제출 완료
- [ ] 새 글 발행 절차에 `python3 tools/indexnow.py <URL>` 를 포함
