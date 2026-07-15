import streamlit as st

# ==========================================
# 기본 설정
# ==========================================

st.set_page_config(
    page_title="진로메타버스 | 작업치료학과",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# CSS
# ==========================================

st.markdown("""
<style>

/* ------------------------------
   전체 배경
------------------------------ */

.stApp{
background:
linear-gradient(
135deg,
#EAF8FF 0%,
#D8F2FF 35%,
#F5FCFF 70%,
#FFFFFF 100%
);
}

/* 화면 여백 */

.block-container{
max-width:1100px;
padding-top:2rem;
padding-bottom:2rem;
}

/* 제목 */

.main-title{

font-size:68px;

font-weight:900;

color:#0077B6;

text-align:center;

letter-spacing:-2px;

margin-bottom:5px;

line-height:1.3;

}


/* 부제목 */

.sub-title{

text-align:center;

font-size:24px;

color:#118AB2;

font-weight:600;

margin-bottom:35px;

}


/* 정보 카드 */

.info-card{

background:rgba(255,255,255,.78);

backdrop-filter:blur(14px);

border-radius:24px;

padding:28px;

text-align:center;

box-shadow:
0 15px 35px rgba(0,119,182,.12);

border:1px solid rgba(255,255,255,.8);

transition:.3s;

height:170px;

}


.info-card:hover{

transform:translateY(-6px);

box-shadow:
0 20px 40px rgba(0,119,182,.18);

}


.info-card h2{

color:#0077B6;

margin-bottom:8px;

}


.info-card p{

font-size:18px;

color:#555;

}


/* 아코디언 */

div[data-testid="stExpander"]{

background:white;

border-radius:22px;

border:none;

box-shadow:
0 12px 28px rgba(0,0,0,.08);

margin-bottom:18px;

overflow:hidden;

}


/* 버튼 */

.stButton>button{

background:#0096C7;

color:white;

font-weight:bold;

border:none;

border-radius:30px;

padding:12px 30px;

transition:.3s;

}


.stButton>button:hover{

background:#0077B6;

transform:scale(1.05);

}


/* metric */

div[data-testid="metric-container"]{

background:white;

padding:18px;

border-radius:20px;

box-shadow:
0 10px 20px rgba(0,0,0,.08);

}


/* 안내창 */

.stAlert{

border-radius:18px;

}

</style>

""",unsafe_allow_html=True)

# ==========================================
# 메인 화면
# ==========================================

st.markdown("""
<div class="main-title">
🌐 진로메타버스
</div>

<div class="sub-title">
Occupational Therapy Career Explorer
</div>
""",unsafe_allow_html=True)

st.info(
"""
💙 작업치료학과의 다양한 진로와 역할을 탐색해보세요.
아래의 카드를 확인한 후, 각 항목을 펼쳐 자세한 내용을 살펴볼 수 있습니다.
"""
)

# ==========================================
# 요약 정보
# ==========================================

col1,col2,col3,col4=st.columns(4)

with col1:
    st.metric(
        "진출 분야",
        "10+"
    )

with col2:
    st.metric(
        "치료 대상",
        "전 연령"
    )

with col3:
    st.metric(
        "국가자격",
        "면허 취득"
    )

with col4:
    st.metric(
        "미래 전망",
        "★★★★★"
    )

st.divider()
# =========================================================
# 1-2 : 메인 소개 + 작업치료란
# (1-1 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<div style="
background:rgba(255,255,255,0.75);
backdrop-filter:blur(15px);
padding:35px;
border-radius:28px;
box-shadow:0 15px 35px rgba(0,119,182,.12);
margin-bottom:25px;
">

<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:10px;
">
🧠 작업치료학과 진로 탐색
</h2>

<p style="
font-size:18px;
text-align:center;
line-height:1.9;
color:#555;
">

작업치료는 단순히 질병을 치료하는 것이 아니라,
사람이 다시 자신의 일상으로 돌아갈 수 있도록 돕는
보건의료 전문 분야입니다.

<br><br>

이 웹사이트에서는

<br>

✔ 작업치료란 무엇인지

✔ 대학에서 무엇을 배우는지

✔ 졸업 후 어디로 진출하는지

✔ 작업치료사의 전망과 필요한 역량

을 쉽고 재미있게 알아볼 수 있습니다.

</p>

</div>
""", unsafe_allow_html=True)


st.divider()


# =========================================================
# 작업치료란?
# =========================================================

with st.expander("🩺 작업치료란 무엇일까요?"):

    st.markdown("""
### 작업치료(Occupational Therapy)

작업치료는 질병, 사고, 장애, 발달 문제 또는 노화 등으로 인해
일상생활 수행에 어려움을 겪는 사람을 돕는 보건의료 전문 분야입니다.

여기서 말하는 **작업(Occupation)** 은
직업만 의미하는 것이 아니라
사람이 살아가면서 하는 모든 의미 있는 활동을 말합니다.

예를 들면

- 🍚 식사하기
- 👕 옷 입기
- 🏫 학교생활
- 📖 공부하기
- ✍ 글쓰기
- 🪥 양치하기
- 🚶 걷기
- 🎨 취미생활
- 🤝 사회활동

등이 모두 작업에 해당합니다.

작업치료사는 이러한 활동을
다시 스스로 할 수 있도록
평가하고 치료를 제공합니다.
""")

    st.success(
        "💙 목표 : 대상자가 의미 있는 일상생활을 독립적으로 수행하도록 돕는 것"
    )


st.divider()


# =========================================================
# 왜 중요한 직업일까?
# =========================================================

with st.expander("💡 왜 작업치료사가 필요할까요?"):

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 🎯 작업치료가 필요한 이유

✔ 사고 후 재활

✔ 뇌졸중 재활

✔ 치매 예방

✔ 발달지연 치료

✔ 정신건강 회복

✔ 일상생활 훈련
""")

    with col2:

        st.markdown("""
### 🌱 작업치료의 목표

✔ 신체 기능 향상

✔ 인지 기능 향상

✔ 사회 참여

✔ 학교생활 적응

✔ 직업 복귀

✔ 삶의 질 향상
""")

    st.info("""
작업치료는 단순히 기능을 회복시키는 것이 아니라,
대상자가 자신에게 의미 있는 삶을 살아갈 수 있도록
도와주는 것이 가장 큰 목표입니다.
""")
# =========================================================
# 1-3 : 작업치료가 필요한 대상
# (1-2 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:25px;
">
👥 작업치료는 누구에게 필요할까요?
</h2>
""", unsafe_allow_html=True)


st.markdown("""
<p style="
text-align:center;
font-size:18px;
color:#555;
line-height:1.8;
margin-bottom:30px;
">
작업치료는 특정 연령만을 위한 치료가 아닙니다.
영유아부터 노인까지, 일상생활에 어려움을 겪는 모든 사람에게 필요한 전문 재활 분야입니다.
</p>
""", unsafe_allow_html=True)


# =========================================================
# 대상별 탭
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs(
[
"👶 아동",
"🧑 성인",
"👵 노인",
"😊 정신건강"
]
)

# ---------------------------------------------------------
# 아동
# ---------------------------------------------------------

with tab1:

    st.markdown("""
