# -*- coding:utf-8 -*-
# @Time:2019/4/9
# @Author:wangym
# @Email:123@qq.com
# @File:register_http

from day0409.http_request import http_request
import json
#注册接口
url = "http://test.lemonban.com/futureloan/mvc/api/member/register"
para={"mobilephone":"13738000008","pwd":"123456","regname":"明明"}
myregister=http_request().httprequest("post",url,params=para)
print("登录返回：",myregister.json())

# 登陆
url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
para = {"mobilephone":"13738000008","pwd":"123456"}
mylogin = http_request().httprequest("get",url,para)
print("登陆返回cookies:",mylogin.cookies)
print("请求头cookies:",mylogin.request._cookies)
print("登录成功返回:",mylogin.json())
print(type(mylogin.json()))#字典格式textstr格式


# 充值
url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
para={"mobilephone":"13738000008","amount":"100"}
myrecharge=http_request().httprequest("get",url,para,cookies=mylogin.cookies)
print("登陆返回cookies:",myrecharge.cookies)
print("请求头cookies:",myrecharge.request._cookies)
print(dir(myrecharge.request))
print("充值返回结果:",json.dumps(myrecharge.json(),ensure_ascii=False))
print("充值返回结果:",myrecharge.text)
