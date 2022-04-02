# -*- coding:utf-8 -*-
# @Time:2019/6/2
# @Author:wangym
# @Email:123@qq.com
# @File:test_ketangpai


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
"""
5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。 
 【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
"""

class testKe(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        # 等待 查找每个元素都等待20
        cls.driver.implicitly_wait(20)
        # 打开i网址
        cls.driver.get("https://www.ketangpai.com/Home/User/login.html")
        # 登录
        cls.driver.find_element_by_xpath('//input[@name="account"]').send_keys("13738056812")
        cls.driver.find_element_by_xpath('//input[@name="pass"]').send_keys("wym16k")
        time.sleep(5)
        cls.driver.find_element_by_xpath('//a[@class="btn-btn"]').click()
        time.sleep(5)
        # 进入后弹窗，没有弹窗怎么处理
        located = (By.XPATH, '//a[@class="close"]')
        WebDriverWait(cls.driver, 20).until(EC.visibility_of_element_located(located))
        cls.driver.find_element_by_xpath('//a[@class="close"]').click()
        loca = (By.XPATH, '//a[text()="Python全栈第15期"]')  # 需要传一个元祖
        WebDriverWait(cls.driver, 20).until(EC.visibility_of_element_located(loca))
        cls.driver.find_element_by_xpath('//a[text()="Python全栈第15期"]').click()

    def test_search(self):
        # 进入课堂直接进入同学
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//li[@class="li5"]//a[text()="同学"]')))
        self.driver.find_element_by_xpath('//li[@class="li5"]//a[text()="同学"]').click()

        # 直接搜素
        stu = "1501"
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,
                                                                              '//div[@class="fr input-box"]//input')))
        self.driver.find_element_by_xpath('//div[@class="fr input-box"]//input').send_keys(stu,Keys.ENTER) # 键盘enter

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//p[@class="stuno"]//span')))
        search_no = self.driver.find_element_by_xpath('//p[@class="stuno"]//span').text
        print("搜索结果含id:{}".format(search_no))
        # 断言
        self.assertEqual(search_no,stu)

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()