### 👶 아동 작업치료

아동 작업치료는 성장과 발달 과정에서 어려움을 겪는 아이들이
학교와 가정에서 더욱 독립적으로 생활할 수 있도록 돕습니다.
""")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
#### ✔ 주요 대상

- 발달지연
- ADHD
- 자폐스펙트럼장애
- 뇌성마비
- 감각처리 어려움
""")

    with col2:

        st.markdown("""
#### 🎯 목표

- 감각 발달
- 집중력 향상
- 소근육 기능 향상
- 학교생활 적응
- 사회성 발달
""")

    st.success("놀이와 다양한 활동을 활용하여 아이들이 즐겁게 치료를 받을 수 있도록 합니다.")

# ---------------------------------------------------------
# 성인
# ---------------------------------------------------------

with tab2:

    st.markdown("""
### 🧑 성인 작업치료

질병이나 사고 이후 일상생활을 다시 할 수 있도록
재활 프로그램을 진행합니다.
""")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
#### ✔ 주요 대상

- 뇌졸중
- 척수손상
- 외상성 뇌손상
- 손 기능 손상
- 산업재해
""")

    with col2:

        st.markdown("""
#### 🎯 목표

- 일상생활 복귀
- 직업 복귀
- 손 기능 회복
- 인지 기능 향상
- 독립적인 생활
""")

    st.success("환자가 다시 자신의 생활을 스스로 할 수 있도록 지원합니다.")

# ---------------------------------------------------------
# 노인
# ---------------------------------------------------------

with tab3:

    st.markdown("""
