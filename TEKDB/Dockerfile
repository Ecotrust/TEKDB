# pull official base image
#FROM python:3.9.6-alpine
FROM python:3.8.10-alpine

# set work directory
WORKDIR /usr/local/apps/TEKDB/TEKDB

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.6.1

COPY ./requirements.txt .

# install dependencies
RUN \
    apk update &&\
    apk add --no-cache --update \
      python3-dev musl-dev gcc \
      binutils gdal-dev postgresql-libs \
      pkgconfig openssl &&\
    apk add --no-cache --virtual .build-deps \
      postgresql-dev cairo-dev cairo cairo-tools \
      libffi-dev &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    apk --purge del .build-deps &&\
    wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# copy project
COPY . .

COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
