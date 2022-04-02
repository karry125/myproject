# -*- coding:utf-8 -*-
# @Time:2019/4/28
# @Author:wangym
# @Email:123@qq.com
# @File:test_sendcode

from ddt import data ,ddt
from common.DoExcle import DoExcle
import unittest
from common.getfile import casefile
from common.websRequest import WebsRequset
from common.DoMysql import DoMysql
from suds.client import Client
from suds import sudsobject,WebFault
from common.contexts import Context,contextss
from common.mylogs import mylogger

mylog = mylogger(__name__)


@ddt
class testcode(unittest.TestCase):
    doexcle=DoExcle(casefile,"webcode")
    cases=doexcle.getcases()

    @classmethod
    def setUpClass(cls):
        mylog.info("开始执行测试用例")
        cls.client=WebsRequset()
        cls.mysql=DoMysql()

    @data(*cases)
    def test_codes(self,case):
        mylog.info("测试用例方法{},正在执行第{}条用例".format(self._testMethodName,case.id))
        if case.params.find("${phone}"):
            sql = 'select max(Fmobile_no) from sms_db_21.t_mvcode_info_9 where Fmobile_no like "137%921"'
            # 返回是字典
            phone = DoMysql().fetchone(sql)["max(Fmobile_no)"]
            maxphone = int(phone) + 1000
            case.params=case.params.replace("${phone}",str(maxphone))
            setattr(Context, "num", str(maxphone))
            mylog.debug("设置的注册手机号码:{}".format(maxphone))
        re = self.client.sendrequest(case.url, case.api, case.params)
        try:
            #re = sudsobject.asdict(re)
            self.assertEqual(case.exceptend,str(re)) #case.exceptend
            mylog.debug("返回结果:{}".format(re))
            if case.sql is not None:
            #sql='select count(*) from sms_db_21.t_mvcode_info_9 where Fmobile_no={}'.format(maxphone)
                case.sql=contextss(case.sql)
                case.sql =eval(case.sql)
                count=self.mysql.fetchone(case.sql["sql"])["count(*)"]
                self.assertEqual(count,1)
                mylog.debug("查询验证码一条")
            self.doexcle.writerow(case.id + 1, str(re), "Pass")
        except AttributeError as e:
            mylog.error("断言错误信息:{}".format(e))
            self.doexcle.writerow(case.id + 1, str(e), "Fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        mylog.info("测试用例执行完成")
        cls.mysql.close()