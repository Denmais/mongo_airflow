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