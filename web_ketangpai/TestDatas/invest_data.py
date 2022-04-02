# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:invest_data


success_data = {"money":"100","check":"投标成功！"}

# 金额是10倍数 空格 负数错误弹窗提示 超过用户余额 超过标余额
'''
{'''
fail_data = [{"money":"10","check":"投标金额必须为100的倍数"},
             {"money": " ", "check": "请正确填写投标金额"},
             {"money": "-100", "check": "请正确填写投标金额"},
             {"money": "0", "check": "请正确填写投标金额"},
             {"money": "user_max", "check": "投标金额大于可用金额"},
             {"money": "bid_max", "check": "购买标的金额不能大于标剩余金额"}]

# 金额不是10的倍数/小数点/负数
wrong_data = [{"money":"12","check":"请输入10的整倍数"},
              {"money": "10.23", "check": "请输入10的整倍数"},
              {"money": "Ni", "check": "请输入10的整倍数"},]