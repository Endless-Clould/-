# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 11:16
# @Author  : Endless-cloud
# @Site    : 
# @File    : payiliao3.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 19:18
# @Author  : Endless-cloud
# @Site    :
# @File    : payiliao2.py
# @Software: PyCharm
import requests
import json
from bs4 import BeautifulSoup
from lxml import etree
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

}
# url ="http://app.yatiku.com/app/getInformationById?Id=539&catalogId=21"
url ="http://app.yatiku.com/app/getInformationById?Id=252&catalogId=51"
response =requests.get(url=url,headers=headers,stream=True)

text =response.text.strip()
# print(text)
dic_text =json.loads(text)
ner1 =dic_text["item"]["Describe"]
bea = BeautifulSoup(ner1)
nei2=bea.get_text()
with open("13.txt","w",encoding="utf-8") as f:
    f.write(nei2)
print("写入完成")

