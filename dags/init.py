from airflow import DAG
from airflow.operators.python import PythonOperator
from pymongo import MongoClient
from generator.generator import (UserSessions, ProductPriceHistory,
                                 EventLogs, SupportTickets,
                                 UserRecommendations, ModerationQueue,
                                 SearchQueries)
from datetime import datetime

default_args = {
    'owner': 'student',
    'start_date': datetime(2024, 1, 1),
}


def mongo_data():
    client = MongoClient("mongodb://user:user@mongodb:27017/")
    mong = client["mydatabase"]
    mong.UserSessions.insert_many(UserSessions(10))
    mong.ProductPriceHistory.insert_many(ProductPriceHistory(10))
    mong.EventLogs.insert_many(EventLogs(10))
    mong.SupportTickets.insert_many(SupportTickets(10))
    mong.UserRecommendations.insert_many(UserRecommendations(10))
    mong.ModerationQueue.insert_many(ModerationQueue(10))
    mong.SearchQueries.insert_many(SearchQueries(10))


with DAG(
    'generate',
    default_args=default_args,
    schedule_interval=None
) as dag:
    data = PythonOperator(
        task_id="data",
        python_callable=mongo_data)
