import streamlit as st

# 페이지 제목
st.title("노인 복지 웹사이트")

# 메뉴 선택
menu = ["소식", "오늘의 건강", "이야기 나누기", "우리 가족"]
choice = st.sidebar.selectbox("메뉴", menu)

# 홈 화면
if choice == "소식":
    st.write("환영합니다! 오늘도 행복한 하루가 되길 응원합니다.")

# 복지정보 화면
elif choice == "오늘의 건강":
    st.header("오늘의 건강")
    st.write("오늘 당신은 어떤가요? 어디 아프지는 않으신가요?")

# 이벤트 화면
elif choice == "이야기 나누기":
    st.header("이야기 나누기")
    st.write("혼자 힘드신 부분은, 함께 해결할 수 있어요.")

# 연락처 화면
elif choice == "우리 가족":
    st.header("우리 가족")
    st.write("오늘 우리 가족, 손주 손녀는 잘 지내고 있을까요?")
