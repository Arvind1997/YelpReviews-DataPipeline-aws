from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.date import days_ago
from datetime import datetime
from yelp_etl import etl_airflow_run

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2020, 11, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'yelp_dag',
    default_args = default_args,
    description = 'Yelp Restaurants and Bars information'
)

run_etl = PythonOperator(
    task_id = 'process_yelp_etl',
    python_callable = etl_airflow_run,
    dag = dag
)