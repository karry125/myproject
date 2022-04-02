# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:bid_page

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from PageLocaters.bid_locator import BidLocator as loc
import  re
from common.base_page import  BasePage
class BidPage(BasePage):

    def __init__(self,driver):
        self.driver = driver

    def invest(self,money):
        # WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.invest_money_loc))
        # print("投资",money)
        # self.driver.find_element(*loc.invest_money_loc).send_keys(money)
        # time.sleep(1)
        #self.driver.find_element(*loc.invest_button_loc).click()
        self.input_text(loc.invest_money_loc,money)
        time.sleep(5)
        self.click_element(loc.invest_button_loc)


    def get_user_left_money(self):
        self.wait_ele_visible(loc.invest_money_loc,"标页面_获取用户余额")
        user_money =self.get_element_attribute(loc.invest_money_loc,"data-amount","标页面_获取用户余额")
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_money_loc))
        # user_money = self.driver.find_element(*loc.invest_money_loc).get_attribute("data-amount")
        return float(user_money)


    def get_bid_money(self):
        self.wait_ele_visible(loc.bid_left_loc,"标页面_获取标余额")
        bid_money =self.get_element_attribute(loc.invest_money_loc,"data-left","标页面_获取标余额")
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.bid_left_loc))
        # # 获取文本
        # bid_money = self.driver.find_element(*loc.invest_money_loc).get_attribute("data-left")
        print(bid_money)
        return  bid_money

    def invest_max_bid_money(self):
        return  int(self.get_bid_money())+10000

    def invest_user_max_left_money(self):
        return  int(self.get_user_left_money())*100

    def get_alert_error_msg(self):
        self.wait_ele_visible(loc.alert_toast_loc)
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.alert_toast_loc))
        #return self.driver.find_element(*loc.alert_toast_loc).text
        return self.get_element_text(loc.alert_toast_loc)

    def get_button_error_msg(self):
        self.wait_ele_visible(loc.invest_button_loc)
        #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.invest_button_loc))
        return self.get_element_text(loc.invest_button_loc)

    def close_alert(self):
        self.click_element(loc.alert_button_click_loc)
        #self.driver.find_element(*loc.alert_button_click_loc).click()
        print("close")

    def get_invest_success_msg(self):
        return self.driver.find_element(*loc.invest_success_alert_msg).text

    def close_success_alert(self):
        #self.driver.find_element(*loc.invest_success_alert_close).click()
        self.click_element(loc.invest_success_alert_close)

    def replace(self,money):
        if money.find("bid_max")>-1:
            return self.invest_max_bid_money()
        elif money.find("user_max")>-1:
            return  self.invest_user_max_left_money()
        else:
            return money

    def click_user_url(self):
        self.click_element(loc.user_loc)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.user_loc))
        # self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]').click()


    def check_bid_time_allow(self):
        pass

    def check_bid_left_money(self):
        if self.get_bid_money()==0:
            return False
        else:
            return True
