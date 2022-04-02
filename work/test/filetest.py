# -*- coding:utf-8 -*-
# @Time:2019/2/22
# @Author:wangym
# @Email:123@qq.com
# @File:filetest
# file = open("f:\\logi.txt","r")
# print(file.readlines())
# for i in file.readlines():
#      print(i)

# with open("f:\\login.txt","r") as file:
#     for i in file.readlines():
#          print(i)
import requests
def add(**kwargs):
    print(kwargs)
add(a=2,name="name")
b=1,2
print(b)

s =("qwer")
c=s.count("q")
print(c)
print(s.encode("utf-8"))
print(s.endswith(""))

re =requests.get()
def foo(x):
    print(x)
foo(x="q")