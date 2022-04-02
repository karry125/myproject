# -*- coding:utf-8 -*-
# @Time:2019/5/21
# @Author:wangym
# @Email:123@qq.com
# @File:test01


from selenium import webdriver

# python环境变量根目录下找
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
# 1 id定位唯一 如动态id不适合
el=driver.find_element_by_id("kw")
# 有定位属性直接用.
el.text
# 没有定位
el.get_attribute("class")
# 2 name
# 找单个，元素找到有多个，返回找到的第一个
driver.find_element_by_name("")
# 找多个，返回列表,用下标找元素
ele_list=driver.find_elements_by_name("")
#3 class  只能选择一个class值，一个元素中有多个class 用空格隔开，用xpath不用单个？
driver.find_element_by_class_name("")
list=driver.find_elements_by_class_name("")

#4tagname
driver.find_element_by_tag_name()
driver.find_elements_by_tag_name()

# 前面4种元素可以通用

# 5，6 链接元素，在a标签中间的文本，link text 完全匹配 部分匹配
# 不唯一，完全匹配
driver.find_element_by_link_text("")
driver.find_elements_by_link_text("")
# 部分匹配
driver.find_element_by_partial_link_text()


# 7 8 xpath css 每级直接写标签名，属性或者个数写在[],
# //相对  参照物html
# /绝对定位 从html开始 层级有多个相同标签，用下标/div[1]/
#//*[@id="s_kw_wrap"]
# f12元素 ctrl f查找元素 吡大赛
#1 //标签名【@属性=属性值】，//*[]  匹配所有属性，单层的
# 2 逻辑运算 多个属性 //标签名【@属性=属性值 and @】或者or
driver.find_element_by_xpath('//*[@id="s_kw_wrap"]')
# 3 元素文本内容 //标签名[text()==""]完全匹配 可以and，单层
# 部分匹配contains(text()/@属性，部分值)
# //标签名[contains（text()，"部分文本内容"）
# //标签名[contains（@属性，"属性值"）]



# 4 层级查找 通过标签自己的特征不唯一，查找上一层特殊
#4.1 找父级//div[@id="u1"]/a[@name="tj_login"] 第二层a标签属性都不同，如果相同可以用a【1】尽可能不用
#//a[@name="tj_login" and @class="lb" and text()="登录"]
# 4.2 找同级轴定位,找到前面的/轴定位名称：标签名【】，用/
# 找同级在后面的弟弟妹妹，following-sibling::
# 用父亲，先找到同级的/父亲/需要找到的
#//a[@class="toindex"]/parent::div/following-sibling::div//a[@name="tj_login"]

