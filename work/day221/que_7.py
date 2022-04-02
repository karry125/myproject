# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_7


'''
有1 2 3 4 这四个数字，能组成多少个互不相同且无重复数字的三位数？
分别是什么？abc a!=b!=c
'''

l = [1,2,3,4]
count = 0
for i in range(0, len(l)):
   # print(l[i])
    for j in range(0, len(l)):
        for m in range(0, len(l)):
            if l[i] != l[j] != l[m] and l[i] != l[m]:
                count += 1
                print("{}{}{}".format(l[i],l[j],l[m]))
print("有1 2 3 4 这四个数字，共组成{}个互不相同的三位数".format(count))