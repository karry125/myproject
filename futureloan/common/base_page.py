# -*- coding:utf-8 -*-
# @Time:2019/6/23
# @Author:wangym
# @Email:123@qq.com
# @File:base_page
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from PageLocaters.bid_locator import BidLocator as loc
from common import mylog
from common.file_path import screenshot_dir
import datetime
logger = mylog.mylogger(__name__)
class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def wait_ele_visible(self,loc,img_doc="",timeout=30,fe=0.5):
        logger.info("等待元素可见{}".format(loc))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,fe).until(EC.visibility_of_element_located(loc))
            end = datetime.datetime.now()
            logger.info("开始时间点{}，结束时间点{}，等待时长{}".format(start,end,end-start))
        except Exception as e:
            logger.error("等待元素可见失败")
            self.save_web_screenshot(img_doc)
            raise


    def get_element(self,loc,img_doc=""):
        """

        :param loc: 以元祖形式传参（）
        :param img_doc:
        :return:
        """
        logger.info("查找{}种的元素{}".format(img_doc,loc))
        time.sleep(2)
        try:
            ele = self.driver.find_element(*loc) # 解包两个值
            return ele

        except Exception as e:
            # 日志
            logger.exception("查找元素失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise
    def click_element(self,loc,img_doc="",timeout=30,fre=0.5):
        """
        使用前面两个方法 等待 找元素
        :param loc:
        :param img_doc:
        :param timeout:
        :param fre:
        :return:
        """
        self.wait_ele_visible(loc,img_doc,timeout,fre)
        ele = self.get_element(loc,img_doc)
        time.sleep(2)
        print(ele)
        logger.info("点击元素{}".format(loc))
        try:
            print("click")
            self.driver.execute_script("arguments[0].click();",ele)
            #ele.click()
            time.sleep(2)
        except Exception as e:
            logger.error("点击元素失败")
            self.save_web_screenshot(img_doc)
            raise
    def input_text(self,loc,args,img_doc=""):
        self.wait_ele_visible(loc, img_doc)
        ele = self.get_element(loc, img_doc)
        logger.info("元素{}输入文本内容".format(loc,args))
        try:
            ele.send_keys(args)
        except Exception as e:
            # 日志
            logger.exception("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise
    def get_element_attribute(self,loc,attr_name,img_doc):
        ele = self.get_element(loc,img_doc)
        try:
            attr_value = ele.get_attribute(attr_name)
            logger.info("获取元素{}属性{}值为：{}".format(loc,attr_name,attr_value))
            return  attr_value
        except Exception as e:
            # 日志
            logger.exception("元素输入操作失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise

    def get_element_text(self,loc,img_doc=""):
        ele = self.get_element(loc,img_doc)
        try:
            text = ele.text
            logger.info("获取元素{}文本值为：{}".format(loc,text))
            return  text
        except Exception as e:
            # 日志
            logger.exception("获取元素文本值失败")
            # 截图
            self.save_web_screenshot(img_doc)
            raise
    # 实现网页截图操作
    def save_web_screenshot(self,img_doc):
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = "{}_{}.png".format(img_doc,now)
        try:
            self.driver.save_screenshot(screenshot_dir +"/" + filepath)
            logger.info("网页截图成功。图片存储在：{}".format(screenshot_dir +"/" + filepath))
        except:
            logger.exception("网页截屏失败！")
    # window切换
    def switch_windows(self,loc,img_doc="",timeout=10):
        # # 方式二
        # # step1: 获取窗口数
        handles = self.driver.window_handles  # 只有1个窗口。
        # # step2: 执行打开新窗口的操作 -
        self.click_element(*loc)  # 本操作带来了新窗口的出现 -》 2
        # # step3: 确认新的窗口出现了，我再去操作它。等待新窗口出现。
        # # EC.new_window_is_opened  # 比窗口总数的大小。# 传一个窗口总数。
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened(handles))  # 2 > 1 # 确认新窗口出现
        # step4: 再次获取 窗口的handles
        handles = self.driver.window_handles  # 2个窗口
        # step5: 切换 到新窗口
        try:
            self.driver.switch_to.window(handles[-1])
            logger.info("切换新窗口成功")
        except Exception as e:
            logger.info("切换新窗口失败")
            self.save_web_screenshot(img_doc)

    # ifram切换
    def switch_iframe(self,iframe_name,img_doc):
         self.wait_ele_visible(iframe_name)
         try:
             self.driver.switch_to.frame(iframe_name)
             logger.info("切换iframe为{}成功".format(iframe_name))
         except Exception as e:
             logger.error("切换iframe失败")
             self.save_web_screenshot(img_doc)
    # alert 弹窗
    # select 获取列表值
    # 上传操作