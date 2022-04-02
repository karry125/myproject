# -*- coding:utf-8 -*-
# @Time:2019/2/16
# @Author:wangym
# @Email:123@qq.com
# @File:datetest
import  time

date = input("请输入日期20190216:")
tupletime = time.strptime(date, "%Y%m%d")
dd = time.strftime("%Y {} %m {} %d{}", tupletime).format("年", "月", "日")
print(dd)
print(tupletime)