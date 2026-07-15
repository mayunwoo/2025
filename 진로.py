import streamlit as st

# =====================================
# 기본 설정
# =====================================

st.set_page_config(
    page_title="진로메타버스 | 작업치료학과",
    page_icon="🧠",
    layout="wide"
)


# =====================================
# CSS 디자인
# =====================================

st.markdown("""
<style>

/* 전체 배경 */

.stApp{

background:
linear-gradient(
135deg,
#EAF8FF,
#D9F3FF,
#F7FDFF
);

overflow:hidden;

}


/* 배경 원 효과 */

.stApp:before{

content:"";

position:fixed;

width:250px;

height:250px;

background:#BDEBFF;

border-radius:50%;

top:10%;

left:5%;

opacity:0.35;

animation:move1 10s infinite alternate;

z-index:-1;

}


.stApp:after{

content:"";

position:fixed;

width:350px;

height:350px;

background:#90E0EF;

border-radius:50%;

bottom:5%;

right:5%;

opacity:0.25;

animation:move2 12s infinite alternate;

z-index:-1;

}



@keyframes move1{

from{

transform:translateY(0px);

}


to{

transform:translateY(80px);

}

}



@keyframes move2{

from{

transform:translateY(0px);

}


to{

transform:translateY(-100px);

}

}

/* 화면 여백 */

.block-container{

max-width:1100px;

padding-top:2rem;

}


/* 제목 */

h1{

text-align:center;

font-size:58px;

font-weight:900;

color:#0077B6;

letter-spacing:-2px;

}


/* 소제목 */

h2{

color:#006494;

font-weight:800;

}


h3{

color:#118AB2;

}



/* 아코디언 */

div[data-testid="stExpander"]{

background:
rgba(255,255,255,0.85);

border-radius:25px;

border:1px solid #BDE0FE;

box-shadow:
0 10px 25px rgba(0,119,182,0.12);

margin-bottom:20px;

transition:.3s;

}


div[data-testid="stExpander"]:hover{

transform:translateY(-5px);

box-shadow:
0 15px 35px rgba(0,119,182,0.2);

}



/* 버튼 */

.stButton>button{

background:#0096C7;

color:white;

border-radius:30px;

padding:12px 30px;

font-weight:bold;

border:none;

}


.stButton>button:hover{

background:#0077B6;

transform:scale(1.05);

}



/* 카드 */

.card{

background:white;

padding:25px;

border-radius:25px;

box-shadow:
0 10px 25px rgba(0,0,0,0.08);

text-align:center;

height:150px;

}


.card h2{

color:#0077B6;

}



/* 안내창 */

.stAlert{

border-radius:20px;

}


</style>

""",
unsafe_allow_html=True)



# =====================================
# 메인 화면
# =====================================


st.markdown("""
<h1>
🌐 진로메타버스
</h1>

<p style="
text-align:center;
font-size:22px;
color:#0077B6;
font-weight:600;
">
작업치료학과 진로 탐색
</p>

""", unsafe_allow_html=True)


st.write("")
st.write("")


st.divider()



# =====================================
# 정보 카드
# =====================================


col1,col2,col3,col4 = st.columns(4)


with col1:

    st.markdown("""
    <div class="card">

    <h2>10+</h2>

    <p>진출 분야</p>

    </div>
    """,
    unsafe_allow_html=True)



with col2:

    st.markdown("""
    <div class="card">

    <h2>전 연령</h2>

    <p>치료 대상</p>

    </div>
    """,
    unsafe_allow_html=True)



with col3:

    st.markdown("""
    <div class="card">

    <h2>국가시험</h2>

    <p>면허 취득</p>

    </div>
    """,
    unsafe_allow_html=True)



with col4:

    st.markdown("""
    <div class="card">

    <h2>★★★★★</h2>

    <p>미래 전망</p>

    </div>
    """,
    unsafe_allow_html=True)



st.divider()



# =====================================
# 작업치료란
# =====================================


with st.expander("🩺 작업치료란?"):


    st.markdown("""
## 작업치료(Occupational Therapy)


작업치료는 질병, 사고, 장애, 노화 등으로 인해
일상생활에 어려움을 겪는 사람이
독립적인 생활을 할 수 있도록 돕는
보건의료 전문 분야입니다.


여기서 말하는 **작업(Occupation)** 은
직업만 의미하는 것이 아니라


- 식사하기
- 옷 입기
- 공부하기
- 학교생활
- 취미활동
- 사회생활


등 사람이 살아가면서 수행하는
모든 의미 있는 활동을 의미합니다.


작업치료사는 대상자의 신체적 기능뿐 아니라
인지, 감각, 정서, 사회적 능력까지 고려하여
개인에게 맞는 치료를 제공합니다.
""")


    st.success(
    "목표 : 대상자가 원하는 삶을 스스로 살아갈 수 있도록 돕는 것"
    )



