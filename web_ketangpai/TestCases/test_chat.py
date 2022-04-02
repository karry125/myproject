# -*- coding:utf-8 -*-
# @Time:2019/7/3
# @Author:wangym
# @Email:123@qq.com
# @File:test_chat
import pytest
from PageObjects.student_page import StudentPage
from PageObjects.class_page import ClassList
from PageObjects.homework_page import HomeWorkPage
from TestDatas.chat_data import success_data as sd
from TestDatas.chat_data import fail_data as fd
import time
import allure
@allure.feature("聊天")
@pytest.mark.usefixtures("login_web")
@pytest.mark.usefixtures("go_student_detail")
class TestChat:

    @allure.story("发送私信")
    @pytest.mark.parametrize("data",sd)
    def test_chat_msg(self,data,login_web):
        """
        用例描述：发送私信
        :param data:
        :param login_web:
        :return:
        """
        # ClassList(login_web).close_alert()
        # time.sleep(3)
        # ClassList(login_web).go_class()
        # HomeWorkPage(login_web).click_student()
        sp=StudentPage(login_web)
        #num=sp.check_msg_list()
        sp.send_msg(data)
        # after_num=sp.send_msg(data)
        # assert num+1==after_num

    @allure.story("发送失败私信")
    @pytest.mark.parametrize("data", fd)
    def test_chat_fail_msg(self, data, login_web):
        """
        用例描述：发送空消息
        :param data:
        :param login_web:
        :return:
        """
        # ClassList(login_web).close_alert()
        # time.sleep(3)
        # ClassList(login_web).go_class()
        # HomeWorkPage(login_web).click_student()
        StudentPage(login_web).send_msg(data["msg"])
        assert data["check"]==StudentPage(login_web).get_error_msg()

if __name__ == '__main__':
    pytest.main(["-s","test_chat.py"])