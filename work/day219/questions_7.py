# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_7

account = {"name": "huahua", "pwd": 123456}

name = input("请输入用户名：")
pwd = int(input("请输入密码："))
if name in account.values() and pwd in account.values():
    print("登录成功")
else:
    print("用户名或密码错误")
