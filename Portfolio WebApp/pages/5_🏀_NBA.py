import streamlit as st

# title
st.markdown("# NBA")
st.sidebar.markdown("# NBA")

# caption
caption = '''
    MAchine leanring classification and regression of NBA data.
'''
st.caption(caption)

overview, technologies, architectures, final_result = st.tabs(["Overview", "Technologies", "Architecture", "Final Result"])

with overview:
    overview_string = """
        This project
    """
    outcome_string = """
        From this project and everything that lead up to it i.e. the learning process,
        I learnt how to use...
    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    pass
with architectures:
    pass
with final_result:
    pass