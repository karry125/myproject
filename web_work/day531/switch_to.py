# -*- coding:utf-8 -*-
# @Time:2019/5/31
# @Author:wangym
# @Email:123@qq.com
# @File:switch_to


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()

driver.switch_to.frame()
