#!/bin/bash
set -e

ENV_FILE=".env.prod"

if [ -f "$ENV_FILE" ]; then
    set -a
    source "$ENV_FILE" 
    set +a
else
    echo "Warning: $ENV_FILE file not found"
fi

CONTAINER_NAME=db
DB_USER=${SQL_USER}
DB_NAME=${SQL_DATABASE}
BACKUP_DIR="../../backups/postgres"

DATE=$(date +%Y-%m-%d_%H%M%S)
FINAL_BACKUP_FILE="${BACKUP_DIR}/${DB_NAME}_${DATE}.sql"

mkdir -p "${BACKUP_DIR}"

0 9 * * * docker exec -i "${CONTAINER_NAME}" pg_dump -U "${DB_USER}" "${DB_NAME}" > "${FINAL_BACKUP_FILE}"
