#!/usr/bin/python3

import xlsxwriter

filename = 'test.xlsx'
book = xlsxwriter.Workbook(filename)
sheet = book.add_worksheet('what')
sheet.write('A1','hello')   # 在单元格A1写入‘Hello’字符串
cell = book.add_format({'bold':True})  # 定一个加粗的格式对象
sheet.set_row(0,40,cell)  # 第一行单元格高度为40px，且引用加粗格式对象
sheet.set_row(1,None,None,{'bold':True})
book.close()


'''
workbook = xlsxwriter.Workbook('Demo2.xlsx')    # 创建一个名为Dome2.xlsx的表格
worksheet1 = workbook.add_worksheet()           # 添加第一个表单，默认为sheet1
worksheet2 = workbook.add_worksheet('Files')    # 添加一个名为File的表单
worksheet3 = workbook.add_worksheet()           # 添加一个表单，默认为sheet3
workbook.close()
'''

