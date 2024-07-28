import streamlit as st
import pandas as pd

st.title('데이터프레임 튜토리얼')

df = pd.DataFrame({
    'first col': [1, 2, 3, 4],
    'second col': [10, 20, 30, 40]
})

#데이터 프레임을 출력
st.dataframe(df,use_container_width=False) #true : 화면에 맞게 출력, false : 전체화면으로 출력

#고정테이블
st.table(df)

#메트릭
st.metric(label='온도', value='10도', delta='1.2도')
st.metric(label='삼성전자', value='61,000원', delta="-1,200원")
st.metric(label='성적', value='A', delta='B')

