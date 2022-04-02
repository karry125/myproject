# -*- coding:utf-8 -*-
# @Time:2019/4/11
# @Author:wangym
# @Email:123@qq.com
# @File:testcookie

from day0409.http_request import http_request
import requests
def setcookie():
    cookiess = requests.cookies.RequestsCookieJar()
    # 登陆
    url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
    para = {"mobilephone": "13738000008", "pwd": "123456"}
    mylogin = http_request().httprequest("get", url, para)
    cookiess.u
    print("登陆返回cookies:", mylogin.cookies)
    print("请求头cookies:", mylogin.request._cookies)
    print("登录成功返回:", mylogin.json())