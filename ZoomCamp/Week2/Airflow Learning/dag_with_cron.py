from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_with_cron_v01',
    default_args=default_args,
    description='dag test with cron',
    start_date=datetime(2022,8,20, 2), # 5 days back
    schedule_interval='0 0 * * *' # runs the dag at exactly at 12:00 everyday
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command="echo this is a cron test"
    )