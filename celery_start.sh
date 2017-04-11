#!/bin/bash
if [ ! $DEST ]; then
    DEST=/usr/bin
fi
PYTHON=$DEST/python3.4
PROJECT_FOLDER=./
PID_FOLDER=./
LOGS_FOLDER=./
BEAT_SHEDULE_FILE=./celerybeat-schedule
echo $PROJECT_FOLDER

times of the tasks in a local database file

$PYTHON ${PROJECT_FOLDER}manage.py celery worker --concurrency=1 --detach --pidfile=${PID_FOLDER}celery_worker.pid --logfile=${LOGS_FOLDER}celery_worker.log -Q high
$PYTHON ${PROJECT_FOLDER}manage.py celery beat --detach --pidfile=${PID_FOLDER}celery_beat.pid --logfile=${LOGS_FOLDER}celery_beat.log -s ${BEAT_SHEDULE_FILE}
$PYTHON ${PROJECT_FOLDER}manage.py celeryd --logfile=${LOGS_FOLDER}celery_d.log

$PYTHON ${PROJECT_FOLDER}manage.py runserver