#국민대 학사일정https://www.notion.so/b31ca8a9689c47c5804d3a0dac3955c6?v=81637117d3d04155a0eefe7d5c789dda

#둘다 가져오기
from xml.dom.minidom import Element
import cv2
import numpy as np
import requests
from bs4 import BeautifulSoup
from notion.client import NotionClient
from notion.block import * 
from notion.collection import * 
from datetime import datetime 
import notion
from datetime import timedelta, date

#토큰 꼭 지우기
token_v2 = '75e9552fa90925d9a4a34589807560afcaf61076c1174ffced17663455ca99a35131018a607b71df4498da3f409e54ec69ce915858ab15a9d16e0013514b714d6742ef8673a343ee7299d4a13ae8' # token == 비밀번호 라고 생각하면 됩니다. 
client = NotionClient(token_v2=token_v2) 

url = 'https://www.notion.so/python-api-test2-c8e895c76a304731a616361e8b03137a' 
page = client.get_block(url) 

list_day = []
test_url = "https://www.kookmin.ac.kr/user/scGuid/scSchedule/index.do"
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')

#print(html)
rel_day = html.select_one('div.table_wrap')
rel2_day = rel_day.select('tr > td')


list_All = []
#list_Trash = []
list_Day = []
list_Work = []
for A in range(0, len(rel2_day)):
    list_All.append(rel2_day[A].get_text())

for A in range(0, len(list_All)):
    if A % 3 == 1:
        list_Day.append(list_All[A])
    if A % 3 == 2:
        list_Work.append(list_All[A])

for A in range(0, 6):
    del list_Work[-1]
    del list_Day[-1]

print(list_Work)
print(list_Day)

#print(list_Work)
#print(len(list_day), len(list_Work))

for Number2 in range(0, len(list_Day)):
    list_Day[Number2] = list_Day[Number2].split("~")
    list_Day[Number2] = str(list_Day[Number2]).replace(" ", "")
    list_Day[Number2] = str(list_Day[Number2]).replace("(", ".")
    list_Day[Number2] = str(list_Day[Number2]).replace("[", "")
    list_Day[Number2] = str(list_Day[Number2]).replace("]", "")
    list_Day[Number2] = str(list_Day[Number2]).replace("'", "")
#print(list_day)


Final_Day = []
Final_Work = []

for A in range(0, len(list_Day)):

    if len(list_Day[A]) > 1:
        date_diff = date(2022, int(list_Day[A].split(".")[0]), int(list_Day[A].split(".")[1]))
        now = date(2022, int(list_Day[A].split(".")[2][3:]), int(list_Day[A].split(".")[3]))

        date_diff1 = now - date_diff
        print("차이 :", date_diff1) 
        if now != date_diff:
            Final_Work.append(list_Work[A])
            for B in range(0, int(str(date_diff1).split(" ")[0])):
                Final_Work.append(list_Work[A])
                #print(list_Work[A])
                #print(list_Work)
            for numbers in range(int(str(date_diff1).split(" ")[0]),0,-1):
                Final_Day.append(now - timedelta(numbers))
            Final_Day.append(now)
        else:
            Final_Day.append(date(2022,int(list_Day[A].split(".")[0]), int(list_Day[A].split(".")[1])))
            Final_Work.append(list_Work[A])
print(Final_Day)

print(Final_Work)
#print(Final_Day)


#print(page.title)
#print("======")
#print(page.children)
myViewBlock = page.children[0] 
#print(myViewBlock)

for B in range(0, len(Final_Work)):
    new_row_of_my_table = myViewBlock.collection.add_row() 

    new_row_of_my_table.title = Final_Work[B]
    new_row_of_my_table.Day = Final_Day[B]

