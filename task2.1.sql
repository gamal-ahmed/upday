SELECT
     COUNT(DISTINCT session_id) AS session_count,
     COUNT(DISTINCT user_id) AS user_id,
     SUM(CASE WHEN event_name = 'top_news_card_viewed' THEN 1 ELSE 0 END) AS
    tn_count
FROM
source_blacklisted_pdt sbp JOIN tn_count_pdt tcp ON sbp.session_id = tcp.session_id
 AND sbp.user_id = tcp.user_id
