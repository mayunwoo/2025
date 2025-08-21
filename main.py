import streamlit as st

# 🎭 MBTI별 추천 직업 데이터 (16개 전부!)
mbti_jobs = {
    "ISTJ": ["💼 회계사", "🏛️ 공무원", "📊 데이터 분석가", "⚒️ 엔지니어"],
    "ISFJ": ["🤝 사회복지사", "🏫 교사", "💊 간호사", "👩‍🍳 영양사"],
    "INFJ": ["💞 상담가", "📚 교사", "✍️ 작가", "🧘 심리학자"],
    "INTJ": ["🧠 전략기획가", "🔬 연구원", "📈 데이터 사이언티스트", "⚙️ 엔지니어"],
    "ISTP": ["🔧 기술자", "🚓 경찰관", "🛠️ 정비사", "🕵️ 탐정"],
    "ISFP": ["🎨 디자이너", "🎶 음악가", "📸 사진작가", "🌿 환경운동가"],
    "INFP": ["✍️ 작가", "🎭 예술가", "💖 상담사", "🌍 인권운동가"],
    "INTP": ["🔬 과학자", "👨‍💻 프로그래머", "📊 연구원", "🤖 AI 엔지니어"],
    "ESTP": ["💼 영업사원", "🏅 운동선수", "📈 투자자", "🎤 쇼호스트"],
    "ESFP": ["🎤 배우", "🎨 디자이너", "🎉 이벤트 플래너", "🌟 방송인"],
    "ENFP": ["🌍 여행 가이드", "🎬 광고 기획자", "📝 작가", "💖 심리상담사"],
    "ENTP": ["🚀 기업가", "📣 마케팅 전문가", "💡 벤처 창업가", "📝 기획자"],
    "ESTJ": ["🏢 관리자", "📊 경영 컨설턴트", "📈 회계사", "⚖️ 판사"],
    "ESFJ": ["👩‍🏫 교사", "🤝 사회복지사", "💊 간호사", "🎤 홍보 담당자"],
    "ENFJ": ["🎓 교육자", "🌍 NGO 활동가", "💼 리더십 코치", "🎤 강연자"],
    "ENTJ": ["🚀 기업 CEO", "📊 전략가", "🏢 조직 관리자", "⚖️ 변호사"],
}

# 🌈 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="🎯", layout="centered")

# 🏆 타이틀 꾸미기
st.markdown(
    """
    <h1 style='text-align: center; color: #FF6F61;'>
    🌟🎯 MBTI 기반 진로 추천 🎯🌟
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center; color: #6A5ACD;'>✨ 나의 성격 유형과 찰떡궁합 직업을 찾아보세요! ✨</h3>",
    unsafe_allow_html=True
)

st.write("")

# 🎲 MBTI 선택 박스
selected_mbti = st.selectbox("🧩 당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

if selected_mbti:
    st.success(f"💡 당신은 **{selected_mbti}** 유형이에요! 🎉")
    st.markdown("### 🌈 추천 직업 리스트 🌈")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

    st.balloons()  # 🎈🎉 풍선 효과

# 📝 하단 안내
st.info("💡 MBTI는 성향 참고용 도구이며, 직업 선택은 다양한 요소를 함께 고려하는 것이 좋아요! 🌱")

# ✨ 푸터
st.markdown(
    "<hr><p style='text-align: center; color: gray;'>🚀 Made with ❤️ using Streamlit 🎨</p>",
    unsafe_allow_html=True
)
