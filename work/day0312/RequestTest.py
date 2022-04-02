# -*- coding:utf-8 -*-
# @Time:2019/3/12
# @Author:wangym
# @Email:123@qq.com
# @File:RequestTest
'''1：作业安排：

写一个类：里面有一个方法 http_request 能够完成get请求或post请求，要求有返回值

每个请求要求有请求参数

登录请求地址：http://47.107.168.87:8080/futureloan/mvc/api/member/login

请求参数：mobilephone:18688773467 pwd：123456 登录的时候需要提供手机号码和密码 '''

import  requests
import  json

class HttpRequest:
    def http_request(self,mthod,url,params=None):
        if mthod.upper() == "GET":
            try:
                re = requests.get(url,params=params)
                return re
            except Exception as e:
                return e
        elif mthod.upper() == "POST":
            re = requests.post(url,data=json.dumps(params))
            return re
        else:
            return "请求方式错误"

if __name__ == '__main__':

    httpre = HttpRequest()
    url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    parm = {"mobilephone": "18688773467", "pwd": "123456"}
    re = httpre.http_request("post",url,params=parm)
    print("post请求返回内容：",re.text,re.cookies)
    reget = httpre.http_request("get",url,params=parm)
    print(reget.text)
   # print("get请求返回内容：",reget.cookies,reget.headers,reget.request_cookies)


