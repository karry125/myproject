# -*- coding:utf-8 -*-
# @Time:2019/3/26
# @Author:wangym
# @Email:123@qq.com
# @File:testserach



import requests
import  json

url = 'https://api.douban.com/v2/movie/search'
params = {"q":"2049"}
r = requests.get(url, params=params)
print(r.json())
#print('Search Params:\n', json.dumps(params, ensure_ascii=False))
#print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))