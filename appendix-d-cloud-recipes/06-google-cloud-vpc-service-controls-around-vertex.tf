resource "google_access_context_manager_service_perimeter" "ai" {
  parent = "accessPolicies/${var.access_policy_id}"
  name   = "accessPolicies/${var.access_policy_id}/servicePerimeters/ai_platform"
  title  = "ai_platform"

  status {
    resources = ["projects/${var.ai_project_number}"]
    restricted_services = [
      "aiplatform.googleapis.com",
      "storage.googleapis.com",
      "bigquery.googleapis.com",
    ]
  }
}
