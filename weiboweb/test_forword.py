# -*- coding:utf-8 -*-
# @Time:2019/6/12
# @Author:wangym
# @Email:123@qq.com
# @File:test_forword

from do_excle import do_excle
import unittest
from ddt import ddt,data
from random import randint
import json
import time
from httpforword import httpfor
from getcookies import gettokenwebexcle
print(randint(1,100))
fielname='account.xlsx'
work=do_excle(fielname,"20")
account=work.read_excle()

@ddt
class TestFor(unittest.TestCase):
    def setUp(self):
        pass

    @data(*account)
    def test_01(self,account):
        print("第{}行账号{}".format(account.id,account.name))
        cook =account.cook
        cook=gettokenwebexcle(cook)
        print(cook)

        i=0

        code = httpfor(cook)
        if code == "100000":
            i = i + 1
            print(i)
        time.sleep(10)
        # while i < 4:
        #     time.sleep(10)
        #     code = httpfor(cook)
        #     if code == "100000":
        #         i=i+1
        #         print(i)
        #         continue
        #     else:
        #         break
            #print(cook)

    def tearDown(self):
        time.sleep(10)

if __name__ == '__main__':
    unittest.main(verbosity=2)
