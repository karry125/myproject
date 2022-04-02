# -*- coding:utf-8 -*-
# @Time:2019/2/21
# @Author:wangym
# @Email:123@qq.com
# @File:que_6
'''经典冒泡算法：
 利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序：
  冒泡排序：小的排前面，大的排后面。'''

a = [1,7,4,89,34,2]
print("原排序{}".format( a))
for i in range(0, len(a)-1):  # len(a)数组会越界,-1最后一位不用在比较
    for j in range(0, len(a)-1-i):  # 每次比较，最大在最后了
        if a[j] > a[j+1]:
            # num = a[j]
            # a[j] = a[j+1]
            # a[j+1] = num
            a[j],a[j+1]=a[j+1],a[j]
    print("第{}次排序后{}".format(i+1, a))
print("最终排序", a)