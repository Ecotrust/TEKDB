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

  # TODO: fix this! currently does not work
  # Install Docker, AWS CLI v2, and git on first boot
  user_data = file("user_data.sh")

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