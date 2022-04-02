# -*- coding:utf-8 -*-
# @Time:2019/4/20
# @Author:wangym
# @Email:123@qq.com
# @File:context
import re
from common.readconf import conf
import random
from inspect import isfunction
import datetime
from common.getfile import cardfile


class Context:
    """存储变量值"""
    code = None


def getuid():
    """获得用户名"""
    name="karry"+str(random.randint(10,1000))
    return  name


def getcre_id():
        """获取身份证"""
        codelist = []
        with open(cardfile, mode="r", encoding="utf-8") as file:
            codelist = file.readlines()
            print(codelist)
            id = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
            id = id + str(random.randint(1980, 2019))  # 年份项
            da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))  # 月份和日期项
            id = id + da.strftime('%m%d')
            id = id + str(random.randint(100, 300))  # ，顺序号简单处理

            i = 0
            count = 0
            weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
            checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5',
                         '8': '5', '9': '3', '10': '2'}  # 校验码映射
            for i in range(0, len(id)):
                count = count + int(id[i]) * weight[i]
            id = id + checkcode[str(count % 11)]  # 算出校验码
            return id


def contextss(data):
    p = "\$\{(.*?)\}"  # p1="#(.*?)#"
    while re.search(p,data):
            print(data)
            m = re.search(p, data)  # 从任意位置开始找，找第一个就返回Match object, 如果没有找None
            keys = m.group(1) # 获取参数值，不带##，group没有参数或者0，有##
            print(keys)
            try:
               value = conf.getstr("webdata",keys) # 从配置文件读取值，找不到用上下文类取值
            except Exception as e:
                if hasattr(Context,keys):
                    value=getattr(Context,keys)
                    print("添加项目值",value)
                elif isfunction(eval(keys)):
                    value = eval(keys+"()")
                else:
                    print("没有对应值")
                    raise e
            print(type(value))
            """
            # data是字符串，value需要时字符串或者方法，不能用int或其他类型，
            # 传值时转换查找到p的内容，用value替换，
            # count次数限制，替换后继续用data，保证下次替换的是上次替换过的
            """
            data = re.sub(p, value, data, count=1)
            # print(para)
            #  return data 结束循环，只替换了一个
    return data

def query_mvcode(mobile):
        db_name = mobile[9:11]
        table_name = mobile[8]
        sql = 'SELECT * FROM sms_db_{0}.t_mvcode_info_{1} WHERE Fmobile_no="{2}"'.format(db_name, table_name, mobile)
        print(sql)
        # row = self.mysql.fetch_one(sql)
        # if row:
        #     return row["Fverify_code"]





# paras='{"mobilephone":"#login_user#","pwd":"#login_pwd#","pwd":"${login_pwd}"}'
# para ='{"mobilephone":"#login_user#","pwd":"#login_pwd#"}'
# p = r'\$\{(.*?)\}' # 元字符需要反斜杠转义
# p1="#(.*?)#"
# a =re.compile(p)
# r = re.search(p,paras)
# all =re.findall(p,paras)  # ()只返回（）内容
# # # keys =r.group(1)
# # # b = re.sub(p,"137",para,count=1)
# print(r)
# print(all)
# # print(b)
# print(r.group(1))
# while re.search(p, para):
#     print(para)
#     r = re.search(p, para)
#     keys = r.group(1)
#     print(keys)
#     value = conf.getstr("data", keys)
#     print(value)
#     para = re.sub(p, value, para, count=1)
#     print(para)
# setattr(Context,"mobile","1234")
# setattr(Context,"code","2344")
data='{"mobilephone":"${getuid}","pwd":"#login_pwd#"}'
dats='{"channel_id":2,"ip":"129.45.6.7","mobile":${mobiles} ,"pwd":"123456","user_id" :"karry1","verify_code":${code}}'
# u='{"channel_id":2,"ip":"10.0.10.18","mobile":${mobiles} ,"pwd":"123456","user_id" :"karry6","verify_code":"${code}"'
# f=contextss(u)
# print(f)
#for d in data.items():
#    print(d)
# f = contextss(data)
# print(f)
# r = getuid()
# print(isfunction(getuid))
# print(r)
# n =replace(data)
# print(n)
# r= getcre_id()
# print(r)

query_mvcode("13722222222")
