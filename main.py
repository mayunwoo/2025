import streamlit as st

# MBTI별 추천 직업 데이터 (예시)
mbti_jobs = {
    "INTJ": ["전략기획가", "연구원", "데이터 사이언티스트", "엔지니어"],
    "ENTP": ["기업가", "마케팅 전문가", "벤처 창업가", "기획자"],
    "INFJ": ["상담가", "교사", "작가", "심리학자"],
    "ESFP": ["배우", "디자이너", "마케팅 전문가", "이벤트 플래너"],
    "ISTJ": ["회계사", "공무원", "데이터 분석가", "엔지니어"],
    "ENFP": ["광고 기획자", "작가", "심리상담사", "여행 가이드"],
    # 필요시 더 추가 가능
}

st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯")

st.title("🎯 MBTI 기반 진로 추천 웹앱")
st.write("자신의 MBTI 유형을 선택하면, 적합한 직업을 추천해드립니다!")

# MBTI 선택
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_jobs.keys()))

if selected_mbti:
    st.subheader(f"🧩 {selected_mbti} 유형의 추천 직업")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

# 부가 기능 (선택 사항)
st.info("💡 MBTI는 성향을 참고할 수 있는 도구일 뿐, 직업 선택은 다양한 요소를 함께 고려해야 합니다.")
