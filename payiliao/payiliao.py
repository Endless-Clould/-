# -*- coding: utf-8 -*-
# @Time    : 2019/3/5 14:37
# @Author  : Endless-cloud
# @Site    : 
# @File    : payiliao.py
# @Software: PyCharm
import requests
import re
from multiprocessing import Pool

# url ="http://v.yatiku.com/mp4640/AZXKGMFJUTIYOPLGFAA.mp4"
# response =requests.get(url=url,headers=headers,stream=True)
# print(response.status_code)
# with open('1.mp4', 'wb') as mp4:
#     for chunk in response.iter_content(chunk_size=1024*1024):
#         if chunk:
#             mp4.write(chunk)
# print('1download over')

def fun1(i,url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",

    }
    response = requests.get(url=url, headers=headers, stream=True)
    print("%s正在下载%s"%(i,response.status_code))
    with open(str(i)+'.mp4', 'wb') as mp4:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                mp4.write(chunk)
    print('{}download over'.format(i))
list =["http://v.yatiku.com/mp4640/AZXKGMFJUTIYOPLGFAA.mp4",
       "http://v.yatiku.com/mp4640/AZXKGMFJUTIYOPLGFAB.mp4",
       "http://v.yatiku.com/mp4640/AZXKGMFJUTIYOPLGFAC.mp4",
       "http://v.yatiku.com/mp4640/AZXKGMFJUTIYOPLGFAD.mp4",
       "http://v.yatiku.com/mp4640/CZXKGMFJUTIYOPLGFAA.mp4",
       "http://v.yatiku.com/mp4640/BZXKGMFJUTIYOPLGFAA.mp4",
       "http://v.yatiku.com/mp4640/BZXKGMFJUTIYOPLGFAB.mp4",
       "http://v.yatiku.com/mp4640/BZXKGMFJUTIYOPLGFAC.mp4",
       "http://v.yatiku.com/mp4640/BZXKGMFJUTIYOPLGFAD.mp4",
       "http://v.yatiku.com/mp4640/CZXKGMFJUTIYOPLGFAA.mp4",
       "http://v.yatiku.com/mp4640/CZXKGMFJUTIYOPLGFAC.mp4",
       "http://v.yatiku.com/mp4640/CZXKGMFJUTIYOPLGFAD.mp4",
       "http://v.yatiku.com/mp4640/DZXKGMFJUTIYOPLGFAA.mp4",
       "http://v.yatiku.com/mp4640/DZXKGMFJUTIYOPLGFAB.mp4"
       ]
# fun1(1,url)
for i,url in enumerate(list):
    fun1(i, url)

# for  i,url in enumerate(list):
#     print(str(i) +" "+url)


