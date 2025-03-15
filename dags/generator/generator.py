from pymongo import MongoClient
import os
import random
import uuid
from datetime import datetime, timedelta
from faker import Faker


# client = MongoClient("mongodb://user:user@mongodb:27017")
# mong = client['mongodb']
fake = Faker()
action = ['open', 'close']
status = ["approved", "rejected"]
user_id = [x for x in range(1000)]
product_id = [x for x in range(500)]


# TODO Models
def UserSessions(count):
    return [{"session_id": str(uuid.uuid4()), "user_id": random.choice(user_id),
             "start_time": fake.date_time_this_year(), "end_time": fake.date_time_this_year(), 
             "pages_visited": [fake.uri() for _ in range(5)], "device": fake.user_agent(),
             "actions": random.choice(action) } for _ in range(count)]


def ProductPriceHistory(count):
    return [{"product_id": random.choice(product_id), "price_changes": 100, 
             "current_price": random.randint(1, 1000), 
             "currency": "RUB"} for _ in range(count)]


def EventLogs(count):
    return [{"event_id": str(uuid.uuid4()), "timestamp": fake.date_time_this_year(), 
             "event_type": random.choice(action), "details": 'some_details'} for _ in range(count)]


def SupportTickets(count):
    return [{"ticket_id": str(uuid.uuid4()), "user_id": random.choice(user_id),
             "status": random.choice(status), "issue_type": 'issue',
             "messages": 'message1', "created_at": fake.date_time_this_year(),
             "updated_at": fake.date_time_this_year().isoformat()} for _ in range(count)]


def UserRecommendations(count):
    return [{"user_id": random.choice(user_id), "recommended_products": 1,
             "last_updated": fake.date_time_this_year().isoformat()} for _ in range(count)]


def ModerationQueue(count):
    return [{"review_id": str(uuid.uuid4()), "user_id": random.choice(user_id),
             "product_id": random.choice(product_id),
             "review_text": fake.text(), "rating": random.randint(1, 5),
             "moderation_status": random.choice(status), "flags": '12123',
             "submitted_at": fake.date_time_this_year().isoformat()} for _ in range(count)]


def SearchQueries(count):
    return [{"query_id": str(uuid.uuid4()), "user_id": random.choice(user_id),
             "query_text": fake.sentence(), "timestamp": fake.date_time_this_year().isoformat(),
             "filters": 'flag', "results_count": random.randint(0, 50)} for _ in range(count)]



