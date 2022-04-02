# -*- coding:utf-8 -*-
# @Time:2019/3/16
# @Author:wangym
# @Email:123@qq.com
# @File:conf_class


from configparser import  ConfigParser,RawConfigParser

class cf_help:
    def __init__(self,filename, encoding="utf-8"):
        self.cf = RawConfigParser() #%（filename）ConfigParser会报错
        self.cf.read(filename, encoding=encoding)

    def get_sections(self):
        """返回一个list"""
        return self.cf.sections()

    def get_options(self,section):
        """返回一个list"""
        return self.cf.options(section)

    def get_str(self,section,option):
        """返回的都是字符串，list 元祖 字典可以加eval（）获取原本类型"""
        return self.cf.get(section,option)

    def get_int(self, section, option):
        return self.cf.getint(section,option)

    def get_float(self, section, option):
        return self.cf.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.cf.getboolean(section, option)
if __name__ == '__main__':

    cf = cf_help("all.conf",encoding="utf-8")
    name = cf.get_str("excle","excle_list")
    print(eval(name))
    print(cf.get_sections())