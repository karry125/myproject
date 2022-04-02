# -*- coding:utf-8 -*-
# @Time:2019/3/21
# @Author:wangym
# @Email:123@qq.com
# @File:http_request

'''3-21 为http_request这个类进行单元测试
1：自己做好梳理和笔记
2：为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试 ，并且用老师教的3个方法 分别去加载用例执行

3：4条用例里面要求有2个正常用例 2个异常用例'''

import requests

class http_request:

    def allrequest(self,mthod,url,params=None):
        if type(params) is not dict:
            paramss=eval(params)
        if mthod.upper() == "GET":
            re = requests.get(url,params=params)
            print(params)
            return re
        elif mthod.upper() == "POST" :
            print(params)

            re = requests.post(url,data=params)
            return re
        else:
            return "请求方式错误"