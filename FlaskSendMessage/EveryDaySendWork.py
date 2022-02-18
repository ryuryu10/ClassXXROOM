import json
from datetime import datetime
import threading
import time
import requests

with open(r"C:\testAi\2022New\kakao_code.json","r") as fp:
    tokens = json.load(fp)


def SendMessage(text, Day):
    friend_url = "https://kapi.kakao.com/v1/api/talk/friends"
    headers={"Authorization" : "Bearer " + tokens["access_token"]}
    result = json.loads(requests.get(friend_url, headers=headers).text)
    friends_list = result.get("elements")
    friend_id = friends_list[1].get("uuid")
    print(friend_id)
    send_url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    data={
        'receiver_uuids': '["{}"]'.format(friend_id),
        "template_object": json.dumps({
            "object_type":"text",
            "text": text + "\n> " + Day + " <",
            "link":{
                "web_url":"www.daum.net",
                "web_url":"www.naver.com"
            },
            "button_title": "바로 확인"
        })
    }

    response = requests.post(send_url, headers=headers, data=data)


Today = datetime.today().strftime('%Y-%m-%d')

file_path = "./UnivClassList.json"

with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)
    #print(type(data))
    #print(data)


for A in datas:
    if Today == A:
        print(A)
        print(Today)
        SendMessage(datas[A],Today)
        print("오늘의 할 일은 : '{}' 입니다.".format(datas[A]))

#threading.Timer(86400, TodayWork).start()

