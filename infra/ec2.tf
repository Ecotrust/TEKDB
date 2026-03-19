resource "aws_key_pair" "itkdb" {
  key_name   = "${var.project_name}-key"
  public_key = var.ssh_public_key

  tags = {
    Project = "${var.project_name}-staging"
  }
}

resource "aws_instance" "itkdb" {
  ami                         = var.ec2_ami
  instance_type               = var.ec2_instance_type
  key_name                    = aws_key_pair.itkdb.key_name
  vpc_security_group_ids      = [aws_security_group.itkdb.id]
  iam_instance_profile        = aws_iam_instance_profile.ec2_profile.name
  subnet_id                   = tolist(data.aws_subnets.default.ids)[0]
  user_data_replace_on_change = true

  # Install Docker, AWS CLI v2, and git on first boot
  user_data = templatefile("user_data.tftpl", {
    aws_region           = var.aws_region
    web_ecr_image_uri    = var.web_ecr_image_uri
    proxy_ecr_image_uri  = var.proxy_ecr_image_uri
    django_secret_key    = var.django_secret_key
    sql_host             = var.sql_host
    sql_db_name          = var.sql_db_name
    sql_db_user          = var.sql_db_user
    sql_db_password      = var.sql_db_password
    sql_port             = var.sql_port
    django_allowed_hosts = var.django_allowed_hosts
    celery_broker_url    = var.celery_broker_url
  })

  root_block_device {
    volume_size = 20
    volume_type = "gp3"
    encrypted   = true
  }

  tags = {
    Name    = "${var.project_name}-staging-server"
    Project = var.project_name
  }
}

# Elastic IP so the address never changes across stop/start
resource "aws_eip" "itkdb" {
  instance = aws_instance.itkdb.id
  domain   = "vpc"

  tags = {
    Name    = "${var.project_name}-staging-eip"
    Project = var.project_name
  }
}