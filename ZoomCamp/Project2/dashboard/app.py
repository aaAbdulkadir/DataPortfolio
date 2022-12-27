import streamlit as st
# from streamlit_autorefresh import st_autorefresh
import time

st.set_page_config(
    page_title="STOCK-TWITTER ANALYTICS",
    layout="centered",
    initial_sidebar_state="expanded",
)


# title
st.markdown("<h1 style='text-align: center;'>Welcome</h1>", unsafe_allow_html=True)

with st.empty():
    for seconds in range(60):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")