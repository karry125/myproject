# -*- coding:utf-8 -*-
# @Time:2019/2/19
# @Author:wangym
# @Email:123@qq.com
# @File:questions_1

score = float(input("请输入学生成绩："))
print(type(score))
if score >= 90:
    print("学生成绩为{},等级为A".format(score))
elif score >= 80:
    print("学生成绩为{},等级为B".format(score))
elif score >= 70:
    print("学生成绩为{},等级为C".format(score))
elif score >= 60:
    print("学生成绩为{},等级为D".format(score))
else:
    print("学生成绩为{},等级为E,不及格".format(score))



