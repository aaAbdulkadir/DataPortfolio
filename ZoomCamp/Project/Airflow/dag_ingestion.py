from asyncio import tasks
from datetime import datetime, timedelta
import os
from collect_data import API_data, bs4_data
from ingest_to_azure import ingest_to_azure
from transform_data import pyspark_transformations

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# FILES SAVED LOCALLY
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
API_OUTPUT_FILE = AIRFLOW_HOME + '/api_data.parquet'
BS4_OUTPUT_FILE = AIRFLOW_HOME + '/bs4_data.parquet'

# OUTPUT FILES
AZURE_FILE_NAMES = ['top_ranked.csv', 'top_ranked_fluctuations.csv',
                    'best_performing_90_days.csv', 'price_chart.csv', 'top_gainers.csv',
                    'top_losers.csv', 'bs4_df.csv']

# from .env file and docker compose
MY_API_KEY = os.getenv('MY_API_KEY')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='ingestinator_v1',
    description='ingest data',
    start_date=datetime.today()-timedelta(days=2),
    schedule_interval='0 9 * * *' # 9am everyday
) as dag:
    collect_API_data = PythonOperator(
        task_id='collect_api_dataset',
        python_callable=API_data,
        op_kwargs=dict(
            api_key = MY_API_KEY,
            output_file = API_OUTPUT_FILE
        )
    )
    collect_bs4_data = PythonOperator(
        task_id='collect_bs4_dataset',
        python_callable=bs4_data,
        op_kwargs=dict(
            output_file = BS4_OUTPUT_FILE
        )   
    )
    transform_dataset = PythonOperator(
        task_id='pyspark_transformations',
        python_callable=pyspark_transformations,
        op_kwargs=dict(
            api_filepath = API_OUTPUT_FILE,
            bs4_filepath = BS4_OUTPUT_FILE,
            airflow_home = AIRFLOW_HOME
        )
    )
    data_to_azure = PythonOperator(
        task_id='data_to_azure',
        python_callable=ingest_to_azure,
        op_kwargs=dict(
            local_file_path = AIRFLOW_HOME,
            conn_string = AZURE_STORAGE_CONNECTION_STRING,
            container_name = CONTAINER_NAME,
            csv_name = AZURE_FILE_NAMES
        )
    )
    delete_data_locally = BashOperator(
        task_id='delete_data_locally',
        bash_command=f"rm -r {API_OUTPUT_FILE} {BS4_OUTPUT_FILE} {AIRFLOW_HOME}/output"
    )

    [collect_API_data, collect_bs4_data] >> transform_dataset >> data_to_azure >> delete_data_locally
