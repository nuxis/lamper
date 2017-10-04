#!/usr/bin/env python3


import pprint
import os
import lamper

from flask import Flask, request
from flask_api import status
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():

    pprint.pprint(request.form)

    if request.form.get('command') != '/lamper':
        return "wrong command" , status.HTTP_400_BAD_REQUEST

    if request.form.get('team_id') != os.environ['SLACK_TEAMID']:
        return "wrong team id" , status.HTTP_403_FORBIDDEN

    if request.form.get('token') != os.environ['SLACK_TOKEN']:
        return "wrong token", status.HTTP_403_FORBIDDEN

    if request.form.get('channel_id') != os.environ['SLACK_CHANNELID']:
        return "wrong channel id", status.HTTP_403_FORBIDDEN

    if request.form.get('text') not in lamper.colors.keys():
        return "wrong color" , status.HTTP_400_BAD_REQUEST

    lamper.set_dmx(lamper.colors[request.form.get('text')])

    #return "Hello World! " + request.form.get('text')

    return """
    {
    "response_type": "in_channel",
    "text": "Light switched to {}",
    "attachments": [
        {
            "text":"Light switched to {}"
        }
        ]
    }
    """.format(request.form.get('text'))