### 👵 노인 작업치료

고령화 사회에서 작업치료사의 역할은 점점 더 중요해지고 있습니다.
""")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
#### ✔ 주요 대상

- 치매
- 파킨슨병
- 낙상 위험
- 노인성 질환
- 관절 질환
""")

    with col2:

        st.markdown("""
#### 🎯 목표

- 인지 기능 유지
- 치매 예방
- 낙상 예방
- 일상생활 유지
- 삶의 질 향상
""")

    st.success("노인의 건강한 생활과 지역사회 참여를 지원합니다.")

# ---------------------------------------------------------
# 정신건강
# ---------------------------------------------------------

with tab4:

    st.markdown("""
### 😊 정신건강 작업치료

정신건강 문제로 인해 사회생활에 어려움을 겪는 사람들이
자신의 삶을 회복하도록 돕습니다.
""")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
#### ✔ 주요 대상

- 우울증
- 조현병
- 불안장애
- 양극성장애
""")

    with col2:

        st.markdown("""
#### 🎯 목표

- 사회 적응
- 대인관계 향상
- 일상생활 회복
- 자립 능력 향상
""")

    st.success("대상자가 지역사회에서 건강하게 생활할 수 있도록 지원합니다.")


st.divider()

st.markdown("""
<div style="
background:rgba(255,255,255,0.8);
padding:30px;
border-radius:25px;
box-shadow:0 10px 30px rgba(0,119,182,.10);
text-align:center;
">

<h3 style="color:#0077B6;">
💙 작업치료의 핵심 가치
</h3>

<p style="
font-size:18px;
line-height:1.8;
color:#555;
">

작업치료는 질병만 치료하는 것이 아니라,
사람이 다시 자신이 원하는 삶을 살아갈 수 있도록
의미 있는 활동을 통해 회복을 돕는 전문 분야입니다.

</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# =========================================================
# 2-1 : 작업치료학과에서 배우는 과목
# (1-3 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
📚 작업치료학과에서는 무엇을 배울까?
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:18px;
line-height:1.8;
color:#555;
margin-bottom:35px;
">
작업치료학과에서는 사람의 신체와 마음을 이해하는 기초 의학부터
실제 치료를 위한 전문 지식까지 다양한 내용을 배웁니다.
이론뿐 아니라 실습을 통해 실제 현장에서 필요한 능력을 키우게 됩니다.
</p>
""", unsafe_allow_html=True)

# =========================================================
# 1학년
# =========================================================

with st.expander("🎓 1학년 - 기초를 배우는 시기", expanded=False):

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
### 📖 주요 과목

- 해부학
- 생리학
- 의학용어
- 인간발달
- 작업치료개론
""")

    with c2:

        st.markdown("""
### 💡 배우는 내용

✔ 사람의 몸 구조 이해

✔ 근육과 뼈의 기능

✔ 신경계의 기본 원리

✔ 작업치료의 개념

✔ 의료인의 기본 소양
""")

    st.success("기초 의학 지식을 배우며 작업치료사의 기본기를 갖추게 됩니다.")

