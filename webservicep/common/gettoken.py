# -*- coding:utf-8 -*-
# @Time:2019/4/14
# @Author:wangym
# @Email:123@qq.com
# @File:gettoken
from common import HttpRequests
#获取tokenhttp://test.lemonban.com/futureloan/mvc/api
url = "/member/login"
para = {"mobilephone":"13738000008","pwd":"123456"}
mylogin =HttpRequests.HttpRequest().httprequests(url,"get",para)
print("登录成功返回:",mylogin.text)
cookies = mylogin.cookies
print("登陆返回cookies:",mylogin.cookies)

# print("请求头cookies:",mylogin.request._cookies)

# print(type(mylogin.json()))#字典格式textstr格式