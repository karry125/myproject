# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:test_login
# 需要加在最前面
import sys
sys.path.append("./")
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import login_data as ld
from TestDatas import common_data as cd
from PageObjects.index_page import IndexPage
from ddt  import  data,ddt
import pytest

@pytest.mark.usefixtures("open_url")
@pytest.mark.usefixtures("refresh_page")
class TestLogin():
     # def setUp(self):
     #     pass
     #
     # @classmethod
     # def setUpClass(cls):
     #     cls.driver = webdriver.Chrome()
     #     cls.driver.get("{}/Index/login.html".format(cd.base_url))

     # 异常用例
     # @data(*ld.wrong_datas)
     @pytest.mark.parametrize("data",ld.wrong_datas)
     def test_login_0_failed_by_wrong_datas(self, data,open_url):
         # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
         LoginPage(open_url).login(data["user"], data["passwd"])
         # 断言 - 页面的提示内容为：请输入密码
         #self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_loginForm())
         assert  data["check"]==LoginPage(open_url).get_error_msg_from_loginForm()


     #@data(*ld.fail_datas)
     @pytest.mark.parametrize("data", ld.fail_datas)
     def test_login_1_failed_by_fail_datas(self, data,open_url):
         # 步骤 - 登陆操作 - 登陆页面 - 密码为空 18684720553
         LoginPage(open_url).login(data["user"], data["passwd"])
         # 断言 - 页面的提示内容为：请输入密码
         #self.assertEqual(data["check"], LoginPage(self.driver).get_error_msg_from_pageCenter())
         assert data["check"] == LoginPage(open_url).get_error_msg_from_pageCenter()

     def test_login_2_success_login(self, open_url):
         # 步骤 - 登陆操作 - 登陆页面 - 18684720553、python
         LoginPage(open_url).login(ld.success_data["user"], ld.success_data["passwd"])  # 测试对象+测试数据
         # 断言 - 页面是否存在   我的帐户   元素   元素定位+元素操作
         # self.assertTrue(IndexPage(self.driver).check_nick_name_exists())  # 测试对象+测试数据
         # # url跳转
         # self.assertEqual(self.driver.current_url, ld.success_data["check"])  # 测试对象+测试数据
         assert IndexPage(open_url).check_nick_name_exists()
         assert open_url.current_url == ld.success_data["check"]
     # def tearDown(self):
     #     self.driver.refresh()
     #
     # @classmethod
     # def tearDownClass(cls):
     #     cls.driver.quit()

if __name__ == '__main__':
        #unittest.main(verbosity=2)
        pytest.main(["-s","test_login.py"])