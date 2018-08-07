
-- WHERE restricts the result set before returning rows and HAVING restricts the result set after bringing all the rows.
-- So WHERE is faster. On SQL Standard compliant DBMSs in this regard,
--  only use HAVING where you cannot put the condition on a WHERE (like computed columns in some RDBMSs.)

SELECT
 COUNT(DISTINCT CASE WHEN event_name = 'article_shared' THEN event_id ELSE NULL
END) AS share_count,
 COUNT(DISTINCT CASE WHEN event_name = 'article_shared' THEN user_id ELSE NULL
END) AS user_share_count
FROM
 events_table
where country NOT IN('de','fr','be','gb');



-- I also thought in this way
SELECT COUNT(DISTINCT event_id) AS eid, COUNT(DISTINCT user_id) AS uid FROM events_table
WHERE event_name = 'article_shared' AND country NOT IN ('de','fr','be','gb');
