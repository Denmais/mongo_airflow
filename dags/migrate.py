import psycopg2
from datetime import datetime

from airflow import DAG
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator


def connect_cursor():
    conn_dwh = psycopg2.connect(dbname="mydb",
                                user="user",
                                password="password",
                                host="db",
                                port="5432",
                                )
    return conn_dwh


def pg_init_migration():
    pg_conn = connect_cursor()
    with open("/opt/airflow/dags/sql/migrate.sql") as file:
        sql_query = file.read()
    cur = pg_conn.cursor()
    cur.execute(sql_query)
    pg_conn.commit()
    pg_conn.close()


default_args = {
    'owner': 'student',
    'start_date': datetime(2024, 1, 1),
}

with DAG('migrate',
         default_args=default_args,
         schedule_interval=None,
         catchup=False
         ) as dag:
    generate_report = PythonOperator(
        task_id='generate_report',
        python_callable=pg_init_migration)
