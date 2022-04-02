class Student():
    def __init__(self,name="1",age=18):
        self.name = name
        self.age = age

    def say(self):
        print(self.age)

Student.__dict__
print(Student.__dict__)
def say(a):
    print(a)
#if __name__ =='__main__':#主程序调敌用才打印，其他引用模板不调用，程序入口
    # print("nihao")
s=Student()
#s.name ="89"
print(s.name)

s.say()
print(type(s.say()))
#Student.age  #类实例

help("keywords")

class Per():
    def fget(self):
        return  self._name
