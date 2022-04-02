# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_4


year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    print("{}是闰年".format(year))
else:
    print("{}不是闰年".format(year))