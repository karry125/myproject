# -*- coding:utf-8 -*-
# @Time:2019/7/3
# @Author:wangym
# @Email:123@qq.com
# @File:student_page
from common.base_page import BasePage
from PageLocaters.student_page_locator import StudentLocator as loc
import time
class StudentPage(BasePage):

    def click_all_student(self):
        self.click_element(loc.all_student_loc)
    def click_stu_chat(self):
        self.move_click_element(loc.sen_student_loc,loc.msg_loc)
    def send_msg(self,msg):
        self.click_all_student()
        time.sleep(2)
        self.click_stu_chat()
        self.input_text(loc.chat_input_loc,msg)
        self.click_element(loc.send_msg_loc)
        time.sleep(2)
        self.click_element(loc.close_chat_loc)
    def get_error_msg(self):
        self.wait_ele_visible(loc.error_toast_loc)
        return self.get_element_text(loc.error_toast_loc)
    def check_msg_list(self):
        self.wait_ele_visible(loc.msg_list_loc)
        return len(self.get_elements(loc.msg_list_loc))