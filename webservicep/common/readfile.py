# -*- coding:utf-8 -*-
# @Time:2019/4/19
# @Author:wangym
# @Email:123@qq.com
# @File:readfile


from common import getfile

file=getfile.accountfile

with open(file,"r") as files:
    b = "mobilephone"
    #read =files.readline()
    reads =files.readlines()
    #print(read)
    print(reads)
    #print(read.strip().split(","))
    for a in reads:
        #b = "mobilephone"
        c=a.strip().split(",")[0]
        print("第一个每个",c)
        print(a.strip().split(",")[0])
        if a.strip().split(",")[0] != "mobilephone":
            b=b.replace("mobilephone",c)
        print("循环",b)

#print(b)


