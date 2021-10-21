#!/bin/bash

PROJECT_NAME=TEKDB
APP_NAME=TEKDB
HOME=/home/vagrant
APP_DB_NAME=tekdb

APP_DIRECTORY=/usr/local/apps
PROJECT_DIR=$APP_DIRECTORY/$PROJECT_NAME
VIRTUALENV_DIR=$APP_DIRECTORY/env

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip

USER=`whoami`

echo "resetting DB"
$PROJECT_DIR/scripts/reset_db.sh $APP_DB_NAME #$USER

echo "updating apps ownership"
sudo chown $USER $APP_DIRECTORY

# Virtualenv setup for project
echo "setting up virtualenvs"
# /usr/local/bin/virtualenv --system-site-packages $VIRTUALENV_DIR && \
/usr/bin/python3 -m venv $VIRTUALENV_DIR &&
    /usr/bin/python3 -m venv --system-site-packages $VIRTUALENV_DIR && \
    source $VIRTUALENV_DIR/bin/activate && \
    echo $PROJECT_DIR > $VIRTUALENV_DIR/.project && \
    cd $PROJECT_DIR && \
    echo "installing project dependencies"
    $PIP install --upgrade pip
    $PIP install --src ./deps -r requirements.txt
    ### INSERT PROJECT PROVISION FILES HERE ###
    ### END PROJECT PROVISION FILES ###

# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py

# set local_settings
cp $PROJECT_DIR/$APP_NAME/local_settings.py.template $PROJECT_DIR/$APP_NAME/local_settings.py

$PYTHON $PROJECT_DIR/manage.py migrate

# Add a couple of aliases to manage.py into .bashrc
touch ~/.bash_aliases
echo 'alias go="source '$VIRTUALENV_DIR'/bin/activate && cd '$PROJECT_DIR'"
alias dj="'$PYTHON' '$PROJECT_DIR'/manage.py"
alias djrun="dj runserver 0.0.0.0:8000"' > ~/.bash_aliases
