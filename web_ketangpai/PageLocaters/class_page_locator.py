# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:class_locator


from selenium.webdriver.common.by import By


class ClassLocator:
   add_class_button_loc = (By.XPATH,'//div[@class="ktcon1l fl"]')
   class_code_loc = (By.XPATH,'//input[@placeholder="请输入课程加课验证码"]')
   sure_add_class_loc = (By.XPATH,'//a[text()="加入"]')
   alert_close_loc = (By.XPATH,'//a[@class="close"]')
   # //a[text()="Python全栈第15期"]
   class_name_loc = (By.XPATH,'//dt[contains(@class,"bgclass")]//strong//a')