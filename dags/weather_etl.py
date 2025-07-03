from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import random
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
}

dag = DAG(
    'weather_etl_test',
    default_args=default_args,
    description='DAG de test pour simuler un ETL météo',
    schedule_interval='@daily',
    catchup=False,
)

def extract_weather():
    # Données météo simulées
    return {
        'city': 'Paris',
        'temp': round(random.uniform(15, 30), 2),
        'humidity': random.randint(40, 90),
        'description': random.choice(['sunny', 'cloudy', 'rainy']),
        'timestamp': datetime.utcnow().isoformat(),
    }

def transform_data(ti):
    data = ti.xcom_pull(task_ids='extract_weather')
    df = pd.DataFrame([data])
    df['temp_fahrenheit'] = df['temp'] * 9/5 + 32
    ti.xcom_push(key='transformed_df', value=df.to_dict())

def load_data(ti):
    df_dict = ti.xcom_pull(task_ids='transform_data', key='transformed_df')
    df = pd.DataFrame.from_dict(df_dict)
    
    output_dir = '/opt/airflow/dags/output'
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, 'weather_paris_test.csv')
    df.to_csv(file_path, index=False)
    print(f'Data saved to {file_path}')

extract = PythonOperator(
    task_id='extract_weather',
    python_callable=extract_weather,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

load = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

extract >> transform >> load
