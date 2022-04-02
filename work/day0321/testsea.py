# -*- coding:utf-8 -*-
# @Time:2019/3/26
# @Author:wangym
# @Email:123@qq.com
# @File:testsea

import unittest
from ddt import ddt,data,unpack
from day0321.http_request import http_request
@ddt
class TestSearch(unittest.TestCase):
    a = [['https://api.douban.com/v2/movie/search', 'get', '{"q":"2049"}'],
         ['https://api.douban.com/v2/movie/search', 'get', '{"q":"张艺谋"}']]

    @data(*a)
    @unpack
    def test_se(self,url,mathod,dat):
        a = http_request().allrequest(mathod,url,dat)
        print(a.text)

