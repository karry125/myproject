# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""

import unittest

from ddt import ddt, data

from WebService_API.common import context
from WebService_API.common import do_excel, contants
from WebService_API.common import logger
from WebService_API.common import ws_request
from WebService_API.common.do_mysql import DoMysql

logger = logger.get_logger(__name__)
import warnings



@ddt
class SendMCodeTest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'sendMCode')
    cases = excel.get_cases()

    @classmethod
    def setUpClass(cls):
        logger.info("测试前置，初始化数据库连接~~~")
        cls.mysql = DoMysql()
        warnings.simplefilter("ignore", ResourceWarning)

    @data(*cases)
    def test_send(self, case):
        logger.info("开始执行：{0}".format(case.title))
        # 参数化替换
        data = context.replace(case.data)
        # 发起请求，拿到响应结果
        resp = ws_request.WSRequest().request(case.url, case.method, data)
        # 断言
        try:
            self.assertEqual(case.expected, resp)

            if case.case_id == 1:
                code = context.CheckSQL(self.mysql).query_mvcode(data['mobile'])
                self.assertIsNotNone(code)

            self.excel.write_result(case.case_id + 1, str(resp), 'PASS')

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, str(resp), 'FAIL')
        logger.info("结束执行：{0}".format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info("测试后置关闭连接")
        cls.mysql.close()
