# -*- coding:utf-8 -*-
# @Time:2019/7/8
# @Author:wangym
# @Email:123@qq.com
# @File:test_list_swip

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#跨应用
#应用当中可以切换到其它的acitivity
#启动参数
desired_caps = {}
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["noReset"] = True

#保证终端设备上，已安装了对应的app。
desired_caps["appPackage"] = "com.lemon.lemonban"
desired_caps["appActivity"] = "com.lemon.lemonban.activity.WelcomeActivity"

#连接appium server，然后告诉它server，我要干什么。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

WebDriverWait(driver,20).until(EC.visibility_of_element_located((MobileBy.ID,"com.lemon.lemonban:id/navigation_my")))

#切换到题库
driver.find_element_by_android_uiautomator('new UiSelector().text("题库")').click()
time.sleep(4)
#滑动一次查一次。
#滑动的距离要控制，要确保页面内容没有过度滑掉。
#如何确认已经滑到了底部。如果滑到了底部，再滑一次，两次内容一致。
#内容比对。滑动前的内容，和滑动后的内容比较。
#滑动前的内容 - old
#滑动后的内容 - new_src
old = driver.page_source
new_src = ""
size = driver.get_window_size()

while old != new_src:
    #重新给old赋值。因为new马就要更新了。
    old = new_src
    #滑动一次
    driver.swipe(size["width"]*0.5,size["height"]*0.9,size["width"]*0.5,size["height"]*0.2,200)
    time.sleep(2)
    #获取滑动之后的页面内容
    new_src = driver.page_source
    #其它的需求：滑一次找一次的内容
    if new_src.find("逻辑思维题") != -1:
        print("找到了了了！！")
        break