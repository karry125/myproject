# -*- coding:utf-8 -*-
# @Time:2019/3/23
# @Author:wangym
# @Email:123@qq.com
# @File:testexcle


from openpyxl import load_workbook,workbook,worksheet

work = load_workbook("kk.xlsx")
sheet = work["开心"]



class Model:
    def __init__(self,name):
        self.name=name
    def save(self,force_update=False,force_insert=False):
        if force_update and force_insert:
            print('cannt perform both operations') #故意写作cannt而非cannot
        if force_update:
            print('updated an existing record')
        if force_insert:
            print('created a new record')

class Child(Model):
    def save(self,*args,**kwargs):
        if self.name=='abcd':
            super().save(*args,**kwargs)
            print(**kwargs)
            #super(Model,self).save(*args,**kwargs)
        else:
            return None
child=Child('abcd')
child.save(force_update=True)
child.save(force_insert=True)
child.save(force_insert=True,force_update=True)
# updated an existing record
# created a new record
# ValueError: cannt perform both operations
