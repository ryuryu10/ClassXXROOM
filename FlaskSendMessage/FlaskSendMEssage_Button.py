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
    print(content['userRequest']['user']['id'])
    content = content['action']['name']
    #content=content.replace("\n","")
    #print(content)
    for A in datas:
        if Today == A:
            #SendMessage(datas[A],Today)
            texts = str(datas[A]).replace("[","").replace("]","").replace(",","\n-").replace("\'","") + "\n입니다."     #['2022뭐시기','2022년 뭐시기']
    if texts == "":
        texts = "존재하지 않습니다"
    #print(texts)
    if content == u"테스트":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "오늘의 할 일은 : \n-{}".format(texts)
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