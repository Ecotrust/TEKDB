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

echo "Collecting static files..."
python manage.py collectstatic --noinput
echo "Applying database migrations..."
python manage.py migrate --noinput
# Load default users only if no users exist
echo "Checking for existing users..."
if [ "$(python manage.py shell -c 'from django.contrib.auth import get_user_model; print(get_user_model().objects.count())')" = "0" ]; then
    python manage.py loaddata TEKDB/fixtures/default_users_fixture.json
fi
# Load default lookups only if no lookups exist. Use LookupPlanningUnit as the check.
echo "Checking for existing lookups..."
if [ "$(python manage.py shell -c 'from TEKDB.models import LookupPlanningUnit; print(LookupPlanningUnit.objects.count())')" = "0" ]; then
	python manage.py loaddata TEKDB/fixtures/default_lookups_fixture.json
fi

if [ "$1" = "prod" ]; then
    echo "Starting uWSGI (HTTP) on :8000"
    uwsgi --http :8000 --master --enable-threads --module TEKDB.wsgi
elif [ "$1" = "dev" ]; then
    echo "Starting python development server on :8000"
    python manage.py runserver 0.0.0.0:8000
else
    # Default to the passed command if not 'prod' or 'dev'
    exec "$@"
fi