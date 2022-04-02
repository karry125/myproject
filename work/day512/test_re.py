# -*- coding:utf-8 -*-
# @Time:2019/5/29
# @Author:wangym
# @Email:123@qq.com
# @File:test_re


import re

a="<12>12345<12/>"
p="\>(.*?)\<"
if re.search(p,a):
    v=re.search(p,a)
    m=v.group(1)
    print(m,v)
    #b=a.replace(m,"888")
    c=re.sub(p,m,a)
    print(a,c)

a.strip()