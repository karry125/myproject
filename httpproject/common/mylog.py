# -*- coding:utf-8 -*-
# @Time:2019/3/22
# @Author:wangym
# @Email:123@qq.com
# @File:mylog
from common.confread import confreads
import logging
class mylog:
    def __init__(self):
        self.cf = confreads("../conf/logging.conf")
        #self.cf.get_str()
        #第一步创建收集器logger
        self.logger= logging.getLogger(self.cf.get_str("logger","logger_name"))
        #设置日志级别，与输出器也设置日志级别，取交集
        self.logger.setLevel( self.cf.get_str("logger","logger_level"))
        #日志格式，输出器都需要设置
        self.formate=logging.Formatter(self.cf.get_str("logger","logger_formate"))
        str =  self.cf.get_str("logger","handles")
        if str == "StreamHandler":
            self.shandlelog()
        elif str == "FileHandler":
            self.filehanderlog()
        elif str == "StreamHandler&FileHandler":
            self.shandlelog()
            self.filehanderlog()

    def shandlelog(self):
        s = logging.StreamHandler()
        s.setLevel(self.cf.get_str("logger","logger_level"))
        s.setFormatter(self.formate)
        self.logger.addHandler(s)
    def filehanderlog(self):
         filehander=logging.FileHandler(self.cf.get_str("FileHandler","filepath"))
         filehander.setLevel(self.cf.get_str("FileHandler","filelevel"))
         filehander.setFormatter(self.formate)
         self.logger.addHandler(filehander)

    def debug(self,msg):
        self.logger.debug(msg)
        self.logger.removeHandler()

    def info(self,msg):
        self.logger.info(msg)

    def warning(self,msg):
        self.logger.warning(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

if __name__ == '__main__':
    mylogger = mylog()
    mylogger.info("info")

