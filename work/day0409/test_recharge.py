# -*- coding:utf-8 -*-
# @Time:2019/4/9
# @Author:wangym
# @Email:123@qq.com
# @File:test_recharge
import unittest
from day0409.http_request import http_request
class rechaegeTest(unittest.TestCase):
    # def setUpClass(cls):
    #     cls.https=http_request()

    def test_login(self):
        url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
        para = {"mobilephone": "13738000008", "pwd": "123456"}
        mylogin = http_request().httprequest("get", url, para)
        code =mylogin.status_code
        datas=mylogin.json()["code"]
        self.assertEqual(datas,"10001")
        return mylogin.cookies

    def test_recharge(self):
        url = "http://test.lemonban.com/futureloan/mvc/api/member/recharge"
        para = {"mobilephone": "13738000008", "amount": "100"}
        myrecharge = http_request().httprequest("get", url, para, cookies=self.test_login())
        datamsg = myrecharge.json()["msg"]
        self.assertEqual(datamsg,"充值成功")
        print(myrecharge.cookies,myrecharge.json(),myrecharge.request._cookies)