# -*- coding:utf-8 -*-
# @Time:2019/5/15
# @Author:wangym
# @Email:123@qq.com
# @File:que_3


"""
传入一个Json串，返回一个字典，字典只取出Json最底层的数据，
中间如果有字符串也要进行处理，请以下面的数据为例，请用递归方法实现
Json：{"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
输出：
Dic:{'a':'aa','c':'cc','d':'dd','e':'ee'}
"""
json={"a":"aa","b":['{"c":"cc","d":"dd"}',{"f":{"e":"ee"}}]}
newjson={}
for key in json:
    if type(json[key]) == str:
        newjson[key]=json[key]
    elif type(json[key]) == list:
        # 循环列表值
        for i in json[key]:
            # 判断值类型
            if type(i) == dict:
                # 在读取字典值i,列表
                for k in i:
                   if type(i[k]) == dict:
                     for j in i[k]:
                        newjson[j]=i[k][j]
            elif type(i)==str:
                for w in eval(i):
                    newjson[w]=eval(i)[w]

print(newjson)

def read(data):
    newjson={}
    if type(data) == str:
        data =eval(data)
    if type(data) == dict:
        for k,v in data.items():
            if type(v) == list or type(v)==dict:
                d=read(v)
                newjson.update(d)
            else:
                newjson[k]=v
    if type(data) == list:
        for i in data:
            d= read(i)
            newjson.update(d)

    return newjson
a=read(json)
print(a)