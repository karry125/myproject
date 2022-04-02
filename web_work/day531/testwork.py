# -*- coding:utf-8 -*-
# @Time:2019/6/1
# @Author:wangym
# @Email:123@qq.com
# @File:testwork

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//h2[@class="foot-con-tit"]')))
re=driver.find_element_by_xpath('//h2[@class="foot-con-tit"]')
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
print(re)
