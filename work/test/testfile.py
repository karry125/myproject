# -*- coding:utf-8 -*-
# @Time:2019/3/24
# @Author:wangym
# @Email:123@qq.com
# @File:testfile

import  os
print(os.getcwd())
p=os.path.realpath(__file__)
print(p)
print(os.path.abspath("re.html"))
print(os.path.split(p))#元祖
s ="a b"
print(s.split())
print(os.path.dirname(p))