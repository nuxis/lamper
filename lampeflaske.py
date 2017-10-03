#!/usr/bin/env python3


import pprint
import os
import lamper

from flask import Flask, request
from flask_api import status
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    # FIXME args/form
    if request.form.get('token') != os.environ['SLACK_TOKEN']:
        return "wrong token", status.HTTP_403_FORBIDDEN

    # FIXME args/form
    if request.form.get('channel_name') != os.environ['SLACK_CHANNEL']:
        return "wrong channel", status.HTTP_403_FORBIDDEN

    if request.form.get('text') not in lamper.colors.keys():
        return "wrong color" , status.HTTP_400_BAD_REQUEST

    lamper.set_dmx(lamper.colors[request.form.get('text')])

    return "Hello World! " + request.form.get('text')
