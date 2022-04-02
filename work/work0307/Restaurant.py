# -*- coding:utf-8 -*-
# @Time:2019/3/9
# @Author:wangym
# @Email:123@qq.com
# @File:Restaurant
'''1：创建一个名为 Restaurant 的类，其方法 init ()设置两个属性： restaurant_name 和 cooking_type。
创建一个名为 describe_restaurant()的方法和一个名为 open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，
 指出餐馆正在营业。 根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。'''


class Restaurant:

    def __init__(self, restaurant_name, cooking_type):
        self.restaurant_name = restaurant_name
        self.cooking_type = cooking_type

    def describe_restaurant(self):
        print("餐馆名称{},餐馆类型{}".format(self.restaurant_name, self.cooking_type))

    def open_restaurant(self):
        print("餐馆正在营业")


restaurant = Restaurant("中餐厅","中国菜")
restaurant.describe_restaurant()
restaurant.open_restaurant()
'''2:写一个子类，继承1 这个父类，
且添加函数：discount 打折扣用的     
 pay_money 支付餐费用，重写 open_restaurant() ，并完成子类完成调用 '''


class Restaurant_1(Restaurant):
    # def __init__(self, restaurant_name, cooking_typ):
    #     self.restaurant_name = restaurant_name
    #     self.cooking_typ= cooking_typ
    def discount(self,money):
        sum = money*(1-0.2)
        print("原价{},8折优惠价格{}".format(money,sum))
        return  sum

    def pay_money(self,payway,money):

        a = self.discount(money)
        print("用{}支付了{}".format(payway,a))

    def open_restaurant(self):
        print("{}{}每周一到周五营业".format(self.restaurant_name,self.cooking_type))


small = Restaurant_1("外婆家","杭帮菜")

small.open_restaurant()
small.pay_money("支付宝",100)

