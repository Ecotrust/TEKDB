#!/bin/sh
# CREATE ROLE vagrant SUPERUSER LOGIN PASSWORD $2;

cat << EOF | sudo -u postgres psql
-- uncomment to reset your DB
DROP DATABASE $1;
CREATE DATABASE $1;
\connect $1
CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;

EOF
