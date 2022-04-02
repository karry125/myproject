# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_3

''' 一个足球队在寻找年龄在10岁到12岁的小女孩（包括10岁和12岁）加入。
编写一个程序，询问用户的性别（m表示男性，f表示女性）和年龄，
然后显示一条消息指出这个人是否可以加入球队，询问10次后，输出满足条件的总人数。 '''

i = 0
num = 0
while i < 10:
    age = int(input("请输入您的年龄："))
    sex = input("请输入M/F:")
    if (age >= 10 and age <= 12) and (sex == "F" or sex == "f"):
        print("你可以加入足球队")
        num += 1
    else:
        print("你不可以加入足球队")
    i += 1
print("共{}人可以加入".format(num))