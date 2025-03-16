from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

import psycopg2


def connect_cursor():
    conn_dwh = psycopg2.connect(dbname="mydb",
                                user="user",
                                password="password",
                                host="db",
                                port="5432",
                                )
    return conn_dwh


def pg_mart_1():
    pg_conn = connect_cursor()
    with open("/opt/airflow/dags/sql/mart_users.sql") as file:
        sql_query = file.read()
    cur = pg_conn.cursor()
    cur.execute(sql_query)
    pg_conn.commit()
    pg_conn.close()


def pg_mart_2():
    pg_conn = connect_cursor()
    with open("/opt/airflow/dags/sql/mart_search.sql") as file:
        sql_query = file.read()
    cur = pg_conn.cursor()
    cur.execute(sql_query)
    pg_conn.commit()
    pg_conn.close()


with DAG(
    dag_id="mart",
    start_date=datetime(2023, 10, 11),
    catchup=False,
    schedule_interval=None,
    tags=["mart"],
) as dag:

    create_mart_users = PythonOperator(
        task_id="create_mart_1",
        python_callable=pg_mart_1
    )

    create_mart_search = PythonOperator(
        task_id="create_mart_2",
        python_callable=pg_mart_2
    )

create_mart_users >> create_mart_search
