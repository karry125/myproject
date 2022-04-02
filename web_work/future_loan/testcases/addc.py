# -*- coding:utf-8 -*-
# @Time:2019/7/18
# @Author:wangym
# @Email:123@qq.com
# @File:addc


from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.get("https://web.jituancaiyun.com")#https://web.jituancaiyun.com
time.sleep(10)
# cook=driver.get_cookies()
# with open('cookies.txt', 'w', encoding='utf-8') as file:
#     file.write(str(cook))
# with open('cookies.txt','r',encoding='utf-8') as file:
#             r=file.readline()
#             print(r)
#             for i in eval(r):
#                driver.add_cookie(i)
#             driver.refresh()

time.sleep(10)
js='window.scrollTo(0,document.body.scrollHeight)'
driver.execute_script(js)
loc ='//div[contains(@class,"app_content")]/div[contains(@class,"container")]'#action._actions.pop()#加上这句就没有问题啦
time.sleep(8)
driver.get_window_size()
locc = '//div[contains(@class,"inner_content")]' # 审批
bb ='//button[contains(@class,"btn")]'
bu ='//div[contains(@class,"footer")]//button[contains(@class,"btn")]'
dai='//div[contains(@class,"module")]//div[contains(@class,"container")]'
#daix=driver.find_elements_by_xpath(dai)[6]
#b = driver.find_elements_by_xpath(bb)[3]
ele = driver.find_element_by_xpath(bu).click()
#driver.execute_script("arguments[0].scrollIntoView();",ele)
# ac=ActionChains(driver)
# #ac.drag_and_drop_by_offset(ele,100,0).perform()
# # ac.click_and_hold(ele).perform()
# ac.drag_and_drop_by_offset(ele,1500,2500).perform()

# for i in range(5):
#    ac.send_keys(Keys.ARROW_DOWN).perform()
#    # ac.key_down(Keys.ARROW_DOWN,ele).key_up(Keys.ARROW_DOWN).perform()
#    # #ac._actions.pop()
#    time.sleep(2)
#    i=i+1
print("zhix")