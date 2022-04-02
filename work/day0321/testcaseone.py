# -*- coding:utf-8 -*-
# @Time:2019/3/27
# @Author:wangym
# @Email:123@qq.com
# @File:testcaseone

import  unittest
from ddt import ddt,data,unpack
from day0321.http_request import  http_request
from date0314.xlsxhelp import XlsxHelp
import  json
@ddt #装饰测试类
class ddttest(unittest.TestCase):
    url="http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    dat={"mobilephone": "18688773467", "pwd": "123456"}
    mthod = "get"
    readdata =[{"url":url,"datas":{"mobilephone": "18688773467", "pwd": "123456"},"mthod":"get"},
               {"url":url,"datas":{"mobilephone": "18688773467", "pwd": "1234576"},"mthod":"post"}]
    listdata = XlsxHelp("http.xlsx", "开心").readxlxs()
    #单个参数，不需要拆分，收集参数给*args，一个元素一组数据，比如，单个参数值，单个元祖，列表，列表
    # @data(*readdata)
    # @unpack
    # def testlogin(self,url,datas,mthod):
    #     httpre = http_request().allrequest(mthod,url,datas)
    #     print(httpre.text)
    @classmethod
    def setUpClass(cls):
        cls.listdata = XlsxHelp("http.xlsx", "开心").readxlxs()

    @data(*listdata)
    @unpack
    def testread(self,url,mthod,dataa):
        httpres = http_request().allrequest(mthod, url, dataa)
        print(httpres.json())

