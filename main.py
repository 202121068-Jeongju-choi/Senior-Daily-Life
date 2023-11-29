import streamlit as st

# 페이지 제목
st.title("노인 복지 웹사이트")

# 메뉴 선택
menu = ["홈", "복지정보", "이벤트", "연락처"]
choice = st.sidebar.selectbox("메뉴", menu)

# 홈 화면
if choice == "홈":
    st.write("노인 복지 웹사이트에 오신 것을 환영합니다! 여기에서 다양한 정보를 얻을 수 있습니다.")

# 복지정보 화면
elif choice == "복지정보":
    st.header("복지정보")
    st.write("여기에 복지 정보를 표시합니다.")

# 이벤트 화면
elif choice == "이벤트":
    st.header("이벤트")
    st.write("다가오는 이벤트 및 행사 정보를 표시합니다.")

# 연락처 화면
elif choice == "연락처":
    st.header("연락처")
    st.write("문의 및 연락처 정보를 표시합니다.")
