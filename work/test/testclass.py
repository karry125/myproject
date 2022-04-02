# -*- coding:utf-8 -*-
# @Time:2019/2/25
# @Author:wangym
# @Email:123@qq.com
# @File:testclass


class Person(object):
    address = 'Earth'  # 类属性address
    name = "leilei"
    __sum= 12
    def __init__(self, name):
        self.name = name
        print(self.__sum)
        #print(Person.name) 无属性
        print(id(self.name))
        print(id(Person.name))
    def __pay(self):
        print("pay")
    def sum(self):
        print("sum")
    def aum(self):
        self.__pay()
        #self.speak()
        self.play()

        #print(Person.pay()) # 实例方法不能类调用
    @classmethod
    def  add(cls):
        Person.play()
        print("lei")
    @classmethod
    def speak(cls):
       # cls.aum()
        cls.play()
        ##cls.aum()

        print("类")
    @staticmethod
    def play():
       #Person.add()
       print("静态",Person.address)

print (Person.address)  # => Earth  类属性直接绑定在类上的，可以不实例化直接通过类名调用类属性

p1 = Person('Bob')
#p2 = Person('Alice')
print (p1.aum())  # => Earth   # 通过实例来调用类属性
#print (p2.address)
a =10
#print('10%%,%f'%(a))
print(p1._Person__sum)
print(p1._Person__pay())
print(Person.__dict__)

# str = "-";
# seq = ("a", "b", "c"); # 字符串序列
# print (str.join( seq ))
