#!/bin/bash

# quick dirty runscript

cd /home/pi/lamper

export SLACK_TEAMID=''
export SLACK_CHANNELID=''
export SLACK_TOKEN=''
export LAMPER_URL='http://127.0.0.1:9090'
export FLASK_APP=lampeflaske.py
flask run --host=0.0.0.0
