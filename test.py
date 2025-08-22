import streamlit as st

st.set_page_config(page_title="보건 웹앱", page_icon="🧑‍⚕️", layout="wide")

# 앱 제목
st.title("🧑‍⚕️ 보건 웹앱: 물리치료 & 작업치료")
st.write("남녀노소 누구나 쉽게 사용할 수 있는 **보건 교육 & 체험 앱**입니다.")
st.write("👵👴 할머니, 할아버지도 편하게 보고, 학생들도 공부할 수 있도록 만들었어요!")

# 사이드바 메뉴
menu = st.sidebar.radio("메뉴 선택", ["홈", "물리치료", "작업치료"])

# ------------------------------
# 홈
# ------------------------------
if menu == "홈":
    st.header("🏠 홈")
    st.write("이 앱은 **물리치료와 작업치료**에 대해 배우고, 간단한 자가 진단과 치료 방법을 확인할 수 있도록 만든 앱입니다.")
    st.write("👉 왼쪽 메뉴에서 원하는 항목을 선택하세요!")

# ------------------------------
# 물리치료
# ------------------------------
elif menu == "물리치료":
    st.header("💪 물리치료 (Physiotherapy)")

    st.subheader("📖 물리치료란?")
    st.write("""
    물리치료는 **통증을 줄이고 근육과 관절의 기능을 회복**시키며, **재활을 돕는 치료 방법**입니다.
    운동, 전기 자극, 온열 요법 등이 사용됩니다.
    """)

    st.subheader("✨ 물리치료의 주요 효과")
    st.markdown("""
    - ✅ **통증 감소**: 급성 및 만성 통증 완화
    - ✅ **기능 회복**: 근력 및 관절 가동 범위 향상
    - ✅ **재활 지원**: 수술 후 회복 촉진
    - ✅ **부상 예방**: 운동 및 자세 교정을 통한 재발 방지
    - ✅ **신경학적 증상 완화**: 뇌졸중, 파킨슨병 등 관련 증상 개선
    """)

    st.subheader("📝 간단 진단 (신체 기능 자가 평가)")
    pt_questions = {
        "허리 통증이 얼마나 자주 있나요?": ["없다", "가끔 있다", "자주 있다"],
        "무릎 통증이 있나요?": ["없다", "약간 있다", "심하다"],
        "계단을 오르내릴 때 불편함이 있나요?": ["전혀 없다", "약간 있다", "많이 있다"],
        "목이나 어깨 뻐근함이 자주 있나요?": ["없다", "가끔 있다", "자주 있다"],
        "걷거나 서 있을 때 피로가 빨리 오나요?": ["전혀 아니다", "약간 그렇다", "매우 그렇다"]
    }

    pt_score = 0
    for q, opts in pt_questions.items():
        ans = st.radio(f"👉 {q}", opts, key=q)
        pt_score += opts.index(ans)

    if st.button("📊 물리치료 진단 결과 보기"):
        st.write(f"총 점수: {pt_score} / {len(pt_questions)*2}")
        if pt_score <= 3:
            st.success("✅ 큰 문제는 없어 보입니다. 규칙적인 운동과 올바른 자세 유지로 건강을 지키세요.")
        elif pt_score <= 6:
            st.warning("⚠️ 근골격계에 약간의 불편이 있습니다. 가벼운 근력 운동과 스트레칭을 권장합니다.")
        else:
            st.error("❗ 통증 및 기능 저하가 우려됩니다. 전문가 상담 및 물리치료가 필요합니다.")

    st.subheader("💡 권장 치료/운동 방법")
    st.markdown("""
    - 🧘 **스트레칭**: 허리, 목, 무릎 관절 스트레칭 (아침/저녁 10분)
    - 💪 **코어 근력 운동**: 플랭크, 브리지, 밴드 운동
    - 🪑 **생활 습관 개선**: 올바른 자세 유지, 무거운 물건 올바르게 들기
    - 🏥 **전문 치료 필요 시**: 온열 요법, 전기 자극치료, 초음파 치료 등
    """)

    # 전문 사이트 버튼
    st.markdown("""
    <a href="https://www.healthline.com/health/benefits-of-physical-therapy" target="_blank">
        <button style="padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px;">전문 사이트 보기</button>
    </a>
    """, unsafe_allow_html=True)

