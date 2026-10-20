resource "aws_cloudwatch_metric_alarm" "bedrock_throttles" {
  alarm_name          = "bedrock-assistant-throttles"
  namespace           = "AWS/Bedrock"
  metric_name         = "InvocationThrottles"
  dimensions = {
    ModelId = var.assistant_model_id
  }
  statistic           = "Sum"
  period              = 60
  evaluation_periods  = 5
  datapoints_to_alarm = 3
  threshold           = 20
  comparison_operator = "GreaterThanThreshold"
  treat_missing_data  = "notBreaching"
  alarm_description   = "Bedrock throttling for the assistant model. See runbook RB-AI-007."
  alarm_actions       = [aws_sns_topic.ai_platform_alerts.arn]
}
