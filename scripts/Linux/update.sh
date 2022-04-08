#!/bin/bash

# CWD=`pwd`
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
# PROJ_ROOT=${BASH_SOURCE}/../..
# PROJ_ROOT=${0}/../..
PROJ_ROOT=$SCRIPT_DIR/../..
# TODO
#   Test if $PROJ_ROOT/env exists and is a dir
ENV_BIN=$PROJ_ROOT/../env/bin
#   If not, test if $PROJ_ROOT/TEKDB/env exists is a dir
#ENV_BINT=$PROJ_ROOT/TEKDB/env/bin
#   If not:
# echo "Python virtual environment does not exist in a standard location."
# echo -n "Please enter the source directory for your Py Venv: "
# read filename
# IF EXISTS:
# ENV_BIN=$filename/bin
PYTHON=$ENV_BIN/python
PIP=$ENV_BIN/pip
echo $PYTHON


cd $PROJ_ROOT
git pull origin main
$PIP install -r $PROJ_ROOT/TEKDB/requirements.txt
$PIP install -r $PROJ_ROOT/TEKDB/requirements_linux.txt
$PYTHON $PROJ_ROOT/TEKDB/manage.py migrate
$PYTHON $PROJ_ROOT/TEKDB/manage.py collectstatic --no-input
$PYTHON $PROJ_ROOT/TEKDB/manage.py compress

service uwsgi restart
service nginx restart