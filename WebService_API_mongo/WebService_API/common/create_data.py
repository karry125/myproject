# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import random

from WebService_API.common import config


def get_mobile():
    suffix = config.config.get('db', 'db_name')+config.config.get('db', 'table_name')
    prefix = ['158', '136', '130', '131', '132', '133', '149', '134', '150', '152', '153']
    middle = random.randint(10000, 99999)
    mobile = random.choice(prefix) + str(middle) + suffix
    return mobile


if __name__ == '__main__':
    mobile = get_mobile()
    print(mobile)
