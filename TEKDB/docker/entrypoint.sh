#!/bin/sh

set -e
[ -e /usr/local/apps/TEKDB/TEKDB/TEKDB/local_settings.py ] && rm /usr/local/apps/TEKDB/TEKDB/TEKDB/local_settings.py
ln -s /usr/local/apps/TEKDB/TEKDB/docker/local_settings.py /usr/local/apps/TEKDB/TEKDB/TEKDB/local_settings.py
#python ./TEKDB/manage.py migrate --noinput

python manage.py collectstatic --noinput
uwsgi --socket :8000 --master --enable-threads --module TEKDB.wsgi
#python manage.py runserver 0.0.0.0:8000
#exec "$@"

WAIT_FOR_POSTGRES=${WAIT_FOR_POSTGRES:-true}

if [[ "$WAIT_FOR_POSTGRES" = true ]]; then
    DATABASE_URL=${DATABASE_URL:-postgres://postgres:postgres@postgres:5432/postgres}

    # convert to connection string
    # https://www.postgresql.org/docs/current/static/libpq-connect.html#LIBPQ-CONNSTRING
    POSTGRES_URL=${DATABASE_URL%%\?*}
    # https://www.gnu.org/software/bash/manual/bash.html#Shell-Parameter-Expansion
    POSTGRES_URL=${POSTGRES_URL/#postgis:/postgres:}

    # let postgres and other services (e.g. elasticsearch) to warm up...
    # https://www.caktusgroup.com/blog/2017/03/14/production-ready-dockerfile-your-python-django-app/
    until psql $POSTGRES_URL -c '\q'; do
        >&2 echo "Postgres is not available - sleeping"
        sleep 1
    done
    # >&2 echo "Postgres is up - executing command"
fi

if [[ $# -ge 1 ]]; then
    exec "$@"
else
    echo "Applying migrations"
    python manage.py migrate --noinput -v 0
    echo "Generate translations"
    python manage.py compilemessages --locale ru -v 0
    echo "Starting server"
    exec python manage.py runserver 0.0.0.0:8000
fi
