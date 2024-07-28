import streamlit as st

st.set_page_config(
    page_title="Cool App",
    page_icon=":ice_cube:",
    layout="wide",
)

# 세로로 나누기
col1, col2, col3 = st.columns(3)

with col1:
    st.header('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with col2:
    st.header('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with col3:
    st.header('A owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')

st.video("https://www.youtube.com/watch?v=9N6HlDCW7qI")

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method:",
        ('Standard(5-15days)','Express(2-5days)')
    )
         
# tab
tab1, tab2, tab3 = st.tabs(['Cat', 'Dog', 'Owl'])

with tab1:
    st.header('A cat')
    st.image('https://static.streamlit.io/examples/cat.jpg')

with tab2:
    st.header('A dog')
    st.image('https://static.streamlit.io/examples/dog.jpg')

with tab3:
    st.header('A owl')
    st.image('https://static.streamlit.io/examples/owl.jpg')




