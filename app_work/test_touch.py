# -*- coding:utf-8 -*-
# @Time:2019/7/7
# @Author:wangym
# @Email:123@qq.com
# @File:test_touch
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
ActionChains(driver).move_to_element()