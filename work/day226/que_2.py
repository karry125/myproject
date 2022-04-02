# -*- coding:utf-8 -*-
# @Time:2019/2/26
# @Author:wangym
# @Email:123@qq.com
# @File:que_2
import  re
'''
搜索引擎中会对用户输入的数据进行处理，第一步就是词法分析，
分离字符串中的数字、中文、拼音、符号。 比如这个字符串： 我的是名字是lemon,今年5岁。
语法分析后得到结果如下：
数字：5
中文：我的名字是、今年、岁
拼音：lemon
符号：，。 请编写程序实现该词法分析功能。
'''

def isAllChinese(s):
     for c in s:
           if not(u'\u4e00' <= c <= u'\u9fa5'):
               return False
           else:
                return True


s = "我的是名字是lemon,今年5岁。"
lnum = []  # 数字
lc = []  # 中文
le = []  # 汉字
lf = []  # 符号

for i in s:
    if i.isdigit() == True:
        lnum.append(i)
    elif isAllChinese(i) == True:  # 先判读中文
        lc.append(i)
    elif i.isalpha() == True:
        le.append(i)
    else:
        lf.append(i)

print('''语法分析后得到结果如下：
         数字是{}
         拼音是{}
         中文是{}
         符号是{}'''.format("".join(lnum), "".join(le),"".join(lc),"".join(lf)))




