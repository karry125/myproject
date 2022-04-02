# -*- coding:utf-8 -*-
# @Time:2019/6/18
# @Author:wangym
# @Email:123@qq.com
# @File:webcooktwo

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://weibo.com")
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'loginname')))
driver.find_element_by_id('loginname').click()
driver.find_element_by_id('loginname').send_keys("13738056812@139.com")
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@class="input_wrap"]//input[@name="password"]')))
driver.find_element_by_xpath('//div[@class="input_wrap"]//input[@name="password"]').send_keys("wym0921")
time.sleep(20)
WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, '//div[@class="info_list login_btn"]//a[@tabindex="6"]')))
driver.find_element_by_xpath('//div[@class="info_list login_btn"]//a[@tabindex="6"]').click()
time.sleep(7)
url =driver.title
if url in "我的首页 微博-随时随地发现新鲜事":
    cook= driver.get_cookies()
    with open("tokenweb.txt", "w+") as file:
         file.write(str(cook))