import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 폭★발 추천기", page_icon="💥", layout="centered")

# 배경 색 및 애니메이션 효과
st.markdown("""
<style>
body {
    background-color: #000000;
    color: white;
}
h1, h2, h3 {
    animation: shake 0.4s infinite;
}
@keyframes shake {
  0% { transform: translate(1px, 1px) rotate(0deg); }
  10% { transform: translate(-1px, -2px) rotate(-1deg); }
  20% { transform: translate(-3px, 0px) rotate(1deg); }
  30% { transform: translate(3px, 2px) rotate(0deg); }
  40% { transform: translate(1px, -1px) rotate(1deg); }
  50% { transform: translate(-1px, 2px) rotate(-1deg); }
  60% { transform: translate(-3px, 1px) rotate(0deg); }
  70% { transform: translate(3px, 1px) rotate(-1deg); }
  80% { transform: translate(-1px, -1px) rotate(1deg); }
  90% { transform: translate(1px, 2px) rotate(0deg); }
  100% { transform: translate(1px, -2px) rotate(-1deg); }
}
</style>
""", unsafe_allow_html=True)

# MBTI 직업 목록 (파괴적 네이밍)
mbti_jobs = {
    "INTJ": ["🧠 천재 전략 폭격기", "💻 디지털 전사", "🛰 데이터 로켓"],
    "ENFP": ["🌈 아이디어 대폭발 크리에이터", "🎤 감성 로켓 런처", "🔥 열정의 핵융합체"],
    "ISFP": ["🎨 감성 예술 폭탄", "🍰 디저트 아티스트", "📷 사진 예술 전사"],
    "ENTP": ["⚡️ 에너지 폭주 기관차", "💡 창의력 미사일", "📢 사고혁명가"],
    # ... 나머지도 넣을 수 있어요
}

# 타이틀
st.markdown("""
<h1 style='text-align:center; font-size:60px; color: #FF4444;'>💥 MBTI 직업 폭★발 추천기 💥</h1>
<h3 style='text-align:center; color:orange;'>네 성격이 뭔지 모르겠지만, 이제 다 터진다... 💣</h3>
""", unsafe_allow_html=True)

# 입력창
mbti_input = st.text_input("🌋 MBTI를 입력해주세요 (예: ENFP)").upper()

# 폭발 GIF
explosion_gif = "https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif"

# 처리
if mbti_input:
    with st.spinner("🧠 성격 분석 중... 폭발물 조립 중..."):
        time.sleep(2)

    st.image(explosion_gif, width=400, caption="💥 BOOM! MBTI Detonated! 💥")

    st.markdown("<hr style='border: 5px dashed red;'/>", unsafe_allow_html=True)

    if mbti_input in mbti_jobs:
        st.markdown(f"<h2 style='text-align:center; color:#FFD700;'>🔥 {mbti_input} 유형의 직업 폭★탄 리스트 🔥</h2>", unsafe_allow_html=True)
        for job in mbti_jobs[mbti_input]:
            color = random.choice(["#FF69B4", "#00FF00", "#FFFF33", "#FF4500"])
            st.markdown(f"<h3 style='color:{color}; text-align:center;'>💣 {job}</h3>", unsafe_allow_html=True)
        st.snow()
        st.balloons()
    else:
        st.error("🚫 존재하지 않는 MBTI입니다. 다시 확인해주세요!")

