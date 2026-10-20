resource "azurerm_monitor_metric_alert" "aoai_throttles" {
  name                = "aoai-assistant-throttles"
  resource_group_name = azurerm_resource_group.ai.name
  scopes              = [azurerm_cognitive_account.aoai.id]
  description         = "Azure OpenAI throttling. See runbook RB-AI-007."
  severity            = 2
  frequency           = "PT1M"
  window_size         = "PT5M"

  criteria {
    metric_namespace = "Microsoft.CognitiveServices/accounts"
    metric_name      = "AzureOpenAIRequests"
    aggregation      = "Total"
    operator         = "GreaterThan"
    threshold        = 20

    dimension {
      name     = "StatusCode"
      operator = "Include"
      values   = ["429"]
    }
  }

  action {
    action_group_id = azurerm_monitor_action_group.ai_platform.id
  }
}
