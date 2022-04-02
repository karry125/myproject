# -*- coding:utf-8 -*-
# @Time:2019/6/7
# @Author:wangym
# @Email:123@qq.com
# @File:login_page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


class LoginPage:
   """
    登录页面 ，元素：手机框 密码 登录按钮
   """
   def __init__(self,driver):
       self.driver = driver

   # 登陆功能
   def login(self,user,passwd):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="phone"]')))
        # 输入用户名，输入密码，点击登陆
        self.driver.find_element_by_xpath('//input[@name="phone"]').send_keys(user)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(passwd)
        self.driver.find_element_by_xpath('//button').click()


   def check_null_phone(self):
        """
        手机号为空提示
        :return:
        """
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[text()="请输入手机号"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//div[text()="请输入手机号"]')
            print(self.driver.find_element_by_xpath('//div[text()="请输入手机号"]').text)
            return True
        except:
            return  False

   def check_null_password(self):
       """
       密码为空校验
       :return:
       """
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="请输入密码"]')))
       time.sleep(0.5)
       try:
           password = self.driver.find_element_by_xpath('//div[text()="请输入密码"]')
           print(password.text)
           return True
       except:
           return False

   def check_right_phone(self):
       """
       手机号格式不对
       :return:
       """
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[text()="请输入正确的手机号"]')))
       time.sleep(0.5)
       try:
           phone = self.driver.find_element_by_xpath('//div[text()="请输入正确的手机号"]')
           print(phone.text)
           return True
       except:
           return False

   def check_wronge_password(self):
       """
       密码错误
       :return:
       """
       WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="layui-layer-content"]')))
       time.sleep(0.5)
       try:
           element = self.driver.find_element_by_xpath('//div[@class="layui-layer-content"]')
           print(element.text)
           return True
       except:
           return False

   def check_not_sign(self):
       """
       未注册
       :return:
       """
       WebDriverWait(self.driver, 20).until(
           EC.visibility_of_element_located((By.XPATH, '//div[text()="此账号没有经过授权，请联系管理员!"]')))
       time.sleep(0.5)
       try:
           element = self.driver.find_element_by_xpath('//div[text()="此账号没有经过授权，请联系管理员!"]')
           print(element.text)
           return True
       except:
           return False