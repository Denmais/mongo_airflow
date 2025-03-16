DROP TABLE IF EXISTS mart_search_data;
CREATE TABLE IF NOT EXISTS mart_search_data AS
SELECT
    user_id,
    COUNT(*) AS search_count,
    AVG(results_count) AS avg_results
FROM SearchQueries
GROUP BY user_id