import streamlit as st
import random

st.set_page_config(page_title="작업치료 실습 앱", page_icon="🧠", layout="centered")

st.title("🖐️ 작업치료 실습 웹앱")
st.write("이 앱은 **작업치료 실습용**으로 일상생활 수행능력 평가, 인지 퀴즈, 재활운동 진행을 체험할 수 있습니다.")

# ------------------------------
# 1. ADL 자가 평가
# ------------------------------
st.header("1️⃣ 일상생활 수행능력(ADL) 자가 평가")
questions = [
    ("옷을 혼자 입을 수 있나요?", ["전혀 못한다", "약간 도움 필요", "완전히 가능"]),
    ("혼자 식사를 할 수 있나요?", ["전혀 못한다", "약간 도움 필요", "완전히 가능"]),
    ("혼자 화장실을 갈 수 있나요?", ["전혀 못한다", "약간 도움 필요", "완전히 가능"]),
    ("혼자 이동할 수 있나요?", ["전혀 못한다", "약간 도움 필요", "완전히 가능"]),
]

adl_score = 0
for q, options in questions:
    choice = st.radio(q, options, key=q)
    adl_score += options.index(choice)  # 0,1,2 점수 부여

if st.button("ADL 평가 결과 보기"):
    st.success(f"총 점수: {adl_score} / {len(questions)*2}")
    if adl_score <= 3:
        st.write("⚠️ **기능 저하**: 많은 도움이 필요합니다.")
    elif adl_score <= 6:
        st.write("🙂 **중간 수준**: 일부 도움이 필요합니다.")
    else:
        st.write("💪 **독립적**: 대부분 스스로 가능합니다.")

# ------------------------------
# 2. 인지 퀴즈 (숫자 기억)
# ------------------------------
st.header("2️⃣ 인지 기능 훈련 - 숫자 기억하기")
if "quiz_numbers" not in st.session_state:
    st.session_state.quiz_numbers = []

if st.button("새 문제 생성"):
    st.session_state.quiz_numbers = [random.randint(0,9) for _ in range(5)]
    st.info("5초 동안 숫자를 외우세요!")
    st.write(st.session_state.quiz_numbers)

answer = st.text_input("숫자를 입력하세요 (띄어쓰기 없이)")
if st.button("정답 확인"):
    correct = "".join(map(str, st.session_state.quiz_numbers))
    if answer == correct:
        st.success("정답! 🧠 기억력이 좋습니다!")
    else:
        st.error(f"틀렸습니다. 정답은 {correct} 였습니다.")

# ------------------------------
# 3. 재활 운동 진행률
# ------------------------------
st.header("3️⃣ 재활 운동 진행률 체크")
if "exercise_progress" not in st.session_state:
    st.session_state.exercise_progress = 0

if st.button("운동 완료 체크 🏃"):
    if st.session_state.exercise_progress < 100:
        st.session_state.exercise_progress += 20
st.progress(st.session_state.exercise_progress)

if st.session_state.exercise_progress >= 100:
    st.balloons()
    st.success("🎉 오늘의 운동 목표를 달성했습니다!")

