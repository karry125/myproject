# -*- coding:utf-8 -*-
# @Time:2019/4/16
# @Author:wangym
# @Email:123@qq.com
# @File:getfile

import os
# 存放配置文件 数据文件路径
# 顶层目录
basefile = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 测试数据路径
casefile = os.path.join(basefile,"data","webcase.xlsx")

switchfile = os.path.join(basefile,"conf","switch.conf")

onfile = os.path.join(basefile,"conf","online.conf")

testfile = os.path.join(basefile,"conf","test.conf")
accountfile=os.path.join(basefile,"data","account.txt")

logsfile = os.path.join(basefile,"logs","log.txt")

cardfile = os.path.join(basefile,"data","distrctcode.txt")