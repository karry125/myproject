# -*- coding:utf-8 -*-
# @Time:2019/3/10
# @Author:wangym
# @Email:123@qq.com
# @File:requesttest

import requests
import json

url = "https://api.douban.com/v2/movie/search"
data = {"q":"招摇"}
header ={"Content-Type":"application/json"}
re = requests.post(url,data = json.dumps(data),headers={'content-type': 'application/json'})
print(re.json()["count"])
print(re.headers)
a = 're.headers.get("Date")'
print(type(eval(a)))
for cooke in re.cookies:
   print(cooke)
# print()
#
# url = "https://www.baidu.com/s?ie=utf-8&newi=1&mod=1&isbd=1&isid=8E1D08F99BC56770&wd=%E6%B5%8B%E8%AF%95&rsv_spt=1&rsv_iqid=0x81cf8817000bd20e&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=5&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&inputT=1956&rsv_sug4=2884&rsv_sid=1462_21087_28607_28585_28638_26350_28518_28606&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=26748"
# data = {"q":"招摇"}
# header ={"Content-Type":"application/json"}
# re = requests.post(url,data)
# #re.json().get
# print(re.json())
# print(re.cookies)
# for cooke in re.cookies:
#     print(cooke)