# =========================================================
# 2학년
# =========================================================

with st.expander("🧠 2학년 - 전공 심화", expanded=False):

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
### 📖 주요 과목

- 운동학
- 신경과학
- 평가학
- 감각통합
- 인지재활
""")

    with c2:

        st.markdown("""
### 💡 배우는 내용

✔ 움직임 분석

✔ 인지 기능 평가

✔ 감각 기능 이해

✔ 치료 계획 수립

✔ 다양한 평가 방법
""")

    st.info("환자의 상태를 평가하고 적절한 치료 방법을 계획하는 능력을 기릅니다.")

# =========================================================
# 3~4학년
# =========================================================

with st.expander("🏥 3~4학년 - 임상실습", expanded=False):

    c1, c2 = st.columns(2)

    with c1:

        st.markdown("""
### 📖 주요 활동

- 병원 실습
- 재활 프로그램 참여
- 사례 연구
- 치료 계획 작성
- 국가시험 준비
""")

    with c2:

        st.markdown("""
### 💡 배우는 내용

✔ 실제 환자 치료

✔ 의료진과 협업

✔ 의사소통 능력

✔ 임상 판단 능력

✔ 전문 치료기술
""")

    st.success("학교에서 배운 내용을 실제 의료기관에서 적용하며 경험을 쌓게 됩니다.")

st.divider()

# =========================================================
# 핵심 역량 카드
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:25px;
">
✨ 학과에서 키우는 핵심 역량
</h2>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="info-card">

<h2>🧠 전문지식</h2>

<p>

인체 구조와 기능을 이해하고
치료에 활용하는 능력

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="info-card">

<h2>🤝 의사소통</h2>

<p>

대상자와 보호자,
의료진과 협력하는 능력

</p>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="info-card">

<h2>💡 문제해결</h2>

<p>

대상자에게 맞는
치료 방법을 계획하는 능력

</p>

</div>
""", unsafe_allow_html=True)

st.divider()
# =========================================================
# 2-2 : 작업치료사는 어떤 일을 할까?
# (2-1 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
❤️ 작업치료사는 어떤 일을 할까요?
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:18px;
line-height:1.8;
color:#555;
margin-bottom:35px;
">
작업치료사는 대상자의 신체 기능뿐만 아니라
인지, 감각, 정서, 사회 참여 능력까지 종합적으로 평가하여
일상생활을 독립적으로 수행할 수 있도록 돕습니다.
</p>
""", unsafe_allow_html=True)

# =========================================================
# 역할 카드
# =========================================================

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="info-card">

<h2>🔍 평가(Evaluation)</h2>

<p>

✔ 신체 기능 평가<br>

✔ 손 기능 평가<br>

✔ 인지 기능 평가<br>

✔ 감각 기능 평가<br>

✔ 일상생활 수행능력 평가

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="info-card">

<h2>📝 치료계획</h2>

<p>

✔ 목표 설정<br>

✔ 맞춤형 프로그램 구성<br>

✔ 보호자 상담<br>

✔ 치료 일정 계획<br>

✔ 치료 효과 확인

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col3, col4 = st.columns(2)

with col3:

    st.markdown("""
<div class="info-card">

<h2>🧩 치료</h2>

<p>

✔ 감각통합치료<br>

✔ 인지재활<br>

✔ 일상생활훈련<br>

✔ 손 기능 훈련<br>

✔ 상지 기능 향상

</p>

</div>
""", unsafe_allow_html=True)

with col4:

    st.markdown("""
<div class="info-card">

<h2>🤝 사회 복귀 지원</h2>

<p>

✔ 학교생활 적응<br>

✔ 직업 복귀<br>

✔ 지역사회 적응<br>

✔ 보조기기 활용<br>

✔ 삶의 질 향상

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# 실제 치료 예시
# =========================================================

