# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import sys

sys.path.append('./')  # project根目录地址


import unittest

from WebService_API.common import HTMLTestRunnerNew
from WebService_API.common import contants

discover = unittest.defaultTestLoader.discover(contants.case_dir, "test_*.py")

with open(contants.report_dir + '/report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title="PYTHON15 API TEST REPORT",
                                              description="WebService API",
                                              tester="mongo")
    runner.run(discover)
