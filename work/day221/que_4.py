# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_4
'''
利用Python代码画出直角三角形以及等边三角形，
'''
# 直角三角形
for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()
# 等边三角形
for m in range(0, 5):
    for n in range(0, 4-m):
        print(end=" ")
    for o in range(0,m+1):
        print("*", end=" ")
    print()

for i in (1,2,3,4,5):
    print(' '*(5-i), end="")
    print((" *")*i)