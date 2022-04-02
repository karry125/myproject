# -*- coding:utf-8 -*-
# @Time:2021/1/9
# @Author:wangym
# @Email:123@qq.com
# @File:testrequest


import  requests
from datetime import datetime
import time

res = requests.get("http://www.baidu.com")
#print(res.text)

buy_time = datetime.strptime("2021-01-02 09:59:59.500", "%Y-%m-%d %H:%M:%S.%f")
buy_time_ms = int(time.mktime(buy_time.timetuple()) * 1000.0 + buy_time.microsecond / 1000)
print(buy_time.timetuple())
print(buy_time.microsecond)
print(buy_time_ms)
print(buy_time)
print(time.mktime(buy_time.timetuple()))