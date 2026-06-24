#!/bin/bash
ENV_FILE="${1:-.env.prod}"

if [ ! -f "$ENV_FILE" ]; then
    echo "Environment file $ENV_FILE not found!"
    exit 1
fi

# Add Docker’s official GPG Key:
echo "Adding Docker's official GPG key..."
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to apt sources:
echo "Adding Docker's official repository..."
sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update

# Install Docker packages:
echo "Installing Docker packages..."
sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation:
if systemctl is-active --quiet docker; then
    echo "Docker is installed and running."
else
    echo "Docker installation failed or Docker is not running."
    echo "Starting Docker..."
    sudo systemctl start docker
    if systemctl is-active --quiet docker; then
        echo "Docker started successfully."
    else
        echo "Failed to start Docker. Please check the installation and try again."
        exit 1
    fi
fi

echo "Adding ubuntu user to the docker group..."
sudo usermod -aG docker ubuntu

echo "Installing git..."
sudo apt install git -y

echo "Creating TEKDB directory"
mkdir tekdb
cd tekdb

echo "Creating a media directory for TEKDB..."
mkdir media

echo "Cloning the TEKDB repository..."
git clone https://github.com/Ecotrust/TEKDB.git

echo "Checking out the main branch..."
cd TEKDB
git checkout main    
git pull origin main

echo "Moving the .env.prod file to the Docker directory..."
mv $ENV_FILE docker/.env.prod

echo "Pulling the latest Docker image..."
docker pull ghcr.io/ecotrust/tekdb/web:latest

echo "Starting the Docker containers..."
docker compose --env-file docker/.env.prod -f docker/docker-compose.prod.local.yaml up -d

echo "Verifying that the containers are running..."
if [ "$(docker container inspect -f '{{.State.Status}}' "tekdb_web" 2>/dev/null)" = "running" ] && [ "$(docker container inspect -f '{{.State.Status}}' "db" 2>/dev/null)" = "running" ] && [ "$(docker container inspect -f '{{.State.Status}}' "tekdb_proxy" 2>/dev/null)" = "running" ]; then;
    echo "TEKDB containers are running successfully."
else
    echo "Failed to start TEKDB containers. Please check the Docker logs for more information."
    exit 1 
fi
exit 0