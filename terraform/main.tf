variable "project_name" {
  type = "string"
  default = "memento-mori-universitas"
}

provider "google" {
  project = "${var.project_name}"
  region  = "us-east4"
  zone    = "us-east4-a"
}

# BIG QUERY DATASET
resource "google_bigquery_dataset" "default" {
  dataset_id                  = "universitas_library"
  friendly_name               = "memento-mori-universitas-library"
  description                 = "Library for projects"
}

# BIG QUERY TABLE
resource "google_bigquery_table" "default" {
  dataset_id = "${google_bigquery_dataset.default.dataset_id}"
  table_id   = "projects"
  schema = "${file("bq/schema.json")}"
}