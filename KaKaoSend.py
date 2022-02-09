import requests
import json

with open(r"C:\testAi\2022New\kakao_code.json","r") as fp:
    tokens = json.load(fp)
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
        "text":"성공입니다!",
        "link":{
            "web_url":"www.daum.net",
            "web_url":"www.naver.com"
        },
        "button_title": "바로 확인"
    })
}

response = requests.post(send_url, headers=headers, data=data)