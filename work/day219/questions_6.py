# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_6
import random

num = int(input("请输入数："))
ran = random.randint(1,9)
if num > ran:
    print("bigger",ran)
elif num < ran:
    print("less",ran)
elif num == ran:
    print("equal",ran)

