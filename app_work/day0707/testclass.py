# -*- coding:utf-8 -*-
# @Time:2020/3/16
# @Author:wangym
# @Email:123@qq.com
# @File:testclass


class Person:
    def __init__(self,name):
        self.name = name



p=Person("aa")
#a=Person.name
#print(a)


class Province(object):  # 类也是一个对象  类对象
    # 类属性 类空间内函数外定义的属性
    country = '中国'

    def __init__(self, name):
        # 实例属性
        self.name = name


# 创建了一个实例对象
obj = Province('山东省')
obj2 = Province('山西省')
# 直接访问实例属性
print(obj.name)
print(obj2.name)
# 直接访问类属性
Province.country

wname=11
