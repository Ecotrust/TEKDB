provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-west-2"
}

variable "project_name" {
  description = "Project name used to prefix all resources"
  type        = string
  default     = "itkdb"
}

variable "bucket_name" {
  description = "S3 bucket name for Terraform state (must be globally unique)"
  type        = string
  default     = "itkdb-tf-state"
}

variable "ec2_instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.small"
}

variable "ec2_ami" {
  description = "Ubuntu 24.04 LTS AMI ID (region-specific — update if changing region)"
  type        = string
  # Ubuntu 24.04 LTS us-west-2 — check https://cloud-images.ubuntu.com/locator/ec2/ for your region
  default = "ami-06b527a1e4cb6f265"
}

variable "ssh_public_key" {
  description = "SSH public key to install on the EC2 instance (contents of your .pub file)"
  type        = string
  sensitive   = true
}

variable "allowed_ssh_cidr" {
  description = "CIDR block allowed to SSH into the EC2 instance (use your IP: x.x.x.x/32)"
  type        = string
}

# vars for Django environment variables
variable "django_secret_key" {
  description = "Secret key for Django application"
  type        = string
  sensitive   = true
}

variable "django_allowed_hosts" {
  description = "Comma-separated list of allowed hosts for Django"
  type        = string
}

variable "sql_db_name" {
  description = "Name of the PostgreSQL database"
  type        = string
}

variable "sql_db_user" {
  description = "PostgreSQL database user"
  type        = string
}

variable "sql_db_password" {
  description = "PostgreSQL database password"
  type        = string
  sensitive   = true
}

variable "sql_host" {
  description = "Hostname for the PostgreSQL database"
  type        = string
}

variable "sql_port" {
  description = "Port for the PostgreSQL database"
  type        = number
  default     = 5432
}

variable "web_ecr_image_uri" {
  description = "ECR image URI for the web application"
  type        = string
}

variable "proxy_ecr_image_uri" {
  description = "ECR image URI for the proxy"
  type        = string
}