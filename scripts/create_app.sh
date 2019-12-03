#!/bin/bash
#set -x
set -e

PATH_NAME=$0
APP_NAME=$1
BASE_PATH=$(dirname $0)

if [ -z $APP_NAME ]; then
    echo "Please input app's name Eg. redis_info"
    exit 1
fi

cd apps
CURRENT_PATH=$(pwd)


mkdir -p ./$APP_NAME
touch ./$APP_NAME/__init__.py ./$APP_NAME/views.py ./$APP_NAME/service.py ./$APP_NAME/models.py ./$APP_NAME/settings.py ./$APP_NAME/utils.py
