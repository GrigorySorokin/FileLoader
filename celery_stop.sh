#!/bin/bash
if [ ! $DEST ]; then
    DEST=/usr/bin
fi
PYTHON=$DEST/python3.4
PID_FOLDER=./

$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celerycam.pid
$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celery_beat.pid
$PYTHON -m celery multi stopwait worker1 --pidfile=${PID_FOLDER}celery_worker.pid
