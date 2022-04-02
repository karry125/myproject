# -*- coding:utf-8 -*-
# @Time:2020/2/20
# @Author:wangym
# @Email:123@qq.com
# @File:test

import os
import requests
# a=2
# print(type(a))
# s='1' \
#   '2'
#
# print(len(s))
# b=['1','2']
# print(''.join(b))
#
# s1='12345'
# print(s1[-1::-1])
#
# def ad(x,y=9):
#   return x+y
#
# print(ad(1,6))
s=os.path.split(os.path.realpath(__file__))
print(s)

try:#丢丢
    #print(a)
    s=[1,2,3]
    print(s[4])

except IndexError as e:
    print('我要行使班主任的权利把你关起来')
    print('saber一脸蒙蔽，我犯啥事了！')
    print('丢丢说，你犯错误了，错误是：{}'.format(e))
except NameError as e:
    print('我要行使班主任的权利把你关起来')
    print('saber一脸蒙蔽，我犯啥事了！')
    print('丢丢说，你犯错误了，错误是：{}'.format(e))

'1'.split()
import json
re=requests.get()
