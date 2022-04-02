# -*- coding:utf-8 -*-
# @Time:2019/6/23
# @Author:wangym
# @Email:123@qq.com
# @File:file_path
import  os
base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
testdatas_dir =  os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")



htmlreport_dir =  os.path.join(base_dir,"reports")

logs_dir =  os.path.join(base_dir,"logs")

# config_dir =  os.path.join(base_dir,"Config")

screenshot_dir = os.path.join(base_dir,"screenshots")

print(base_dir,screenshot_dir)