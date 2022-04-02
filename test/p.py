try:
   num = int(input("请输入："))
   rs = 100/num
   print(rs)
except ZeroDivisionError as e:#实例化异常
    print(e)


import calendar
ca = calendar.calendar(2017)
import os.path
r= os.system("ls")
print(r)
print(os.getcwd())