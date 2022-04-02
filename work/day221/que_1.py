# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_1
import  random

role = {1: "曹操", 2: "张飞", 3: "刘备"}
play = {1: "剪刀", 2: "石头", 3: "布"}
computercount = 0  # 电脑赢几局
playercount = 0  # 玩家赢几局
ping = 0  #平局
roleinput = int(input("请选择玩家1 曹操 2张飞 3 刘备,输入数字："))
if roleinput not in role:
    print("请重新选择玩家：")
while 1:
        num = random.randint(1, 3)  # 电脑随机出1 2 3
        playinput = int(input("请出拳1剪刀 2石头 3布,输入数字:"))  # 玩家出拳
        if playinput not in play:
            print("请重新输入：")
        else:
            print(("玩家{}出{}，电脑出{}".format(role[roleinput], play[playinput], play[num])))
        if playinput == num:
            print("猜拳结果平局")
            ping +=1
        elif playinput == 1 and num == 3 or playinput == 2 and num == 1 or playinput ==3 and num ==2:
            playercount += 1
            print("猜拳结果玩家赢")
        else:
            computercount += 1
            print("猜拳结果电脑赢")
        again = input("是否继续YN:")
        if again == "Y" or again == "y":
            continue
        else:
            break

print("玩家角色{}赢{}局,电脑赢{}局".format(role[roleinput], playercount, computercount))
