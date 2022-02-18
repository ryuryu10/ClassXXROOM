from distutils import dep_util
from flask import Flask, json, request, jsonify
from flask import Blueprint

file_path = "./UserId_Univ.json"                                          #<------------------- Path rename


with open(file_path, 'r', encoding="utf-8") as file:
    datas = json.load(file)

bp_test = Blueprint("test", __name__, url_prefix="/test")

@bp_test.route('/', methods=['POST'])
def main():
    content = request.get_json()
    
    dataSend = {
        "version": "2.0",
          "template": {
            "outputs": [
      {
        "simpleText": {
          "text": "원하시는 작업을 선택하세요"
        }
      }
    ],
    "quickReplies": [
      {
        "messageText": "학교 등록하기",
        "action": "message",
        "label": "학교 등록"
      },
      {
        "messageText": "등록된 학교 수정하기",
        "action": "message",
        "label": "등록된 학교 수정 "
      }
    ]
  }
}
    return jsonify(dataSend)

