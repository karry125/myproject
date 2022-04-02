# -*- coding:utf-8 -*-
# @Time:2019/5/28
# @Author:wangym
# @Email:123@qq.com
# @File:528

import  time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# python环境变量根目录下找
# 启用浏览器
driver=webdriver.Chrome()
# 智能等待 只需要调用一次 ，在调用浏览器后，秒，全局等待，查找每个元素时生效
driver.implicitly_wait(30)
driver.get("http://www.baidu.com")
#

driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
local=(By.XPATH,'//a[text()="_腾讯课堂"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(local))
time.sleep(5)
handls=driver.window_handles
driver.find_element_by_xpath('//a[text()="_腾讯课堂"]').click()
WebDriverWait(driver,20).until(EC.new_window_is_opened(handls))
# 重新获取句柄页面数
handls=driver.window_handles
driver.switch_to.window(handls[-1])


# handls=driver.window_handles
# print(handls)
# new=driver.switch_to.window(handls[-1])
# print(new)



# 智能等待 明确条件 元素可见窗口存在
# 元素存在 元素 可见 元素可用


# 退出浏览器
#driver.quit()

