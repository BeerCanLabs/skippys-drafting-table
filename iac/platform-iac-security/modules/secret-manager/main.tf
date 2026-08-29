# ──────────────────────────────────────────────────────────────────────────────
# Domain IaC Repo: platform-iac-security
# Module: modules/secret-manager
# Owner: SecOps / Identity Team
# ──────────────────────────────────────────────────────────────────────────────

variable "project_id" {
  type        = string
  description = "Target GCP Project ID"
}

variable "secret_id" {
  type        = string
  description = "Secret Manager secret identifier"
}

variable "accessor_service_account" {
  type        = string
  default     = ""
  description = "Service account email granted secretAccessor role"
}

resource "google_secret_manager_secret" "secret" {
  project   = var.project_id
  secret_id = var.secret_id

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_iam_member" "accessor" {
  count     = var.accessor_service_account != "" ? 1 : 0
  project   = var.project_id
  secret_id = google_secret_manager_secret.secret.secret_id
  role      = "roles/secretmanager.secretAccessor"
  member    = "serviceAccount:${var.accessor_service_account}"
}

output "secret_name" {
  value       = google_secret_manager_secret.secret.name
  description = "Full GCP Secret Manager secret resource path"
}
