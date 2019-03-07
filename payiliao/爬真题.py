# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 15:40
# @Author  : Endless-cloud
# @Site    : 
# @File    : 爬真题.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 15:09
# @Author  : Endless-cloud
# @Site    :
# @File    : 爬考点4.py
# @Software: PyCharm
from multiprocessing import Pool
import requests
import json
from bs4 import BeautifulSoup

def fun1():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
    sta_urls = "http://app.yatiku.com/app/getActivityAllSendInformation?catalogId=9&codeId=0"
    response = requests.get(url=sta_urls, headers=headers)
    text = response.text
    dic_text = json.loads(text)
    ids = dic_text['catalogType']["catalogList"][5]["items"]
    print(ids)
    dic_list = []
    for i in ids:
        dic = {"name": i["Name"] + i["Taxis"],
               "Id": i["Id"],
               "url": "http://app.yatiku.com/app/getInformationById?Id=" + i["Id"] + "&catalogId=51"
               }
        dic_list.append(dic)
    # print(dic_list)

    for j in dic_list:
        response = requests.get(url=j["url"], headers=headers)
        text = response.text.strip()

        dic_text = json.loads(text)
        ner1 = dic_text["item"]["Describe"]
        bea = BeautifulSoup(ner1)
        nei2 = bea.get_text()
        with open(j["name"]+".txt", "w", encoding="utf-8") as f:
            f.write(nei2)
        print("{}写入完成".format(j["name"]))
if __name__ == '__main__':
    p =Pool(5)
    ret =p.apply(fun1,args=())
    p.close()
    p.join()

#
# print(dic_text['catalogType']["catalogList"][2]["items"])
# print(type(dic_text))
# print(response.text)
# dic_sta=json.loads()
# def get_urs():
