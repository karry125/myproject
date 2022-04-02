# -*- coding:utf-8 -*-
# @Time:2019/4/13
# @Author:wangym
# @Email:123@qq.com
# @File:run_case
import os
import unittest
import HTMLTestRunnerNew
#from testcases import test_login
import time
from common.readconf import conf
from common.Send_email import sendEmail
basepath = os.path.dirname(os.path.realpath(__file__))
testcasefile = os.path.join(basepath,"testcases")
#加载测试用例
# case = unittest.TestSuite()
# load =unittest.TestLoader()
# case.addTest(load.loadTestsFromModule(test_login))
# run = unittest.TextTestRunner(verbosity=2)
# run.run(case)
# 匹配文件


discover = unittest.defaultTestLoader.discover(testcasefile,"test_*.py")
# 测试报告 集成Jenkins，不用时间来区分，直接文件名report.html，构建后的html地址跟生成的相同，每次生成不同，不好取
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
filepath = os.path.join(basepath,"report","report.html")
# 写入文件 wb,自动创建
with open(filepath,"wb") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="测试报告",
                                              description="web测试",
                                              tester="敏敏")
    runner.run(discover)
# 含中文用encoding
# with open(filepath,"r",encoding="utf-8") as files:
#     msg =files.read()
#     send= sendEmail()
#     send.sender_mails(msg,type="html",subject="测试报告")