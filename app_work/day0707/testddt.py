# -*- coding:utf-8 -*-
# @Time:2020/3/16
# @Author:wangym
# @Email:123@qq.com
# @File:testddt

# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 10:38
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : learn_ddt.py
#安装  pip install  ddt
#ddt:data driver test 数据驱动测试

#装饰器--->@staticmethod  @classmethod   装饰器--->

import unittest
from ddt import ddt,data,unpack  #装饰器

@ddt#@ddt装饰测试类 unittest.TestCase的子类
class TestAdd(unittest.TestCase):

    #@data装饰我们的方法  跟for循环一样 遍历元组每个数据 然后传递给被装饰的方法的一个参数
    #有几条数据  就执行几次用例
    # @data(*[[1,2],[3,4]])#===([1,2],[3,4])--第一次遍历[1,2]  第二次遍历[3,4]
    # @unpack#[1,2]===拆成2个参数传递给test_001
    # def test_001(self,a,b):
    #     print('a:',a)
    #     print('b:',b)

    #元组-->1个元素-->加*号-->元组里面2个元素
    # @data(*[{'a':0,'b':0,'expected':0},{'a':1,'b':1,'expected':2}])
    # @unpack#字典进行拆分（针对每一条用例的数据进行拆分）
    # def test_002(self,expected,a,b,):#如果是字典的话 要用他的key作为参数来进行数据接收
    #     print('a:',a)
    #     print('b:',b)
    #     print('expected:',expected)

    #data里面的数据传进来--元组，有1个元素-->执行1条用例--->data数据加*--->变成了元组 有2个元素--->执行2个用例
    #---加unpack 根据逗号来进行拆分，变成了3个参数---测试方法要用3个参数来进行接收
    @data([0,0,0,9],[1,1,1,9])
    @unpack#字典进行拆分（针对每一条用例的数据进行拆分）
    def test_002(self,a,b,c,d):#如果是字典的话 要用他的key作为参数来进行数据接收
        print('a:',a)
        print('b:',b)
        print('c:',c)
        print('d:',d)

