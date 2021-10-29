# pull official base image
#FROM python:3.9.6-alpine
FROM python:3.8.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

# install dependencies
RUN \
    apk update &&\
    apk add --no-cache --virtual .build-deps \
      python3-dev musl-dev gcc \
      binutils \
      postgresql-dev postgresql-libs \
      libffi-dev \
      pkgconfig openssl &&\
    apk add --no-cache --update \
      libpq gdal-dev && \
    pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    apk --purge del .build-deps

# copy project
COPY ./ /usr/local/apps/TEKDB/TEKDB
COPY ./docker/entrypoint.sh /entrypoint.sh

# set work directory
WORKDIR /usr/local/apps/TEKDB/TEKDB

RUN chmod +x /entrypoint.sh

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D tekdb_user
RUN chown -R tekdb_user:tekdb_user /vol
RUN chmod -R 755 /vol/web

USER tekdb_user

CMD ["/entrypoint.sh"]
