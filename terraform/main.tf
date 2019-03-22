variable "UN" {}
variable "PW" {}

variable "project_name" {
  type = "string"
  default = "memento-mori-universitas"
}

variable "cloud_func_name" {
  type = "string"
  default = "universitas_read_courses"
}

provider "google" {
  project = "${var.project_name}"
  region  = "us-east4"
  zone    = "us-east4-a"
}


# GOOGLE CLOUD FUNCTION - Read records
data "archive_file" "gcp_read_courses_dist" {
  type        = "zip"
  source_dir  = "../gcp-functions/gcp-read-courses"
  output_path = "dist/${var.cloud_func_name}.zip"
}

resource "google_storage_bucket" "retrieve_courses" {
  name = "retrieve_courses"
}

resource "google_storage_bucket_object" "archive" {
  name   = "${var.cloud_func_name}.zip"
  bucket = "${google_storage_bucket.retrieve_courses.name}"
  source = "${data.archive_file.gcp_read_courses_dist.output_path}"
}

resource "google_cloudfunctions_function" "function" {
  name                  = "gcp-read-courses-cf"
  description           = "A serverless function to retrieve records"
  region                = "us-east1"
  available_memory_mb   = 128
  source_archive_bucket = "${google_storage_bucket.retrieve_courses.name}"
  source_archive_object = "${google_storage_bucket_object.archive.name}"
  trigger_http          = true
  timeout               = 60
  entry_point           = "return_all_records"
  runtime               = "python37"

  environment_variables = {
    MONGO_USER = "${var.UN}"
    MONGO_PASS = "${var.PW}"
  }
}