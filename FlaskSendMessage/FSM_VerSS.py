from flask import Flask, json, request, jsonify, Blueprint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
from datetime import datetime

bp_main = Blueprint("a", __name__, url_prefix="/message")

global datas
global texts

Today = datetime.today().strftime('%Y-%m-%d')
file_path = "/workspace/server/NEW/main/UniversityClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)

def WeekDateGet():
    format = '%Y-%m-%d'
    WeekTexts = ""
    for WeekDate in datas:
        if Today == WeekDate:
            for days in range(1, 8):
                #print(datas[WeekDate])
                #SendMessage(datas[A],Today)
                WeekTexts += "D-" + str(days-1) + "\n"
                WeekTexts += "- " + str(datas[WeekDate]).replace("[","").replace("]","").replace(",","\n-").replace("\'","") + "\n\n"
                WeekDate = str(datetime.strptime(WeekDate, format) + relativedelta(days = days)).split(" ")[0]
    return WeekTexts

@bp_main.route('/', methods=['POST'])
def Message():
    #print("실행중입니다")
    texts = ""
    content = request.get_json()
    #print(content)
    #print(content['userRequest']['user']['id'])
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
    if content == u"오늘의일정":
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
    elif content == u"주간학사일정":
        dataSend = {
            "version" : "2.0",
            "template" : {
                "outputs" : [
                    {
                        "simpleText" : {
                            "text" : "이번주 일정 : \n {}".format(WeekDateGet())   
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