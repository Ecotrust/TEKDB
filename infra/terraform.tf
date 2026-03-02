terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  required_version = ">= 1.2"

  backend "s3" {
    bucket  = "itkdb-tf-state"
    key     = "staging/terraform.tfstate"
    region  = "us-west-2"
    profile = "default"
  }
}