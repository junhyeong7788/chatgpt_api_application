import streamlit as st
import pandas as pd


st.markdown('### PUSH버튼')
button = st.button('버튼을 눌러주세요 : ')

if button:
    st.write(' :blue[버튼]이 눌러졌습니다.')

st.markdown('### 박스문답')
title = st.text_input(
    label = '가고 싶은 멋진 곳이 있나요?',
    placeholder = '여행지를 입력해 주세요.'
)
st.write(f'당신이 입력한 여행지는 : :violet[{title}]')

st.markdown('### 비밀번호 입력창')
title = st.text_input(
    label = 'API 키를 입력해 주세요.',
    type = 'password'
)

st.markdown('### csv파일 다운로드')
df = pd.DataFrame({
    'first col': [1, 2, 3, 4],
    'second col': [10, 20, 30, 40]
})

st.download_button(
    label='csv로 다운로드',
    data=df.to_csv(),
    file_name='test.csv',
    mime='text/csv' #데이터 타입 지정
)

st.markdown('### 체크박스')
cb = st.checkbox('동의하십니까?')
if cb:
    st.write('동의하셨습니다.')

# radio button
st.markdown('### Radio버튼')
mbti = st.radio(
    '당신의 mbti는 무엇입니까?',
    ("ESFJ", "ENFJ", "선택지 없음"),
    index=None
)
if mbti == "ESFJ":
    st.write('당신은 :blue[ESFJ] 입니다.')
elif mbti == "ENFJ":    
    st.write('당신은 :blue[ENFJ] 입니다.')
elif mbti == "선택지 없음":
    st.write('당신에 대해 :red[알고 싶습니다.]:grey_exclamation:')
else:
    pass

# selectbox
st.markdown('### selectbox')
mbti = st.selectbox(
    '당신의 mbti는 무엇입니까?',
    ("ESFJ", "ENFJ", "선택지 없음"),
    index=None
)
if mbti == "ESFJ":
    st.write('당신은 :blue[ESFJ] 입니다.')
elif mbti == "ENFJ":    
    st.write('당신은 :blue[ENFJ] 입니다.')
elif mbti == "선택지 없음":
    st.write('당신에 대해 :red[알고 싶습니다.]:grey_exclamation:')
else:
    pass

# multiselect
st.markdown('### multiselect')
ops = st.multiselect(
    '당신이 좋아하는 음식을 선택해 주세요.',
    ['치킨', '피자', '햄버거', '족발', '보쌈'],
    ['치킨', '햄버거']
)
st.write(f'당신이 좋아하는 음식은 : :blue[{ops}]') 
#f : 문자보관법(문자열 포매팅), {}안에 변수를 바로 넣을수 있다.



st.markdown('# Streamlit 특징')
st.markdown('''어떤 변화가 있으면 전체코드가 다시 실행됨  
-> 문제점 : 전체 코드가 다시 실행되면서, 이전에 입력한 데이터가 초기화됨  
-> 해결방법 : 캐시를 사용하면 됨''' )