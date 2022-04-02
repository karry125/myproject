# -*- coding:utf-8 -*-
# @Time:2019/3/23
# @Author:wangym
# @Email:123@qq.com
# @File:testargs

import  unittest
from ddt import ddt,data,unpack
def prin(*args):
    print(*args)
#
# a = [1,2,3]
# prin(*[[1,2],[3,4]])
# prin([[1,2],[3,4]])
# print(prin(*[[1,2],[3,4]]))
#
#
def prina(**args):
    print(*args)

# prina(a=1,c=4,n=8)
def  sum(a,b):
   return a+b
a=[[1,2],[3,4]]
prin(*a)
dic =[{"mobilephone": "18688773467", "pwd": "123456",},
          {"mobilephone": "18688773467", "pwd": "1234566"},
          {"mobilephone": "186887734657", "pwd": "123456"}]
di ={"mobilephone": "18688773467", "pwd": "123456"}
print(*dic)
#print("{mobilephone}{pwd}".format(*dic))
# @ddt
# class testadd(unittest.TestCase):
#
#     @data((1,2))
#     @unpack
#     def testtadd(self,a,b):
#         print(a,b)
#         self.assertEqual(sum(a,b),3)
#         print(self._testMethodName)
#
# if __name__ == '__main__':
#     #unittest.main()
#     print(dir(testadd))