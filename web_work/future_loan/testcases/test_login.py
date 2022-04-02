# -*- coding:utf-8 -*-
# @Time:2019/6/7
# @Author:wangym
# @Email:123@qq.com
# @File:test_login


import unittest
from future_loan.PageObject.login_page import LoginPage
from future_loan.PageObject.index_page import IndexPage
from selenium import webdriver


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://120.78.128.25:8765/Index/login.html")
        self.driver.maximize_window()


    def te1st_login_success(self):
        """
        登录成功
        :return:
        """
        LoginPage(self.driver).login("13738056812","w12345678")
        # 先等待页面元素出现
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())
        assert_url = "http://120.78.128.25:8765/Index/index"
        self.assertEqual(self.driver.current_url,assert_url)
        cook=self.driver.get_cookies()
        file=''
        with open('cookies.txt','w',encoding='utf-8') as file:
            file.write(str(cook))
    def test_login_success_cook(self):
        """
        登录成功
        :return:
        """
        with open('cookies.txt','r',encoding='utf-8') as file:
            r=file.readline()
            print(r)
            for i in eval(r):
               self.driver.add_cookie(i)
            self.driver.refresh()
    def tes2t_login_null_phone(self):
        """手机号为空"""
        login=LoginPage(self.driver)
        login.login("","w12345678")
        assert_toast=""
        self.assertTrue(login.check_null_phone())

    def tes2t_login_null_password(self):
        """密码为空"""
        login = LoginPage(self.driver)
        login.login("13738056812", "")
        self.assertTrue(login.check_null_password())

    def te1st2_login_wrong_phone(self):
        """手机格式错误"""
        login = LoginPage(self.driver)
        login.login("1373805682", "w12345678")
        self.assertTrue(login.check_right_phone())

    def tes2t_login_wrong_password(self):
        """手机号正确 密码错误"""
        login = LoginPage(self.driver)
        login.login("13738056812", "w1234567")
        self.assertTrue(login.check_wronge_password())

    def te2st_login_not_sign(self):
        """未注册"""
        login = LoginPage(self.driver)
        login.login("13738056817", "w1234567")
        self.assertTrue(login.check_not_sign())

    def tearDown(self):

        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)