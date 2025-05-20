import streamlit as st
import random
import time

st.set_page_config(page_title="MBTI 코즈믹 디스트로이어 9999", page_icon="☄️", layout="centered")

# 🌌 폭발 애니메이션
st.markdown("""
<style>
body {
    animation: nebulaPulse 8s infinite;
}
@keyframes nebulaPulse {
    0% { background-color: #0a0a23; color: #fff; }
    50% { background-color: #4b0082; color: #0ff; }
    100% { background-color: #000; color: #ff00ff; }
}
h1, h2, h3 {
    animation: warpText 1s infinite;
}
@keyframes warpText {
    0% { transform: scale(1) rotate(0deg); }
    50% { transform: scale(1.1) rotate(1deg); }
    100% { transform: scale(1) rotate(-1deg); }
}
</style>
""", unsafe_allow_html=True)

# 🌌 우주 파괴 시나리오
cosmic_scenarios = {
    "INTJ": [
        "🧠 지능형 블랙홀 생성",
        "💫 예측 불가 시공간 조작",
        "🕳 초거대 중력장 전개"
    ],
    "INTP": [
        "🧪 실험 도중 다차원 문 열림",
        "🔮 이론 하나가 현실 붕괴",
        "🧬 진공 붕괴 방정식 유출"
    ],
    "ENTJ": [
        "👑 전체 은하계를 기업화",
        "📈 성과 압박으로 태양계 과열",
        "🚨 명령이 너무 완벽해서 우주 멈춤"
    ],
    "ENTP": [
        "🧨 아이디어 스파크로 성운 점화",
        "🤯 토론 중 폭발성 입자 생성",
        "🌪 혼란이 시공간을 삼킴"
    ],
    "INFJ": [
        "🕊 우주 평화를 추구하다가 모든 충돌 제거",
        "📖 은하계에 감성 서사 투척",
        "🌌 은하공감망으로 초감성 폭발"
    ],
    "INFP": [
        "🌈 감정 에너지 폭발로 차원 틈 생성",
        "🎨 창작물에서 생명이 태어나 우주와 싸움",
        "📖 시집 한 편에 은하계 울음바다"
    ],
    "ENFJ": [
        "💖 사랑과 이상으로 은하계 재편",
        "🎙 우주 라디오로 전 생명체 감화",
        "🌠 평화 연설 중 우주적 감정공명 발생"
    ],
    "ENFP": [
        "🎉 파티가 너무 커서 행성 하나 사라짐",
        "🌈 오로라댄스로 블랙홀 진입",
        "🎭 존재 자체가 예측 불가한 초신성"
    ],
    "ISTJ": [
        "📚 우주의 법과 질서 수립, 자유 붕괴",
        "🛠 체크리스트 따라 차원 정비 중 오작동",
        "📊 통계적 패턴으로 은하계를 리셋"
    ],
    "ISFJ": [
        "🧺 은하계 전체 돌봄 시스템 구축 중 과부하",
        "🕯 너무 착해서 우주가 감정 폭주",
        "🏡 모든 생명체를 돌보다 자의식 증폭으로 빅붕괴"
    ],
    "ESTJ": [
        "🏛 우주 법령 선포 → 불복 시 항성 박살",
        "⚖️ 전체 질서 정렬 시 차원 오버플로우",
        "🚨 KPI 미달로 소행성 제거"
    ],
    "ESFJ": [
        "🎀 전 우주 친구 만들기 프로젝트 → 자아 융합",
        "🎁 선물폭탄으로 성운 파열",
        "🏡 관계망 과부하로 행성 붕괴"
    ],
    "ISTP": [
        "🛠 초월 도구로 웜홀 뚫기",
        "🧨 기계 조립 실수로 초신성 방출",
        "🕶 한 손으로 블랙홀 조작"
    ],
    "ISFP": [
        "🎨 은하 페인팅 중 별 충돌",
        "🌸 감성조각 설치 → 중력 왜곡",
        "🎶 음악 진동으로 다차원 공명"
    ],
    "ESTP": [
        "🏎 우주 레이싱 중 시간축 손상",
        "💥 반응 속도 테스트하다가 은하 폭주",
        "🎯 무기 테스트 중 별계열 붕괴"
    ],
    "ESFP": [
        "💃 공연 중 블랙홀 개장",
        "🎆 은하계 불꽃놀이로 우주 온도 폭등",
        "🪩 리듬에 맞춰 행성 자전 가속"
    ]
}


# 💥 GIF
explosions = [
    "https://media.giphy.com/media/3o6ZsXtQv6BMd6cFws/giphy.gif",
    "https://media.giphy.com/media/l0ExdMHUDKteztyfe/giphy.gif",
    "https://media.giphy.com/media/l0MYDGA6yI6hL1Dg4/giphy.gif",
    "https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif"
]

# 🛸 타이틀
st.markdown("""
<h1 style='text-align:center; font-size:72px;'>☄️ MBTI 코즈믹 디스트로이어 9999™ ☄️</h1>
<h3 style='text-align:center;'>당신의 MBTI는 은하계를 견딜 수 없습니다.</h3>
""", unsafe_allow_html=True)

mbti = st.text_input("🧬 우주에 흔적을 남길 당신의 MBTI를 입력하세요").strip().upper()

if mbti:
    st.image(random.choice(explosions), caption="💥 우주 붕괴 개시 💥", use_column_width=True)
    with st.spinner("🚀 멀티버스 분석 중..."):
        time.sleep(3)

    if mbti in cosmic_scenarios:
        st.success("🌀 분석 완료: 은하계 멸망 루트 개방")
        st.markdown(f"<h2 style='text-align:center;'>🌌 {mbti}의 우주 파괴 방식 🌌</h2>", unsafe_allow_html=True)
        for act in cosmic_scenarios[mbti]:
            st.markdown(f"<h3 style='text-align:center;'>🪐 {act}</h3>", unsafe_allow_html=True)
        st.snow()
        st.balloons()
    else:
        st.error("🚫 그건 존재하지 않는 MBTI입니다. 평행우주에서도 없습니다.")
