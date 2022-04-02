# -*- coding:utf-8 -*-
# @Time:2019/3/20
# @Author:wangym
# @Email:123@qq.com
# @File:testconf

import logging
import logging.config

logging.config.fileConfig("logger.conf")
logger = logging.getLogger("example02")
