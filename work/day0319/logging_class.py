# -*- coding:utf-8 -*-
# @Time:2019/3/19
# @Author:wangym
# @Email:123@qq.com
# @File:logging_class

import  logging
from day0316.conf_class import cf_help as conf

class loggers:

    def __init__(self):
        #第一步创建收集器
        self.conf = conf("F:\MyProject\work\day0319\logger.conf")
        self.logger = logging.getLogger(self.conf.get_str("logger","logger_name"))
        self.logger.setLevel(self.conf.get_str("logger","logger_level"))
        # 设置输出格式
        self.forma = logging.Formatter(self.conf.get_str("logger","logger_formate"),
                                       datefmt=self.conf.get_str("logger","logger_datefmt"))
        #判断输出器
        if self.conf.get_str("logger","handles") == "StreamHandler":
           self._StreamHandlerlog()
        elif self.conf.get_str("logger","handles") =="FileHandler":
            self._FileHandlerlog()

    def _StreamHandlerlog(self):
        """创建控制台输出器"""
        self.sh = logging.StreamHandler()
        self.sh.setLevel(self.conf.get_str("StreamHandler", "strhandlelevel"))
        self.sh.setFormatter(self.forma)
        self.logger.addHandler(self.sh)

    def _FileHandlerlog(self):
        """创建文件输出器"""
        filepath = self.conf.get_str("FileHandler", "filepath")
        file = logging.FileHandler(filepath, encoding="utf-8")
        # 设置输出日志级别，收集器跟输出器取交集
        file.setLevel("DEBUG")
        # 设置到文件输出器
        file.setFormatter(self.forma)
        # 日志输出器添加到收集器，
        self.logger.addHandler(file)

    # def write_log(self,logoutlevel,msg):
    #
    #     # 写日志
    #     if logoutlevel.upper() =="DEBUG":
    #         self.logger.debug(msg)
    #     elif logoutlevel.upper()=="INFO":
    #         self.logger.info(msg)
    #     elif logoutlevel.upper() == "WARNING":
    #          self.logger.warning(msg)
    #     elif logoutlevel.upper() == "ERROR":
    #         self.logger.error(msg)

    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)


logger = loggers()

if __name__ == '__main__':

        logger = loggers()
        logger.info("wode")
        logger.logger.info("88") #直接调用属性写，不用再用方法
        #为什么当时不想着直接info debug方法呢，直接方便，写成自己的方法也可以同名
        # logger.write_log("DEBUG","this is debug")
        # logger.write_log("info", "this is info")
        # logger.write_log("warning", "this is warning")
        # logger.write_log("error", "this is error")


