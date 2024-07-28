import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

st.title('차트 튜토리얼')

# 라인차트
st.markdown('## 라인차트')
chart_data = pd.DataFrame(
    np.random.randn(20,3),  #행20 by 열3의 랜덤한 데이터를 생성
    columns=['a','b','c']  #컬럼명을 a,b,c로 지정
)
st.line_chart(chart_data) #라인차트를 그림

# bar chart
st.markdown('## 막대차트')
st.bar_chart(chart_data)

# histogram -> matplotlib 라이브러리를 사용
st.markdown('## 히스토그램')
arr = np.random.normal(1,1,size=100) #평균1, 표준편차1, 사이즈100인 정규분포를 따르는 랜덤한 데이터를 생성
fig, ax = plt.subplots() #fig : 전체 그림, ax : 전체 그림 중 하나의 그림 #subplots : 여러개의 그림을 그릴 수 있음
ax.hist(arr, bins=20) #bins : 막대의 개수
st.pyplot(fig)

# plotly
st.markdown('## plotly')
fig = go.Figure(data = go.Scatter(
    x = [1,2,3,4],
    y = [10,20,30,40],
    mode = 'markers',
    marker = dict(size=[40,60,80,100], 
                  color=[0,1,2,3])
))
st.plotly_chart(fig,use_container_width=True)
