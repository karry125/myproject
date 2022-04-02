# -*- coding:utf-8 -*-
# @Time:2019/3/21
# @Author:wangym
# @Email:123@qq.com
# @File:run_case
import sys
sys.path.append("./")
print(sys.path)
from day0321.test_request import *
from HTMLTestRunner import HTMLTestRunner
from HTMLTestRunnerNew import HTMLTestRunner
from day0321 import  test_request
import unittest
import  os

# 第一步创建测试套件
case = unittest.TestSuite()
# case.addTest(TestRequest("test_login_post")) ddt运行第一种会识别不了测试类
# case.addTest(TestRequest("test_login_get"))
# case.addTest(TestRequest("test_error_password"))
# case.addTest(TestRequest("test_error_account"))
load = unittest.TestLoader()
# 加载模块下的测试用例添加到套件
case.addTest(load.loadTestsFromModule(test_request))
# 第三种加载类下的测试用例
#case.addTest(load.loadTestsFromTestCase(TestRequest))
# 第二步创建运行对象,加载测试用例
#runner = unittest.TextTestRunner()
filepath= os.path.dirname(os.path.realpath(__file__))
discover = unittest.defaultTestLoader.discover(filepath,"test_*.py")
with open("result.html","wb")as file:
    runner = HTMLTestRunner(  stream=file, verbosity=2, title="测试报告", description="http测试",tester="某某")
    runner.run(discover)
#with open('test.txt','w') as file:  #输出到txt
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)
