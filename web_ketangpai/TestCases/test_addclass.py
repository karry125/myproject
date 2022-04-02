# -*- coding:utf-8 -*-
# @Time:2019/7/2
# @Author:wangym
# @Email:123@qq.com
# @File:test_addclass
import pytest
import time
from PageObjects.class_page import ClassList
@pytest.mark.usefixtures("login_web")
class TestAddClass:
    @pytest.mark.skipif()
    def test_add_sucess_class(self,login_web):
       cl= ClassList(login_web)
       cl.close_alert()
       time.sleep(2)
       cl.add_class("123456")



if __name__ == '__main__':
   pytest.main(["-s","test_addclass.py"])
