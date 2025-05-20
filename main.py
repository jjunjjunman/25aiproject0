import streamlit as st
import time
import random

# 💥 핵융합 페이지 설정
st.set_page_config(page_title="MBTI 대폭발 추천기 9000", page_icon="💣", layout="centered")

# 🌈 미친 배경과 진동 스타일 해킹
st.markdown("""
<style>
body {
    animation: colorChange 10s infinite alternate;
    font-family: 'Comic Sans MS', cursive, sans-serif;
}
@keyframes colorChange {
    0% { background-color: #000000; }
    25% { background-color: #440044; }
    50% { background-color: #FF0000; }
    75% { background-color: #FF6600; }
    100% { background-color: #FFFF00; }
}
h1, h2, h3 {
    animation: explodeText 0.5s infinite;
}
@keyframes explodeText {
    0% { transform: scale(1) rotate(0deg); }
    50% { transform: scale(1.1) rotate(1deg); color: #fff; }
    100% { transform: scale(1) rotate(-1deg); color: #ff0; }
}
</style>
""", unsafe_allow_html=True)

# 🎆 GIF 폭발 모음
explosions = [
    "https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif",
    "https://media.giphy.com/media/26FL1soZ3STRDSLGU/giphy.gif",
    "https://media.giphy.com/media/l2Je3vTt0RZcMUM9q/giphy.gif",
    "https://media.giphy.com/media/j2mYvK6D6O3Hq/giphy.gif",
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
]

# 💣 MBTI 폭발형 직업 DB
mbti_jobs = {
    "INTJ": ["🧠 초지능 전략가", "📡 위성통제자", "💻 데이터 전사"],
    "INTP": ["🔬 고독한 논리 폭격기", "🤯 이론 혁신자", "📊 상상 엔지니어"],
    "ENTJ": ["👑 지배하는 CEO", "⚖️ 조직 설계자", "🧠 전략의 군주"],
    "ENTP": ["🧨 아이디어 폭격기", "🧬 혁신 테러리스트", "🚀 논쟁 퓨처리스트"],
    "INFJ": ["🔮 예언자급 전략가", "🕊 영적 리더", "📘 가치 설계사"],
    "INFP": ["🎭 감정 핵융합자", "📚 감성 혁명가", "💫 우주감성 시인"],
    "ENFJ": ["🦸 리더십 전사", "🎙 영혼의 스피커", "🤝 사회 변화 주도자"],
    "ENFP": ["🎤 열정폭탄 크리에이터", "🔥 감성 폭격기", "🪐 상상력 조종사"],
    "ISTJ": ["📋 체계화 폭주기관", "🏛 원칙의 수호자", "🛠 관리 마스터"],
    "ISFJ": ["🧺 사랑의 수호자", "👼 책임감 천사", "🛡 헌신 보호막"],
    "ESTJ": ["🧨 군단의 사령관", "📊 조직 설계 마스터", "💼 실무 파괴자"],
    "ESFJ": ["🎁 관계 설계 마법사", "🎀 친화력 폭탄", "🏡 공동체 돌보미"],
    "ISTP": ["🛠 현장형 해커", "⚙️ 기술 살인머신", "🕶 쿨가이 엔지니어"],
    "ISFP": ["🌸 감성 감각 핵무기", "🧁 비주얼 아티스트", "🎂 예술 베이커"],
    "ESTP": ["🏎 현실 질주 마스터", "💥 즉흥 폭탄", "🎯 행동 기반 CEO"],
    "ESFP": ["🎆 무대의 폭탄요정", "💃 리듬 지배자", "🦄 인생 파티 디렉터"]
}

# 💫 타이틀 폭발
st.markdown("""
<h1 style='text-align:center; font-size:64px;'>💣 MBTI 직업 추천기 9000 💣</h1>
<h2 style='text-align:center;'>🔥 너의 성격, 이제 날려버릴 시간이다 🔥</h2>
""", unsafe_allow_html=True)

# 🎯 사용자 입력
mbti = st.text_input("💥 네 MBTI를 입력해라! (예: ENFP)").strip().upper()

if mbti:
    st.image(random.choice(explosions), caption="💥 BOOOOM 💥", use_column_width=True)
    with st.spinner("☢️ 성격을 해체하고 있습니다..."):
        time.sleep(2)

    st.markdown("<hr style='border: 5px dashed red;'>", unsafe_allow_html=True)

    if mbti in mbti_jobs:
        st.markdown(f"<h2 style='text-align:center;'>🚀 {mbti}의 운명 직업 리스트! 💫</h2>", unsafe_allow_html=True)
        for job in mbti_jobs[mbti]:
            rainbow = random.choice(["#FF69B4", "#00FFFF", "#7FFF00", "#FFA500", "#FF0000", "#FFFF00"])
            st.markdown(f"<h3 style='color:{rainbow}; text-align:center;'>💥 {job}</h3>", unsafe_allow_html=True)

        st.snow()
        st.balloons()
    else:
        st.image("https://media.giphy.com/media/3o6ZsXsZ6J2t29F9XO/giphy.gif", use_column_width=True)
        st.error("💀 존재하지 않는 MBTI입니다! 진짜로 입력하셨습니까...")

