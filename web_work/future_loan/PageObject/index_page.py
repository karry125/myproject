# -*- coding:utf-8 -*-
# @Time:2019/6/7
# @Author:wangym
# @Email:123@qq.com
# @File:index_page


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

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