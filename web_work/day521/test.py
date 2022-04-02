# -*- coding: utf-8 -*-
# @Time:2019/5/21
# @Author:wangym
# @Email:123@qq.com
# @File:test

di ={"mobilephone": "18688773467", "pwd": "123456"}
print("{mobilephone}{pwd}".format(**di))
print(**di)

"""
课程页面
同学：//li[@class="li5"]/a
课堂详情：//li[@class="li6"]/a
左上角切换：//ul[@class="nav-menu-left"]/li/a[@class="side-button"]/span
右上角消息：//a[@id="notice"]/img
个人中心：//a[@id="user"]/img
个人设置：//a[text()="个人设置"]  driver.find_element_by_class_name("setting")


作业tab页
作业：//a[text()="作业"]
元素定位作业链接：//a[contains(text(),"元素定位")]

返回 :driver.find_element_by_tag_name("i")
提交作业：//div[@id="third-nav"]/a[text()="提交作业"]
上传作业：driver.find_element_by_class_name("webuploader-pick")
//a[text()="上次文件"]
提交： //a[text()="提交"]
留言输入框；driver.find_element_by_id（"comment"）
保存按钮：//div[@class="work-message2 clearfix"] 用find定位含空格报错，单个 或者加.
//*[@id="viewer-handup"]/div[2]/div[3]

作业讨论：//div[@id="third-nav"]/a[text()="作业讨论"]
添加评论：//p[text()="添加评论"]
输入评论：//textarea[@class="comment-txt"]
确定：//a[text()="确定]
取消：//a[text()="取消]
附件：//input[@name="file"]/following-sibling::label

top :driver.find_element_by_class_name("back-to-top")
帮助  driver.find_element_by_class_name("help-icon-ques")
反馈问题：//a[text()="作反馈问题]

===============================================
登录页面

账号：driver.find_element_by_name(""account)
密码：//input[@type="password"]
登录 ：/a[@class="btn-btn"]  //div[@class="padding-cont pt-login"]/a[@class="btn-btn"]
忘记密码：//a[contains(@class,"forget)]

"""
