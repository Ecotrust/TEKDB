#!/bin/sh

#set -e
python manage.py collectstatic --noinput
python manage.py migrate --noinput
#python manage.py loaddata /usr/local/apps/TEKDB/TEKDB/TEKDB/fixtures/all_dummy_data.json
uwsgi --socket :8000 --master --enable-threads --module TEKDB.wsgi
#exec "$@"
