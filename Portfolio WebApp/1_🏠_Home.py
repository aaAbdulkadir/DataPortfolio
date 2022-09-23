import streamlit as st

st.set_page_config(
    page_title="Abdulkadir Portfolio WebApp",
    layout="centered",
    initial_sidebar_state="expanded",
)

# title
st.title('Welcome to My Portfolio WebApp!')

with st.sidebar:
    st.markdown("# Home")