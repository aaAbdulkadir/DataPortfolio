from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_catchup_and_fill_v01',
    default_args=default_args,
    description='Catchup and fill',
    start_date=datetime(2022,8,20), # put the date 5 days back to go in the past
    schedule_interval='@daily',
    catchup=True # by default this is on
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo hello testing"
    )

# this script with the captchup runs the 5 days that I have missed from the date set