# =====================================
# 작업치료 대상
# =====================================


with st.expander("👥 작업치료가 필요한 대상"):


    tab1,tab2,tab3,tab4 = st.tabs(
    [
    "👶 아동",
    "🧑 성인",
    "👵 노인",
    "😊 정신건강"
    ]
    )


    with tab1:

        st.markdown("""
### 👶 아동 작업치료

대상

- 발달지연
- 자폐스펙트럼장애
- ADHD
- 뇌성마비


주요 목표

✔ 감각 발달

✔ 집중력 향상

✔ 학교생활 적응

✔ 사회성 발달
""")


    with tab2:

        st.markdown("""
### 🧑 성인 작업치료

대상

- 뇌졸중
- 척수손상
- 외상성 뇌손상
- 손 기능 손상


주요 목표

✔ 신체 기능 회복

✔ 일상생활 복귀

✔ 직업 및 사회 참여
""")


    with tab3:

        st.markdown("""
### 👵 노인 작업치료

대상

- 치매
- 파킨슨병
- 노인성 질환


주요 목표

✔ 인지 기능 유지

✔ 낙상 예방

✔ 독립적인 생활 지원
""")


    with tab4:

        st.markdown("""
### 😊 정신건강 작업치료

대상

- 우울증
- 조현병
- 정신건강 어려움


주요 목표

✔ 사회 적응

✔ 일상생활 회복

✔ 사회 복귀 지원
""")
# =====================================
# 작업치료학과에서 배우는 내용
# =====================================

with st.expander("📚 작업치료학과에서는 무엇을 배울까?"):

    st.markdown("""
작업치료학과에서는 사람의 신체 구조와 기능을 이해하고,
대상자의 상태에 맞는 재활 프로그램을 계획하고 적용하는 방법을 배웁니다.

기초 의학 지식부터 실제 치료 방법까지 다양한 영역을 학습하며,
졸업 후 임상 현장에서 활용할 수 있는 전문성을 키우게 됩니다.
""")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### 🧬 기초 의학 영역

📌 해부학

인체의 구조와 근육, 뼈, 신경의 기능을 이해합니다.


📌 생리학

우리 몸의 기능과 신체 변화 과정을 배웁니다.


📌 신경과학

뇌와 신경계가 움직임과 인지에 미치는 영향을 학습합니다.


📌 운동학

움직임의 원리와 신체 기능을 분석합니다.
""")


    with col2:

        st.markdown("""
### 🧠 작업치료 전문 영역

📌 아동 작업치료

발달 과정과 아동의 성장 지원 방법을 배웁니다.


📌 노인 작업치료

치매 예방, 인지 기능 향상 방법을 학습합니다.


📌 정신건강 작업치료

정신건강 대상자의 사회 참여와 적응을 지원합니다.


📌 보조공학

보조기기를 활용하여 독립적인 생활을 돕는 방법을 배웁니다.
""")


    st.info("""
또한 병원 및 재활기관에서 임상실습을 진행하며
실제 대상자를 평가하고 치료하는 경험을 쌓습니다.
""")


# =====================================
# 작업치료사의 역할
# =====================================

with st.expander("❤️ 작업치료사는 어떤 일을 할까?"):

    st.markdown("""
작업치료사는 대상자가 일상생활 속에서 어려움을 겪는 부분을 파악하고,
개인에게 맞는 치료 목표를 설정하여 기능 회복을 돕습니다.
""")

    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown("""
<div class="card">

<h2>🔍 평가</h2>

<p>
신체 기능<br>
인지 능력<br>
감각 기능<br>
일상생활 수행 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    with col2:

        st.markdown("""
<div class="card">

<h2>🧩 치료</h2>

<p>
인지재활<br>
감각통합<br>
손 기능 훈련<br>
일상생활 훈련
</p>

</div>
""",
        unsafe_allow_html=True)



    with col3:

        st.markdown("""
<div class="card">

<h2>🤝 지원</h2>

<p>
사회 복귀<br>
학교생활 적응<br>
직업 재활<br>
보조기기 활용
</p>

</div>
""",
        unsafe_allow_html=True)



    st.success("""
작업치료의 핵심은 단순히 기능을 회복시키는 것이 아니라,
대상자가 자신의 삶에서 의미 있는 활동을 다시 수행하도록 돕는 것입니다.
""")


# =====================================
# 졸업 후 진로
# =====================================

