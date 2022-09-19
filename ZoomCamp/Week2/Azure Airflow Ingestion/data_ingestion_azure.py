from datetime import datetime, timedelta
import os, uuid
import pandas as pd

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

URL_PREFIX = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
URL_TEMPLATE = URL_PREFIX + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
# gets current date in the format of 2022-01, like the link. As the DAG starts
# a year back, it will back fill once a month until the current month
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
OUTPUT_FILE_TEMPLATE = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.parquet'
OUTPUT_FILE_TEMPLATE_CSV = AIRFLOW_HOME + '/output_{{ execution_date.strftime(\'%Y-%m\') }}.csv'
TABLE_NAME_TEMPLATE = 'ny_taxi_{{ execution_date.strftime(\'%Y_%m\') }}.csv'

CONTAINER_NAME = os.getenv('CONTAINER_NAME')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

def change_parquet_to_csv(parquet_name, csv_name):
    df = pd.read_parquet(parquet_name)
    df.to_csv(csv_name)
    print('File saved as csv and ready to ingest...')

def ingest_to_azure(local_file_path, container_name, csv_name):
    from azure.storage.blob import BlobServiceClient

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

    print('Connection to Azure established.')

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=csv_name)

    print(f"\nUploading to Azure Storage as blob: {csv_name}\n\t")

    # Upload the created file
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data)

    print('File uploaded sucessfully!')

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='local_ingestion_v05',
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
    parquet_to_csv = PythonOperator(
        task_id='parquet_to_csv',
        python_callable=change_parquet_to_csv,
        op_kwargs=dict(
            parquet_name=OUTPUT_FILE_TEMPLATE,
            csv_name=OUTPUT_FILE_TEMPLATE_CSV
        )
    )
    azure_ingestion = PythonOperator(
        task_id='ingest_data_into_azure', 
        python_callable=ingest_to_azure,
        op_kwargs=dict(
            local_file_path=OUTPUT_FILE_TEMPLATE_CSV,
            container_name=CONTAINER_NAME,
            csv_name=TABLE_NAME_TEMPLATE
        )
    )
    get_data >> parquet_to_csv >> azure_ingestion
