#!/bin/sh
ln -s /usr/local/apps/TEKDB/TEKDB/docker/local_settings.py /usr/local/apps/TEKDB/TEKDB/TEKDB/local_settings.py
python manage.py migrate --noinput
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:8000
exec "$@"
