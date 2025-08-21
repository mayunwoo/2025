import streamlit as st

# 🎭 MBTI별 추천 직업 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략기획가", "🔬 연구원", "📊 데이터 사이언티스트", "⚙️ 엔지니어"],
    "ENTP": ["🚀 기업가", "📣 마케팅 전문가", "💡 벤처 창업가", "📝 기획자"],
    "INFJ": ["💞 상담가", "📚 교사", "✍️ 작가", "🧘 심리학자"],
    "ESFP": ["🎤 배우", "🎨 디자이너", "🎉 이벤트 플래너", "🌟 마케팅 전문가"],
    "ISTJ": ["💼 회계사", "🏛️ 공무원", "📈 데이터 분석가", "⚒️ 엔지니어"],
    "ENFP": ["🌍 여행 가이드", "🎬 광고 기획자", "📝 작가", "💖 심리상담사"],
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
