# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:home_detail_page

from PageLocaters.work_detail_page_locator import DetailLocator as loc
from common.base_page import BasePage
from common.uploadfile import upload
from PageObjects.homework_page import HomeWorkPage
from PageObjects.class_page import ClassList
import  time
class DetailPage(BasePage):

    def click_comment(self):
        self.click_element(loc.chat_page_loc)
    def add_comment(self,msg):
        self.click_element(loc.click_input_loc)
        self.input_text(loc.comment_input_loc,msg)
        self.click_element(loc.sure_add_loc)
    def add_work_msg(self,msg):
        self.click_element(loc.click_msg_loc)
        self.input_text(loc.click_input_loc,msg)
        self.click_element(loc.sure_msg_loc)

    def upload_file(self,file):
        self.click_element(loc.upload_loc)
        time.sleep(3)
        upload(file)
        self.click_element(loc.sure_upload_loc)
        self.click_element(loc.close_alert_loc)
    def new_upload(self,file):
        self.click_element(loc.new_upload_loc)
        self.click_element(loc.sure_new_upload_loc)
        self.click_element(loc.upload_loc)
        time.sleep(3)
        upload(file)
        time.sleep(2)
        self.click_element(loc.sencond_upload_sure_loc)
        #self.driver.switch_to.alert.accept()
        time.sleep(3)
        self.click_element(loc.close_alert_loc)
    def go_work_detail(self):
        ClassList(self.driver).close_alert()
        time.sleep(3)
        ClassList(self.driver).go_class()
        HomeWorkPage(self.driver).click_work_title()
    def check_upload_log(self):
       self.click_element(loc.upload_log_click_loc)
       self.wait_ele_visible(loc.upload_log_list_loc)
       return len(self.get_elements(loc.upload_log_list_loc))

    def check_work_list(self):
        return len(self.get_elements(loc.work_list_loc))

    def check_comment_list(self):
        self.wait_ele_visible(loc.comment_list_loc)
        return  len(self.get_elements(loc.comment_list_loc))