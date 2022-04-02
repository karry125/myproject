# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_3
 
 
num = int(input("请输入整数："))
if num % 3 == 0 and num % 5 == 0:
    print("{}能同时被3和5整除".format(num))
else:
    print("{}不能同时被3和5整除".format(num))