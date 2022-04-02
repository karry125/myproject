# -*- coding:utf-8 -*-
# @Time:2019/6/29
# @Author:wangym
# @Email:123@qq.com
# @File:conftest


from selenium import webdriver
import pytest

@pytest.fixture(scope="class")  #Base
def open_url():
    # 前置
    driver = webdriver.Chrome()
    driver.get(cd.web_login_url)
    yield driver  # yield之前代码是前置，之后的代码就是后置。
    # 后置
    driver.quit()

