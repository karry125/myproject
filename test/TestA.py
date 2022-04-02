#!/usr/bin/python3

import sys  # 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
'''
var1 = 100
if var1:
    print('true')
    print(var1)

var2 = 0
if var2:
    print("2")
    print(var2)
print("bye")       #从结果可以看到由于变量 var2 为 0，所以对应的 if 内的语句没有执行

'''


n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

def hell( ):
    print("hello")

hell()



print('命令行参数如下:')
for i in sys.argv:  # 是一个包含命令行参数的列表
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')
'''
str = input("请输入：")
print("你输入的内容是: ", str)


'''
# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))