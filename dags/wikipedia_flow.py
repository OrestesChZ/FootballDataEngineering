from airflow import DAG
from datetime import datetime

dag = DAG(
    dag_id='wikipedia_flow',
    default_args={
        "owner": "Orestes Chiabra",
        "start_date": datetime(2025, 4, 24),
    },
    schedule_interval=None,
    catchup=False
)

#EXTRACTION
#PREPROCESSING
#WRITE