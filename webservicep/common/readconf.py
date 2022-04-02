# -*- coding:utf-8 -*-
# @Time:2019/4/14
# @Author:wangym
# @Email:123@qq.com
# @File:readconf

from configparser import ConfigParser,RawConfigParser
import os
from common import getfile


class ReadConf:

    def __init__(self):
        self.conf = ConfigParser()
        self.conf.read(getfile.switchfile,encoding="utf-8")
        switch = self.conf.getboolean("switch","on")
        if switch:
            self.conf.read(getfile.onfile,encoding="utf-8")
        else:
            self.conf.read(getfile.testfile,encoding="utf-8")

    def getsections(self):
        return  self.conf.sections()

    def getoptions(self,sections):
        return self.conf.options(sections)

    def getstr(self,section,options):
        # 返回配置项值，字符串类型
        return  self.conf.get(section,options)

    def getint(self,section,options):
        # 返回配置项值，int类型
        return  self.conf.getint(section,options)

    def getfloat(self,section,options):
        # 返回配置项值，浮点类型
        return  self.conf.getfloat(section,options)

    def getboolen(self,section,options):
        #  返回配置项值，布尔值类型
        return  self.conf.getboolean(section,options)

#实例化，其他直接调用
conf = ReadConf()

if __name__ == '__main__':
    base=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    file =os.path.join(base,"conf","base.conf")
    conf = ReadConf()
    #print(conf.getoptions("mysql"))
    print(conf.getstr("api","url"))