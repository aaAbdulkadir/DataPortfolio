from datetime import datetime, timedelta
import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

"""HOMEWORK: collect yellow taxi data for the years 2019 and 2020"""

# base
URL_PREFIX = 'https://d37ci6vzurychx.cloudfront.net/trip-data'
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

# Yellow taxi data for years 2019 and 2020
YELLOW_TAXI_DATA = URL_PREFIX + '/yellow_tripdata_{{ execution_date.strftime(\'%Y-%m\') }}.parquet' # extract
OUTPUT_YELLOW_TAXI = AIRFLOW_HOME + '/yellow_taxi_{{ execution_date.strftime(\'%Y-%m\') }}.parquet' # save in docker
YELLOW_TAXI_FINAL = 'yellow_taxi_{{ execution_date.strftime(\'%Y-%m\') }}.parquet' # file name to save as in azure

# Azure connection
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
AZURE_STORAGE_CONNECTION_STRING = os.getenv('AZURE_STORAGE_CONNECTION_STRING')


def ingest_to_azure(local_file_path, container_name, file_name):
    from azure.storage.blob import BlobServiceClient

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
    print('Connection to Azure established.')

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
    print(f"\nUploading to Azure Storage as blob: {file_name}\n\t")

    # Upload the created file
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data)
    print('File uploaded sucessfully!')

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    default_args=default_args,
    dag_id='yellow_taxi_ingestion_hw_v1',
    description='ingest the yellow taxi data for years 2019 and 2020 for the homework',
    start_date=datetime(2019,1,1), # dag starts on this day
    end_date=datetime(2021,1,1),
    schedule_interval='0 9 1 * *' # 9am on the first day, once a month, the dag runs
) as dag:
    get_data = BashOperator(
        task_id='get_data',
        bash_command=f'curl -kL {YELLOW_TAXI_DATA} > {OUTPUT_YELLOW_TAXI}' 
        # save to AIRFLOW_HOME as without it, it saves in the temp folder which will be removed
    )
    airflow_to_azure = PythonOperator(
        task_id='yellow_taxi_to_azure',
        python_callable=ingest_to_azure,
        op_kwargs=dict(
            local_file_path=OUTPUT_YELLOW_TAXI,
            container_name=CONTAINER_NAME,
            file_name=YELLOW_TAXI_FINAL
        )
    )
