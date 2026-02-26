resource "aws_ecr_repository" "web" {
  name                 = "ecotrust/${var.project_name}"
  image_tag_mutability = "MUTABLE"

  tags = {
    Project = var.project_name
  }
}

resource "aws_ecr_repository" "proxy" {
  name                 = "ecotrust/${var.project_name}-proxy"
  image_tag_mutability = "MUTABLE"

  tags = {
    Project = var.project_name
  }
}
