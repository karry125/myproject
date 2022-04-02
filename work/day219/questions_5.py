# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_5

num = input("请输入五位数：")
if len(int(num)) != 5:
    print("请输入五位数字")
elif num[0] == num[-1] and num[1] == num[-2]:  # num == num[::-1]
    print("{}是回文数".format(num))
else:
    print("不是回文数")


