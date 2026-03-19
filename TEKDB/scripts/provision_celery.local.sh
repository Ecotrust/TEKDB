#!/bin/bash

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo bash $0"
  exit 1
fi

PROJECT_DIR=/usr/local/apps/TEKDB
APP_USER=vagrant

# Install Redis
apt-get install -y redis-server
systemctl enable redis-server
systemctl start redis-server

# Create log and pid directories
mkdir -p /var/log/celery /var/run/celery
chown $APP_USER:$APP_USER /var/log/celery /var/run/celery

# Copy service files into systemd
cp $PROJECT_DIR/deployment/celery-worker-local.service /etc/systemd/system/
cp $PROJECT_DIR/deployment/celery-beat-local.service /etc/systemd/system/

# Enable and start services
systemctl daemon-reload
systemctl enable celery-worker-local
systemctl enable celery-beat-local
systemctl start celery-worker-local
systemctl start celery-beat-local

echo "Done. Check status with: systemctl status celery-worker-local celery-beat-local"