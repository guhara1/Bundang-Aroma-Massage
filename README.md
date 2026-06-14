# 간다GO — 분당 출장마사지·홈타이 안내 사이트

경기도 성남시 분당구 전지역 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 메인 페이지 (+ Organization/FAQPage JSON-LD)
  areas.py          # 지역별: 분당구 허브 + 대표 행정동 12개
  stations.py       # 지하철역·철도역별: 허브 + 9개 역
  themes.py         # 테마별: 허브 + 14개 테마
  info.py           # 출장마사지 안내·코스·예약·가이드·후기·고객센터·약관
  magazine.py       # 매거진 허브 + 아티클
  about.py          # 운영자 소개 (E-E-A-T)
assets/             # CSS, 모바일 내비 JS, 파비콘·OG 이미지
```

## URL 구조

```
/                                              메인 (분당 출장마사지·홈타이)
/bundang/                                      지역 허브
/bundang/{동}-dong-chuljangmassage/            대표 행정동 12개
/bundang/stations/                             역 허브
/bundang/{역}-station-chuljangmassage/         지하철역·철도역 9개
/themes/{테마}/ /courses/ /reservation/ /guide/ /reviews/ /support/ /magazine/ /about/
```

대표 행정동(12): 분당동·수내동·정자동·서현동·이매동·야탑동·금곡동·구미동·판교동·삼평동·백현동·운중동
역(9): 판교역·성남역·정자역·미금역·오리역·서현역·수내역·이매역·야탑역

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 행정동은 대표 동 단위만 (수내1·2·3동 → 수내동 등) — 숫자 행정동 페이지 없음
- 역은 역 1개당 페이지 1개 — 환승역(정자역·미금역·판교역·성남역)도 URL 하나
- **지역+역+테마 조합 페이지 없음** (도어웨이 방지) — 테마는 독립 페이지로만 운영
- 메타 디스크립션은 **80자 이내** (네이버 기준)
- 실제 오프라인 매장 주소가 없으므로 LocalBusiness 계열 Schema 미사용 — Organization 사용
- 모든 페이지 본문은 페이지별 고유 작성 (지역명만 바꾼 복붙 없음)

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. 파비콘 PNG(`assets/favicon-16/32.png`, `apple-touch-icon.png`, `icon-192/512.png`)와
   `assets/og-image.png`를 **간다GO 브랜드(이니셜 G)** 기준으로 재생성
   (현재 `favicon.svg`만 G로 교체되어 있고 PNG·OG는 재생성 필요)
3. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
4. Google Search Console / 네이버 서치어드바이저에 `sitemap.xml` 제출
