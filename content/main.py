# 메인 페이지 — 허브 역할. 모든 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
# 실제 오프라인 매장 주소가 없으므로 LocalBusiness 계열 Schema 대신 Organization 을 사용한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "분당구 전지역 방문 출장마사지·홈타이 예약 안내",
  "telephone": "{PHONE}",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "경기도 성남시 분당구"
  }},
  "contactPoint": {{
    "@type": "ContactPoint",
    "telephone": "{PHONE}",
    "contactType": "reservations",
    "areaServed": "KR",
    "availableLanguage": "Korean"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "분당구 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 분당동, 수내동, 정자동, 서현동, 야탑동, 판교동 등 대표 행정동 기준으로 확인할 수 있습니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "판교역이나 정자역 근처도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "판교역, 정자역, 서현역, 야탑역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "정자1동, 수내2동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "정자1·2·3동은 정자동, 수내1·2·3동은 수내동 페이지에서 통합 안내합니다. 같은 생활권을 잘게 나누면 비슷한 내용이 반복되어 이용자에게도 혼란스럽기 때문입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "당일 예약도 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "가능할 수 있지만 평일 저녁과 주말, 판교 업무지구 주변은 문의가 많을 수 있어 사전 예약을 권장합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "분당 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스로, 출장마사지와 같은 방문 관리의 한 형태입니다. 코스와 테마에 따라 구성이 달라집니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 분당구 전지역</p>
    <h1>분당 출장마사지 · 분당구 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 프리미엄 방문 관리.<br>자택·오피스텔·숙소 어디든 전화 한 통이면 예약이 끝납니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/courses/">코스 안내 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>12개</strong><span>대표 행정동</span></li>
      <li><strong>9개</strong><span>역세권 안내</span></li>
      <li><strong>14개</strong><span>관리 테마</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="service">
<h2>분당구에서 출장마사지를 찾는 이유</h2>
<p>분당 출장마사지를 찾는 분들은 대부분 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 분당구는 성남시 안에서도 주거지, 업무지구, 상권, 판교테크노밸리, 역세권이 함께 섞여 있는 지역입니다. 판교동과 삼평동은 판교 업무지구와 테크노밸리 수요가 많고, 정자동과 수내동은 주거지와 카페거리, 업무시설이 함께 있는 생활권입니다. 서현동과 야탑동은 분당 중심 상권과 대중교통 이용 수요가 강하고, 미금역·오리역 주변은 구미동과 금곡동 생활권을 함께 고려해야 합니다. 이 페이지는 분당구 전체 구조를 설명하는 허브 역할을 하며, 자세한 내용은 지역별·역세권별·테마별 안내에서 확인하실 수 있습니다.</p>
</section>

<section id="hometai">
<h2>분당 홈타이 이용 전 확인할 사항</h2>
<p>분당 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스입니다. 출장마사지와 같은 방문 관리의 한 형태로, 받으실 공간과 시간만 정해지면 이동 없이 편하게 받으실 수 있습니다. 이용 전에는 방문 가능 지역, 관리 가능 시간, 추가 이동비 여부, 결제 방식, 취소 기준, 서비스 범위를 먼저 확인해 주세요. 분당구는 같은 구 안에서도 판교 업무권, 서현·야탑 중심 상권, 정자·수내 주거권, 미금·오리 생활권의 이동 시간이 달라, 예약 전 위치와 희망 시간을 알려주시면 가능 여부를 정확히 안내해 드립니다.</p>
</section>

<section id="coverage">
<h2>분당구 전지역 방문 가능 안내</h2>
<p>분당구는 법정동과 행정동이 세분되어 있지만, 이 사이트는 대표 행정동 12곳을 중심으로 안내합니다. 수내1·2·3동은 수내동, 정자1·2·3동은 정자동, 서현1·2동은 서현동, 이매1·2동은 이매동, 야탑1·2·3동은 야탑동, 구미1동과 구미동은 구미동으로 통합합니다. 같은 생활권을 잘게 쪼개 비슷한 내용을 반복하기보다, 동 단위로 묶어 생활권 특징과 방문 조건을 한 번에 설명하는 편이 이용자에게도 정확하기 때문입니다. 방문 가능 여부는 행정동 경계가 아니라 실제 위치와 예약 시간으로 판단합니다.</p>
</section>

<section id="areas">
<h2>대표 행정동별 방문 가능 지역 안내</h2>
<p>대표 행정동 페이지에서는 해당 생활권의 특징, 가까운 역세권, 방문 전 확인사항, 예약 가능 시간, 어울리는 테마를 동마다 고유한 내용으로 설명합니다. 거주하시거나 머무시는 동을 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/bundang/bundang-dong-chuljangmassage/">분당동</a></li>
<li><a href="/bundang/sunae-dong-chuljangmassage/">수내동</a></li>
<li><a href="/bundang/jeongja-dong-chuljangmassage/">정자동</a></li>
<li><a href="/bundang/seohyeon-dong-chuljangmassage/">서현동</a></li>
<li><a href="/bundang/imae-dong-chuljangmassage/">이매동</a></li>
<li><a href="/bundang/yatap-dong-chuljangmassage/">야탑동</a></li>
<li><a href="/bundang/geumgok-dong-chuljangmassage/">금곡동</a></li>
<li><a href="/bundang/gumi-dong-chuljangmassage/">구미동</a></li>
<li><a href="/bundang/pangyo-dong-chuljangmassage/">판교동</a></li>
<li><a href="/bundang/sampyeong-dong-chuljangmassage/">삼평동</a></li>
<li><a href="/bundang/baekhyeon-dong-chuljangmassage/">백현동</a></li>
<li><a href="/bundang/unjung-dong-chuljangmassage/">운중동</a></li>
</ul>
<p>분당구 전체 구조가 궁금하시면 <a href="/bundang/">분당구 전체 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>판교역·정자역·서현역·야탑역 역세권 안내</h2>
<p>역세권 안내는 분당구를 지나는 신분당선, 수인분당선, 경강선, GTX-A 주요 역을 기준으로 구성합니다. 각 역 페이지에서는 인근 생활권, 주변 대표 동, 예약 가능 시간, 방문 전 준비사항을 설명하며, 출구별 페이지나 역과 테마를 조합한 페이지는 만들지 않습니다. 정자역, 미금역처럼 노선이 두 개인 환승역도 페이지는 하나로 운영합니다.</p>
<ul class="card-grid">
<li><a href="/bundang/pangyo-station-chuljangmassage/">판교역</a></li>
<li><a href="/bundang/seongnam-station-chuljangmassage/">성남역</a></li>
<li><a href="/bundang/jeongja-station-chuljangmassage/">정자역</a></li>
<li><a href="/bundang/migeum-station-chuljangmassage/">미금역</a></li>
<li><a href="/bundang/ori-station-chuljangmassage/">오리역</a></li>
<li><a href="/bundang/seohyeon-station-chuljangmassage/">서현역</a></li>
<li><a href="/bundang/sunae-station-chuljangmassage/">수내역</a></li>
<li><a href="/bundang/imae-station-chuljangmassage/">이매역</a></li>
<li><a href="/bundang/yatap-station-chuljangmassage/">야탑역</a></li>
</ul>
</section>

<section id="themes">
<h2>테마별 관리 안내</h2>
<p>테마별 안내에서는 관리 유형별 특징, 추천 대상, 예약 전 확인사항을 설명합니다. 테마는 각각 독립 페이지로 운영하며, 지역 페이지와 역 페이지에서는 관련 테마로 연결만 해 드립니다. 특정 역과 테마를 조합한 페이지는 운영하지 않으니, 원하시는 관리 유형을 먼저 고른 뒤 예약 시 위치를 알려주시면 됩니다.</p>
<ul class="card-grid">
<li><a href="/themes/swedish/">스웨디시</a></li>
<li><a href="/themes/lomilomi/">로미로미</a></li>
<li><a href="/themes/thai/">타이마사지</a></li>
<li><a href="/themes/chinese/">중국마사지</a></li>
<li><a href="/themes/aroma/">아로마테라피</a></li>
<li><a href="/themes/homecare/">홈케어</a></li>
<li><a href="/themes/hotel-style/">호텔식마사지</a></li>
<li><a href="/themes/foot/">발마사지</a></li>
<li><a href="/themes/sports/">스포츠·경락</a></li>
<li><a href="/themes/skincare/">스킨케어</a></li>
<li><a href="/themes/waxing/">왁싱</a></li>
<li><a href="/themes/couple/">커플 관리</a></li>
<li><a href="/themes/24hours/">24시간</a></li>
<li><a href="/themes/overnight/">수면 가능</a></li>
</ul>
</section>

<section id="course">
<h2>코스 선택 안내</h2>
<p>코스는 이용 목적과 그날의 컨디션에 따라 선택하시는 것이 좋습니다. 누적된 피로를 풀고 싶은 분, 편안한 휴식이 필요한 분, 운동 후 근육 이완이 필요한 분, 숙소로 방문을 원하시는 분, 커플이 함께 받고 싶은 분 등 상황에 맞는 선택 기준을 <a href="/courses/">코스안내</a> 페이지에서 자세히 다룹니다. 고민되시면 예약 전화에서 상태를 말씀해 주세요. 함께 정해 드립니다.</p>
</section>

<section id="how">
<h2>예약 전 꼭 확인해야 할 기준</h2>
<p>예약은 다섯 단계로 진행됩니다. 먼저 희망 지역 또는 역 인근 위치를 확인하고, 희망 시간을 확인한 뒤, 코스와 인원을 정하고, 방문 가능 여부를 안내받은 다음, 예약을 확정합니다. 특히 평일 저녁, 출퇴근 시간, 판교 업무지구 주변은 이동 상황에 따라 예약 가능 시간이 달라질 수 있으므로 한두 시간 이상 여유를 두고 예약하시기를 권장합니다. 자세한 절차는 <a href="/reservation/">예약안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>이용 전 확인사항</h2>
<p>원활한 방문 관리를 위해 정확한 주소, 공동현관 출입 방법, 주차 가능 여부, 조용한 공간 확보 여부를 미리 확인해 주시면 좋습니다. 숙소나 오피스텔로 방문을 요청하실 때는 건물 출입 안내와 예약 시간대 연락 가능 여부를 함께 알려주세요. 준비사항 전체는 <a href="/guide/">이용가이드</a>에 정리되어 있습니다.</p>
</section>

<section id="safety">
<h2>위생 및 안전 안내</h2>
<p>건전하고 안전한 방문 관리를 위해 위생 기준, 예약 정보 확인, 개인정보 보호, 금지행위 안내를 명확히 제공합니다. 과장된 표현, 허위 후기, 선정적인 문구 없이 이용 가능 지역, 예약 절차, 취소 기준, 개인정보 처리 기준, 고객 유의사항을 분명하게 안내드리며, 불법적이거나 무리한 요청은 어떤 경우에도 진행하지 않는다는 기준을 분명히 합니다. 예약 정보는 관리 목적 외에 사용하지 않습니다.</p>
</section>

<section id="faq">
<h2>분당 출장마사지 사이트 이용 가이드</h2>
<div class="faq-item">
<h3>분당구 전지역 방문이 가능한가요?</h3>
<p>예약 시간, 정확한 위치, 배정 상황에 따라 가능 여부가 달라집니다. 지역별 안내에서 분당동, 수내동, 정자동, 서현동, 야탑동, 판교동 등 대표 행정동 기준으로 확인할 수 있습니다.</p>
</div>
<div class="faq-item">
<h3>판교역이나 정자역 근처도 가능한가요?</h3>
<p>판교역, 정자역, 서현역, 야탑역 등 주요 역세권은 역 상세 페이지에서 주변 생활권과 함께 안내합니다. 정확한 가능 여부는 예약 시 위치를 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>정자1동, 수내2동은 왜 따로 없나요?</h3>
<p>정자1·2·3동은 정자동, 수내1·2·3동은 수내동 페이지에서 통합 안내합니다. 같은 생활권을 잘게 나누면 비슷한 내용이 반복되어 이용자에게도 혼란스럽기 때문입니다.</p>
</div>
<div class="faq-item">
<h3>당일 예약도 가능한가요?</h3>
<p>가능할 수 있지만 평일 저녁과 주말, 판교 업무지구 주변은 문의가 많을 수 있어 사전 예약을 권장합니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 어떻게 다른가요?</h3>
<p>분당 홈타이는 자택, 숙소, 사무실 인근에서 예약 가능 여부를 먼저 확인한 뒤 이용하는 방문형 관리 서비스로, 출장마사지와 같은 방문 관리의 한 형태입니다. 코스와 테마에 따라 구성이 달라집니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>분당구 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "분당 출장마사지｜분당구 홈타이 지역별 예약 안내",
    "desc": "분당 출장마사지·홈타이 예약 전 행정동, 역세권, 이용 기준을 정리했습니다.",
    "h1": "분당 출장마사지 · 분당구 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
