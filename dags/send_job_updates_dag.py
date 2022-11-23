from airflow.models import DAG
from airflow.operators.python import PythonOperator
from utils.remotejobs import get_jobs
from datetime import datetime

args = {
    'owner': 'Odomero Omokahfe',
    'start_date': datetime(2022, 11, 15),
    'schedule_interval': '@hourly' 
}

dag = DAG(
    dag_id='send-job-updates-dag',
    default_args=args
)

with dag:
    hello_world = PythonOperator(
        task_id='job-update',
        python_callable=get_jobs
    )

