# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:user_page
from PageLocaters.user_page_locator import UserPageLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

class UserPage:

    def __init__(self,driver):
        self.driver = driver

    def get_user_left_money(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.user_left_money_loc))
        money =  self.driver.find_element(*loc.user_left_money_loc).text
        return money[:-1:]

    def check_user_url(self,pagetitle):
        return  pagetitle in self.driver.title

    def click_invest_tab(self):
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.invest_tab_loc))
        self.driver.find_element(*loc.invest_tab_loc).click()
        print("tab")

    def get_invest_log_first_page_num(self):
        return len(self.driver.find_elements(*loc.invest_log_loc))

    def get_first_num_time(self):
        date = self.driver.find_element(*loc.log_date_loc).text
        time =self.driver.find_element(*loc.log_time_loc).text
        strtime = date+time
        return strtime