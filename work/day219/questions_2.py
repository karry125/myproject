# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_2

price = float(input("请输入价格："))
if (price >= 50 )and (price <= 100):
    newprice = round(price *(1-0.1),2)
    print("您输入的价格{}，折扣10%，最终价格为{}".format(price,newprice))  # 用%f格式化，10%会报错，要加10%%
elif price > 100:
    newprice = round(price * (1-0.2),2)
    print("您输入的价格{}，折扣20%，最终价格为{}".format(price, newprice))
else:
    print("您输入的价格{}，没有折扣".format(price))