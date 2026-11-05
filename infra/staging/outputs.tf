output "ec2_public_ip" {
  description = "Elastic IP of the EC2 instance — use this for DNS and GitHub secrets"
  value       = aws_eip.itkdb.public_ip
}

output "ecr_web_url" {
  description = "ECR URL for the web image"
  value       = aws_ecr_repository.web.repository_url
}

output "ecr_proxy_url" {
  description = "ECR URL for the proxy image"
  value       = aws_ecr_repository.proxy.repository_url
}