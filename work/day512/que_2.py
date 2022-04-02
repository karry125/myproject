# -*- coding:utf-8 -*-
# @Time:2019/5/15
# @Author:wangym
# @Email:123@qq.com
# @File:que_2


"""
2）编写程序实现:
n=5，输出：
--*   1 2
-***   3 1
*****  5 0
 ***
  *
n=6，输出：
  *
 ***
*****
*****
 ***
  *"""

def fun(n):
    i=1
    w=n
    if n <=1:
       print("n要大于1")
       return
    if n %2 !=0:
        space=int(n//2)+1
    else:
        space=int(n/2)
    while i <= n:
       if (2*i-1) <=n:
         print((space-i)*" ",end="")
         print ("*" *(2*i-1))
       else:
         print((space-w)*" ",end="")
         print("*" * (2* w - 1))
       i = i + 1
       w-=1
fun(6)

# 行数等于输入数 星号+空格=输入数，前面空格等于后面空格
#（输入的数-型号个数）//2=单边空格

def print_img(n):
    for i in range(1,n+1,2):
        img = " "*((n-i)//2)+"*"*i
        print(img)
    if n%2==0:
        s=n-1
    else:
        s=n-2
    for i in range(s,0,-2):
        img = " "*((n-i)//2)+"*"*i
        print(img)
print_img(5)