with st.expander("💼 작업치료학과 졸업 후 진로"):

    st.markdown("""
작업치료사는 병원뿐 아니라 공공기관과 지역사회 기관 등
다양한 분야에서 활동할 수 있습니다.

대상자의 특성과 관심 분야에 따라 여러 진로 방향을 선택할 수 있습니다.
""")


    # 진로 카드 1

    col1,col2 = st.columns(2)


    with col1:

        st.markdown("""
<div class="card">

<h2>🏥 의료기관</h2>

<p>
대학병원<br>
종합병원<br>
재활병원<br>
요양병원<br>
어린이병원
</p>

</div>
""",
        unsafe_allow_html=True)



    with col2:

        st.markdown("""
<div class="card">

<h2>🏛 공공기관</h2>

<p>
국민건강보험공단<br>
건강보험심사평가원<br>
근로복지공단
</p>

</div>
""",
        unsafe_allow_html=True)



    st.write("")


    col3,col4 = st.columns(2)


    with col3:

        st.markdown("""
<div class="card">

<h2>🏠 지역사회</h2>

<p>
보건소<br>
치매안심센터<br>
정신건강복지센터<br>
장애인복지관
</p>

</div>
""",
        unsafe_allow_html=True)



    with col4:

        st.markdown("""
<div class="card">

<h2>👶 기타 분야</h2>

<p>
아동발달센터<br>
특수학교<br>
보조공학센터<br>
의료기기 회사
</p>

</div>
""",
        unsafe_allow_html=True)



    st.divider()


    st.markdown("""
### 🌱 분야별 역할

🏥 **병원**

뇌졸중, 손상, 질환 이후 환자의 재활과 일상생활 회복 지원


🏛 **국민건강보험공단**

국민 건강 증진과 건강 관련 사업 지원


🏠 **보건소·치매안심센터**

지역 주민과 노인의 건강관리 및 인지 프로그램 운영


👶 **아동발달센터**

아동의 발달과 학교생활 적응 지원


🦾 **보조공학센터**

보조기기 평가 및 활용 지원
""")


    st.success(
    "작업치료사는 의료, 복지, 공공 분야를 연결하는 다양한 진로를 선택할 수 있습니다."
    )


st.divider()
# =====================================
# 작업치료사에게 필요한 역량
# =====================================

