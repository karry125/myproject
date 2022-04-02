# -*- coding:utf-8 -*-
# @Time:2019/3/7
# @Author:wangym
# @Email:123@qq.com
# @File:testclass
'''1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，
而后者打印一条消息， 指出餐馆正在营业。 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。'''


class Restaurant:
    here = "hangzhou"
    def __init__(self,restaurant_name,cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print("餐馆名称{},餐馆类型{}".format(self.restaurant_name,self.cooking_type))

    def open_restaurant(self):
        print("餐馆正在营业")


restaurant = Restaurant("中餐厅","中国菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()

'''2:建一个名为 User 的类，其中包含属性 first_name 和 last_name，还有用户简介通常会存储的其他几个属性。
在类 User 中定义一个名为 describe_user()的方法，它打印用户信息摘要；
再定义一个名为 greet_user()的方法，它向用户发出个性化的问候。'''


class User:
    def __init__(self,first_name,last_name,age,job,like):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
        self.like =like

    def describe_user(self, *args):
        d = "、"
        d.join(args)
        print("大家好，我是{}{},{}岁,工作是{},喜欢{}"
              .format(self.first_name, self.last_name,self.age,self.job,self.like, d.join(args)))

    def greet_user(self):
        print("{}{}你好".format(self.first_name,self.last_name))


us = User("karry", "wang","20","测试工程师","旅游")
us.describe_user()
us.greet_user()

'''3：思考问题：

#为什么会有对象方法 类方法 静态方法？我什么时候写什么类型的方法呢？ 

#什么时候用？ 

#写成不同的方法类型 有啥用呢？对我来说有啥用? 

实例方法需要创建实例才能调用，适用于具体对象
类方法，类直接调用，不需要实例，用于某一个类的方法
静态方法，没有self cls参数,没有使用类或实例属性，又归于类的方法方便管理代码逻辑

#他们有什么区别呢？ #自己总结一波。'''
'''
实例方法：有默认self参数
定义 用self调用实例属性跟方法，也可以调用类属性跟类方法
调用 只有实例对象可以调用
类方法：带类参数cls
定义 用cls调用类属性类方法,不能传实例的属性和方法
调用  类跟实例对象都可以调用
静态方法：
定义 不带参数
调用 类跟实例对象都可以调用
'''