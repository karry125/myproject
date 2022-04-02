# -*- coding:utf-8 -*-
# @Time:2019/3/25
# @Author:wangym
# @Email:123@qq.com
# @File:testmysql

import  pymysql

host = "localhost"
port = 3306
user = "root"
password = "123456"
database = "students"
con = pymysql.connect(host=host,port=port,user=user,password=password,database=database)
#参数为空，返回结果为元祖cursor=pymysql.cursors.DictCursor，返回字典
# 使用 cursor() 方法创建一个游标对象cur，查询页面
cur = con.cursor()
sql="select * from student;"
sqlinsert ='insert into student(name,class) values("王王","大二19班")'

cur.execute(sql) #执行几条数据？
#增删改后都要提交才能更新成功，查不需要
#con.commit()
#关闭游标
cur.close()
#关闭连接
con.close()
# 使用 fetchall() 方法获取查询结果,返回每列值在元祖((1, '某某', '大一15班'), (3, '王王', '大二19班'), (4, '王王', '大二19班'))
r=cur.fetchall()
print(r)
'''f1 = open('test1.txt', 'w')
f1.writelines(["1", "2", "3"])
#    此时test1.txt的内容为:123

f1 = open('test1.txt', 'w')
f1.writelines(["1\n", "2\n", "3\n"])
#    此时test1.txt的内容为:
#    1
#    2        
#    3'''
with open("w.txt","w+",encoding="utf-8") as file:
    for i in r:
        file.write("{},{}\n".format(i[0], i[1]))
        #file.writelines("{},{}\n".format(i[0], i[1]))

        print("{},{}".format(i[0], i[1]))
