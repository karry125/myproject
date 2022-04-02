# -*- coding:utf-8 -*-
# @Time:2019/3/19
# @Author:wangym
# @Email:123@qq.com
# @File:loggingtest

import  logging
#第一步创建收集器
logger = logging.getLogger("wym")  #不带参数默认为root，name值日志对象
logger.setLevel("DEBUG") #设置日志级别，必须大写，logging.DEBUG也可以，从低到高DEBUG INFO WARNING ERROR CRITICLE
#创建日日志输出器到控制台,常用这两种输出
sh = logging.StreamHandler()
#创建一个文件输出器，要传一个文件名称，默认a模式，不存在创建，日志含中文加编码
file = logging.FileHandler("log.txt",encoding="utf-8")
#设置输出日志级别，收集器跟输出器取交集
sh.setLevel("DEBUG")
file.setLevel("DEBUG")
#设置输出格式，使用常用变量
forma = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s",datefmt='%a, %d %b %Y %H:%M:%S')
#设置到文件输出器
file.setFormatter(forma)
#设置到控制台输出器
sh.setFormatter(forma)
#日志输出器添加到收集器，
logger.addHandler(sh)
logger.addHandler(file)
#记录日志 放在最后
logger.debug("this is debug")
logger.info("this is info")
logger.warning("this is warning")
logger.error("this is error")


def FileHandlerlog(self, logoutlevel, msg):
    # 创建一个文件输出器，要传一个文件名称，默认a模式，不存在创建，日志含中文加编码
    # filepath = self.conf.get_str("FileHandler","filepath")
    # file = logging.FileHandler(filepath,encoding="utf-8")
    # #设置输出日志级别，收集器跟输出器取交集
    # file.setLevel("DEBUG")
    # #设置到文件输出器
    # file.setFormatter(self.forma)
    # #日志输出器添加到收集器，
    # self.logger.addHandler(file)
    if logoutlevel == "DEBUG":
        self.logger.debug(msg)
    elif logoutlevel == "info":
        self.logger.info(msg)
    elif logoutlevel == "warning":
        self.logger.warning(msg)
    elif logoutlevel == "error":
        self.logger.error(msg)
# def debug(self,msg):
#     self.logger.debug(msg)
# def info(self,msg):
#     self.logger.info(msg)
