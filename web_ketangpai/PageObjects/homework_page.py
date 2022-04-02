# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:homework_page
from common.base_page import BasePage
from PageLocaters.homework_page_locator import HomeworkPageLocator as loc
class HomeWorkPage(BasePage):
    def click_work_title(self):
        # 第一个
        self.click_element(loc.work_title_loc)
    def click_student(self):
        self.click_element(loc.student_loc)