from flask import Flask, json, request, jsonify
import sys
from flask import Flask, json, request, jsonify
import sys
import json
from datetime import datetime
import threading
import time
import requests
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

default_buttons = ['오늘 학사 일정 조회하기', '주간 학사 일정 조회하기', '대학교 등록 및 수정']


global datas
global texts
Today = datetime.today().strftime('%Y-%m-%d')

def WeekDateGet():
    format = '%Y-%m-%d'

    WeekTexts = ""
    for WeekDate in datas:
            if Today == WeekDate:
                for days in range(1, 8):
                    print(datas[WeekDate])
                    #SendMessage(datas[A],Today)
                    WeekTexts += "D-" + str(days-1) + "\n"
                    WeekTexts += "- " + str(datas[WeekDate]).replace("[","").replace("]","").replace(",","\n-").replace("\'","") + "\n\n"
                    WeekDate = str(datetime.strptime(WeekDate, format) + relativedelta(days = days)).split(" ")[0]

    return WeekTexts

file_path = "./UniversityClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)

@app.route('/keyboard')
def keyboard():
    return jsonify({
        'type' : 'buttons',
        'buttons' : default_buttons
       })

@app.route('/message', methods=["POST"])
def Message():
    dataRecieve = request.get_json()
    user_input = dataRecieve["content"]
    
    texts = ""
    content = request.get_json()
    print(content['userRequest']['user']['id'])
    content = dataRecieve["content"]
    #content=content.replace("\n","")
    print(content)
    for A in datas:
        if Today == A:
            #SendMessage(datas[A],Today)
            texts = str(datas[A]).replace("[","").replace("]","").replace(",","\n-").replace("\'","") + "\n입니다."     #['2022뭐시기','2022년 뭐시기']
    if texts == "":
        texts = "존재하지 않습니다"
    #print(texts)
    if user_input == default_buttons[0]:
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "오늘의 일정 : \n-{}".format(texts)
                        }
                    }
                ]
            }
        }
    elif content == u"주간일정확인":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "이번주 일정 : {}".format(WeekDateGet())   #<---------- WeekDateGet function Error
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