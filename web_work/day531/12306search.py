# -*- coding:utf-8 -*-
# @Time:2019/6/1
# @Author:wangym
# @Email:123@qq.com
# @File:weboper


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.12306.cn/index/")

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'fromStationText')))
# 需要点击才能输入?
driver.find_element_by_id('fromStationText').clear()
driver.find_element_by_id('fromStationText').click()
# 点击后，输入，有弹窗 需要关闭 弹窗右上角x或者enter
driver.find_element_by_id('fromStationText').send_keys("杭州",Keys.ENTER)

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'toStationText')))
driver.find_element_by_id('toStationText').click()
driver.find_element_by_id('toStationText').send_keys("北京",Keys.ENTER)

# 直接输入时间 不选择
js_date = 'var date = document.getElementById("train_date");date.readOnly = false;date.value = "2019-07-02";'
driver.execute_script(js_date)

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.ID,'search_one')))
driver.find_element_by_id('search_one').click()


