# Проект на Airflow и spark!

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

## Описание

Витрина data_mart используется для демонстрации данных о заказах, пользователях и продуктов, которые они заказали. В ней содержится полная информация для каждого отдельного заказа.

## Структура витрины

|     Поле          | Описание      |
| ------------      | ------------- |
|   order_id        | Номер заказа  |
|   order_total     | Номер заказа  |
|   status          | Статус заказа |
|   order_date      | Дата заказа   |
|   full_name       | Полное имя    |
|   email           | Почта         |
|   phone           | Телефон       |
|   loyalty_status  | Статус карты  |
|   product_name    | Имя продукта  |
|   category_name   | Имя категории |


## SQL код
```sql
CREATE TABLE data_mart AS 
SELECT
    o.order_id,
    o.total_amount AS order_total,
    o.status,
    o.order_date,
    CONCAT(u.first_name, " ", u.last_name) as full_name,
    u.email,
    u.phone,
    u.loyalty_status,
    p.name as product_name,
    pc.name as category_name
FROM
    orders o
JOIN
    users u ON o.user_id = u.user_id
LEFT JOIN
    orderDetails od ON o.order_id = od.order_id
LEFT JOIN
    products p ON od.product_id = p.product_id
LEFT JOIN
    productCategories pc ON p.category_id = pc.category_id;
```

