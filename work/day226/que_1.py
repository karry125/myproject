# -*- coding:utf-8 -*-
# @Time:2019/2/26
# @Author:wangym
# @Email:123@qq.com
# @File:que_1
'''1、请编程实现字符串的转换：将”sdSdsfdAdsdsdfsfdsdASDSDFDSFa”字符串大写变小写，小写变大写。
并且将字符串变为镜像字符串。 例如：字符串里面的’A’变为’Z’,’b’变为’y’ ，
镜像的意思就是照镜子，对比了解下。'''

s = "sdSdsfdAdsdsdfsfdsdASDSDFDSFa"
q = s.swapcase()
print("字符串大写变小写，小写变大写为:", q)
a = str.maketrans("SDsFad", "MVmUZv")  # 字符串映射
print("镜像字符串:", q.translate(a))  # 字符串替换

