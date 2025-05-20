import streamlit as st
import time
import random

# 🔥 페이지 세팅
st.set_page_config(page_title="MBTI 광기 직업 추천기 🧨", page_icon="🌀", layout="centered")

# 🎉 배경 gif를 위한 스타일 해킹 (조심!)
st.markdown("""
<style>
body {
    background-image: url("https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif");
    background-size: cover;
    background-attachment: fixed;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 🤯 MBTI 직업 폭격 리스트
mbti_jobs = {
    "INTJ": ["🧠 천재 전략가", "🧮 데이터 마법사", "💻 프로그래밍 군주"],
    "INTP": ["🔬 고독한 연구광", "🤖 AI 마스터", "📡 사이언스 아인슈타인"],
    "ENTJ": ["🦁 CEO 제왕", "📈 사업 폭격기", "⚖️ 법률의 지배자"],
    "ENTP": ["🚀 아이디어 분출가", "🎭 창의력 미친놈", "🎨 UX의 반란자"],
    "INFJ": ["🔮 운명을 꿰뚫는 예언자", "📚 내면 탐색가", "🕊 감성 전략가"],
    "INFP": ["🎨 감성 폭발 예술가", "💌 사랑 전달자", "🧘 영혼의 치유자"],
    "ENFJ": ["🦸 히어로 리더", "💬 대중의 영혼 스피커", "🤝 사람 붙잡는 마법사"],
    "ENFP": ["🎆 불꽃 에너지 크리에이터", "📢 열정의 전도사", "🌈 세상 밝히는 아이디어 뱅크"],
    "ISTJ": ["📋 규칙 수호자", "💼 냉철한 정리왕", "🏛 시스템의 척추"],
    "ISFJ": ["🧺 따뜻함의 끝판왕", "🌸 감성 철벽 수비수", "👼 세상에서 가장 착한 인간"],
    "ESTJ": ["🧨 지휘관", "💣 조직 마스터", "💸 현실 폭격기"],
    "ESFJ": ["🎁 선물 같은 인간", "🌞 미소천사", "🫂 사랑의 마케터"],
    "ISTP": ["🔧 메카닉 천재", "🛠 인생 해결사", "🚁 파일럿 느낌 충만"],
    "ISFP": ["🧑‍🎨 감각 천재", "📷 인스타 감성왕", "🎂 감성 셰프"],
    "ESTP": ["⚡️ 액션 히어로", "📣 하이텐션 CEO", "🏎 속도광 기획자"],
    "ESFP": ["🌟 연예인 급 존재감", "👠 무대 위의 여왕", "💃 라이브 감성 폭발"]
}

# 🎇 헤드라인 폭주
st.markdown("""
<h1 style='text-align:center; font-size: 60px; color: #FF00FF;'>🌪 MBTI 광기의 직업 추천기 🌪</h1>
<h3 style='text-align:center; color: gold;'>🤯 여기는 MBTI와 직업의 카오스! 당신의 운명을 불태워드립니다 🔥</h3>
""", unsafe_allow_html=True)

# 🎤 입력창
mbti_input = st.text_input("🌈 당신의 MBTI를 입력하세요! (예: ENFP)", max_chars=4).upper()

# 🔮 출력
if mbti_input:
    with st.spinner("🌀 당신의 혼돈을 분석 중입니다..."):
        time.sleep(2)

    st.markdown("<hr style='border: 3px dotted #FF1493;' />", unsafe_allow_html=True)

    if mbti_input in mbti_jobs:
        st.markdown(f"""
        <h2 style='text-align:center; color:#00FFFF; font-size: 45px;'>🎊 {mbti_input} 유형의 직업 카오스 대공개! 🎊</h2>
        """, unsafe_allow_html=True)

        for job in mbti_jobs[mbti_input]:
            color = random.choice(["#FF69B4", "#7FFF00", "#FFD700", "#00CED1", "#FF4500"])
            st.markdown(f"<h3 style='color:{color}; text-align:center;'>{job}</h3>", unsafe_allow_html=True)

        st.snow()  # 눈 대신 혼돈 느낌
        st.balloons()  # 폭죽 느낌
    else:
        st.markdown("""
        <h3 style='color: red; text-align: center;'>🚫 잘못된 MBTI 유형입니다! 다시 확인해주세요! 🤖</h3>
        """, unsafe_allow_html=True)
