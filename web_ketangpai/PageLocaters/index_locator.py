# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:index_locator

from selenium.webdriver.common.by import By

class IndexPageLocator:
    # 第一个
    invest_loc =(By.XPATH,'//a[@class="btn btn-special"]')
    user_loc = (By.XPATH,'//a[@href="/Member/index.html"]')