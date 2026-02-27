#!/bin/bash
sudo snap install aws-cli --classic # install aws cli to pull images from ECR
sudo apt-get update && sudo apt-get upgrade -y

# https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository
sudo apt update -y
sudo apt install ca-certificates curl -y
sudo install -m 0755 -d /etc/apt/keyrings

echo "Installing Docker's official GPG key..."
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

sudo chmod a+r /etc/apt/keyrings/docker.asc

echo "Adding Docker's official repository..."
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

echo "Installing Docker packages..."
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

echo "Adding user 'ubuntu' to the 'docker' group..."
sudo usermod -aG docker ubuntu

# install git to pull TEKDB repo
echo "Installing git..."
sudo apt install git -y

# create directory for docker-compose files
echo "Creating directory for docker-compose files..."
mkdir -p ~/tekdb/docker