with st.expander("⭐ 작업치료사에게 필요한 역량"):

    st.markdown("""
작업치료사는 사람을 직접 만나고,
개인의 삶을 회복하도록 돕는 직업이기 때문에
전문지식뿐 아니라 다양한 역량이 필요합니다.
""")


    col1,col2,col3 = st.columns(3)


    with col1:

        st.markdown("""
<div class="card">

<h2>💙 공감 능력</h2>

<p>
대상자의 어려움을 이해하고
심리적으로 지지하는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    with col2:

        st.markdown("""
<div class="card">

<h2>🗣 소통 능력</h2>

<p>
대상자와 보호자,
의료진과 효과적으로
소통하는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    with col3:

        st.markdown("""
<div class="card">

<h2>🧠 전문성</h2>

<p>
의학 지식을 바탕으로
문제를 분석하고
치료를 계획하는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    st.write("")


    col4,col5,col6 = st.columns(3)


    with col4:

        st.markdown("""
<div class="card">

<h2>👀 관찰력</h2>

<p>
대상자의 작은 변화까지
파악하는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    with col5:

        st.markdown("""
<div class="card">

<h2>💡 창의성</h2>

<p>
개인에게 맞는
새로운 치료 방법을
찾는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



    with col6:

        st.markdown("""
<div class="card">

<h2>🤝 협업 능력</h2>

<p>
의료진과 함께
최적의 치료 방향을
만드는 능력
</p>

</div>
""",
        unsafe_allow_html=True)



# =====================================
# 작업치료사의 전망
# =====================================

with st.expander("📈 작업치료사의 전망"):


    st.success(
    "고령화와 재활의료 서비스 확대에 따라 작업치료사의 역할은 더욱 중요해지고 있습니다."
    )


    col1,col2 = st.columns(2)


    with col1:

        st.markdown("""
### 📊 수요 증가 요인

✔ 고령 인구 증가

✔ 치매 환자 증가

✔ 장애인 복지 확대

✔ 재활 의료 발전

✔ 지역사회 건강관리 확대
""")


    with col2:

        st.markdown("""
### 🔮 미래 변화

✔ 방문재활 확대

✔ 공공보건 분야 증가

✔ 보조공학 발전

✔ 디지털 재활 기술 발전

✔ 예방 중심 건강관리
""")


    st.info("""
앞으로의 작업치료사는 병원 중심의 치료를 넘어
지역사회와 공공 영역에서 사람들의 건강한 삶을 지원하는 역할이 더욱 확대될 것으로 예상됩니다.
""")


# =====================================
# 작업치료사가 되는 과정
# =====================================

with st.expander("🎓 작업치료사가 되는 과정"):


    st.markdown("""
## 작업치료사가 되기 위한 과정


### 1️⃣ 작업치료학과 진학

대학교에서 작업치료 관련 전공을 공부합니다.


⬇️


### 2️⃣ 전공 수업 및 임상실습

해부학, 생리학, 재활 관련 과목을 배우고
병원 및 기관에서 실습을 진행합니다.


⬇️


### 3️⃣ 국가시험 응시

작업치료사 국가시험에 응시합니다.


⬇️


### 4️⃣ 면허 취득

시험 합격 후 작업치료사 면허를 취득합니다.


⬇️


### 5️⃣ 다양한 분야 취업

병원, 보건소, 치매안심센터,
국민건강보험공단 등에서 활동할 수 있습니다.
""")


# =====================================
# 적성 테스트
# =====================================

with st.expander("🧩 나에게 맞는 작업치료 진로 찾기"):


    st.markdown("""
자신이 관심 있는 분야를 선택하면
어울리는 작업치료 진로를 추천해드립니다.
""")


    choice = st.selectbox(
        "관심 분야를 선택하세요.",
        [
            "선택하세요",
            "👶 아이들의 성장과 발달",
            "👵 노인의 건강과 치매 예방",
            "🏥 병원 재활 분야",
            "🏛 공공기관 분야",
            "😊 정신건강 분야",
            "🦾 보조공학 분야"
        ]
    )


    if st.button("🔎 추천 진로 확인"):


        if choice == "선택하세요":

            st.warning(
            "먼저 관심 있는 분야를 선택해주세요."
            )


        elif choice == "👶 아이들의 성장과 발달":

            st.success("""
### 추천 진로 👶

**아동발달센터 · 특수학교 · 특수교육지원센터**

발달지연, ADHD, 자폐스펙트럼 아동의
성장과 학교생활 적응을 지원합니다.
""")


        elif choice == "👵 노인의 건강과 치매 예방":

            st.success("""
### 추천 진로 👵

**치매안심센터 · 노인복지기관**

치매 예방 프로그램과
인지 기능 향상 활동을 운영합니다.
""")


        elif choice == "🏥 병원 재활 분야":

            st.success("""
### 추천 진로 🏥

**대학병원 · 종합병원 · 재활병원**

뇌졸중, 손상 환자의
기능 회복과 일상생활 복귀를 돕습니다.
""")


        elif choice == "🏛 공공기관 분야":

            st.success("""
### 추천 진로 🏛

**국민건강보험공단 · 보건소**

국민 건강 증진과
재활 관련 사업에 참여합니다.
""")


        elif choice == "😊 정신건강 분야":

            st.success("""
### 추천 진로 😊

**정신건강복지센터**

정신건강 대상자의 사회 참여와
일상생활 적응을 지원합니다.
""")


        elif choice == "🦾 보조공학 분야":

            st.success("""
### 추천 진로 🦾

**보조공학센터 · 의료기기 분야**

보조기기를 활용하여
대상자의 독립적인 생활을 돕습니다.
""")


# =====================================
# 작업치료 상식
# =====================================

with st.expander("💡 작업치료 상식"):

    st.markdown("""
### 알고 있으면 좋은 작업치료 이야기


🧠 작업치료는 신체뿐 아니라
인지, 감정, 사회 참여까지 고려하는 치료입니다.


👶 아동부터 👵 노인까지
모든 연령층을 대상으로 합니다.


🏥 작업치료사는 병원뿐 아니라
보건소, 치매안심센터, 공공기관 등
다양한 곳에서 활동합니다.


🦾 보조공학 기술과 함께 발전하며
앞으로 활동 분야가 더욱 넓어질 가능성이 있습니다.
""")


# =====================================
# Q&A
# =====================================

with st.expander("❓ 자주 묻는 질문"):


    st.write("### Q. 작업치료와 물리치료의 차이는 무엇인가요?")


    st.info("""
물리치료는 신체 기능 회복에 중심을 두고,
작업치료는 일상생활 수행 능력과 사회 참여 향상에 중심을 둡니다.
""")


    st.write("### Q. 작업치료사는 병원에서만 일하나요?")


    st.info("""
아닙니다.

병원뿐 아니라 보건소,
치매안심센터,
국민건강보험공단,
정신건강복지센터,
장애인복지관,
아동발달센터 등 다양한 기관에서 활동합니다.
""")


    st.write("### Q. 작업치료사가 되려면 어떻게 해야 하나요?")


    st.info("""
작업치료학과를 졸업하고
국가시험에 합격하여 면허를 취득해야 합니다.
""")


# =====================================
# 마무리
# =====================================

st.divider()


st.success("""
🎉 진로 탐색 완료!

작업치료사는 사람들의 일상과 삶의 질을 향상시키는
보건의료 전문가입니다.

병원뿐 아니라 공공기관과 지역사회까지
다양한 분야에서 활동할 수 있습니다.
""")


st.caption(
"🌐 진로메타버스 | 작업치료학과 진로 탐색 | Made with Streamlit"
)
