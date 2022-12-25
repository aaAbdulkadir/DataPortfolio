import streamlit as st

# @st.cache
st.set_page_config(
    page_title="Twwets",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.markdown("<h1 style='text-align: center;'>Tweets</h1>", unsafe_allow_html=True)