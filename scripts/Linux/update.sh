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

usage() {
    echo "Usage: $(basename "$0") --git-ref=<ref>]"
    echo "  <ref>: optional tag, or commit hash to checkout"
    echo "  If omitted, script pulls latest from 'origin main' (default behavior)."
}

REF=""

# Parse args: support --git-ref=value and --help
while [ $# -gt 0 ]; do
    case "$1" in
        -h|--help)
            usage
            exit 0
            ;;
        --git-ref=*)
            REF="${1#*=}"
            shift
            ;;
        --*)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
        *)
    esac
done

cd "$PROJ_ROOT"

if [ -z "$REF" ]; then
    # Default behavior: update main
    echo "No git ref provided. Updating 'main' branch by default."
    git pull origin main
else
    # Fetch all branches and tags, then try to checkout the requested ref
    git fetch --all --tags
    echo "Checking out git ref: '$REF'"
    if git checkout "$REF"; then
        echo "Checked out '$REF' successfully."
        If on a branch (not detached HEAD), fast-forward pull
        CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
        if [ "$CURRENT_BRANCH" != "HEAD" ]; then
            git pull --ff-only || git pull
        fi
    else
        echo "Error: failed to checkout '$REF'. Ensure it's a valid tag, or commit." >&2
        exit 1
    fi
fi

$PIP install -r $PROJ_ROOT/TEKDB/requirements.txt
$PIP install -r $PROJ_ROOT/TEKDB/requirements_linux.txt
$PYTHON $PROJ_ROOT/TEKDB/manage.py migrate
$PYTHON $PROJ_ROOT/TEKDB/manage.py collectstatic --no-input

sudo service uwsgi restart
sudo service nginx restart