# -*- coding:utf-8 -*-
# @Time:2019/3/2
# @Author:wangym
# @Email:123@qq.com
# @File:testfile
'''有两行数据，存在txt文件里面：
url:http://47.107.168.87:8080/futureloan/mvc/api/member/register@mobile:18688773467@pwd:123456
url:http://47.107.168.87:8080/futureloan/mvc/api/member/recharge@mobile:18688773467@amount:1000
请利用上课所学知识，把txt里面的两行内容，写一个函数，返回如下格式的数据：
[{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/register','mobile':'18688773467','pwd':'123456'},
{'url':'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge','mobile':'18688773467','amount':'1000'}]
请自行copy数据到Python里面，进行完整的分析后，再进行程序的编写！！！！'''


def tolist(re):
    l = []
    # d= {}不能放外面，每次赋值到list会覆盖之前值，位置相同
    for i in re:
        d = {}  # 放循环里面，每次重新赋值，地址不一样，不会被覆盖
        j = i.split("\n")
        b = j[0].split("@")  # i.strip("\n").split("@")
        print("切割@后", b)#列表
        for n in b:
            c = n.split(":", 1)
            d[c[0]] = c[1]
            print("切割：", c)
        print("转换成字典", d)
        l.append(d)
        print("每次循环加入到列表后", l)
    #print(id(l[0]), id(l[1]))
    return  l


file = open("url.txt","r",encoding="utf-8")
re = file.readlines()
alist = tolist(re)
print("最终转化list格式:", alist)