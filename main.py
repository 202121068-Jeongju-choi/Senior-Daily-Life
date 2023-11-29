import streamlit as st

# 페이지 제목
st.title("도담도담 - 은퇴 후의 삶을 더욱 윤택하게.")

# 메뉴 선택
menu = ["소식", "오늘의 건강", "이야기 나누기", "우리 가족"]
choice = st.sidebar.selectbox("메뉴", menu)

# 소식 화면
if choice == "소식":
    st.write("환영합니다! 오늘도 행복한 하루가 되길 응원합니다.")
    
    # 소식 화면에 이미지 추가
    image_url = "https://raw.githubusercontent.com/202121068-Jeongju-choi/Senior-Daily-Life/8f4ab7cfc78808c316ac1f232d7b501a3674588a/%EC%BA%A1%EC%B2%98.PNG"
    caption_text = ""
    st.image(image_url, caption=caption_text, use_column_width=True)

# 오늘의 건강 화면
elif choice == "오늘의 건강":
    st.header("오늘의 건강")
    st.write("오늘 당신은 어떤가요? 어디 아프지는 않으신가요?")

# 이야기 나누기 화면
elif choice == "이야기 나누기":
    st.header("이야기 나누기")
    st.write("혼자 힘드신 부분은, 함께 해결할 수 있어요.")

# 우리 가족 화면
elif choice == "우리 가족":
    st.header("우리 가족")
    st.write("오늘 우리 가족, 손주 손녀는 잘 지내고 있을까요?")
