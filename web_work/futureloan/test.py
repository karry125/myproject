# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:test
from selenium import webdriver
import datetime
import time
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# js='window.open("https://www.sogou.com");'
# driver.execute_script(js)
#driver.get("http://web.jituancaiyun.com")

# money ="可用余额:110.99元"
# m=float(money[5:-1:1])
# print(m)
# print(m*1000)
# money = '{"money":"bid_max"}'
# if money.find("bid_max") > -1:
#     print("2")
s='2019-06-1617:19'
w=time.strftime('%Y-%m-%d%H:%M',time.localtime())#datetime.datetime.now().strftime()
print(type(w),w)
print(s<w)
