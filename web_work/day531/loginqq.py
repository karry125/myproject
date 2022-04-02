# -*- coding:utf-8 -*-
# @Time:2019/6/1
# @Author:wangym
# @Email:123@qq.com
# @File:loginke

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://ke.qq.com/")

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'js_login')))
driver.find_element_by_id('js_login').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@data-type="1"]')))
driver.find_element_by_xpath('//a[@data-type="1"]').click()

# 进去iframe,用name属性确定
driver.switch_to.frame("login_frame_qq")
#driver.switch_to.default_content()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'switcher_plogin')))
driver.find_element_by_id('switcher_plogin').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'u')))
driver.find_element_by_id('u').send_keys("2031510010")

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'p')))
driver.find_element_by_id('p').send_keys("123456")

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'login_button')))
driver.find_element_by_id('login_button').click()





