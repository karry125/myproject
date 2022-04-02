# -*- coding:utf-8 -*-
# @Time:2019/3/23
# @Author:wangym
# @Email:123@qq.com
# @File:runcase

from HTMLTestRunnerNew import HTMLTestRunner
import time
import os
import unittest
from testcase import test_http
resultpath = os.path.join(os.getcwd(),"result")
casepath =os.path.join(os.getcwd(),"testcase")
times = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename=os.path.join(resultpath,"result"+times+".html")
#列举test_dir目录下的所有文件（名），结果以列表形式返回。
listhtml = os.listdir(resultpath)
# sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
# 最后对lists元素，按文件修改时间大小从小到大排序。
# 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
listhtml.sort(key=lambda fn:os.path.getmtime(os.path.join(resultpath,fn)))
filepath = os.path.join(resultpath,listhtml[-1])#从小到大排序，取最后一个，反向取值
print(listhtml)
print(filepath)
#resultpath = os.path.join(os.getcwd(),"result")
#匹配文件名运行
discover = unittest.defaultTestLoader.discover(casepath,"test*.py")
#第二种加载模块

case = unittest.TestSuite()
load = unittest.TestLoader()
case.addTest(load.loadTestsFromModule(test_http))
# case.addTest((load.loadTestsFromTestCase("")))
print(filename)
# runner=unittest.TextTestRunner(verbosity=2)#创建一个对象来执行用例
# runner.run(case)
# with open(filename,"wb") as file:
#    runner = HTMLTestRunner(stream=file, verbosity=2,title=None,description=None,tester=None)
#    runner.run(discover)