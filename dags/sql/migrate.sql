BEGIN;

CREATE TABLE IF NOT EXISTS UserSessions (
    session_id text not null,
    user_id int NOT NULL,
    start_time timestamp NOT NULL,
    end_time timestamp NOT NULL,
    pages_visited VARCHAR(50),
    device int not null,
    actions VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS ProductPriceHistory (
    product_id int,
    price_changes text,
    current_price int,
    currency varchar(100)
);

CREATE TABLE IF NOT EXISTS EventLogs(
    event_id text not null,
    timestamp timestamp NOT NULL,
    event_type TEXT,
    details varchar(100)
);

CREATE TABLE IF NOT EXISTS SupportTickets (
    ticket_id text,
    user_id INT,
    status varchar(50),
    issue_type text,
    messages text,
    created_at timestamp,
    updated_at timestamp
);

CREATE TABLE if not exists UserRecommendations (
    user_id int,
    recommended_products text,
    last_updated timestamp
);

CREATE TABLE if not exists ModerationQueue (
    review_id text,
    user_id int,
    product_id int,
    review_text text,
    rating int,
    moderation_status varchar(100),
    flags text,
    submitted_at timestamp
);


CREATE TABLE if not exists SearchQueries (
    query_id text,
    user_id int,
    query_text text,
    timestamp timestamp,
    filters text,
    results_count int
);
COMMIT;