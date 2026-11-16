# ──────────────────────────────────────────────────────────────────────────────
# Domain IaC Repo: platform-iac-data
# Module: modules/cloud-sql-postgres
# Owner: Data / DBA Team
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

variable "instance_name" {
  type        = string
  description = "Cloud SQL instance identifier"
}

variable "database_version" {
  type        = string
  default     = "POSTGRES_15"
  description = "PostgreSQL engine version"
}

variable "tier" {
  type        = string
  default     = "db-f1-micro"
  description = "Machine tier for instance"
}

resource "google_sql_database_instance" "postgres" {
  project          = var.project_id
  name             = var.instance_name
  region           = var.region
  database_version = var.database_version

  settings {
    tier = var.tier

    backup_configuration {
      enabled    = true
      start_time = "03:00"
    }

    ip_configuration {
      ipv4_enabled    = true
      require_ssl     = true
    }
  }

  deletion_protection = false
}

resource "google_sql_database" "db" {
  project  = var.project_id
  name     = "${var.instance_name}-db"
  instance = google_sql_database_instance.postgres.name
}

output "instance_connection_name" {
  value       = google_sql_database_instance.postgres.connection_name
  description = "Cloud SQL instance connection string"
}

output "database_name" {
  value       = google_sql_database.db.name
  description = "Database name"
}
