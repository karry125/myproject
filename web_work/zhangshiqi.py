# -*- coding:utf-8 -*-
# @Time:2019/7/23
# @Author:wangym
# @Email:123@qq.com
# @File:zhangshiqi

import time


def runtime(func):
    def wrapper():
        start = time.time()
        f = func()     # 原函数
        end = time.time()
        print("运行时长：%.4f 秒" % (end-start))
        return f
    return wrapper


@runtime
def func_a():
    print("hello")
    time.sleep(0.5)


# @runtime
# def func_b():
#     print("world")
#     time.sleep(0.8)

if __name__ == '__main__':
    func_a()
    #func_b()