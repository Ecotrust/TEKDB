provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  description = "AWS region to deploy into"
  type        = string
  default     = "us-west-2"
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
  description = "Ubuntu 26.04 LTS AMI ID (region-specific — update if changing region)"
  type        = string
  # Ubuntu 26.04 LTS us-west-2 — check https://cloud-images.ubuntu.com/locator/ec2/ for your region
  default = "ami-029e1938545a0ba14"
}
variable "project_name" {
  description = "Project name"
  type        = string
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

variable "django_secret_key" {
  description = "Django secret key"
  type        = string
  sensitive   = true
}

variable "django_allowed_hosts" {
  description = "Django allowed hosts"
  type        = string
}

variable "sql_db_name" {
  description = "PostgreSQL database name"
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
  description = "PostgreSQL host"
  type        = string
}

variable "sql_port" {
  description = "PostgreSQL port"
  type        = number
}

variable "web_ghcr_image_uri" {
  description = "Web Docker image GHCR URI"
  type        = string
}

variable "proxy_ghcr_image_uri" {
  description = "Proxy Docker image GHCR URI"
  type        = string
}

variable "celery_broker_url" {
  description = "Celery broker URL"
  type        = string
}

variable "gis_user_password" {
  description = "GIS user password"
  type        = string
  sensitive   = true
}

variable "domain_names" {
  description = "Comma-separated list of domain names"
  type        = string
}

variable "ssl_admin_email" {
  description = "Admin email for SSL certificate"
  type        = string
}

variable "munin_user" {
  description = "Username for the Munin dashboard Basic Authentication"
  type        = string
  default     = "admin"
}

variable "munin_password" {
  description = "Password for the Munin dashboard Basic Authentication"
  type        = string
  sensitive   = true
}