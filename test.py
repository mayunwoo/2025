import streamlit as st

# ----------------------------
# 기본 설정
# ----------------------------
st.set_page_config(page_title="보건의료 웹앱", page_icon="🧑‍⚕️", layout="wide")

st.title("🧑‍⚕️ 누구나 쉽게 사용하는 보건의료 웹앱")

# ----------------------------
# 메뉴 선택
# ----------------------------
menu = st.sidebar.radio("메뉴 선택", ["홈", "자가진단", "운동 가이드", "약품 정보", "응급처치"])

# ----------------------------
# 홈
# ----------------------------
if menu == "홈":
    st.subheader("🏠 홈")
    st.write("""
    - 이 앱은 의료 전문가의 진료를 **대체하지 않습니다**.  
    - 가벼운 건강 확인 및 생활 관리에 활용하세요.  
    - 증상이 심각하다면 반드시 가까운 병원에 방문하세요.  
    """)

# ----------------------------
# 자가진단
# ----------------------------
elif menu == "자가진단":
    st.subheader("🤒 자가진단 도구")
    st.write("현재 겪고 있는 증상을 선택하세요:")

    symptom = st.selectbox("증상 선택", 
                           ["선택 안 함", "두통", "기침", "복통", "발열", "피로감", "발목통증", "눈충혈"])

    if symptom != "선택 안 함":
        st.write(f"선택한 증상: **{symptom}**")

        if symptom == "두통":
            st.info("긴장성 두통일 가능성이 있습니다. 충분한 수면과 수분 섭취가 필요합니다.")
        elif symptom == "기침":
            st.warning("감기, 기관지염 등일 수 있습니다. 기침이 2주 이상 지속되면 병원 진료를 권장합니다.")
        elif symptom == "복통":
            st.error("소화불량, 위염, 장염 등 원인이 다양합니다. 지속되면 내과 진료가 필요합니다.")
        elif symptom == "발열":
            st.warning("감염성 질환일 수 있습니다. 체온이 38도 이상 지속되면 병원에 방문하세요.")
        elif symptom == "피로감":
            st.info("과로, 수면 부족, 빈혈 등 원인이 있을 수 있습니다. 생활습관을 점검하세요.")
        elif symptom == "발목통증":
            st.warning("발목 염좌, 근육 손상 가능성이 있습니다. 심하면 병원 진료를 권장합니다.")
        elif symptom == "눈충혈":
            st.warning("결막염, 피로, 알레르기 가능성이 있습니다. 증상이 심하면 안과 진료를 권장합니다.")

# ----------------------------
# 운동 & 재활 가이드
# ----------------------------
elif menu == "운동 가이드":
    st.subheader("💪 재활 운동 가이드")
    exercise = st.selectbox("운동 부위 선택", ["어깨", "허리", "발목", "목"])

    if exercise == "어깨":
        st.write("✅ 어깨 스트레칭: 벽에 손을 대고 천천히 팔을 위로 올려주세요.")
        st.markdown("[영상 보기](https://www.youtube.com/watch?v=4BOTvaRaDjI)")
    elif exercise == "허리":
        st.write("✅ 허리 스트레칭: 무릎을 가슴 쪽으로 당겨 20초 유지하세요.")
        st.markdown("[영상 보기](https://www.youtube.com/watch?v=2pLT-olgUJs)")
    elif exercise == "발목":
        st.write("✅ 발목 강화: 밴드를 이용해 발목 외번/내번 운동을 15회 반복하세요.")
        st.markdown("[영상 보기](https://www.youtube.com/watch?v=Eys2RTh9agk)")
    elif exercise == "목":
        st.write("✅ 목 스트레칭: 고개를 좌우로 천천히 기울여 근육을 이완하세요.")
        st.markdown("[영상 보기](https://www.youtube.com/watch?v=R9sTBIcixWY)")

# ----------------------------
# 약품 정보
# ----------------------------
elif menu == "약품 정보":
    st.subheader("💊 약품 정보 검색")
    drug = st.text_input("검색할 약품 이름을 입력하세요 (예: 타이레놀, 아스피린)")

    drug_info = {
        "타이레놀": {"효능": "해열, 진통", "부작용": "간 손상 위험 (과다 복용 시)"},
        "아스피린": {"효능": "혈액 응고 억제, 해열, 진통", "부작용": "위장 장애, 출혈 위험"},
        "판토덱스": {"효능": "위산 억제제", "부작용": "두통, 복통"},
    }

    if st.button("검색"):
        if drug in drug_info:
            st.success(f"💊 {drug} 정보")
            st.write(f"**효능:** {drug_info[drug]['효능']}")
            st.write(f"**부작용:** {drug_info[drug]['부작용']}")
        else:
            st.error("데이터베이스에 없는 약품입니다. 약사/의사에게 문의하세요.")

# ----------------------------
# 응급처치
# ----------------------------
elif menu == "응급처치":
    st.subheader("🚑 응급처치 가이드")
    emergency = st.selectbox("상황 선택", ["심정지", "화상", "골절", "출혈"])

    if emergency == "심정지":
        st.error("👉 즉시 119에 신고 후 심폐소생술(CPR) 실시\n- 가슴 압박 30회 + 인공호흡 2회 반복")
        st.markdown("[영상 보기](https://www.youtube.com/watch?v=2pw8xNL1vOA)")
    elif emergency == "화상":
        st.warning("👉 화상 부위를 흐르는 찬물에 10~20분 식히세요. 얼음은 피하세요.")
    elif emergency == "골절":
        st.warning("👉 골절 부위를 움직이지 않게 고정하고, 얼음찜질 후 병원으로 이동하세요.")
    elif emergency == "출혈":
        st.warning("👉 깨끗한 천으로 출혈 부위를 압박하세요. 출혈이 심하면 지혈대 사용 고려")
