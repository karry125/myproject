# -*- coding:utf-8 -*-
# @Time:2019/5/3
# @Author:wangym
# @Email:123@qq.com
# @File:test_bindBankCard


from ddt import data ,ddt
from common.DoExcle import DoExcle
import unittest
from common.getfile import casefile
from common.websRequest import WebsRequset
from common.DoMysql import DoMysql
from suds.client import Client
from suds import sudsobject
from common.mylogs import mylogger
from common.contexts import contextss,Context,getuid,getcre_id

mylog =mylogger(__name__)

@ddt
class testbindBankCard(unittest.TestCase):
    doexcle=DoExcle(casefile,"bind")
    cases=doexcle.getcases()

    @classmethod
    def setUpClass(cls):
        cls.client=WebsRequset()
        cls.mysql=DoMysql()

    @data(*cases)
    def test_bindBankCards(self,case):
        mylog.info("测试用例方法{},正在执行第{}条用例".format(self._testMethodName, case.id))
        if case.params.find("${phone}")!=-1:
            sql = 'select max(Fmobile_no) from sms_db_12.t_mvcode_info_9 where Fmobile_no like "137%912"'
            # 返回是字典
            phone = DoMysql().fetchone(sql)["max(Fmobile_no)"]
            maxphone = int(phone) + 1000
            case.params = case.params.replace("${phone}", str(maxphone))
            setattr(Context, "num", str(maxphone))
            mylog.debug("设置的注册手机号码:{}".format(maxphone))

        if case.params.find("${name}") != -1:
            name = getuid()
            case.params = case.params.replace("${name}", name)
            setattr(Context, "name", name)

        if case.params.find("${user_cre}"):
            user_cre = getcre_id()
            case.params = case.params.replace("${user_cre}", str(user_cre))
            setattr(Context, "user_cre", str(user_cre))

        case.params = contextss(case.params)
        mylog.debug("url地址:{}".format(case.url))
        mylog.debug("请求参数:{}".format(case.params))
        re = self.client.sendrequest(case.url, case.api, case.params)
        res = sudsobject.asdict(re)
        try:
            self.assertEqual(str(res), case.exceptend)
            mylog.debug("返回结果:{}".format(res))
            if case.sql is not None:
                sql = eval(contextss(case.sql))
                if sql.__contains__("phonecode"):
                    print(sql["phonecode"])
                    code = self.mysql.fetchone(sql["phonecode"])
                    print("某某", code["Fverify_code"])
                    setattr(Context, "code", str(code["Fverify_code"]))  #
                    mylog.debug("验证码:{}".format(code["Fverify_code"]))
                elif sql.__contains__("reg"):
                    # sqls = 'select count(*) from user_db.t_user_info where Fuser_id="karry"'
                    uid = self.mysql.fetchone(sql["reg"])["Fuid"]
                    print(uid)
                    setattr(Context, "uid", str(uid))
                    mylog.debug("注册成功后uid:{}".format(uid))
                # sql='select count(*) from sms_db_21.t_mvcode_info_9 where Fmobile_no=%s'.format(maxphone)
                # 认证查询
                else:
                    count = self.mysql.fetchone(sql["auto"])["count(*)"]
                    self.assertEqual(count, 1)
                    mylog.debug("数据库添加一条记录成功")
            self.doexcle.writerow(case.id + 1, str(res), "Pass")
        except Exception as e:
            self.doexcle.writerow(case.id + 1, str(res), "Fail")
            mylog.error("错误信息:{}".format(e))
            raise e

    @classmethod
    def tearDownClass(cls):
        mylog.info("测试用例执行完成")
        cls.mysql.close()