# -*- coding:utf-8 -*-
# @Time:2019/3/24
# @Author:wangym
# @Email:123@qq.com
# @File:httprequest

import requests
from common.exclehelp import xlsxhelp

class HttpRequest:
    def req(self,url,mothod,data):

        self.mothod = mothod
        self.url =url
        self.data =data

        if self.mothod == "get":
            # data=json.dumps(eval(self.data)
            #print(eval(self.data))
            return requests.get(url, params=eval(data) )
        elif self.mothod == "post":
            return requests.post(url, data=eval(data))
        else:
            print("pp", self.mthod)
            return "error"

    def httprequests(self):

        if self.mothod  == "get":
            #data=json.dumps(eval(self.data)
            return requests.get(self.url, self.data,self.header)
        elif self.mothod == "post":
            return requests.post(self.url, eval(self.data),self.header)
        else:
            print("pp",self.mthod)
            return  "error"

    def get(self,url,params,headers=None):
        return requests.get(url,params,headers=headers)

    def post(self, url, data=None,json=None, headers=None,cooki=None):
        return requests.post(url, data,json, headers=headers,cookies=cooki)

    def allrequest(self,mothod,url, data=None,headers=None,cooki=None):
        if self.mothod == "get":
            return requests.get(self.url, self.data)
        elif self.mothod =="post":
            return requests.post(self.url,self.data)

if __name__ == '__main__':
    https = HttpRequest()
    work = xlsxhelp("../data/http.xlsx", "开心")
    url=work.readcell(2,1)
    mothod = work.readcell(2,2)
    data = work.readcell(2,3)
    re=https.httprequests(url,mothod,data)
    print(re.text)
