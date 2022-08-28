from datetime import datetime, timedelta
import os
from ingest_script import ingest_callabe # imported function from ingest_script.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

URL_PREFIX = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
URL_TEMPLATE = URL_PREFIX + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
# gets current date in the format of 2022-01, like the link. As the DAG starts
# a year back, it will back fill once a month until the current month
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
OUTPUT_FILE_TEMPLATE = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
TABLE_NAME_TEMPLATE = 'ny_taxi_{{ execution_date.strftime(\'%Y_%m\') }}'
OUTPUT_FILE_TEMPLATE_CSV = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.csv'

# from .env file and docker compose
PG_HOST = os.getenv('PG_HOST')
PG_USER = os.getenv('PG_USER')
PG_PASSWORD = os.getenv('PG_PASSWORD')
PG_PORT = os.getenv('PG_PORT')
PG_DATABASE = os.getenv('PG_DATABASE')

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='local_ingestion_v21',
    description='ingest ny taxi data to airflow',
    start_date=datetime(2022,2,1), # dag starts on this day
    end_date=datetime(2022,3,1),
    schedule_interval='0 9 1 * *' # 9am on the first day, once a month, the dag runs
) as dag:
    get_data = BashOperator(
        task_id='get_data',
        bash_command=f'curl -kL {URL_TEMPLATE} > {OUTPUT_FILE_TEMPLATE}' 
        # save to AIRFLOW_HOME as without it, it saves in the temp folder which will be removed
    )
    ingest_data = PythonOperator(
        task_id='ingest_data_into_postgress', # import for ingest_script.py
        python_callable=ingest_callabe,
        op_kwargs=dict(
            user=PG_USER,
            password=PG_PASSWORD,
            host=PG_HOST,
            port=PG_PORT,
            db=PG_DATABASE,
            table_name=TABLE_NAME_TEMPLATE,
            parquet_name=OUTPUT_FILE_TEMPLATE,
            csv_name=OUTPUT_FILE_TEMPLATE_CSV
        )
    )
    get_data >> ingest_data
