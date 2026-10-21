#!/bin/bash
set -euo pipefail

ENV_FILE="${1:-docker/.env.prod}"
COMPOSE_FILE="${2:-docker/docker-compose.prod.local.yaml}"

REMOVE_VOLUMES="${REMOVE_VOLUMES:-0}"
REMOVE_IMAGES="${REMOVE_IMAGES:-0}"

# Optional flags can be passed after positional args.
#   --volumes   => remove named/anonymous volumes
#   --rmi-local => remove images built locally by compose
shift $(( $# > 2 ? 2 : $# )) || true
for arg in "$@"; do
  case "$arg" in
    --volumes)
      REMOVE_VOLUMES=1
      ;;
    --rmi-local)
      REMOVE_IMAGES=1
      ;;
    *)
      echo "Unknown option: $arg"
      echo "Usage: $0 [env_file] [compose_file] [--volumes] [--rmi-local]"
      exit 1
      ;;
  esac
done

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker CLI not found. Install Docker first."
  exit 1
fi

if [ ! -f "$ENV_FILE" ]; then
  echo "Environment file not found: $ENV_FILE"
  exit 1
fi

if [ ! -f "$COMPOSE_FILE" ]; then
  echo "Compose file not found: $COMPOSE_FILE"
  exit 1
fi

echo "Stopping and removing TEKDB containers..."
DOWN_CMD=(docker compose --env-file "$ENV_FILE" -f "$COMPOSE_FILE" down)

if [ "$REMOVE_VOLUMES" = "1" ]; then
  DOWN_CMD+=(--volumes)
fi

if [ "$REMOVE_IMAGES" = "1" ]; then
  DOWN_CMD+=(--rmi local)
fi

"${DOWN_CMD[@]}"

echo "TEKDB stack has been brought down successfully."