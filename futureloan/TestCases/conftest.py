# -*- coding:utf-8 -*-
# @Time:2019/6/29
# @Author:wangym
# @Email:123@qq.com
# @File:conftest


from selenium import webdriver
import pytest
from TestDatas import common_data as cd
from PageObjects.login_page import LoginPage
@pytest.fixture(scope="class")  #Base
def open_url():
    # 前置
    driver = webdriver.Chrome()
    print(cd.web_login_url)
    driver.get(cd.web_login_url)
    driver.maximize_window()
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

@pytest.fixture(scope="function")
def refresh_page(open_url):
    yield
    open_url.refresh()

@pytest.fixture(scope="class")
def login_web(open_url):
    # 登陆操作
    LoginPage(open_url).login(cd.user,cd.passwd)
    yield open_url


