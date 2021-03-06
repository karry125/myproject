# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import os


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # API_3
print(base_dir)

root_dir = os.path.dirname(base_dir)

case_file = os.path.join(base_dir, 'data', 'case1.xlsx')
print(case_file)

global_file = os.path.join(base_dir, 'config', 'global.conf')
print(global_file)

online_file = os.path.join(base_dir, 'config', 'online.conf')
print(online_file)

test_file = os.path.join(base_dir, 'config', 'test.conf')
print(test_file)

log_dir = os.path.join(base_dir, 'log')

case_dir = os.path.join(base_dir, 'testcases')

report_dir = os.path.join(base_dir, 'reports')
