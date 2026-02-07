from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

from src.extract import fetch_weather
from src.transform import transform_weather_data
from src.load import upsert_dim_location, insert_fact_weather


default_args = {
    "owner": "airflow",
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
}


def etl_task():
    raw_data = fetch_weather(city="Dubai", api_key="97c293f674ef74b015d4004a1946f1fc")
    
   
    dim_data, fact_data = transform_weather_data(raw_data)
    
  
    location_id = upsert_dim_location(dim_data)
    insert_fact_weather(fact_data, location_id)


with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2026, 1, 25),
    schedule_interval="@hourly",
    catchup=False,
    default_args=default_args,
    tags=["weather"],
) as dag:

    run_etl = PythonOperator(
        task_id="etl_task",
        python_callable=etl_task,
    )
