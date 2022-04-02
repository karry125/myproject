# -*- coding:utf-8 -*-
# @Time:2019/6/16
# @Author:wangym
# @Email:123@qq.com
# @File:test_user


import unittest
from selenium import webdriver
from PageObjects.user_page import UserPage
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage

from TestDatas.login_data import success_data as sd
from TestDatas.common_data import base_url
import time

class TestUser(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        #self.driver.get()
        self.driver.get("{}/Index/login.html".format(base_url))
        self.driver.maximize_window()
        LoginPage(self.driver).login(sd["user"], sd["passwd"])


    def test_userinfo(self):

        IndexPage(self.driver).click_user_url()
        time.sleep(2)
        #
        # handles = self.driver.window_handles
        # self.driver.current_window_handle
        # print(handles,self.driver.current_url)
        # self.driver.switch_to.window(handles[-1])
        userpage = UserPage(self.driver)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        userpage.click_invest_tab()
        time.sleep(10)
        num=userpage.get_first_num_time()
        print(num)

    def tearDown(self):
        pass