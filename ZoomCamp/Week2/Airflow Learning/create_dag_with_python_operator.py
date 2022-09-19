from datetime import datetime, timedelta
from logging.config import valid_ident

from airflow import DAG
from airflow.operators.python import PythonOperator

def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name = ti.xcom_pull(task_ids='get_name', key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    print(f"hello, my name is {first_name} {last_name} and I am {age} years old.") 
    # op_kwargs in python operator

def get_name(ti):
    ti.xcom_push(key='first_name', value='Jerry') # max size of xcom is 48kb
    ti.xcom_push(key='last_name', value='Springer')

def get_age(ti):
    ti.xcom_push(key='age', value=21)

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}
with DAG(
    default_args=default_args,
    dag_id='our_dag_with_python_operator_v013',
    description='this is the first dag with python operator',
    start_date=datetime(2022,8,25, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        # op_kwargs={'age':'20'}
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )
    [task2, task3] >> task1