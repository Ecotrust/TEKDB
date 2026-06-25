#!/bin/bash
set -euo pipefail

ENV_FILE="${ENV_FILE:-$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/docker/.env.prod}"

if [ -f "$ENV_FILE" ]; then
    set -a
    source "$ENV_FILE" 
    set +a
else
    echo "Warning: $ENV_FILE file not found"
fi

CONTAINER_NAME=db
SQL_USER=${SQL_USER:?SQL_USER is not set}
SQL_DATABASE=${SQL_DATABASE:?SQL_DATABASE is not set}
BACKUP_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)/backups/postgres"

BACKUP_FILE="${BACKUP_DIR}/${SQL_DATABASE}.sql"

mkdir -p "${BACKUP_DIR}"

echo "Dumping database '${SQL_DATABASE}' from container '${CONTAINER_NAME}' to '${BACKUP_FILE}'..."
docker exec -i "${CONTAINER_NAME}" pg_dump -b -c -n public -O --quote-all-identifiers --no-acl -w -U "${SQL_USER}" "${SQL_DATABASE}" > "${BACKUP_FILE}"
echo "Database dump completed successfully."