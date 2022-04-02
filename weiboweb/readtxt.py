# -*- coding:utf-8 -*-
# @Time:2019/6/12
# @Author:wangym
# @Email:123@qq.com
# @File:readtxt
from  do_excle import do_excle

fielname='account.xlsx'
works=do_excle(fielname,"21")
account=works.read_excle()

with open("ac.txt","r",encoding="utf-8") as file:
    r =file.readlines()
    print(r)
    d = {}
    for i in range(0,len(r)):
        #print(i)

        lii = r[i].strip("\n")
        print(lii, type(lii))
        li = lii.split("----")  # 本来是字符串，分裂成列表
        works.write_excle(i+1,2,str(li[0]))
        works.write_excle(i+1,3,str(li[1]))
        #d[li[0]] = li[1]
        print(li[0],li[1])

    # print(r)
    print(d)
