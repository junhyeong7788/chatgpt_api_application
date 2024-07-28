import streamlit as st
import pandas as pd

st.title('이것은 타이틀입니다.')

st.header('이것은 헤더를 입력할 수 있습니다.')

st.subheader('이것은 서브헤더 입니다.')

st.text('이것은 텍스트입니다.')

st.caption('이것은 캡션입니다.')

sample_code = '''
def function():
    print('hello, world!')
'''
st.code(sample_code, language='python')

st.markdown('스트림릿은 **마크다운**도 지원합니다.')
st.markdown('# 이것은 마크다운입니다.')

st.markdown("텍스트 색상 --> : green[초록색] 으로 그리고 **:blue[파란색]** 볼드체로 설정")
st.markdown(":green[$\sqrt{x^2+y^2}=1$]-> latex 문법으로 만든 수식")

