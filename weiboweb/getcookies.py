# -*- coding:utf-8 -*-
# @Time:2019/6/11
# @Author:wangym
# @Email:123@qq.com
# @File:getcookies

def gettokenweb():
    with open("tokenweb.txt", "r") as file:
        r = file.readline()
        li = r.strip("\n")
        # print(type(li))
        # print(eval(r))
        newd = {}
        for i in eval(r):
            newd[i["name"]] = i["value"]
            #print(i)
        #print(newd)

        return newd


re=gettokenweb()
print(re)


def gettokenwebexcle(cook):
    newd = {}
    for i in eval(cook):
        newd[i["name"]] = i["value"]
        #print(i)
    #print(newd)

    return newd

#gettokenwebexcle()