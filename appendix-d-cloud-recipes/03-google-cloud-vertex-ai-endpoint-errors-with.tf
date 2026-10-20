resource "google_monitoring_alert_policy" "vertex_endpoint_errors" {
  display_name = "vertex-ranking-endpoint-errors"
  combiner     = "OR"

  conditions {
    display_name = "Online prediction errors above threshold"
    condition_threshold {
      filter = join(" AND ", [
        "resource.type = \"aiplatform.googleapis.com/Endpoint\"",
        "metric.type = \"aiplatform.googleapis.com/prediction/online/error_count\"",
        "resource.label.endpoint_id = \"${var.ranking_endpoint_id}\"",
      ])
      comparison      = "COMPARISON_GT"
      threshold_value = 20
      duration        = "180s"
      aggregations {
        alignment_period   = "60s"
        per_series_aligner = "ALIGN_SUM"
      }
    }
  }

  documentation {
    content = "Vertex AI endpoint errors. See runbook RB-AI-011."
  }
  notification_channels = [google_monitoring_notification_channel.ai_oncall.id]
}
