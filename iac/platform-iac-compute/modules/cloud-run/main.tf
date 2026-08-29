# ──────────────────────────────────────────────────────────────────────────────
# Domain IaC Repo: platform-iac-compute
# Module: modules/cloud-run
# Owner: Platform / DevEx Team
# ──────────────────────────────────────────────────────────────────────────────

variable "project_id" {
  type        = string
  description = "Target GCP Project ID"
}

variable "region" {
  type        = string
  default     = "us-central1"
  description = "GCP Deployment Region"
}

variable "service_name" {
  type        = string
  description = "Cloud Run service identifier"
}

variable "image" {
  type        = string
  description = "Artifact Registry container image URL"
}

variable "env_vars" {
  type        = map(string)
  default     = {}
  description = "Container environment variables"
}

resource "google_service_account" "runner_sa" {
  project      = var.project_id
  account_id   = "${var.service_name}-sa"
  display_name = "${var.service_name} Execution Service Account"
}

resource "google_cloud_run_v2_service" "service" {
  project  = var.project_id
  name     = var.service_name
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.runner_sa.email

    scaling {
      min_instance_count = 0
      max_instance_count = 1
    }

    containers {
      image = var.image

      resources {
        limits = {
          cpu    = "1000m"
          memory = "2Gi"
        }
      }

      dynamic "env" {
        for_each = var.env_vars
        content {
          name  = env.key
          value = env.value
        }
      }
    }
  }
}

output "service_url" {
  value       = google_cloud_run_v2_service.service.uri
  description = "Public or internal Cloud Run HTTPS URI"
}

output "service_account_email" {
  value       = google_service_account.runner_sa.email
  description = "Service account email for IAM delegation"
}
