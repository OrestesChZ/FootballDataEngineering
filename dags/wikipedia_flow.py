from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from pipelines.wikipedia_pipeline import get_wikipedia_page
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sqlalchemy import extract

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

extract_data_from_wikipedia = PythonOperator(
    task_id="extract_data_from_wikipedia",
    python_callable=get_wikipedia_page,
    provide_context=True,
    op_kwargs={"url": "https://en.wikipedia.org/wiki/List_of_association_football_stadiums_by_capacity"},
    dag = dag

)

#PREPROCESSING
#WRITE