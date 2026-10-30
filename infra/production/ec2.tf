resource "aws_key_pair" "itkdb" {
  key_name   = "TEK Key Pair"
  public_key = var.ssh_public_key

  lifecycle {
    ignore_changes = [public_key]
  }

}

resource "aws_instance" "itkdb" {
  ami                    = var.ec2_ami
  instance_type          = var.ec2_instance_type
  key_name               = aws_key_pair.itkdb.key_name
  vpc_security_group_ids = [aws_security_group.itkdb.id]

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