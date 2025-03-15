from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from pymongo import MongoClient
import psycopg2


def UserSessionsTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong.UserSessions.find()
    print(1111111111111111111, collections)
    print(222222)
    for i in collections:
        print(i)
    for collection in collections:
        cursor.execute("""
            INSERT INTO UserSessions
            (session_id, user_id, start_time, end_time, device)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            collection['session_id'],
            collection['user_id'],
            collection['start_time'],
            collection['end_time'],
            collection['device']
        ))

    postg.commit()
    cursor.close()
    postg.close()


def ProductPriceHistoryTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['ProductPriceHistory'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO ProductPriceHistory
            (product_id, price_changes, current_price, currency)
            VALUES (%s, %s, %s, %s)
        """, (
            collection['product_id'],
            collection['price_changes'],
            collection['current_price'],
            collection['currency']
        ))

    postg.commit()
    cursor.close()
    postg.close()


def EventLogsTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['EventLogs'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO EventLogs
            (event_id, timestamp, event_type, details)
            VALUES (%s, %s, %s, %s)
        """, (
            collection['event_id'],
            collection['timestamp'],
            collection['event_type'],
            collection['details']
        ))

    postg.commit()
    cursor.close()
    postg.close()


def SupportTicketsTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['SupportTickets'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO SupportTickets
            (ticket_id, user_id, status, issue_type, messages, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (
            collection['ticket_id'],
            collection['user_id'],
            collection['status'],
            collection['issue_type'],
            collection['messages'],
            collection['created_at'],
            collection['updated_at']
        ))

    postg.commit()
    cursor.close()
    postg.close()


def UserRecommendationsTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['UserRecommendations'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO UserRecommendations
            (user_id, recommended_products, last_updated)
            VALUES (%s, %s, %s)
        """, (
            collection['user_id'],
            collection['recommended_products'],
            collection['last_updated']
        ))

    postg.commit()
    cursor.close()
    postg.close()


def ModerationQueueTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['ModerationQueue'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO ModerationQueue
            (review_id, user_id, product_id, review_text, rating, moderation_status, flags, submitted_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            collection['review_id'],
            collection['user_id'],
            collection['product_id'],
            collection['review_text'],
            collection['rating'],
            collection['moderation_status'],
            collection['flags'],
            collection['submitted_at'],
        ))

    postg.commit()
    cursor.close()
    postg.close()


def SearchQueriesTask():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    postg = psycopg2.connect(dbname="mydb", 
                             user="user", 
                             password="password", 
                             host="db", 
                             port="5432")
    cursor = postg.cursor()
    collections = mong['SearchQueries'].find()
    for collection in collections:
        cursor.execute("""
            INSERT INTO SearchQueries
            (query_id, user_id, query_text, timestamp, filters, results_count)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            collection['query_id'],
            collection['user_id'],
            collection['query_text'],
            collection['timestamp'],
            collection['filters'],
            collection['results_count'],
        ))

    postg.commit()
    cursor.close()
    postg.close()


default_args = {
    'owner': 'student',
    'start_date': datetime(2024, 1, 1),
}

with DAG(
    dag_id="replicate",
    start_date=datetime(2023, 12, 11),
    catchup=False,
    schedule_interval=None,
    tags=["replicate"],
) as dag:

    UserSessions = PythonOperator(
        task_id="UserSessions",
        python_callable=UserSessionsTask
    )

    ProductPriceHistory = PythonOperator(
        task_id="ProductPriceHistoryTask",
        python_callable=ProductPriceHistoryTask
    )

    EventLogs = PythonOperator(
        task_id="EventLogs",
        python_callable=EventLogsTask
    )

    SupportTickets = PythonOperator(
        task_id="SupportTickets",
        python_callable=SupportTicketsTask
    )

    UserRecommendations = PythonOperator(
        task_id="UserRecommendations",
        python_callable=UserRecommendationsTask
    )

    ModerationQueue = PythonOperator(
        task_id="ModerationQueue",
        python_callable=ModerationQueueTask
    )

    SearchQueries = PythonOperator(
        task_id="SearchQueries",
        python_callable=SearchQueriesTask
    )

UserSessions >> ProductPriceHistory >> EventLogs >> SupportTickets >> UserRecommendations >> ModerationQueue >> SearchQueries