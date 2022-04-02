
def fib(n):
    if n==1:
        return 1
    if n==2:
        return  1
    return fib(n-1)+fib(n-2)
#print(fib(5))
l1 = list()
l2 = [1,2,3,4,5]
for i in l2:
    print(i)
print(l2[-4:-2])
print(l2[-2:-4:-1])#左边要小于右边，大于用幅度为负数的
print(id(l2))
l3 = l2[2:4]
print(id(l3)) #id查看编号 编码相同时同一个地址


def han(n ,a,b,c):
    '''

    :param n:
    :param a:
    :param b:
    :param c:
    :return:
    '''
    if n==1:
        print(a,c)
        return  None
    if n==2:
       print(b,c )
       print(a,c)
       print(b,c)
       return None
    han(n-1,a,c,b)# n-1从a借助c移动b
    han(n-1, b,a,c)
han(3,"a","b","c")

a=[1,2,33]
b1 = 4
print(b1 in a)
b2 = [i for i in a if i %2 ==0]#a的元素给b新列表，a列表的偶数
print(b2)


#list 遍历for while


a.append(4)#列表插入
print(a)
a.insert(1,6)#位置从下标计算
print(a)
if 2 in a:
   a.remove(2)
a.reverse()
print(a)
f=a#赋值公用同一个地址
f[2]=20
print(a)
print(f)