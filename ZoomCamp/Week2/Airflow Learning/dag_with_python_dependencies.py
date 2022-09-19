from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def get_scikitlearn():
    import sklearn
    print(f"scikit-learn version: {sklearn.__version__}")

default_args = {
    'owner': 'Abdulkadir',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_dependencies_v02',
    description='this contains requirements.txt file with dependencies from dockerfile',
    start_date=datetime(2022,8,26, 2),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_scikitlearn
    )
    task1

