#!/bin/bash
ENV_FILE=`realpath ${1:-.env.prod}`

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
mkdir -p tekdb
cd tekdb

echo "Creating a media directory for TEKDB..."
mkdir -p media

echo "Cloning the TEKDB repository..."
git clone https://github.com/Ecotrust/TEKDB.git

#TODO: change after testing
echo "Checking out the backup-cron-jobs branch..."
cd TEKDB
git checkout backup-cron-jobs    
git pull origin backup-cron-jobs

echo "Moving the .env.prod file to the Docker directory..."
ln -s $ENV_FILE $PWD/docker/.env.prod

echo "Pulling the latest Docker image..."
docker pull ghcr.io/ecotrust/tekdb/web:latest

echo "Building the proxy image..."
docker compose --env-file docker/.env.prod -f docker/docker-compose.prod.local.yaml build proxy

echo "Starting the Docker containers..."
docker compose --env-file docker/.env.prod -f docker/docker-compose.prod.local.yaml up -d

echo "Verifying that the containers are running..."
if [ "$(docker container inspect -f '{{.State.Status}}' "tekdb_web" 2>/dev/null)" = "running" ] && [ "$(docker container inspect -f '{{.State.Status}}' "db" 2>/dev/null)" = "running" ] && [ "$(docker container inspect -f '{{.State.Status}}' "tekdb_proxy" 2>/dev/null)" = "running" ]; then
    echo "TEKDB containers are running successfully."
else
    echo "Failed to start TEKDB containers. Please check the Docker logs for more information."
    exit 1 
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEKDB_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

echo "Please follow these steps to create a database backup at the cadence of your choosing using crontab:"
echo "1. Determine what timezone your server is in by running the command: timedatectl"
echo "2. Determine the desired backup schedule (e.g., daily at 9 PM) considering your server's timezone. https://crontab.guru/ is a helpful resource for determining the correct cron schedule syntax."
echo "3. Ensure you have the correct permissions to run the backup script by running: chmod +x ${TEKDB_ROOT}/scripts/Linux/db-dump.sh"
echo "4. Add to your crontab by running: crontab -e"
echo "5. Add to your cron tab (replace <your cron schedule> with your desired schedule):"
echo "   <your cron schedule> ${TEKDB_ROOT}/scripts/Linux/db-dump.sh ${TEKDB_ROOT}/docker/.env.prod >> $HOME/tekdb_db_dump.log 2>&1"
echo ""
echo "   Example for daily backups at 9 PM:"
echo "   0 21 * * * ${TEKDB_ROOT}/scripts/Linux/db-dump.sh ${TEKDB_ROOT}/docker/.env.prod >> $HOME/tekdb_db_dump.log 2>&1"
echo ""
echo "Note: Log file will be created at $HOME/tekdb_db_dump.log. You can monitor it with: tail -f $HOME/tekdb_db_dump.log" 
exit 0