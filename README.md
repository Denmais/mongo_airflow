# Проект на Airflow и Mongodb!

# 1. Описание <a id=1></a>

Приложение позволяет управлять в airflow процессом репликации данных из postgres в mysql при помощи spark. Данные в постгрес можно дополнить при помощи генерации и записи через брокер Kafka.

---
# 2. Команды для запуска <a id=2></a>

Перед запуском необходимо склонировать проект:
```bash
git clone git@github.com:Denmais/mongo_airflow.git

```

Запускаем докер
```bash
docker compose up
```

# 2. Airflow <a id=2></a>

Вход расположен по адресу: http://localhost:8081/.
Используйте следующие учетные данные для входа:

## Описание DAGs

## generate

Генерация данных в Монго

## migrate

Создание таблиц в постгрес

## replicate

Репликация данных из монго в постгрес

# Аналитическая витрина <a id=2></a>

Витрина активности пользователей
## SQL код
```sql
DROP TABLE IF EXISTS mart_user_activity;
CREATE TABLE IF NOT EXISTS mart_user_activity AS
SELECT
    us.user_id,
    COUNT(us.session_id),
    COUNT(DISTINCT sq.query_id) as query_count,
    COUNT(DISTINCT st.ticket_id) as ticket_count,
    COUNT(DISTINCT ur.recommended_products) as rec_count
FROM UserSessions as us
LEFT JOIN UserRecommendations as ur ON ur.user_id = us.user_id
LEFT JOIN SupportTickets as st ON st.user_id = us.user_id
LEFT JOIN SearchQueries as sq ON sq.user_id = us.user_id
GROUP BY us.user_id;
```

Витрина поисковых запросов
```sql
DROP TABLE IF EXISTS mart_search_data;
CREATE TABLE IF NOT EXISTS mart_search_data AS
SELECT
    user_id,
    COUNT(*) AS search_count,
    AVG(results_count) AS avg_results
FROM SearchQueries
GROUP BY user_id
```