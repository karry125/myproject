# -*- coding:utf-8 -*-
# @Time:2019/6/24
# @Author:wangym
# @Email:123@qq.com
# @File:test_pytest

import  pytest
from selenium import webdriver
import time
@pytest.fixture()
def login():

    print("输入账号，密码先登录")
    yield 5
@pytest.mark.smoke
def test_s1(login):
    print("用例1：登录之后其它动作111",login)

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")
@pytest.mark.usefixtures("login")
def test_s3():
    print("用例3：登录之后其它动作333",login)

@pytest.fixture(scope='function')
def open():
    driver=webdriver.Chrome()
    print('打开浏览器')
    driver.get('https://www.baidu.com')
    yield driver
    driver.quit()
#@pytest.mark.usefixtures("open")
def test_01(opene):
    print('执行测试用例1')
    opene.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
    time.sleep(3)
def test_02(open):
    print('执行测试用例2')
    open.find_element_by_xpath('//*[@id="kw"]').send_keys('jmeter')
    time.sleep(3)
if __name__ == "__main__":
    pytest.main(["-s","test_pytest.py"])