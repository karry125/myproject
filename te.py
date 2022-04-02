# -*- encoding=utf8 -*-
__author__ = "asus"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "android://127.0.0.1:5037/CUYDU19710006367?cap_method=JAVACAP&&ori_method=ADBORI&&touch_method=MINITOUCH",
    ])

print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
poco("com.huawei.calculator:id/digit_7").click()
poco("com.huawei.calculator:id/op_mul").swipe([0.0037, 0.0])
poco("com.huawei.calculator:id/op_mul").click()
poco("com.huawei.calculator:id/digit_8").click()
poco("com.huawei.calculator:id/digit_8").click()
poco("com.huawei.calculator:id/eq").click()
poco("com.huawei.calculator:id/eq").click()

