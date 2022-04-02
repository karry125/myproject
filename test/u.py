#!/usr/bin/python


a = 1
print(a)
b=2
if b == 2:
    print(6)

for i in range(1,10):
    if i == 7:
        print(i)
print("end")


print("{0}".format(b))
#九九乘法表
for i in range(1,10):
     for j in range(1,i+1):
         print(j*i,end=" ") #end为了不换行
     print("") #为了换行

#定义函数
def p(i):
    for j in range(1, i + 1):
        print(i * j, end = " ")
    print(" ")# 为了换行
for i in range(1,10):
      p(i)

     #关键字函数 字典形式
def stu(**kwargs):
    for k,w in kwargs.items():
        print(k,w)
stu(name="a",age=19)


def stu(*args):
    '''
    函数文档说明
    :param args:
    :return: 返回值
    '''
    for i in args:
        print (i)
#stu(a,b,c)
l=[1,2,3]
stu(*l)# l是list类型，args当作一个参数，用*后可以解包
       #字典dict可以加两个**

#杭州方得投资管理有限公司1010420007290908

def  b():
    global c #全局变量
    c = 100
    print(c)
#print(c)
b()
print(c)  #在函数上面会报错
print(globals()) #打印全局变量
 #eval()  把一个字符串当成表达式来执行，返回表达式执行后的结果

x = 0
def fun( ):
    global x
    x += 1
    print(x)
    fun()
fun()
