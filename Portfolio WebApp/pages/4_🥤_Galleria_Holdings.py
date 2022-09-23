import streamlit as st

# title
st.markdown("# Galleria Holdings")
st.sidebar.markdown("# Galleria Holdings")

# caption
caption = '''
    An ETL pipeline which involves data warehousing for business analytical reporting.
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