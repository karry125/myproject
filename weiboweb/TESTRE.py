# -*- coding:utf-8 -*-
# @Time:2019/6/12
# @Author:wangym
# @Email:123@qq.com
# @File:TESTRE
import re


html='<img width="95" height="34" action-type="btn_change_verifycode" node-type="verifycode_image" src="https://login.sina.com.cn/cgi/pin.php?r=67986969&amp;s=0&amp;p=gz-74145a9175e93140b1884cc2d532cd4099aa">'
pattern= 'node-type="verifycode_image"(.+?)>'
r=re.search(pattern,html)
print(r.group(1))