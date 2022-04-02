# -*- coding:utf-8 -*-
# @Time:2019/4/28
# @Author:wangym
# @Email:123@qq.com
# @File:test_webregist

from ddt import data ,ddt
from common.DoExcle import DoExcle
import unittest
from common.getfile import casefile
from common.websRequest import WebsRequset
from common.DoMysql import DoMysql
from suds.client import Client
from suds import sudsobject
from common.contexts import Context,contextss,getuid
from common.mylogs import mylogger

mylog = mylogger(__name__)


@ddt
class testcode(unittest.TestCase):
    doexcle=DoExcle(casefile,"webregist")
    cases=doexcle.getcases()

    @classmethod
    def setUpClass(cls):
        mylog.info("开始执行测试用例")
        cls.client=WebsRequset()
        cls.mysql=DoMysql()

    @data(*cases)
    def test_codes(self,case):
        mylog.info("测试用例方法{},正在执行第{}条用例".format(self._testMethodName,case.id))
        if case.params.find("regist_phone") != -1:
            sql = 'select max(Fmobile_no) from sms_db_12.t_mvcode_info_9 where Fmobile_no like "137%912"'
            # 返回是字典
            phones = self.mysql.fetchone(sql)["max(Fmobile_no)"]
            maxphone = int(phones) + 1000
            print(maxphone)
            case.params=case.params.replace("regist_phone",str(maxphone))
            setattr(Context, "num", str(maxphone))
            mylog.debug("设置的注册手机号码:{}".format(maxphone))
        if case.params.find("${name}")!=-1:
            name=getuid()
            setattr(Context,"regist_name",name)
            case.params = case.params.replace('${name}', str(name))

        if case.params.find('chaoshi_code') > -1 and case.sql is not None:
            sql = eval(case.sql)['sql1']
            chaoshi_code = self.mysql.fetchone(sql)['Fverify_code']
            case.params = case.params.replace('chaoshi_code', str(chaoshi_code))
        if case.params.find('chaoshi_phone') > -1:
            sql = eval(case.sql)['sql1']
            chaoshi_phone = self.mysql.fetchone(sql)['Fmobile_no']
            case.params = case.params.replace('chaoshi_phone', str(chaoshi_phone))
        # 替换参数值
        case.params=contextss(case.params)
        re = self.client.sendrequest(case.url,case.api,case.params)
        # 可以用re.retCode,re.retInfo 取值

        try:
            res = sudsobject.asdict(re)
            self.assertEqual(case.exceptend,str(res))
            mylog.debug("返回结果:{}".format(res))
            if case.sql is not None :
                sqll=eval(contextss(case.sql))
                # 查询验证码
                if sqll.__contains__("phonecode"):
                    code=self.mysql.fetchone(sqll["phonecode"])
                    setattr(Context,"code",str(code["Fverify_code"]))
                    mylog.debug("查询的验证码:{}".format(code["Fverify_code"]))
                # 查询注册插入数据
                if sqll.__contains__("reg") and getattr(Context,"code") is not None:
                    count =self.mysql.fetchone(sqll["reg"])["count(*)"]
                    self.assertEqual(count,1)
                    mylog.debug("注册成功一条")
            self.doexcle.writerow(case.id + 1, str(res), "Pass")
        except Exception as e:
            self.doexcle.writerow(case.id + 1, str(res), "Fail")
            mylog.error("错误信息:{}".format(e))
            raise  e

    @classmethod
    def tearDownClass(cls):
        mylog.info("测试用例执行完成")
        cls.mysql.close()