# -*- coding:utf-8 -*-
# @Time:2019/7/6
# @Author:wangym
# @Email:123@qq.com
# @File:test_app
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy

# 操作系统、系统版本、app应用
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True
# app应用：包名 - 唯一标识
# 如何得到app的包名吗？ apk包。  aapt命令
# aapt dump badging apk应用名
desired_caps["appPackage"]="com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"

# 2、 appium在线
# 与appium 建立连接，并告诉它，我要干什么！！
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

# 等待
loc = (MobileBy.ID,"com.lemon.lemonban:id/navigation_tiku")
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
#id
# driver.find_element_by_id("com.lemon.lemonban:id/navigation_tiku").click()
driver.find_element(*loc).click()

# 等待
loc = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Linux")')
WebDriverWait(driver,30).until(EC.visibility_of_element_located(loc))
# uiautomator
driver.find_element(*loc).click()
# driver.find_element_by_accessibility_id()
# driver.find_element_by_android_uiautomator()
driver.background_app(10)
# driver.swipe()

# 整个屏幕的高和宽
size=driver.get_window_size()
# 获取屏幕宽度 width
width = size['width']
print(width)
# 获取屏幕高度 height
height = size['height']
print(height)
driver.location
