# -*- coding:utf-8 -*-
# @Time:2019/7/9
# @Author:wangym
# @Email:123@qq.com
# @File:test_swip lef

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#启动参数
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "7.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True

#保证终端设备上，已安装了对应的app。
desired_caps["appPackage"] = "com.xxzb.fenwoo"
desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"


#连接appium server，然后告诉它server，我要干什么。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

#等待
WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("首页")')))
#滑屏操作
#获取 设备的大小
import time
time.sleep(1)
size = driver.get_window_size()

#从右向左滑  y轴取中间size["height"]*0.5   x轴：size["width"]*0.9   终点size["width"]*0.1
driver.swipe(size["width"]*0.9,size["height"]*0.5,size["width"]*0.1,size["height"]*0.5)
#从左向右滑
#从上往下滑，从下往上滑
'''
kkk
'''

"""
j
"""