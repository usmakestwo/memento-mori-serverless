variable "UN" {}
variable "PW" {}

variable "ACCESS_TOKEN" {}
variable "ORG" {}

variable "project_name" {
  type = "string"
  default = "memento-mori-universitas"
}

variable "cloud_func_name_read" {
  type = "string"
  default = "universitas_read_courses"
}

variable "cloud_func_name_write" {
  type = "string"
  default = "universitas_write_courses"
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
  output_path = "dist/${var.cloud_func_name_read}.zip"
}

resource "google_storage_bucket" "retrieve_courses" {
  name = "retrieve_courses"
}

resource "google_storage_bucket_object" "read_archive" {
  name   = "${var.cloud_func_name_read}.zip"
  bucket = "${google_storage_bucket.retrieve_courses.name}"
  source = "${data.archive_file.gcp_read_courses_dist.output_path}"
}

resource "google_cloudfunctions_function" "read_function" {
  name                  = "gcp-read-courses-cf"
  description           = "A serverless function to retrieve records"
  region                = "us-east1"
  available_memory_mb   = 128
  source_archive_bucket = "${google_storage_bucket.retrieve_courses.name}"
  source_archive_object = "${google_storage_bucket_object.read_archive.name}"
  trigger_http          = true
  timeout               = 60
  entry_point           = "return_all_records"
  runtime               = "python37"

  environment_variables = {
    MONGO_USER = "${var.UN}"
    MONGO_PASS = "${var.PW}"
  }
}

# GOOGLE CLOUD FUNCTION - Write Records
data "archive_file" "gcp_write_courses_dist" {
  type        = "zip"
  source_dir  = "../gcp-functions/gcp-write-courses"
  output_path = "dist/${var.cloud_func_name_write}.zip"
}

resource "google_storage_bucket" "write_courses" {
  name = "write_courses"
}

resource "google_storage_bucket_object" "write_archive" {
  name   = "${var.cloud_func_name_write}.zip"
  bucket = "${google_storage_bucket.write_courses.name}"
  source = "${data.archive_file.gcp_write_courses_dist.output_path}"
}

resource "google_cloudfunctions_function" "write_function" {
  name                  = "gcp-write-courses-cf"
  description           = "A serverless function to create records"
  region                = "us-east1"
  available_memory_mb   = 128
  source_archive_bucket = "${google_storage_bucket.write_courses.name}"
  source_archive_object = "${google_storage_bucket_object.write_archive.name}"
  trigger_http          = true
  timeout               = 60
  entry_point           = "create_project"
  runtime               = "python37"

  environment_variables = {
    ACCESS_TOKEN = "${var.ACCESS_TOKEN}"
    ORG = "${var.ORG}"
    MONGO_USER = "${var.UN}"
    MONGO_PASS = "${var.PW}"
  }
}