# -*- coding:utf-8 -*-
# @Time:2019/5/15
# @Author:wangym
# @Email:123@qq.com
# @File:que_1

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
import re

def isAllChinese(data):
    for j in data:
        if not (u'\u4e00' <= j <= u'\u9fa5'):
            return False
        else:
            return True


str = input("请输入字符串:")
print(str)
num =[]
ch = []
en =[]
fu =[]
for i in str:
    if i.isdigit()==True:
        num.append(i)
    elif isAllChinese(i)==True:
        ch.append(i)
    elif i.isalpha()==True:
        en.append(i)
    else:
        fu.append(i)
print("""
数字：{}
中文：{}
拼音：{}
符号：{}""".format(" ".join(num)," ".join(ch)," ".join(en)," ".join(fu)))

# 正则表达式查找 /d
def p(s):
    # num = []
    # ch = []
    # en = []
    # fu = []
    pa={"数字":"\d","拼音":"[a-zA-Z]","汉字":"[\u4e00-\u9fff]"}
    for k,v in pa.items():
        num = re.findall(v, s)
        print(k+":"+"".join(num))
        # 替换成空字符
        s = re.sub(v, " ", s)
    print("符号:{}".format(s))

    # if re.search("\d",s):
    #     num=re.findall("\d",s)
    #     s=re.sub("d"," ",s)

p(str)

