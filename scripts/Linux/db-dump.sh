#!/bin/bash
set -euo pipefail

ENV_FILE="${1:-}"

if [ -f "$ENV_FILE" ]; then
    set -a
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Loading environment variables from $ENV_FILE..."
    source "$ENV_FILE" 
    set +a
else
    echo "$(date +"%Y-%m-%d %H:%M:%S") - Error: File "$ENV_FILE" not found. Please provide a valid environment file as an argument."
    exit 1
fi

CONTAINER_NAME=db
SQL_USER=${SQL_USER:?SQL_USER is not set}
SQL_DATABASE=${SQL_DATABASE:?SQL_DATABASE is not set}
BACKUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)/backups/postgres"

BACKUP_FILE="${BACKUP_DIR}/${SQL_DATABASE}.sql"

mkdir -p "${BACKUP_DIR}"

# Use full path to docker for cron compatibility
# Find docker location
if [ -x "/usr/bin/docker" ]; then
    DOCKER_CMD="/usr/bin/docker"
elif [ -x "/usr/local/bin/docker" ]; then
    DOCKER_CMD="/usr/local/bin/docker"
else
    DOCKER_CMD="docker"
fi

echo "$(date +"%Y-%m-%d %H:%M:%S") - Dumping database '${SQL_DATABASE}' from container '${CONTAINER_NAME}' to '${BACKUP_FILE}'..."
"${DOCKER_CMD}" exec -t "${CONTAINER_NAME}" pg_dump -b -c -n public -O --quote-all-identifiers --no-acl -w -U "${SQL_USER}" "${SQL_DATABASE}" > "${BACKUP_FILE}"
echo "$(date +"%Y-%m-%d %H:%M:%S") - Database dump completed successfully."