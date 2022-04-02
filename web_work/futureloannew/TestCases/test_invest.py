# -*- coding:utf-8 -*-
# @Time:2019/6/14
# @Author:wangym
# @Email:123@qq.com
# @File:test_invest

import  unittest
from futureloan.PageObjects.index_page import IndexPage
from futureloan.PageObjects.login_page import LoginPage
from futureloan.TestDatas.common_data import base_url
from futureloan.TestDatas import login_data as ld
from futureloan.PageObjects.bid_page import BidPage
from selenium import webdriver
from futureloan.TestDatas.invest_data import fail_data as fd
from futureloan.TestDatas.invest_data import wrong_data as wd
from futureloan.TestDatas.invest_data import success_data as sd
from ddt import ddt,data
from futureloan.PageObjects.user_page import UserPage
import datetime
import time


@ddt
class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("{}/Index/login.html".format(base_url))
        cls.driver.maximize_window()
        LoginPage(cls.driver).login(ld.success_data["user"],ld.success_data["passwd"])

    def test_invest_0_click_bid(self):
        # 首页选择第一个标
        index_page = IndexPage(self.driver)
        index_page.check_nick_name_exists()
        index_page.click_invest_button()

    #  投资金额为负数 空格 不是100倍数 ，弹窗提示
    @data(*fd)
    def tes2t_invest_1_fail_by_fail_datas(self,data):
        # 进入投标页面，
        bidpage = BidPage(self.driver)
        # 获取标剩余可投金额
        bid_money = bidpage.get_bid_money()
        # 获取输入框种的可用余额
        user_left_money = bidpage.get_user_left_money()
        print(bid_money,user_left_money)
        # 输入投资金额
        time.sleep(1)
        max=bidpage.replace(data["money"])
        print("最大",max)
        bidpage.invest(str(max))
        time.sleep(2)
        # 断言 提示音
        self.assertEqual(data["check"],bidpage.get_alert_error_msg())
        bidpage.close_alert()
        after_bid_money = (bidpage.get_bid_money())
        after_user_money = (bidpage.get_user_left_money())
        self.assertEqual(after_bid_money, bid_money )
        self.assertEqual(after_user_money, user_left_money )


    # 投资金额 非10倍数 含小数点 中英文，按钮提示
    @data(*wd)
    def tes2t_invest_2_fail_by_wrong_datas(self, data):
        bidpage = BidPage(self.driver)
        bid_money = bidpage.get_bid_money()
        user_left_money = bidpage.get_user_left_money()
        print(bid_money, user_left_money)
        bidpage.invest(data["money"])
        self.assertEqual(data["check"], bidpage.get_alert_error_msg())
        after_bid_money = (bidpage.get_bid_money())
        after_user_money = (bidpage.get_user_left_money())
        self.assertEqual(after_bid_money, bid_money)
        self.assertEqual(after_user_money, user_left_money)

    def test_invest_3_success(self):
        # 2000 步骤
        # 首页 - 选标投资
        # 获取 个人余额、获取 当前标的可投金额
        # 标页面 - 获取用户余额、获取标的可投金额
        # 标页面 - 投资操作 2000
        # 标页面 - 弹出框
        # 断言
        # 投资金额  = 投资前的钱 - 投资后的钱
        # 个人页面 - 获取投资后的用户可用余额
        # 标页面 - 获取投资后的标可投金额
        bidpage = BidPage(self.driver)
        # 获取当前标的可投剩余金额
        bid_money = (bidpage.get_bid_money())
        # 获取用户的余额
        user_left_money = (bidpage.get_user_left_money())
        print(bid_money, user_left_money)
        bidpage.invest(sd["money"])
        time.sleep(5)
        self.assertEqual(sd["check"], bidpage.get_invest_success_msg())
        bidpage.close_success_alert()
        time.sleep(5)
        self.driver.refresh()
        after_bid_money = (bidpage.get_bid_money())
        after_user_money=( bidpage.get_user_left_money())
        print(after_user_money,after_bid_money)
        self.assertEqual(float(sd["money"]),bid_money-after_bid_money)
        self.assertEqual(float(sd["money"]),user_left_money-after_user_money)
        # 进入个人页面
        bidpage.click_user_url()
        userpage = UserPage(self.driver)
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        userpage.click_invest_tab()
        time.sleep(2)
        new_time = userpage.get_first_num_time()
        now_time=datetime.datetime.now().strftime('%Y-%m-%d%H:%M')
        print(new_time,now_time)
        self.assertLessEqual(new_time,now_time)


    def tearDown(self):
        self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)