# -*- coding:utf-8 -*-
# @Time:2019/5/12
# @Author:wangym
# @Email:123@qq.com
# @File:study_work

"""
搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，分离字符串中的数字、中文、拼音、符号。
比如这个字符串：
我的是名字是ths,今年18岁
语法分析后得到结果如下：
数字：18
中文：我的名字是 今年 岁
拼音：ths
符号：，。
请编写程序实现该词法分析功能
"""


# def isAllChinese(data):
#     for j in data:
#         if not (u'\u4e00' <= j <= u'\u9fa5'):
#             return False
#         else:
#             return True
#
#
# str = input("请输入字符串:")
# print(str)
# num =[]
# ch = []
# en =[]
# fu =[]
# for i in str:
#     if i.isdigit()==True:
#         num.append(i)
#     elif isAllChinese(i)==True:
#         ch.append(i)
#     elif i.isalpha()==True:
#         en.append(i)
#     else:
#         fu.append(i)
# print("""
# 数字：{}
# 中文：{}
# 拼音：{}
# 符号：{}""".format(" ".join(num)," ".join(ch)," ".join(en)," ".join(fu)))

"""
2）编写程序实现:
n=5，输出：
--*   1 2
-***   3 1
*****  5 0
 ***
  *  
n=6，输出：
  *  
 ***
*****
*****
 ***
  *"""
n=5
"""
先打空格5-n，*号n
"""
# print("======n=5======")
def phone(n):
    for i in range(1,n+1):
        if i %2 !=0:
           for a in range(n-i):
              print(end=" ")
           for a in range(i):
             print("* ",end="")
           print("")
    for w in range(0,n):
        if w % 2 != 0:
            for j in range(0, w):
                print(end=" ")
            for j in range(w, n-1):
                print("*", end=" ")
            print("")
phone(6)

def fun(n):
    i=1
    w=n
    if n <=1:
       print("n要大于1")
       return
    if n %2 !=0:
        space=int(n//2)+1
    else:
        space=int(n/2)
    print(space)
    while i <= n:
       if (2*i-1) <=n:
     # if i <= h:
         print((space-i)*" ",end="")
         print ("*" *(2*i-1))
       else:
         print((space-w)*" ",end="")
         print("*" * (2* w - 1))
       i = i + 1
       w-=1
fun(6)

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
    if type(data) == dict:
        for j in data:
            newjson[j] = i[k][j]
    if type(data) == str:
        for w in eval(i):
            newjson[w] = eval(i)[w]
