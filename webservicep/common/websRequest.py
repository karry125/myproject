# -*- coding:utf-8 -*-
# @Time:2019/4/28
# @Author:wangym
# @Email:123@qq.com
# @File:websRequest
from suds.client import Client
from common.DoMysql import DoMysql
from common.readconf import conf
from suds import sudsobject
import json
from common.mylogs import mylogs,mylogger


class WebsRequset:
    mylog = mylogger(__name__)

    def sendrequest(self,url,api,para=None):
        """
        :param url: url地址
        :param api: 接口名称
        :param para: 参数 dict
        :return:
        """
        url = conf.getstr("api","weburl")+url
        self.mylog.debug("url地址:{}".format(url))
        self.mylog.debug("请求参数:{}".format(para))
        client = Client(url)
        api = "client.service.{}".format(api)
        # 空传None？转成字典
        if type(para) == str:
            para = eval(para)
        try:
           re = eval(api)(para)
        except Exception as e:
            re = e
        return re

    def GetArrayOfStringValue(self, array, info):
        '''处理webservice返回的array of string，并获取返回值列表'''
        getarray = array
        getdict = sudsobject.asdict(getarray)
        getlist = getdict.get('%s' % info)
        return getlist

if __name__ == '__main__':
    webs=WebsRequset()
    # url = "http://120.24.235.105:9010/sms-service-war-ws/smsF1.0/acade.ws?wsdl"
    dict = {"client_ip": "10.0.10.229", "tmpl_id": 1, "mobile": "13704399912"}
    # re = webs.sendrequest(url,"sendMCode",dict)
    # api = "client.service.{}".format("sendMCode")
    # # re = eval(api)
    # print(sudsobject.asdict(re))
    # mysql=DoMysql()
    url="http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
    client = Client(url)
    d='{"client_ip":"10.0.10.229","mobile":"13730000678","tmpl_id":null}'
    dict2={"client_ip":"10.0.10.229","tmpl_id":1,"mobile":"13702001921"}
    # re=client.service.sendMCode(dict)
    # # sqle='select * from sms_db_21.t_mvcode_info_9 where Fmobile_no="13702001921"'
    # # code= mysql.fetchone(sqle)["Fverify_code"]
    # print(re)
   #  """
   #  {'Fmobile_no': '13700000921', 'Ftmpl_id': 1, 'Fverify_code': '260853', 'Frela_key': None, 'Frela_info': None, 'Fchk_suc_times': 0, 'Fchk_err_times': 0, 'Fclient_ip': '10.0.10.229', 'Fsend_time': datetime.datetime(2019, 4, 28, 21, 59, 27), 'Fcheck_time': None, 'Fexpired_time': datetime.datetime(2019, 4, 28, 22, 5, 27), 'Fstandby1': None, 'Fstandby2': None}"""
    registurl="http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
    clientre=Client(registurl)
    pa={"channel_id":2,"ip":"129.45.6.7","mobile":13700001921 ,"pwd":"123456","user_id" :"karry","verify_code":12}#用字典的方式传值
    p={"channel_id":2,"ip":"129.45.6.9","mobile":13704395912 ,"pwd":"123456","user_id" :"rr","verify_code":246183}
    y={"channel_id":2,"ip":"10.0.10.11","mobile":13703391912,"pwd":"123456","user_id":"karry38","verify_code":904718}
    u={"channel_id":2,"ip":"10.0.10.118","mobile":13704401912,"pwd":"123456","user_id":"karry12","verify_code":"751238"}
    regi =clientre.service.userRegister(u)
    # sqls='select * from user_db.t_user_info where Fuser_id="karry"'
    # name =mysql.fetchone(sqls)
    #print(name)
    print(regi)

