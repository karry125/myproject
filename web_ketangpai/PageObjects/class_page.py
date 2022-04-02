# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:class_page
from common.base_page import BasePage
from PageLocaters.class_page_locator import ClassLocator as loc
import time
class ClassList(BasePage):
    def close_alert(self):
        # # 如果有公告弹框，则需要关闭公告弹框(注意弹框的id带数字，考虑id是变动的)
        try:
          self.wait_ele_visible(loc.alert_close_loc)
          #self.get_element(loc.alert_close_loc)
        except :
            pass
        else:
            self.click_element(loc.alert_close_loc)

    def add_class(self,code):
        self.click_element(loc.add_class_button_loc)
        self.input_text(loc.class_code_loc,code)

        self.click_element(loc.sure_add_class_loc)

    def go_class(self):
        self.click_element(loc.class_name_loc)

    def check_add_class_exist(self):
        self.click_element(loc.alert_close_loc)
        self.wait_ele_visible(loc.add_class_button_loc)
        time.sleep(0.5)
        try:
            self.get_element(loc.add_class_button_loc, "首页_加班级元素")
            return True
        except:
            return False