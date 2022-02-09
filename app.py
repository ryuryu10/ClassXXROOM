#-*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

default_buttons = ['파이썬 퀴즈', '웹 퀴즈', '컴퓨터 퀴즈']


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)


@app.route('/message', methods=["POST"])
def true_or_false():
    dataRecieve = request.get_json()
    response_data = {
                "version": "2.0",
                "template": {
                    "outputs": [{"simpleText": {"text": "123"}}],
                    "quickReplies": [{"label": "처음으로", "action": "message", "messageText": "처음으로"},
                                     ]
                }
            }
 


    return jsonify(response_data)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)