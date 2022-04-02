# -*- coding:utf-8 -*-
# @Time:2019/4/13
# @Author:wangym
# @Email:123@qq.com
# @File:HttpRequests

import requests
from common.readconf import conf
import json

class HttpRequest:
    # 不使用session
    def httprequests(self,url,methods,params=None,cookies=None):
        # session 可以保存cookies
        # 判断参数是否为字符串
        if type(params) == str: # 不加引号
            params = eval(params)
        print(type(params),params)
        url = conf.getstr("api","url")+url
        if methods.upper() == "GET":
            # re = requests.get(url,params=params,cookies=cookies)
            re = requests.get(url, params=params, cookies=cookies)
            return  re
        elif methods.upper() == "POST":
            re = requests.post(url, data=params, cookies=cookies)
            return  re
        else:
            return "请求方式错误"

    # def close(self):
    #     self.session.close()

class HttpRequestsession:

    def __init__(self):
         #可以保存cookies
        self.session= requests.sessions.session()

    def httprequests(self,url,methods,params=None,cookies=None):
        # session 可以保存cookies
        # 判断参数是否为字符串
        if type(params) == str: # 不加引号
            params = eval(params)
        url = conf.getstr("api", "url") + url
        if methods.upper() == "GET":
            # re = requests.get(url,params=params,cookies=cookies)
            re = self.session.get(url, params=params, cookies=cookies)
            return  re
        elif methods.upper() == "POST":
            re = self.session.post(url, data=params, cookies=cookies)
            return  re
        else:
            return "请求方式错误"

    def close(self):
        self.session.close() # 用完记得关闭，很关键！！！