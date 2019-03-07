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
url ="http://app.yatiku.com/app/getInformationById?Id=67&catalogId=21"
response =requests.get(url=url,headers=headers,stream=True)

text =response.text.strip()
dic_text =json.loads(text)
ner1 =dic_text["item"]["Describe"]
# print(ner1)
#
# html =etree.HTML(ner1)
# uls =html.xpath("//span/text()")
# print(uls)
# print(etree.tostring(uls,encoding=('utf-8')).decode('utf-8'))
# print(uls)
bea = BeautifulSoup(ner1)
nei2=bea.get_text()
# print(type(nei2))
# l1 ="1111"
with open("1.txt","w",encoding="utf-8") as f:
    f.write(nei2)
# nei2.decode("utf-8")
# with open("1.txt","w") as f:
#     f.write(nei2)
print("写入完成")
# print(nei2.strip())
