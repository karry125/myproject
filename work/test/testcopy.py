# -*- coding:utf-8 -*-
# @Time:2019/3/26
# @Author:wangym
# @Email:123@qq.com
# @File:testcopy


a ="12"
print(id(a))
a=13
print(id(a))
import requests
from requests.cookies import  RequestsCookieJar
s = requests.session()
a=s.get("http://47.107.168.87:8080/futureloan/mvc/api/member/login")
print(a.cookies)
h={'JSESSIONID':'BB4834DF781D5B9B2CBD82ABD7605A56'}
#s = requests.sessions()
coo = RequestsCookieJar()
coo.set('JSESSIONID', 'BB4834DF781D5B9B2CBD82ABD7605A56')
#requests.utils.add_dict_to_cookiejar(h)

s.cookies.update(coo)
print(s.cookies)
re =s.get("http://47.107.168.87:8080/futureloan/mvc/api/member/login",cookies=h)
print(re.cookies)