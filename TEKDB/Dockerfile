# pull official base image
#FROM python:3.9.6-alpine
FROM python:3.8.10-alpine

# set work directory
WORKDIR /usr/local/apps/TEKDB

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

# install dependencies
RUN \
    apk update &&\
    apk add --no-cache --update \
      python3-dev musl-dev gcc \
      binutils gdal-dev postgresql-libs \
      pkgconfig &&\
    apk add --no-cache --virtual .build-deps \
      postgresql-dev cairo-dev cairo cairo-tools \
      libffi-dev &&\
    pip install --upgrade pip &&\
    pip install -r requirements.txt &&\
    apk --purge del .build-deps

# copy project
COPY . .
