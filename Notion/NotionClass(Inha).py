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
token_v2 = '' # token == 비밀번호 라고 생각하면 됩니다. 
client = NotionClient(token_v2=token_v2) 

url = 'https://www.notion.so/python-notion-API-25afad8464354d03b33ae7dd208d6fbf' 
page = client.get_block(url) 

list_day = []
test_url = "https://www.inha.ac.kr/kr/1908/subview.do"
resp = requests.get(test_url)
html = BeautifulSoup(resp.content, 'html.parser')

#print(html)
rel_day = html.select_one('div.listDay')
rel2_day = rel_day.select('li > dl > dt > span')

rel_work = html.select_one('div.listDay')
rel2_work = rel_work.select('li > dl > dd')

list_Work = []

#print(rel2)

for title in rel2_work:
        text = title.get_text().replace("\n",'').replace("\t","")
        #print(text)
        list_Work.append(text)


for title in rel2_day:
        text = title.get_text().replace("\n",'').replace("\t","")
        #print(text)
        list_day.append(text)

list_day = list_day[3:]
list_Work = list_Work[3:]
del list_Work[-1]
del list_day[-1]
#print(list_Work)
#print(len(list_day), len(list_Work))

for Number2 in range(0, len(list_day)):
    list_day[Number2] = list_day[Number2].split("~")

#print(list_day)


Final_Day = []
Final_Work = []

for A in range(0, len(list_day)):

    if len(list_day[A]) > 1:
        date_diff = date(2022, int(list_day[A][0].split(".")[0]), int(list_day[A][0].split(".")[1]))
        now = date(2022, int(list_day[A][1].split(".")[0]), int(list_day[A][1].split(".")[1]))

        date_diff1 = now - date_diff
        #print("차이 :", date_diff1) 
        Final_Work.append(list_Work[A])
        for B in range(0, int(str(date_diff1).split(" ")[0])):
            Final_Work.append(list_Work[A])
            #print(list_Work[A])
            #print(list_Work)
        for numbers in range(int(str(date_diff1).split(" ")[0]),0,-1):
            Final_Day.append(now - timedelta(numbers))
        Final_Day.append(now)
    else:
        Final_Day.append(date(2022,int(list_day[A][0].split(".")[0]), int(list_day[A][0].split(".")[1])))
        Final_Work.append(list_Work[A])
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