with st.expander("🩺 실제 작업치료 사례 보기"):

    tab1, tab2, tab3 = st.tabs([
        "👶 아동",
        "🧑 성인",
        "👵 노인"
    ])

    with tab1:

        st.markdown("""
### 👶 아동

대상 : 발달지연 아동

치료

- 블록 놀이
- 가위질
- 그림 그리기
- 균형 활동
- 감각 놀이

목표

✔ 집중력 향상

✔ 소근육 발달

✔ 학교생활 적응
""")

    with tab2:

        st.markdown("""
### 🧑 성인

대상 : 뇌졸중 환자

치료

- 손 기능 훈련
- 옷 입기 연습
- 식사 훈련
- 보행 보조
- 인지 훈련

목표

✔ 일상생활 독립

✔ 직업 복귀

✔ 기능 회복
""")

    with tab3:

        st.markdown("""
### 👵 노인

대상 : 치매 환자

치료

- 기억력 활동
- 퍼즐
- 미술 활동
- 음악 활동
- 생활훈련

목표

✔ 인지 기능 유지

✔ 치매 예방

✔ 사회 참여
""")

st.success(
"💙 작업치료의 가장 큰 목표는 대상자가 '다시 자신의 일상으로 돌아갈 수 있도록 돕는 것'입니다."
)

st.divider()
# =========================================================
# 2-3 : 작업치료학과 졸업 후 진로
# (2-2 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
💼 작업치료학과 졸업 후 진로
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:18px;
line-height:1.8;
color:#555;
margin-bottom:35px;
">
많은 사람들이 작업치료사는 병원에서만 근무한다고 생각하지만,
실제로는 의료기관뿐 아니라 공공기관과 지역사회 기관 등
다양한 분야에서 활동할 수 있습니다.
</p>
""", unsafe_allow_html=True)

# =========================================================
# 진출 분야 카드
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="info-card">

<h2>🏥 병원</h2>

<p>

대학병원<br>
종합병원<br>
재활병원<br>
요양병원<br>
어린이병원

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="info-card">

<h2>🏛 공공기관</h2>

<p>

국민건강보험공단<br>
건강보험심사평가원<br>
근로복지공단

</p>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="info-card">

<h2>🏠 지역사회</h2>

<p>

보건소<br>
치매안심센터<br>
정신건강복지센터

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
<div class="info-card">

<h2>👶 아동 분야</h2>

<p>

아동발달센터<br>
특수학교<br>
특수교육지원센터

</p>

</div>
""", unsafe_allow_html=True)

with col5:

    st.markdown("""
<div class="info-card">

<h2>♿ 복지 분야</h2>

<p>

장애인복지관<br>
노인복지관<br>
주간보호센터

</p>

</div>
""", unsafe_allow_html=True)

