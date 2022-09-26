import streamlit as st

# title
st.markdown("# NBA")
st.sidebar.markdown("# NBA")
st.sidebar.subheader("""Full projects on GitHub - [Classification](https://github.com/aaAbdulkadir/DataPortfolio/blob/main/ML%20Projects/NBA%20Classification.ipynb) and [Regression](https://github.com/aaAbdulkadir/DataPortfolio/blob/main/ML%20Projects/NBA%20MVP%20Prediction%20Regression.ipynb) """)


# caption
caption = '''
    MAchine leanring classification and regression of NBA data.
'''
st.caption(caption)

overview, technologies, architectures = st.tabs(["Overview", "Technologies", "Architecture"])

with overview:
    overview_string = """
        For this project, two machine learning models were created using NBA datasets, one being 
        regression, and the other, classification. The regression model consisted of prediciting 
        who would win the MVP award at the end of this current season using player performance statistics and this worked by predicting the MVP
        win share, which is a number that corresponds to a share of how many votes a player gets. 
        This was calculated using regression and then sorted to find the top voted. The classification model
        consisted of determining the position of a player based on their statistics. The project is explained thoroughly in
        their notebooks.
    """
    outcome_string = """
        From these projects, I learnt how to train and a test a machine 
        laerning model, and with that, make predictions for both regression and 
        classification. With the regression model, I learnt how to use the RMSE with cross 
        validation to evaluate the perforamnce of a regression model and compare them with
        eachother to find the best models. With that, I went onto use grid search for these
        top models to tune the models for an optimal regressor. Likewise, with classfication, I 
        compared the classification report i.e. precision, recall and F1-score using cross validation and
        again, used grid search to find the optimal classifier.


    """
    st.subheader('Outline')
    st.markdown(overview_string)
    st.subheader('Learning Outcome')
    st.markdown(outcome_string)
with technologies:
    st.subheader('Technologies Implemented')
    with st.expander("Python"):
        st.write("""
        Used pandas for data wrangling, matplotlib and seaborn 
        for visualisations, scikit-learn for machine learning 
        and beautifulsoup for data collection.
        """)
with architectures:
    st.subheader('Architectural Diagram')
    st.image('portfolio/pages/nba.png')