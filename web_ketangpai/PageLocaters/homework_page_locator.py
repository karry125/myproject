# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:homework_locator
from selenium.webdriver.common.by import By
class HomeworkPageLocator:
  work_title_loc = (By.XPATH,'//h3[@class="work-title "]//a')
  student_loc = (By.XPATH,'//li[@class="li5"]//a[text()="同学"]')