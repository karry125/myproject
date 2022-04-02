# -*- coding:utf-8 -*-
# @Time:2019/6/1
# @Author:wangym
# @Email:123@qq.com
# @File:ketangpai

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
"""
0、使用帐号和密码登陆课堂派。
1、进入你所在的班级，随机选择一个已提交的作业(带有"查看成绩"的作业)，查看你的成绩是多少 
2、获取1中作业下，作业被分享的同学名称。 
3、在1中，切换到作业讨论，并发表你的评论。
 4、点击【同学】，在同学当中，随便选一个学生，向其发送消息（鼠标悬浮后，发消息图标才出现）。  
5、在4的【同学】当中，使用右上角搜索功能。输入任意一个学生id，搜索学生信息。 
 【进阶思考：设计一条测试用例，来确认你的搜索结果与期望的匹配。使用unittest哦！！】
"""

driver = webdriver.Chrome()
driver.maximize_window()
# 等待 查找每个元素都最长等待20
driver.implicitly_wait(20)
# 打开网址
driver.get("https://www.ketangpai.com/Home/User/login.html")
# 登录
driver.find_element_by_xpath('//input[@name="account"]').send_keys("13738056812")
driver.find_element_by_xpath('//input[@name="pass"]').send_keys("wym16k")
time.sleep(5)
driver.find_element_by_xpath('//a[@class="btn-btn"]').click()
time.sleep(5)
# 进入后弹窗，没有弹窗?
located=(By.XPATH,'//a[@class="close"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(located))
driver.find_element_by_xpath('//a[@class="close"]').click()
# 点击班级
loca=(By.XPATH,'//a[text()="Python全栈第15期"]') # 需要传一个元祖
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loca))
driver.find_element_by_xpath('//a[text()="Python全栈第15期"]').click()

# 进入课堂后
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="查看成绩"]')))
driver.find_element_by_xpath('//a[text()="查看成绩"]').click() # 有多个 获取第一个
# 获取成绩 文本用元素.text
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//p[@class="score fr"]//span')))
core = driver.find_element_by_xpath('//p[@class="score fr"]//span').text
print("我的成绩{}".format(core))
# 分享名字
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//p[@class="share-name"]')))
share_list=driver.find_elements_by_xpath('//p[@class="share-name"]')
for share in share_list:
    share_name = share.text
    print("分享同学名称为{}".format(share_name))

# 切换作业讨论 评论
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="作业讨论"]')))
driver.find_element_by_xpath('//a[text()="作业讨论"]').click()
# 点击添加评论
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="input-click clearfix"]//p')))
driver.find_element_by_xpath('//div[@class="input-click clearfix"]//p').click()

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//textarea[@class="comment-txt"]')))
driver.find_element_by_xpath('//textarea[@class="comment-txt"]').send_keys("今天周六")
# 确定提交
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@class="sure active"]')))
driver.find_element_by_xpath('//a[@class="sure active"]').click()
time.sleep(4)
# 返回课堂
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//a[@id="return-course"]//i')))
driver.find_element_by_xpath('//a[@id="return-course"]//i').click()

# 进入同学
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//li[@class="li5"]//a[text()="同学"]')))
driver.find_element_by_xpath('//li[@class="li5"]//a[text()="同学"]').click()

# 全部学生菜单 菜单class是动态的
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//li[contains(@class,"all")]')))
driver.find_element_by_xpath('//li[contains(@class,"all")]').click()
# 等待列表出现
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="fl" and contains(text(),"学生")]')))
# 第二个学生
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="all-list"]//li[2]')))
# 鼠标悬浮 出现消息框
action =ActionChains(driver)
stu = driver.find_element_by_xpath('//div[@class="all-list"]//li[2]')
call = driver.find_element_by_xpath('//div[@class="all-list"]//li[2]//a[@class="call"]')
action.move_to_element(stu).click(call).perform()

# 聊天框
WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//textarea[@class="ps-container"]')))
driver.find_element_by_xpath('//textarea[@class="ps-container"]').send_keys("你好")

WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="btn-group"]//a[text()="发送"]')))
driver.find_element_by_xpath('//div[@class="btn-group"]//a[text()="发送"]').click()
# # 发送空消息 获取提示
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="gTips"]//span')))
# msgcode = driver.find_element_by_xpath('//div[@class="gTips"]//span').text
# print(msgcode)

# 搜索，获取第二个id
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="all-list"]//li[2]//p[@class="stuno"]')))
# stu = driver.find_element_by_xpath('//div[@class="all-list"]//li[2]//p[@class="stuno"]').text
# print(stu)
# 输入id
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="fr input-box"]//input')))
# driver.find_element_by_xpath('//div[@class="fr input-box"]//input').send_keys(stu,Keys.ENTER) # 键盘enter
# #driver.find_element_by_xpath('//div[@class="fr input-box"]//i').click()
# 搜索结果列表
# WebDriverWait(driver,20).until(EC.visibility_of_element_located((By.XPATH,'//p[@class="stuno"]//span')))
# search_no = driver.find_element_by_xpath('//p[@class="stuno"]//span').text
# print("搜索结果含id:{}".format(search_no))








