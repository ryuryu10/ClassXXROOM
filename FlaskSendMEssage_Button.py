from flask import Flask, json, request, jsonify
import sys
from flask import Flask, json, request, jsonify
import sys
import json
from datetime import datetime
import threading
import time
import requests

app = Flask(__name__)

global datas
global texts
Today = datetime.today().strftime('%Y-%m-%d')

file_path = "./UniversityClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)

@app.route('/message', methods=['POST'])
def Message():
    texts = ""
    content = request.get_json()
    content = content['action']['name']
    #content=content.replace("\n","")
    #print(content)
    for A in datas:
        if Today == A:
            #SendMessage(datas[A],Today)
            texts += str(datas[A]) + "\n"
    print(texts)
    if content == u"테스트":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "오늘의 할 일은 : \n '{}' \n 입니다.".format(texts)
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