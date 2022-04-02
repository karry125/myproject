# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:login_page


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from futureloan.PageLocaters.login_page_locator import LoginPageLocator as loc

class LoginPage:
   """
    登录页面 ，元素：手机框 密码 登录按钮
   """
   def __init__(self,driver):
       self.driver = driver

   # 登陆功能
   def login(self,user,passwd):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.user_loc))
        # 输入用户名，输入密码，点击登陆
        # self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys(user)
        # self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
        # self.driver.find_element_by_xpath('//button').click()
        self.driver.find_element(*loc.user_loc).send_keys(user)
        self.driver.find_element(*loc.passwd_loc).send_keys(passwd)
        self.driver.find_element(*loc.login_button_loc).click()


    # 获取表单区域的错误信息
   def get_error_msg_from_loginForm(self):
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_notify_from_loginForm))
       return self.driver.find_element(*loc.error_notify_from_loginForm).text

    # 获取页面中间的错误信息
   def get_error_msg_from_pageCenter(self):
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.error_notify_from_pageCenter))
       return self.driver.find_element(*loc.error_notify_from_pageCenter).text