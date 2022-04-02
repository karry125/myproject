# -*- coding:utf-8 -*-
# @Time:2019/6/2
# @Author:wangym
# @Email:123@qq.com
# @File:test_upload

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from day531.fileupload import upload


driver = webdriver.Chrome()
driver.maximize_window()
# 等待 查找每个元素都等待20
driver.implicitly_wait(20)
 # 打开i网址
driver.get("https://www.ketangpai.com/Home/User/login.html")
# 登录
driver.find_element_by_xpath('//input[@name="account"]').send_keys("13738056812")
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("wym16k")

driver.find_element_by_xpath('//a[@class="btn-btn"]').click()

# 进入后弹窗，没有弹窗怎么处理
located=(By.XPATH,'//a[@class="close"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(located))
driver.find_element_by_xpath('//a[@class="close"]').click()
loca=(By.XPATH,'//a[text()="python-WEB项目-py15"]') # 需要传一个元祖
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loca))
driver.find_element_by_xpath('//a[text()="python-WEB项目-py15"]').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@title="练习练习"]')))
driver.find_element_by_xpath('//a[@title="练习练习"]').click()
# 点击上传文件
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="sc-btn webuploader-container"]')))
# driver.find_element_by_xpath('//a[@class="sc-btn webuploader-container"]').click()
# # 加了等待时间上传成功  //div[@class="webuploader-pick"]
# time.sleep(5)
# upload("f:\\yuzi.jpg")
#
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@class,"tj-btn")]')))
# time.sleep(0.1)
# driver.find_element_by_xpath('//a[contains(@class,"tj-btn")]').click()
#
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="weui_btn_dialog primary"]')))
# driver.find_element_by_xpath('//a[@class="weui_btn_dialog primary"]').click()
# 更新
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@class,"new-tj1")]')))
driver.find_element_by_xpath('//a[contains(@class,"new-tj1")]').click()

# 确定更新
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="update-pop"]//a[contains(@class,"sure")]')))
driver.find_element_by_xpath('//div[@id="update-pop"]//a[contains(@class,"sure")]').click()
# 上传文件与第一次相同
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="sc-btn webuploader-container"]')))
# driver.find_element_by_xpath('//a[@class="sc-btn webuploader-container"]').click()
#//div[contains(@class,"webuploader-pick")]  这个不能点击

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="sc-btn webuploader-container"]')))
driver.find_element_by_xpath('//a[@class="sc-btn webuploader-container"]').click()
# 加了等待时间上传成功  //div[@class="webuploader-pick"]
time.sleep(5)
upload("f:\\o.html")
# 上传后等待更新提交按钮
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[contains(@class,"new-tj2")]')))
time.sleep(0.1)
driver.find_element_by_xpath('//a[contains(@class,"new-tj2")]').click()
# 提交太快没上传完成，有系统弹窗，只有一个系统弹窗
driver.switch_to.alert.accept()
# 点击知道了
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="weui_btn_dialog primary"]')))
# driver.find_element_by_xpath('//a[@class="weui_btn_dialog primary"]').click()


