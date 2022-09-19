from platform import architecture
import streamlit as st
import graphviz as graphviz

def cmc_project():

    caption = '''
        An automated ETL pipeline which transfers data from CoinMarketCap
        to Azure. 
    '''
    st.caption(caption)

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

        with st.expander('Apache Airflow'):
            st.write('Visualised the data via a dashboard.')

    with architectures:
        st.subheader('Architectural Diagram')

        terr = st.image('https://user-images.githubusercontent.com/72317571/189979496-bd6b6c8c-4819-40a7-9cc6-f9c36b276c35.png')

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
        st.write('Hello my name is [This is the link](testing.png) and I am')
        st.subheader('Results')
        st.image('https://user-images.githubusercontent.com/72317571/190189542-2839ba74-a45c-4b52-8407-2c9fed5ae7b2.png')

