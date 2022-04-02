# -*- coding:utf-8 -*-
# @Time:2019/3/18
# @Author:wangym
# @Email:123@qq.com
# @File:testmock

import mock
import unittest
from unittest import mock
import  os
def get(a,b):
    return put(a,b)

def put(a,b):
    sum= a+b
    return sum


class test(unittest.TestCase):
    def testa(self):
        returnb = mock.Mock(return_value=3)
        put = returnb
        self.assertEqual(get(1,2),3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
    case = unittest.TestSuite()
    case.addTest(test("testa"))
    runn= unittest.TextTestRunner()
    unittest.defaultTestLoader
    runn.run(case)
    # p = os.path.realpath(__file__)
    # re= os.path.split(p)
    # t=os.path.join(re[0],"py","uu.txt")
    # print(t)
    # os.mkdir(t)
