resource "google_container_node_pool" "inference_gpu" {
  name     = "inference-l4"
  cluster  = google_container_cluster.ai_platform.id
  location = "asia-south1"

  autoscaling {
    min_node_count = 2
    max_node_count = 20
  }

  node_config {
    machine_type = "g2-standard-8"

    guest_accelerator {
      type  = "nvidia-l4"
      count = 1
      gpu_driver_installation_config {
        gpu_driver_version = "LATEST"
      }
    }

    reservation_affinity {
      consume_reservation_type = "ANY_RESERVATION"
    }

    taint {
      key    = "workload"
      value  = "inference"
      effect = "NO_SCHEDULE"
    }

    labels = {
      workload = "inference"
      team     = "ai-platform"
    }
  }

  management {
    auto_repair  = true
    auto_upgrade = true
  }
}
