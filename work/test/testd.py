# -*- coding:utf-8 -*-
# @Time:2019/2/23
# @Author:wangym
# @Email:123@qq.com
# @File:testd

for i in range(0,0):
    print(i)

a = [1,2,3,4,2,5,6,3,4,3,4,4]

b =[]
c =[]
for i in a:
    if i not in b:
        b.append(i)
print(b)

for j in b:
   c.append(a.count(j))
print(c)

for m in range(len(c)-1):
    for n in range(0,len(c)-m-1):
        if c[n]<c[n+1]:
            c[n+1],c[n]=c[n],c[n+1]
            b[n + 1], b[n] = b[n], b[n + 1]

    print("第{}排序{}".format(m,c))
    break
print(b)
print(c)

print(list(set(a)))
l ="qwerrrw"
lists= list(l)
lists.sort()
print(l.count("w"))
