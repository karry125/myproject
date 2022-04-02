# -*- coding:utf-8 -*-
# @Time:2019/3/22
# @Author:wangym
# @Email:123@qq.com
# @File:confread
import  configparser

class confreads:

    def __init__(self,filename):
        self.conf = configparser.RawConfigParser()
        self.conf.read(filename,encoding="utf-8")
    def get_sections(self):
        return self.conf.sections()
    def get_option(self,sections):
        return self.conf.options(sections)
    def get_str(self,sections,options):
        return self.conf.get(sections,options)
    def get_int(self,sections,options):
        return self.conf.getint(sections,options)
    def get_float(self,sections,options):
        return self.conf.getfloat(sections,options)
    def get_boolean(self,sections,options):
        return self.conf.getboolean(sections,options)

if __name__ == '__main__':
        cf = confreads("../conf/all.conf") #\\文件名需要两个
        print(cf.get_sections())