with col6:

    st.markdown("""
<div class="info-card">

<h2>🦾 기타 분야</h2>

<p>

보조공학센터<br>
의료기기 회사<br>
연구기관

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# 분야별 설명
# =========================================================

with st.expander("🔍 진출 분야 자세히 보기", expanded=False):

    career = st.selectbox(
        "관심 있는 분야를 선택하세요.",
        [
            "선택하세요",
            "🏥 병원",
            "🏛 공공기관",
            "🏠 보건소 · 치매안심센터",
            "👶 아동발달센터",
            "🦾 보조공학센터"
        ]
    )

    if career == "🏥 병원":

        st.success("""
### 🏥 병원

주요 업무

✔ 환자 평가

✔ 일상생활훈련

✔ 손 기능 회복

✔ 인지재활

✔ 퇴원 후 생활 지도

병원은 가장 많은 작업치료사가 근무하는 분야입니다.
""")

    elif career == "🏛 공공기관":

        st.success("""
### 🏛 공공기관

대표 기관

• 국민건강보험공단

• 건강보험심사평가원

• 근로복지공단

건강관리와 재활사업,
국민 건강 증진을 위한 업무에 참여할 수 있습니다.
""")

    elif career == "🏠 보건소 · 치매안심센터":

        st.success("""
### 🏠 보건소 · 치매안심센터

주요 업무

✔ 치매 예방 프로그램

✔ 인지훈련

✔ 지역사회 건강관리

✔ 건강교육

고령화 사회에서 역할이 더욱 확대되고 있습니다.
""")

    elif career == "👶 아동발달센터":

        st.success("""
### 👶 아동발달센터

주요 업무

✔ 감각통합치료

✔ 발달평가

✔ 놀이치료 활동

✔ 학교생활 적응 지원

아동의 성장과 발달을 돕는 중요한 분야입니다.
""")

    elif career == "🦾 보조공학센터":

        st.success("""
### 🦾 보조공학센터

주요 업무

✔ 휠체어 평가

✔ 보조기기 상담

✔ 환경 개선

✔ 독립적인 생활 지원

보조공학은 앞으로 더욱 성장할 분야 중 하나입니다.
""")

st.info(
"""
💙 작업치료사는 병원뿐 아니라 공공기관, 지역사회, 복지기관 등
다양한 환경에서 사람들의 건강한 삶을 지원하는 전문가입니다.
"""
)

st.divider()
# =========================================================
# 3-1 : 작업치료사에게 필요한 역량 + 미래 전망
# (2-3 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
⭐ 작업치료사에게 필요한 역량
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:18px;
line-height:1.8;
color:#555;
margin-bottom:35px;
">
작업치료사는 사람을 대상으로 하는 전문직입니다.
따라서 의학적 지식뿐 아니라 대상자의 입장을 이해하고
함께 소통하는 능력도 매우 중요합니다.
</p>
""", unsafe_allow_html=True)

# =========================================================
# 역량 카드
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
<div class="info-card">

<h2>💙 공감 능력</h2>

<p>

대상자의 어려움을
이해하고 배려하는 마음

</p>

</div>
""", unsafe_allow_html=True)

with col2:

    st.markdown("""
<div class="info-card">

<h2>🗣 의사소통</h2>

<p>

환자와 보호자,
의료진과 협력하는 능력

</p>

</div>
""", unsafe_allow_html=True)

with col3:

    st.markdown("""
<div class="info-card">

<h2>🧠 전문지식</h2>

<p>

해부학, 생리학,
재활치료 지식 활용

</p>

</div>
""", unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:

    st.markdown("""
<div class="info-card">

<h2>👀 관찰력</h2>

<p>

대상자의 작은 변화도
세심하게 확인하는 능력

</p>

</div>
""", unsafe_allow_html=True)

with col5:

    st.markdown("""
<div class="info-card">

<h2>💡 문제 해결</h2>

<p>

상황에 맞는 치료를
계획하는 능력

</p>

</div>
""", unsafe_allow_html=True)

with col6:

    st.markdown("""
<div class="info-card">

<h2>🤝 책임감</h2>

<p>

꾸준하게 치료를
진행하는 자세

</p>

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# 전망
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:25px;
">
📈 작업치료사의 미래 전망
</h2>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 📊 수요가 증가하는 이유

✔ 고령화 사회

✔ 치매 환자 증가

✔ 재활의료 확대

✔ 장애인 복지 확대

✔ 건강에 대한 관심 증가

✔ 지역사회 돌봄 서비스 확대
""")

with col2:

    st.markdown("""
### 🌱 앞으로의 변화

✔ 방문 재활 증가

✔ 공공기관 진출 확대

✔ 보조공학 발전

✔ 디지털 재활 기술 활용

✔ 예방 중심 치료 확대

✔ 다양한 전문 분야로 진출 가능
""")

st.success("""
앞으로 작업치료사는 병원뿐 아니라
보건소, 치매안심센터, 국민건강보험공단 등
지역사회와 공공기관에서도 더욱 중요한 역할을 하게 될 것으로 기대됩니다.
""")

# =========================================================
# 작업치료사가 되는 과정
# =========================================================

with st.expander("🎓 작업치료사가 되는 과정", expanded=False):

    st.markdown("""
### ① 작업치료학과 진학

