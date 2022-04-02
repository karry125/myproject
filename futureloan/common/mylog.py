# -*- coding:utf-8 -*-
# @Time:2019/6/23
# @Author:wangym
# @Email:123@qq.com
# @File:mylog
import logging
from common.file_path import logs_dir
import time
import os

def mylogger(name):
    logger = logging.Logger(name)
    logger.setLevel("DEBUG")
    str = logging.StreamHandler()
    str.setLevel("DEBUG")
    form = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
    str.setFormatter(form)
    logger.addHandler(str)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
    filepath = os.path.join(logs_dir,now + ".txt")
    file = logging.FileHandler(filepath, encoding="utf-8")
    file.setLevel("DEBUG")
    file.setFormatter(form)
    logger.addHandler(file)
    return  logger

if __name__ == '__main__':
    mylogger(__name__).info("test")