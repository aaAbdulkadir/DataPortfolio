import streamlit as st
import graphviz as graphviz
import pandas as pd
from datetime import datetime

# title
st.markdown("# CoinMarketCap")
st.sidebar.markdown("# Project 1")

# caption
caption = '''
    An automated ETL pipeline which transfers data from CoinMarketCap to Azure. 
'''
st.caption(caption)

# main
overview, technologies, architectures, final_result = st.tabs(["Overview", "Technologies", "Architecture", "Final Result"])

with overview:
    overview_string = """
        This project consisted of working with batch data to create a dashboard 
        for monitoring crypto currencies on a daily basis. 
        The data was collected from CoinMarketCap (a crypto currency website) 
        and transformed to produce useful datasets and charts to create a visual
        dashboard for daily monitoring.
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
    st.subheader('Technologies Implemented')

    with st.expander("Terraform"):
        st.write("Created the Azure infrastructure using code. This consisted of creating a resource group, storage accoumt, a blob container, a virtual machine and everything that comes with it.")

    with st.expander('Azure'):
        st.write('Used Azure to store the data and run a virtual machine to host the pipeline on Docker.')

    with st.expander('Docker'):
        st.write('Hosted Airflow via docker-compose and all the dependencies needed for Spark and Python via Dockerfile.')
    
    with st.expander('Apache Airflow'):
        st.write('Created a pipeline that governed the process of moving the data.')

    with st.expander('Apache Spark'):
        st.write('Transformed the raw data into useful datasets.')

    with st.expander('PowerBI'):
        st.write('Visualised the data via a dashboard.')

with architectures:
    st.subheader('Architectural Diagram')

    terr = st.image('https://user-images.githubusercontent.com/72317571/191299277-89d27c12-c84d-4f06-83ab-559189b913af.png')

    st.text("")
    st.text("")
    st.text("")


    st.subheader('Flow Chart')
    graph = graphviz.Digraph()
    st.graphviz_chart('''
        digraph {
            Terraform -> Azure -> VM
            VM -> Docker
            Docker -> Spark
            Spark -> Airflow
            Docker -> Airflow
            Airflow -> CoinMarketCap
            CoinMarketCap -> Airflow
            Airflow -> AzureBlobStorage
            AzureBlobStorage -> PowerBI
        }
    ''')


with final_result:
    
    st.write('')

    # --- data collection ---

    # load data
    date = pd.read_csv('portfolio/pages/data/cmc/Date.csv')

    date = date.rename(columns={'Earliest last_updated':'date_collected'})
    date['date_collected'] = pd.to_datetime(date['date_collected'])
    date_formatted = date['date_collected'][0]
    day, month, year = date_formatted.day, date_formatted.month, date_formatted.year
    st.subheader(f"Snapshot of Data: {day}/{month}/{year}")


    st.write("""
        An important metric to monitor is the top cryptocurrency coins as their performance
        are an indication to the rest of the market. The following coins are top coins which 
        also are coins of interest...
    """)
    

    # --- metrics ---

    # load data
    performance = pd.read_csv('portfolio/pages/data/cmc/fluctuations.csv')
    
    # 24 hour performance
    performance_24h = performance[performance['Time Frame'] == '24h']

    # get price
    summary = pd.read_csv('portfolio/pages/data/cmc/pricechart.csv')
    summary = summary[summary['Coin'].isin(performance_24h['Coin'])]

    # merge tables
    summarised = summary.merge(performance_24h, how='left')

    # card formation
    def cards(coin):
        df = summarised[summarised['Coin'] == coin].reset_index(drop=True)
        return df['Coin'][0], df['Price'][0], df['Percentage Change'][0]

    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric(label=cards('Bitcoin')[0], value=cards('Bitcoin')[1], delta=cards('Bitcoin')[2])
    col2.metric(label=cards('Ethereum')[0], value=cards('Ethereum')[1], delta=cards('Ethereum')[2])
    col3.metric(label=cards('BNB')[0], value=cards('BNB')[1], delta=cards('BNB')[2])
    col4.metric(label=cards('Cardano')[0], value=cards('Cardano')[1], delta=cards('Cardano')[2])

    st.write('')

    # -- performance of these top coins
    coins_of_interest = performance[performance['Coin'].isin(['Bitcoin', 'Ethereum', 'BNB', 'Cardano'])]
    st.line_chart(data=coins_of_interest)
    




    