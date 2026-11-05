resource "aws_key_pair" "itkdb" {
  key_name   = "TEK Key Pair"
  public_key = var.ssh_public_key

  lifecycle {
    ignore_changes = [public_key]
  }

}

resource "aws_instance" "itkdb" {
  ami                         = var.ec2_ami
  instance_type               = var.ec2_instance_type
  key_name                    = aws_key_pair.itkdb.key_name
  iam_instance_profile        = aws_iam_instance_profile.ec2_profile.name
  vpc_security_group_ids      = [aws_security_group.itkdb.id]
  user_data_replace_on_change = true

  user_data = templatefile("user_data.tftpl", {
    aws_region           = var.aws_region
    web_ghcr_image_uri   = var.web_ghcr_image_uri
    proxy_ghcr_image_uri = var.proxy_ghcr_image_uri
    django_secret_key    = var.django_secret_key
    sql_host             = var.sql_host
    sql_db_name          = var.sql_db_name
    sql_db_user          = var.sql_db_user
    sql_db_password      = var.sql_db_password
    sql_port             = var.sql_port
    django_allowed_hosts = var.django_allowed_hosts
    celery_broker_url    = var.celery_broker_url
    gis_user_password    = var.gis_user_password
    domain_names         = [for d in split(",", var.domain_names) : trimspace(d)]
    ssl_admin_email      = var.ssl_admin_email
  })

  tags = {
    "Name" = "ITK2.0"
  }

  root_block_device {
    encrypted   = false
    volume_size = 15
    volume_type = "gp2"
  }
}

resource "aws_eip" "itkdb" {
  instance = aws_instance.itkdb.id
  domain   = "vpc"

  tags = {
    "Name" = "ITK V2"
  }
}