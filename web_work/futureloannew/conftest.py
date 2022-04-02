# -*- coding:utf-8 -*-
# @Time:2019/7/13
# @Author:wangym
# @Email:123@qq.com
# @File:conftest
import pytest
from selenium import webdriver
@pytest.fixture(scope='function')
def open():
    driver=webdriver.Chrome()
    print('打开浏览器')
    driver.get('https://www.baidu.com')
    yield driver
