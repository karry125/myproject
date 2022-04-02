# -*- coding:utf-8 -*-
# @Time:2019/5/25
# @Author:wangym
# @Email:123@qq.com
# @File:ketangpai

from selenium import webdriver


driver = webdriver.Chrome()

# 课程页面
#同学：
driver.find_element_by_xpath('//li[@class="li5"]/a')#
#课堂详情：
driver.find_element_by_xpath('# //li[@class="li6"]/a')
#左上角切换：
driver.find_element_by_xpath('# //ul[@class="nav-menu-left"]/li/a[@class="side-button"]/span')
# 右上角消息：
driver.find_element_by_xpath('//a[@id="notice"]/img')
#个人中心：
driver.find_element_by_xpath('//a[@id="user"]/img')
# 个人设置：
driver.find_element_by_xpath('//a[text()="个人设置"]')
driver.find_element_by_class_name("setting") # 匹配单个class


#作业列表
#作业菜单：
driver.find_element_by_xpath('//a[text()="作业"]')
#元素定位作业链接：
driver.find_element_by_xpath('//a[contains(text(),"元素定位")]')

# 作业详情页返回 :
driver.find_element_by_tag_name("i")
#提交作业：
driver.find_element_by_xpath('//div[@id="third-nav"]/a[text()="提交作业"]')
#上传作业：
driver.find_element_by_class_name("webuploader-pick")
driver.find_element_by_xpath('//a[text()="上传文件"]')
#提交：
driver.find_element_by_xpath('# //a[text()="提交"]')
#留言输入框；
driver.find_element_by_id("comment")
#保存按钮：
driver.find_element_by_xpath('//div[@class="work-message2 clearfix"] ')# class多个可以全部匹配



#作业讨论：
driver.find_element_by_xpath('//div[@id="third-nav"]/a[text()="作业讨论"]')
#添加评论：
driver.find_element_by_xpath('//p[text()="添加评论"]')
#输入评论：
driver.find_element_by_xpath('//textarea[@class="comment-txt"]')
#确定：
driver.find_element_by_xpath('//a[text()="确定]')
#取消：
driver.find_element_by_xpath('//a[text()="取消]')
#评论附件：
driver.find_element_by_xpath('//input[@name="file"]/following-sibling::label')

#右下角top :
driver.find_element_by_class_name("back-to-top")
#帮助
driver.find_element_by_class_name("help-icon-ques")
#反馈问题：
driver.find_element_by_xpath('//a[text()="作反馈问题]')


#登录页面

#账号：
# driver.find_element_by_name(""account)
#密码：
driver.find_element_by_xpath('//input[@type="password"]')
#登录 ：
driver.find_element_by_xpath('/a[@class="btn-btn"]')
driver.find_element_by_xpath('//div[@class="padding-cont pt-login"]/a[@class="btn-btn"]')
#忘记密码：
driver.find_element_by_xpath('//a[contains(@class,"forget)]')

#话题页
driver.find_element_by_xpath('//div[@id="third-nav"]/a[text()="话题"]')
#点击发起
driver.find_element_by_xpath('//div[@class="send-an"]')
#发起话题
driver.find_element_by_xpath('//div[@class="send-an"]/a')
#内容
driver.find_element_by_xpath('//div[@class="wangEditor-txt"]')
#取消
driver.find_element_by_xpath('//div[@class="opt-btn fr"]/a[text()="取消"]')
#确定
driver.find_element_by_xpath('//div[@class="opt-btn fr"]/a[text()="取消"]')
#全部列表
driver.find_element_by_xpath('//div[@class="all active"]')
#精华
driver.find_element_by_xpath('//div[@class="essence"]')
#标题
driver.find_element_by_xpath('//div[@class="title clearfix"]')

#资料
driver.find_element_by_xpath('//div[@id="third-nav"]/a[text()="资料"]')
#附件
driver.find_element_by_xpath('//li[contains(@class,"attachment")]')
#外链
driver.find_element_by_xpath('//li[contains(@class,"outlink")]')
#文件
driver.find_element_by_xpath('//ul[@class="clearfix"]/li[0]')

