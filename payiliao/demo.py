# -*- coding: utf-8 -*-
# @Time    : 2019/3/6 14:57
# @Author  : Endless-cloud
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:49:32 2019

@author: Administrator
"""
import json
import requests

headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_6e4561c33160d9e705ee81816c27e9b3=1551843194; Hm_lpvt_6e4561c33160d9e705ee81816c27e9b3=1551843955; JSESSIONID=4DDEDEF656056E35C66A7935C1C35B1A',
        'Host': 'app.yatiku.com',
        'Referer': 'http://app.yatiku.com/ac/sendInfor?id=9&codeId=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
# 获取id
tem = requests.get('http://app.yatiku.com/app/getInformationById?Id=530&catalogId=45',headers = headers)
ls = tem.text
catalog = json.loads(ls)
items = catalog['list']['items']
ides = []
for item in items:
    ides.append(item['Id'])
def get_href(Id):
    tem_all = requests.get('http://app.yatiku.com/app/getInformationById?Id={}&catalogId=45'.format(Id),headers = headers)
    ls_all = tem_all.text
    catalog_all = json.loads(ls_all)
    hr = catalog_all['item']['Describe'][32:-16]
    return hr
for ID in ides:
    print(get_href(ID))