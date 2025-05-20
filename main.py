import streamlit as st
import time

# 🎨 Streamlit 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기 💼✨", page_icon="🧠", layout="centered")

# 💡 MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["🧠 전략 컨설턴트", "📊 데이터 과학자", "💻 소프트웨어 엔지니어"],
    "INTP": ["🔬 연구원", "🤖 AI 엔지니어", "🧪 이론 물리학자"],
    "ENTJ": ["🏢 기업가", "📈 프로젝트 매니저", "⚖️ 변호사"],
    "ENTP": ["🎯 마케터", "🚀 창업가", "🎨 UX 디자이너"],
    "INFJ": ["🧘 상담가", "✍️ 작가", "📚 정책 분석가"],
    "INFP": ["🎭 예술가", "🧠 심리학자", "📖 문학가"],
    "ENFJ": ["👩‍🏫 교사", "📣 홍보 담당자", "🤝 HR 매니저"],
    "ENFP": ["📺 콘텐츠 기획자", "📸 크리에이터", "🗂 기획자"],
    "ISTJ": ["🧾 회계사", "👨‍⚖️ 판사", "🏛 행정 공무원"],
    "ISFJ": ["👩‍⚕️ 간호사", "👶 초등교사", "🤲 사회복지사"],
    "ESTJ": ["🪖 군인", "🧑‍💼 매니저", "💼 보험 설계사"],
    "ESFJ": ["🎧 고객 서비스", "🛍 영업 사원", "📂 행정 직원"],
    "ISTP": ["🔧 기계공", "🚑 응급 구조사", "✈️ 파일럿"],
    "ISFP": ["👨‍🍳 요리사", "🖼 그래픽 디자이너", "📷 사진작가"],
    "ESTP": ["🗣 영업 전문가", "🎉 이벤트 플래너", "🏋️ 운동선수"],
    "ESFP": ["🎤 배우", "🎙 MC", "👗 패션 스타일리스트"]
}

# 💫 타이틀과 설명
st.markdown("""
# 💼 MBTI 직업 추천기
### 너의 성격이 궁금해! 너에게 어울리는 직업은 과연...? 🌟
---
""")

# 🎯 MBTI 입력창
mbti_input = st.text_input("🔎 MBTI를 입력해주세요! (예: INFP, ENFP)", max_chars=4).upper()

if mbti_input:
    with st.spinner("✨ 성격 분석 중입니다..."):
        time.sleep(1.5)

    st.markdown("---")
    if mbti_input in mbti_jobs:
        st.markdown(f"""
        <div style='text-align:center'>
            <h2>🎉 {mbti_input} 유형에게 어울리는 직업은?</h2>
            <hr style='border: 2px dashed #ccc;' />
        </div>
        """, unsafe_allow_html=True)

        for job in mbti_jobs[mbti_input]:
            st.markdown(f"<h4 style='text-align:center; color:#4CAF50;'>{job}</h4>", unsafe_allow_html=True)
        
        st.balloons()
    else:
        st.markdown(f"""
        <div style='color:red; font-weight:bold;'>
            ⚠️ 잘못된 MBTI 유형입니다! 다시 입력해주세요. (예: INTJ, ESFP)
        </div>
        """, unsafe_allow_html=True)
