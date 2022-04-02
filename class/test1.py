#-*- coding:utf-8 -*-
#!/usr/bin/python3
#@Time:
#@Author:
#@Email:
#@File:

import time
a = "18"

#print("%d"%a)
d={"name":'华华',
   'hobby':'学Python',
   'age':18,
   'score':{'en':120,'math':99.99,'ch':'A'},
   'friend':['bay max','小CC','如意'],
   True:'good_man',
   0.02:'python',
   False:'这个value对应的key是布尔值',
   (1,2,3):'我就是元组大大！！！',
   0:'这是真爱呀',
   1:'socre is 99.9'}
print(d)
print(id(d[True]),id(d[1]))
print(d[0.02])
'''str = time.strptime("20190216","%Y%m%d")
print(str)
da = time.strftime("%Y {y} %m {m} %d{d} ", time.localtime()).format(y ="年",m="月",d="日")
#dd = time.strftime("%Y 年 %m 月 %d日 ", time.localtime()).format(y ="年",m="月",d="日")
print(da)
print(time.strftime("%a %b %d %H:%M:%S %Y", str))
'''
date = input("请输入日期20190216:")
tupletime = time.strptime(date,"%Y%m%d")
dd  = time.strftime("%Y {} %m {} %d{}",tupletime).format("年", "月", "日")
d = "{}年{}月{}日".format(date[0:4:1],date[5:6:1],date[6:8:1])
a = int('02')
t="abcd"
print(list(t))

print(a)
print(tupletime)
