# -*- coding:utf-8 -*-
# @Time:2019/4/9
# @Author:wangym
# @Email:123@qq.com
# @File:http_request

import requests
import json

class http_request:
    # def __init__(self):
    #     self.session = requests.sessions.session()
    #     self.session.request()
    def httprequest(self,mthod,url,params,header=None,cookies=None):
           #可以保存历史cookie
            if mthod.upper() == "GET":
                try:
                    re = requests.get(url, params=params,headers=header,cookies=cookies)
                    return re
                except Exception as e:
                    return e
            elif mthod.upper() == "POST":
                re = requests.post(url, data=params,headers=header,cookies=cookies)
                return re
            else:
                return "请求方式错误"
    def close(self):
        self.session.close()
