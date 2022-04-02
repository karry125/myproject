
#p= student()

from TestC import Student
import requests
class people():
    name = "b"
    __age = 14
    def sleep(self):
        print("sleep")


class student(people):
    core = 33
    def sleep(self):
        people.sleep(self)#调用父类方法
        print(self.core)

p = student()
p.sleep()

print(p.name)
print(people.__dict__)
print(p._people__age)

print(issubclass(student,people))
help(issubclass)

a=Student.s
print(a)
#help(requests)