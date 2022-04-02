# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:test_work
from PageObjects.home_detail_page import DetailPage
from PageObjects.homework_page import HomeWorkPage
from PageObjects.class_page import ClassList
import pytest
import time
import allure
@pytest.mark.usefixtures("login_web")
@pytest.mark.usefixtures("go_work_detail")
@allure.feature("作业")
class TestWork:
    @allure.story("上传文件")
    def test_upload(self,go_work_detail,login_web):
        time.sleep(2)
        work_num=go_work_detail.check_work_list()
        print(work_num)
        log_num =go_work_detail.check_upload_log()
        print(log_num)
        time.sleep(2)
        go_work_detail.new_upload("f:\\o.html")
        login_web.refresh()
        time.sleep(2)
        after_work_num = go_work_detail.check_work_list()
        after_log_num = go_work_detail.check_upload_log()
        print(work_num,log_num,after_log_num,after_work_num)
        assert work_num+1==after_work_num
        #assert log_num+1==after_log_num

    @pytest.mark.xfail
    def test_add_msg(self,go_work_detail):
        go_work_detail.add_work_msg("msg")

    @allure.story("评论")
    def test_add_comment(self,go_work_detail):
        # ClassList(login_web).close_alert()
        # time.sleep(3)
        # ClassList(login_web).go_class()
        # HomeWorkPage(login_web).click_work_title()
        # dp = DetailPage(login_web)
        # dp.go_work_detail()
        go_work_detail.click_comment()
        com_list = go_work_detail.check_comment_list()
        go_work_detail.add_comment("test")
        time.sleep(1)
        after_list=go_work_detail.check_comment_list()
        assert com_list+1==after_list





if __name__ == '__main__':
    pytest.main(["-s","test_work.py"])


