#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)
PROJ_ROOT=$SCRIPT_DIR/../..

# Test if $PROJ_ROOT/env exists and is a dir
if [ -d $PROJ_ROOT/env ]
    then
        # This matches the suggested production install pattern
        ENV_BIN=$PROJ_ROOT/env/bin
        echo env bin found: $ENV_BIN
    #   If not, test if $PROJ_ROOT/TEKDB/env exists is a dir
    elif [ -d $PROJ_ROOT/../env ]
        then
            # This matches vagrant dev environment install pattern
            ENV_BIN=$PROJ_ROOT/../env/bin
            echo env bin found: $ENV_BIN
    #   If not:
else
    echo Proj root identified here: $PROJ_ROOT
    echo "Python virtual environment does not exist in a standard location."
    echo -n "Please enter the source directory for your Py Venv: "
    read filename
    ENV_BIN=$filename/bin
    # IF it doesn't exist:
    if [[ ! -d $ENV_BIN ]]
    then
        echo Virtual Environment $filename does not contain 'bin' directory
        exit 0
    fi
fi
PYTHON=$ENV_BIN/python
PIP=$ENV_BIN/pip

cd $PROJ_ROOT
git pull origin main
$PIP install -r $PROJ_ROOT/TEKDB/requirements.txt
$PIP install -r $PROJ_ROOT/TEKDB/requirements_linux.txt
$PYTHON $PROJ_ROOT/TEKDB/manage.py migrate
$PYTHON $PROJ_ROOT/TEKDB/manage.py collectstatic --no-input
$PYTHON $PROJ_ROOT/TEKDB/manage.py compress

service uwsgi restart
service nginx restart