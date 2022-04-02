
t = ()
print(type(t))
t =(1,)
print(t)

a = (1,2,3,4,5)
t1=a[1::2]
t2=a[1:2]
print(t1)
print(t2)

b=[1,2,2]
print(len(b))
print(max(b))

c={(1,2,3),(4,5,6),("b","u","y")}
for k,m,n in c:
    print(k,m,n)

d ={"q":1,"w":2,"e":3}

for k in d:
    print(k,d[k])
for k in d.keys():
    print(k,d[k])
for k,v in d.items():
     print(k,v)
fq =dict(q=1,w=2,e=3)
print(fq)

r = ["b","i","o"]
j =dict.fromkeys(r,"o")
print(j)