⬇️

### ② 전공 수업 및 임상실습

⬇️

### ③ 작업치료사 국가시험 응시

⬇️

### ④ 국가시험 합격 후 면허 취득

⬇️

### ⑤ 병원 · 보건소 · 치매안심센터 · 국민건강보험공단 등 다양한 기관으로 진출

""")

st.divider()
# =========================================================
# 3-2 : 나에게 맞는 작업치료 진로 찾기 + 작업치료 상식
# (3-1 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
🧩 나에게 맞는 작업치료 분야 찾기
</h2>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
font-size:18px;
line-height:1.8;
color:#555;
margin-bottom:35px;
">
관심 있는 분야를 선택하면
어울리는 작업치료 분야를 추천해드립니다.
</p>
""", unsafe_allow_html=True)

interest = st.selectbox(
    "관심 분야를 선택하세요.",
    [
        "선택하세요",
        "👶 아이들과 함께하는 일",
        "👵 노인의 건강을 돕는 일",
        "🏥 병원에서 재활치료",
        "🏛 공공기관에서 건강관리",
        "🦾 보조공학 및 재활기기",
        "😊 정신건강 지원"
    ],
    index=0
)

# 처음에는 아무 결과도 표시되지 않음
if interest != "선택하세요":

    if interest == "👶 아이들과 함께하는 일":

        st.success("""
### 👶 추천 분야

🏫 아동발달센터

🏫 특수학교

🏫 특수교육지원센터

발달지연이나 감각처리에 어려움이 있는 아동의 성장과 학교생활을 지원합니다.
""")

    elif interest == "👵 노인의 건강을 돕는 일":

        st.success("""
### 👵 추천 분야

🏠 치매안심센터

🏠 노인복지관

🏠 보건소

치매 예방 프로그램과 인지활동을 통해 건강한 노후를 지원합니다.
""")

    elif interest == "🏥 병원에서 재활치료":

        st.success("""
### 🏥 추천 분야

✔ 대학병원

✔ 종합병원

✔ 재활병원

뇌졸중, 척수손상, 골절 등 다양한 환자의 일상생활 회복을 돕습니다.
""")

    elif interest == "🏛 공공기관에서 건강관리":

        st.success("""
### 🏛 추천 분야

✔ 국민건강보험공단

✔ 건강보험심사평가원

✔ 보건소

국민 건강 증진과 재활 관련 사업에 참여할 수 있습니다.
""")

    elif interest == "🦾 보조공학 및 재활기기":

        st.success("""
### 🦾 추천 분야

✔ 보조공학센터

✔ 의료기기 회사

✔ 재활공학 분야

보조기기를 활용하여 장애인의 독립적인 생활을 지원합니다.
""")

    elif interest == "😊 정신건강 지원":

        st.success("""
### 😊 추천 분야

✔ 정신건강복지센터

✔ 정신재활시설

정신질환 대상자의 사회 적응과 일상생활을 지원합니다.
""")

st.divider()

# =========================================================
# 작업치료 상식
# =========================================================

with st.expander("💡 알아두면 좋은 작업치료 상식", expanded=False):

    st.markdown("""
### ✔ 작업치료는 언제 시작되었을까요?

작업치료는 제1차 세계대전 이후
재활의 중요성이 커지면서 전문 분야로 발전했습니다.

---

### ✔ 작업치료사는 누구를 치료할까요?

영유아부터 노인까지,
연령과 관계없이 도움이 필요한 사람이라면 누구나 대상이 될 수 있습니다.

---

### ✔ 병원에서만 근무하나요?

아닙니다.

병원뿐 아니라

• 국민건강보험공단

• 보건소

• 치매안심센터

• 아동발달센터

• 정신건강복지센터

• 장애인복지관

등 다양한 기관에서 근무할 수 있습니다.

---

### ✔ 작업치료와 물리치료의 차이

🩺 물리치료

→ 통증 감소와 운동 기능 회복 중심

🧠 작업치료

→ 일상생활 수행과 학교·직장·사회생활 복귀를 중심으로 치료
""")

