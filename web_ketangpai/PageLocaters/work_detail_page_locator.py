# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:work_detail_page_locator

from selenium.webdriver.common.by import By

class DetailLocator:
    chat_page_loc = (By.XPATH,'//a[text()="作业讨论"]')
    click_input_loc = (By.XPATH,'//div[@class="input-click clearfix"]//p')
    comment_input_loc = (By.XPATH,'//textarea[@class="comment-txt"]')
    sure_add_loc = (By.XPATH,'//a[@class="sure active"]')
    comment_list_loc =(By.XPATH,'//ul[@class="comment-list"]//li')
    back_class_loc =(By.XPATH,'//a[@id="return-course"]//i')
    click_msg_loc=(By.XPATH,'//span[@class="s2"]')
    msg_input_loc = (By.XPATH,'//textarea[@id="comment"]')
    sure_msg_loc = (By.XPATH,'//a[contains(@class,"sure active")]')
    upload_loc =(By.XPATH,'//a[@class="sc-btn webuploader-container"]')
    sure_upload_loc = (By.XPATH,'//a[contains(@class,"tj-btn")]')
    close_alert_loc =(By.XPATH,'//a[@class="weui_btn_dialog primary"]')
    new_upload_loc=(By.XPATH,'//a[contains(@class,"new-tj1")]')
    sure_new_upload_loc=(By.XPATH,'//div[@id="update-pop"]//a[contains(@class,"sure")]')
    sencond_upload_sure_loc =(By.XPATH,'//a[contains(@class,"new-tj2")]')
    upload_log_click_loc=(By.XPATH,'//div[@class="homework-log"]//a')
    work_list_loc=(By.XPATH,'//div[@class="work-list"]//li')
    upload_log_list_loc =(By.XPATH,'//div[@class="content"]//li')
