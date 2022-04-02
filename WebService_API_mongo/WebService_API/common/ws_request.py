# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import suds
from suds.client import Client

from WebService_API.common import config
from WebService_API.common import logger

logger = logger.get_logger(__name__)


class WSRequest:

    def request(self, url, method, data):
        # 拼接URL
        self.url = config.config.get('api', 'pre_url') + url
        self.method = method
        self.data = eval(data)
        logger.info('请求URL：{0}'.format(self.url))
        logger.info('请求METHOD：{0}'.format(self.method))
        logger.info('请求DATA：{0}'.format(self.data))
        client = Client(self.url)

        try:
            resp = eval("client.service.{0}({1})".format(self.method, self.data))
            msg = resp.retInfo
        except suds.WebFault as e:
            msg = e.fault.faultstring
            print(e.document)

        logger.info("返回信息:{0}".format(msg))
        return msg


if __name__ == '__main__':
    from WebService_API.common import do_excel, contants
    from WebService_API.common import context
    from WebService_API.common.do_mysql import DoMysql

    mysql = DoMysql()

    excel = do_excel.DoExcel(contants.case_file, 'sendMCode')
    cases = excel.get_cases()
    for case in cases:
        if case.sql is not None and 'before' in eval(case.sql):
            sql = eval(case.sql)['before']
            mysql.fetch_one(sql)

        data = context.replace(case.data)

        resp = WSRequest().request(case.url, case.method, data)

        if case.sql is not None and 'after' in eval(context.replace(case.sql)):

            sql = eval(context.replace(case.sql))['after']
            print(sql)
            code = mysql.fetch_one(sql)
