# -*- coding:utf-8 -*-
# @Time:2019/3/17
# @Author:wangym
# @Email:123@qq.com
# @File:testtime

import  time
import  datetime

a=time.strftime("%Y %m %d",time.localtime())
b =time.strptime("20190316","%Y%m%d")
# print(time.time())#当前时间戳
# print(time.localtime())#默认为当前时间戳的时间元祖time（）,k
# print(time.asctime())#默认当前时间Sun Mar 17 16:09:49 2019
# print(time.struct_time)
# print(time.ctime("1552810189.5562181"))#默认当前时间，传时间戳转换日期
print(a)
print(time.mktime(time.localtime()))
datetime.datetime.today()