from flask import Flask, json, request, jsonify
import sys
import json
from datetime import datetime
import threading
import time
import requests

global datas
Today = datetime.today().strftime('%Y-%m-%d')

file_path = "./UnivClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)


app = Flask(__name__)

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']['utterance']
    content=content.replace("\n","")
    print(content)
    for A in datas:
        if Today == A:
            #SendMessage(datas[A],Today)
            text = "오늘의 할 일은 : '{}' 입니다.".format(datas[A])
    if content == u"오늘의 메뉴":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : text
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "error입니다."
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)