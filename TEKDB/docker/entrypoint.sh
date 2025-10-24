#!/bin/sh

# Exit on errors
set -e

# If a SQL_HOST is provided, wait for Postgres to become available before running
# migrations. This prevents race conditions when using docker-compose where the
# web container starts before the DB is ready.
if [ -n "$SQL_HOST" ]; then
	echo "Waiting for database at ${SQL_HOST}:${SQL_PORT:-5432}..."
	# pg_isready is available after installing postgresql-client in the image
	until pg_isready -h "$SQL_HOST" -p "${SQL_PORT:-5432}" >/dev/null 2>&1; do
		echo "Postgres is unavailable - sleeping"
		sleep 1
	done
	echo "Postgres is up"
fi

python manage.py collectstatic --noinput
python manage.py migrate --noinput
# python manage.py loaddata /usr/local/apps/TEKDB/TEKDB/TEKDB/fixtures/all_dummy_data.json
echo "Starting uWSGI (HTTP) on :8000"
# Use HTTP socket so direct HTTP clients (browsers) can connect to the container port.
# If you proxy with nginx using the uwsgi protocol, switch back to --socket and use
# uwsgi_pass in nginx configuration.
uwsgi --http :8000 --master --enable-threads --module TEKDB.wsgi
exec "$@"
