import streamlit as st

# total = 0

# num = st.text_input(" ")
# if num :
#     total = total+int(num)

# st.title(total)

if "total"  not in st.session_state: #not in : not in 연산자는 해당 키가 없을 때 True를 반환합니다.
    st.session_state["total"] = 0 #session_state에 total이라는 키가 없으면 0으로 초기화

num = st.text_input(" ") #입력받고 변수에 저장
if num : #num이 있다면
    st.session_state["total"] = st.session_state["total"] + int(num) #session_state에 total이라는 키에 입력받은 값을 더해줌

st.title(st.session_state["total"]) #session_state에 total이라는 키에 저장된 값을 출력