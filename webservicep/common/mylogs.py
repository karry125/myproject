# -*- coding:utf-8 -*-
# @Time:2019/4/22
# @Author:wangym
# @Email:123@qq.com
# @File:mylogs

import logging
from common.getfile import logsfile


class Mylogs:

    def __init__(self):
        self.logger = logging.Logger("future")
        self.logger.setLevel("DEBUG")
        self.str = logging.StreamHandler()
        self.str.setLevel("DEBUG")
        form = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        self.str.setFormatter(form)
        self.logger.addHandler(self.str)
        self.file = logging.FileHandler(logsfile,encoding="utf-8")
        self.file.setLevel("DEBUG")
        self.file.setFormatter(form)
        self.logger.addHandler(self.file)

    def debug(self,msg):
        """收集日志"""
        self.logger.debug(msg)

    def info(self, msg):
        """收集日志"""
        self.logger.info(msg)

    def warning(self, msg):
        """收集日志"""
        self.logger.warning(msg)

    def error(self, msg):
        """收集日志"""
        self.logger.error(msg)

    def remove(self):
        self.logger.removeHandler(self.str)

def mylogger(name):
    logger = logging.Logger(name)
    logger.setLevel("DEBUG")
    str = logging.StreamHandler()
    str.setLevel("DEBUG")
    form = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    str.setFormatter(form)
    logger.addHandler(str)
    file = logging.FileHandler(logsfile, encoding="utf-8")
    file.setLevel("DEBUG")
    file.setFormatter(form)
    logger.addHandler(file)
    return  logger

mylogs = Mylogs()

if __name__ == '__main__':
    m = Mylogs()
    m.debug("kk")