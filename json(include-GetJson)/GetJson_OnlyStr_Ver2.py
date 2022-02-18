#둘다 가져오기
from xml.dom.minidom import Element
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import json
from datetime import timedelta, date

str_datetime = []
Final_Day = []
Final_Work = []
Str_Final_Day = []
format = '%Y-%m-%d'

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

try:
    for A in range(0, len(New_Str_Final_Day)):
        globals()['List_' + str(Str_Final_Day[A])] = []
except:
    pass

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


#Month1, Month2, Month3, Month4, Month5, Month6, Month7, Month8, Month9, Month10, Month11, Month12 = []

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


for A in range(0, len(Final_Day)):
    Str_Final_Day.append(datetime.strftime(Final_Day[A],format))

print(len(Str_Final_Day), len(Final_Work))
FinalSumList = list(zip(Str_Final_Day, Final_Work))

List_Names = {}
New_Str_Final_Day = []

for v in Str_Final_Day:
    if v not in New_Str_Final_Day:
        New_Str_Final_Day.append(v)
'''
for A in range(0, len(New_Str_Final_Day)):
    List_Names[str(New_Str_Final_Day[A])+ '_'] = ''
#print(List_Names)
'''

for A in range(0, len(Str_Final_Day)):
    try:
        globals()['List_' + str(Str_Final_Day[A])].append(Final_Work[A])
    except:
        globals()['List_' + str(Str_Final_Day[A])] = []
        globals()['List_' + str(Str_Final_Day[A])].append(Final_Work[A])
    #print('List_' + str(Str_Final_Day[A]))
    #print(globals()['List_' + str(Str_Final_Day[A])])
    #print(globals()['List_' + str(Str_Final_Day[A])])
    #print(Str_Final_Day.index(str(Str_Final_Day[A])))
    
    List_Names[str(Str_Final_Day[A])] = globals()['List_' + str(Str_Final_Day[A])]


with open('UniversityClassList.json', 'w', encoding="utf-8") as make_file:
    json.dump(List_Names, make_file, ensure_ascii=False, indent="\t")