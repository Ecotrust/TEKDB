FROM python:3.11-slim

# Prevent Python from writing .pyc files and enable unbuffered stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install system dependencies 
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
       gcc \
       gdal-bin \
       libgdal-dev \
       libgeos-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/src/app

# Copy requirements first (cache pip install step when dependencies don't change)
COPY requirements.txt requirements_linux.txt /usr/src/app/

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip \
    && pip install -r requirements.txt -r requirements_linux.txt || pip install -r requirements.txt

# Copy the rest of the application code
COPY . /usr/src/app

# Copy and make entrypoint executable. The repository contains `docker/entrypoint.sh`
# which runs collectstatic, migrations and launches uWSGI.
COPY docker/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

# Expose the port the app runs on (entrypoint starts uWSGI on 8000)
EXPOSE 8000

# Default settings module (can be overridden at runtime)
ENV DJANGO_SETTINGS_MODULE=TEKDB.settings

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
