# -*- coding:utf-8 -*-
# @Time:2019/3/9
# @Author:wangym
# @Email:123@qq.com
# @File:classjic


class Peson():
    name = "wo"
    def __init__(self):
       pass
    def add(self):
        print("self")
    @classmethod
    def speak(cls):
        print("类")

    @staticmethod
    def say():
        print("静态")

class boy(Peson):
    def __init__(self):
        print("子类初始化")
    def play(self):
        print("子类")

boy.say()

boy.speak()
a  = boy()
a.add()