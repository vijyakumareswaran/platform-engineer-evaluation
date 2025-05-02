from airflow import DAG
from airflow.decorators import task, task_group
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import json

default_args = {
    'retries': 3,
    'retry_delay': timedelta(minutes=2),
    'retry_exponential_backoff': True,
    'max_retry_delay': timedelta(minutes=10),
    'on_failure_callback': lambda ctx: print(f"Task failed! {ctx}")
}

with DAG(
    dag_id='etl_api_to_s3',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    default_args=default_args
) as dag:

    @task_group(group_id='extract_transform')
    def etl():
        @task(retries=2)
        def extract():
            response = requests.get("https://api.example.com/data", timeout=30)
            response.raise_for_status()
            return response.json()

        @task
        def transform(data):
            return [record for record in data if record.get("is_valid")]

    @task
    def write_to_file(data):
        with open("/tmp/transformed.json", "w") as f:
            json.dump(data, f)

    upload = LocalFilesystemToS3Operator(
        task_id='upload_to_s3',
        filename='/tmp/transformed.json',
        dest_key='etl/{{ ds }}.json',
        dest_bucket='my-bucket',
        replace=True
    )

    # Pipeline
    etl() >> write_to_file() >> upload