# ------------------------------
# 작업치료
# ------------------------------
elif menu == "작업치료":
    st.header("🎨 작업치료 (Occupational Therapy)")

    st.subheader("📖 작업치료란?")
    st.write("""
    작업치료는 **일상생활에 필요한 활동(옷 입기, 식사, 글쓰기 등)을 스스로 할 수 있도록 돕는 치료**입니다.
    또한 인지 기능과 정신 건강 향상에도 도움을 줍니다.
    """)

    st.subheader("✨ 작업치료의 주요 효과")
    st.markdown("""
    - ✅ **일상생활 자립 능력 향상**: 옷 입기, 식사 등 기본 활동 수행 능력 개선
    - ✅ **인지 기능 개선**: 기억력, 집중력 등 인지 능력 향상
    - ✅ **손 기능 및 소근육 발달**: 손가락 스트레칭, 점토 반죽하기 등 훈련
    - ✅ **정신적 안정과 사회적 참여 증가**: 감정 조절 및 사회적 상호작용 능력 향상
    """)

    st.subheader("📝 간단 진단 (일상생활 수행능력 + 인지 기능)")
    ot_questions = {
        "혼자 옷을 입는 것이 어렵나요?": ["전혀 어렵지 않다", "가끔 어렵다", "매우 어렵다"],
        "식사를 혼자 하는 데 어려움이 있나요?": ["없다", "약간 있다", "많이 있다"],
        "집안일(청소, 설거지 등)을 스스로 할 수 있나요?": ["잘 할 수 있다", "도움이 필요하다", "거의 못한다"],
        "최근 기억한 내용을 자주 잊는 편인가요?": ["아니다", "가끔 그렇다", "자주 그렇다"],
        "주의 집중이 어려운 경우가 많나요?": ["없다", "가끔 있다", "자주 있다"]
    }

    ot_score = 0
    for q, opts in ot_questions.items():
        ans = st.radio(f"👉 {q}", opts, key=q)
        ot_score += opts.index(ans)

    if st.button("📊 작업치료 진단 결과 보기"):
        st.write(f"총 점수: {ot_score} / {len(ot_questions)*2}")
        if ot_score <= 3:
            st.success("✅ 일상생활과 인지 기능에 큰 어려움은 없어 보입니다.")
        elif ot_score <= 6:
            st.warning("⚠️ 일부 어려움이 있습니다. 간단한 작업치료 훈련이 도움이 될 수 있습니다.")
        else:
            st.error("❗ 일상생활과 인지 기능에 뚜렷한 어려움이 있습니다. 전문 작업치료사의 평가와 훈련이 필요합니다.")

    st.subheader("💡 권장 치료/훈련 방법")
    st.markdown("""
    - ✋ **손 기능 훈련**: 작은 물건 집기, 손가락 스트레칭, 점토 반죽하기
    - 🧠 **인지 훈련**: 숫자/단어 기억하기, 퍼즐 맞추기, 그림 찾기 게임
    - 🏡 **일상생활 훈련**: 식사 준비, 글쓰기, 계산하기 등 실제 생활 활동 반복
    - 🏥 **전문 치료 필요 시**: 인지 재활 프로그램, 감각-운동 통합 훈련, 맞춤형 보조도구 활용
    """)

    # 전문 사이트 버튼
    st.markdown("""
    <a href="https://my.clevelandclinic.org/health/treatments/occupational-therapy" target="_blank">
        <button style="padding:10px 20px; font-size:16px; background-color:#4CAF50; color:white; border:none; border-radius:5px;">전문 사이트 보기</button>
    </a>
    """, unsafe_allow_html=True)
