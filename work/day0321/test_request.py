# -*- coding:utf-8 -*-
# @Time:2019/3/21
# @Author:wangym
# @Email:123@qq.com
# @File:test_request
import unittest
import  requests
from day0319.logging_class import logger
from day0321.http_request import http_request
from ddt import data,unpack,ddt

@ddt #装饰测试类
class TestRequest(unittest.TestCase):
    """测试登陆"""
    dic =[{"mobilephone": "18688773467", "pwd": "123456","code":"10001","case_name":"登陆成功"},
          {"mobilephone": "18688773467", "pwd": "1234566","code":"20111","case_name":"密码错误"},
          {"mobilephone": "186887734657", "pwd": "123456","code":"10001","case_name":"账号错误"}]
    a = [['https://api.douban.com/v2/movie/search', 'get', '{"q":"2049"}'],
         ['https://api.douban.com/v2/movie/search', 'get', '{"q":"张艺谋"}']]
    def setUp(self):
        self.httpre = http_request()
        self.loggers =logger
        self.url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"

    #@data(("18688773467","123456",1001),("18688773467","1234567",1002),("186887734679","123456",22))
    @data(*dic)
    @unpack
    def test_login_post(self,mobilephone,pwd,case_name,code):
        '''post正常登陆,code10001，账号或密码错误20111'''

        parm = {"mobilephone": mobilephone, "pwd": pwd}
        #print(mobilephone,pwd)
        self.loggers.logger.info( "测试用例方法%s,测试参数：%s"%(self._testMethodName,parm))
        re = self.httpre.allrequest("post", self.url, params=parm)
        print(re.text)
        self.assertEqual(re.json()["code"], code)
        self.loggers.logger.info("返回结果：%s" %(re.text))
        # try:
        #    self.assertEqual(re.json()["code"],code)
        # except Exception as e:
        #     self.loggers.logger.error("返回结果:%s"%(e))
"""
    def test_login_get(self):
        '''get正常登陆,code10001'''

        parm = {"mobilephone": "18688773467", "pwd": "123456"}
        self.loggers.logger.info("测试用例方法%s,测试参数：%s" % (self._testMethodName, parm))
        re = self.httpre.allrequest("get", self.url, params=parm)
        self.loggers.logger.info("返回结果：{}".format(re.text))
        try:
            self.assertEqual(re.json()["code"], "10003")
        except Exception as e:
            self.loggers.logger.error("返回结果：%s" % (e.args))

    def test_error_password(self):
        '''账号或密码错误20111'''

        parm = {"mobilephone": "18688773467", "pwd": "1234567"}
        self.loggers.logger.info("测试用例方法%s,测试参数：%s"%(self._testMethodName,parm))
        re = self.httpre.allrequest("post", self.url, params=parm)
        self.loggers.logger.info("返回结果：%s" %(re.text))
        self.assertEqual(re.json()["code"], "20101")

    def test_error_account(self):
        '''账号或密码错误20111'''

        parm = {"mobilephone": "18688773465", "pwd": "123456"}
        self.loggers.logger.info("测试用例方法%s,测试参数：%s"%(self._testMethodName,parm))
        re = self.httpre.allrequest("post", self.url, params=parm)
        self.loggers.logger.info("返回结果：%s" %(re.text))
        self.assertEqual(re.json()["code"], "20111")
"""
