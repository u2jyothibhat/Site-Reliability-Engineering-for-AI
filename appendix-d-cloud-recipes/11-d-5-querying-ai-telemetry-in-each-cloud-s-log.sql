SELECT
  jsonPayload.served_model AS served_model,
  COUNT(*) AS calls,
  COUNTIF(SAFE_CAST(jsonPayload.status AS INT64) >= 500) AS errors
FROM `ai-observability.app_logs.card_assistant_*`
WHERE timestamp > TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 HOUR)
GROUP BY served_model
ORDER BY calls DESC;
