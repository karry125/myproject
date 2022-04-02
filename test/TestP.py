#!/usr/bin/python3

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -5.0)
print(x.r, x.i)




'''
class Complexq:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complexq(3.0, -4.5)
print(x.r, x.i)   # 输出结果：3.0 -4.5
'''


class people:
    # 定义基本属性
    name = ""
    age = 0
    __weight = 0
    def __init__(self,n,a,w): #定义构造方法
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s 说：我%d 岁" % (self.name, self.age))

# 实例化
p = people('rose', 10, 30)
p.speak()

#单继承实例
class student(people):
    grage = ''
    def __init__(self, n, a , w,g):
        people.__init__(self,n,a,w) #调用父类的构函
        self.grage = g
    def speak(self): #覆写父类的方法
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grage))
s = student('ken',10 ,60 ,3)
s.speak()


class Parent:  # 定义父类
    def myMethod(self):
        print('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法
super(Child, c).myMethod()  # 用子类对象调用父类已被覆盖的方法 