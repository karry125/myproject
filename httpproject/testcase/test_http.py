# -*- coding:utf-8 -*-
# @Time:2019/3/24
# @Author:wangym
# @Email:123@qq.com
# @File:testhttp


from common import exclehelp,mylog
from common.httprequest import HttpRequest
import  unittest
import  time
import  json
import requests
import os
from ddt import  ddt,data,unpack
@ddt
class Testhttp(unittest.TestCase):
    file = os.path.dirname(os.path.realpath(__file__))
    files = os.path.join(os.path.dirname(file), "data", "http.xlsx")
    work = exclehelp.xlsxhelp(files, "Sheet1")
    datas = work.readall()
    #print(datas)
    rowss = work.getrows()
    def setUp(self):
        file = os.path.dirname(os.path.realpath(__file__))
        files = os.path.join(os.path.dirname(file), "data", "http.xlsx")
        self.work = exclehelp.xlsxhelp(files, "开心")
        self.data =self.work.readall()
        self.rows=self.work.getrows()

        #print(self.data[1])
    a =[['https://api.douban.com/v2/movie/search', 'get', '{"q":"白夜追凶"}'],
        ['https://api.douban.com/v2/movie/search', 'get', '{"q":"张艺谋"}']]
    # @data(*a)
    # @unpack
    def test_login(self):
       # for i in range(len(*(self.data))):
       """url mothod data"""
       #print(self.data[0])
       #re = HttpRequest().req(url, mthod, para)
       #re= requests.get('https://api.douban.com/v2/movie/search',params={"q":"张艺谋"})
       #print( json.dumps(re.json(), ensure_ascii=False, indent=4))
       for i in range(2,self.rows+1):
           # da = self.work.readrowcell(i)
           # url = self.work.readcell(i,1)
           # mothod =self.work.readcell(i,2)
           # data = self.work.readcell(i,3)
           # header = self.work.readcell(i,4)
            da = self.work.readrowcell(i)
            re = HttpRequest().req(da[0], da[1], da[2])
            print(re.json())

          # re = HttpRequest().httprequests(self.data[1],self.data[0],self.data[2])

            #print(re.text)
           #time.sleep(10)








