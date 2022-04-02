# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_5
'''输出99乘法表 '''
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j,i,i*j), end=" ")
    print()