st.divider()
# =========================================================
# 3-3 : Q&A + 마무리
# (3-2 바로 아래에 이어서 붙여 넣기)
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:30px;
">
❓ 자주 묻는 질문 (Q&A)
</h2>
""", unsafe_allow_html=True)

with st.expander("Q1. 작업치료사와 물리치료사의 차이는 무엇인가요?"):

    st.markdown("""
**물리치료**는 근육, 관절, 통증과 운동기능 회복에 중점을 둡니다.

**작업치료**는 일상생활 수행능력, 손 기능, 인지 기능,
학교생활과 직업 복귀 등 사람이 의미 있는 활동을 할 수 있도록 돕는 치료입니다.
""")

with st.expander("Q2. 작업치료사는 병원에서만 근무하나요?"):

    st.markdown("""
아닙니다.

작업치료사는 다양한 분야에서 활동할 수 있습니다.

- 🏥 대학병원
- 🏥 종합병원
- 🏥 재활병원
- 🏠 보건소
- 🧠 치매안심센터
- 🏛 국민건강보험공단
- 😊 정신건강복지센터
- 👶 아동발달센터
- ♿ 장애인복지관
- 🦾 보조공학센터
""")

with st.expander("Q3. 작업치료사가 되려면 어떻게 해야 하나요?"):

    st.markdown("""
① 작업치료학과 진학

⬇

② 전공 수업 및 임상실습

⬇

③ 작업치료사 국가시험 합격

⬇

④ 작업치료사 면허 취득

⬇

⑤ 다양한 기관 취업
""")

st.divider()

# =========================================================
# 핵심 내용 정리
# =========================================================

st.markdown("""
<h2 style="
text-align:center;
color:#0077B6;
margin-bottom:25px;
">
📌 오늘 알아본 내용
</h2>
""", unsafe_allow_html=True)

summary1, summary2 = st.columns(2)

with summary1:

    st.success("""
### ✅ 작업치료란?

✔ 일상생활 회복을 돕는 전문 치료

✔ 신체와 인지를 함께 고려

✔ 전 연령 대상
""")

    st.success("""
### ✅ 대학에서 배우는 것

✔ 해부학

✔ 생리학

✔ 운동학

✔ 감각통합

✔ 인지재활

✔ 임상실습
""")

with summary2:

    st.success("""
### ✅ 졸업 후 진로

✔ 병원

✔ 보건소

✔ 치매안심센터

✔ 국민건강보험공단

✔ 아동발달센터

✔ 보조공학센터
""")

    st.success("""
### ✅ 필요한 역량

✔ 공감 능력

✔ 의사소통

✔ 책임감

✔ 문제 해결 능력

✔ 전문지식
""")

st.divider()

# =========================================================
# 마지막 화면
# =========================================================

st.balloons()

st.markdown("""
<div style="
background:linear-gradient(135deg,#0096C7,#48CAE4);
padding:45px;
border-radius:30px;
text-align:center;
color:white;
box-shadow:0 15px 35px rgba(0,119,182,.25);
">

<h1 style="
color:white;
margin-bottom:20px;
">

🌐 진로메타버스

</h1>

<h3 style="
color:white;
">

작업치료학과 진로 탐색

</h3>

<p style="
font-size:20px;
line-height:1.8;
">

작업치료사는 사람의 질병만 치료하는 것이 아니라

<strong>사람의 '삶'을 회복시키는 전문가</strong>입니다.

<br><br>

이번 진로 탐색을 통해
작업치료학과의 역할과 다양한 진출 분야를
이해하는 계기가 되었기를 바랍니다.

</p>

<h2 style="
color:white;
margin-top:30px;
">

감사합니다 😊

</h2>

</div>
""", unsafe_allow_html=True)

st.write("")

st.caption(
"© 2026 Career Metaverse | Occupational Therapy | Made with Streamlit"
)
