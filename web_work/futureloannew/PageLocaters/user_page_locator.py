# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:user_page_locator

from selenium.webdriver.common.by import By

class UserPageLocator:

    user_left_money_loc = (By.XPATH,'//li[@class="color_sub"]')
    invest_tab_loc=(By.XPATH,'//div[text()="投资项目"]')
    invest_log_loc = (By.XPATH,'//table[@class="deal_mange_tab"]')
    log_date_loc=(By.XPATH,'//table[@class="deal_mange_tab"]//div[@ms-html="item.date"]')
    log_time_loc = (By.XPATH,'//table[@class="deal_mange_tab"]//div[@ms-html="item.time"]')
