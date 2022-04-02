# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:bid_locator


from selenium.webdriver.common.by import By

class BidLocator:
    invest_money_loc = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    # 金额输入10才显示投标，按钮显示提示不同
    invest_button_loc=(By.XPATH,'//button[@class="btn btn-special height_style"]')
    bid_left_loc = (By.XPATH,'//span[@class="mo_span4"]')
    user_left_money_loc = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')
    alert_toast_loc = (By.XPATH,'//div[@class="text-center"]')
    alert_button_click_loc = (By.XPATH,'//a[@class="layui-layer-btn0"]')
    invest_success_alert_msg = (By.XPATH,'//div[@class="layui-layer-content"]//div[@class="capital_font1 note"]')
    #//div[text()="投标成功！"]//preceding-sibling::div[@class="close_pop"]//img
    invest_success_alert_close = (By.XPATH,'//div[@class="layui-layer-content"]//div[@class="close_pop"]//img')
    user_loc = (By.XPATH,'//a[@href="/Member/index.html"]')