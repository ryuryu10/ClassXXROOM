from flask import Flask, json, request, jsonify, Blueprint
from datetime import datetime
from dateutil.relativedelta import relativedelta
import json
from datetime import datetime


app = Flask(__name__)

global datas
global texts

global Today
Today = datetime.today().strftime('%Y-%m-%d')
file_path = "./UniversityClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)

def WeekDateGet():
    format = '%Y-%m-%d'
    WeekTexts = ""
    Today = datetime.today().strftime('%Y-%m-%d')
    for WeekDate in datas:
        if Today == WeekDate:
            NewWeekDate = WeekDate
            for days in range(1, 8):
                print(datas[NewWeekDate])
                #SendMessage(datas[A],Today)
                WeekTexts += "D-" + str(days-1) + "(" + str(int(Today.split("-")[2])+days-1) + "일)" + "\n"
                WeekTexts += "- " + str(datas[NewWeekDate]).replace("[","").replace("]","").replace(",","\n-").replace("\'","") + "\n\n"
                NewWeekDate = str(datetime.strptime(WeekDate, format) + relativedelta(days = days)).split(" ")[0]
    WeekTexts = WeekTexts[:-2]
    return WeekTexts

@app.route('/message', methods=['POST'])
def Message():
    Today = datetime.today().strftime('%Y-%m-%d')
    print("실행중입니다")
    texts = ""
    content = request.get_json()
    print(content)
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
                            "text" : "이번주 일정 : \n {}".format(WeekDateGet())   #<---------- WeekDateGet function Error
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
    app.run(host='0.0.0.0',port=5000, debug=True)