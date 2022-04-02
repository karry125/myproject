# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:index_page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

from futureloan.PageLocaters.index_locator import IndexPageLocator as lc

class IndexPage:
    """
    首页
    """
    def __init__(self,driver):
        self.driver = driver

    def check_nick_name_exists(self):
        """
        :return: 存在返回True,不存在返回False
        """
        WebDriverWait(self.driver,30).until(
            EC.visibility_of_element_located((By.XPATH,'//a[text()="关于我们"]')))
        time.sleep(0.5)
        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False

    def click_invest_button(self):

        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(lc.invest_loc))
        self.driver.find_element(*lc.invest_loc).click()

    def click_user_url(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(lc.user_loc))
        self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]').click()
        # js = 'window.open("http://120.78.128.25:8765/Member/index.html");'
        # self.driver.execute_script(js)
    # def check_url(self,url):
    #     assert self.driver.current_url