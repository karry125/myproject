# -*- coding:utf-8 -*-
# @Time:2019/6/11
# @Author:wangym
# @Email:123@qq.com
# @File:
from  do_excle import do_excle
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


import re
fielname='account.xlsx'
work=do_excle(fielname,"23")
account=work.read_excle()


for i in account:
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    #driver.maximize_window()
    driver.get("https://weibo.com/")
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'loginname')))
    driver.find_element_by_id('loginname').click()
    driver.find_element_by_id('loginname').send_keys(i.name)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="input_wrap"]//input[@name="password"]')))
    driver.find_element_by_xpath('//div[@class="input_wrap"]//input[@name="password"]').send_keys(i.passs)

    # while 1:
    #     driver.find_element_by_id('loginname').click()
    #     time.sleep(0.5)
    #     driver.find_element_by_id('loginname').send_keys(i.name)
    #     name=driver.find_element_by_xpath('loginname').get_attribute('value')
    #     if name is not None:
    #         break
    #     else:
    #         continue
    # print(i.name)
    # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@class="input_wrap"]//input[@name="password"]')))
    # while 1:
    #     driver.find_element_by_xpath('//div[@class="input_wrap"]//input[@name="password"]').send_keys(i.passs)
    #     passw=driver.find_element_by_xpath('//div[@class="input_wrap"]//input[@name="password"]').get_attribute('value')
    #     if passw is not None:
    #         break
    #     else:
    #         continue
    #     print(i.passs)
        #driver.find_element_by_xpath('//a[@class="W_btn_a btn_32px"]').click()
    time.sleep(20)
    # html=driver.page_source
    # pattern= 'node-type="verifycode_image"(.+?)>'
    # if re.search(pattern,html):
    #try:
    code = driver.find_element_by_xpath('//input[@value="验证码"]').get_attribute('value')
    print(code)
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="info_list login_btn"]//a[@tabindex="6"]')))
    driver.find_element_by_xpath('//div[@class="info_list login_btn"]//a[@tabindex="6"]').click()
    print("uuu")
    time.sleep(40)
    url = driver.title
    print(url)
    if url  in "我的首页 微博-随时随地发现新鲜事":
        time.sleep(0.5)
        cook = driver.get_cookies()
        print(cook)
        # co =driver.get_cookie("mobile")
        work.write_excle(i.id, 4, str(cook))
        # print(co)
        with open("tokenweb.txt", "w+") as file:
            file.write(str(cook))

    # except Exception as e:
    #         time.sleep(5)
    #         url = driver.current_url
    #         if url != "https://weibo.com/":
    #             cook=driver.get_cookies()
    #             print(cook)
    #             #co =driver.get_cookie("mobile")
    #             work.write_excle(i.id,4,str(cook))
    #             #print(co)
    #             with open("tokenweb.txt","w+") as file:
    #                    file.write(str(cook))
    #         raise e
    # #driver.quit()
    #print(cook)