#！ /usr/bin/python3

import  xlsxwriter
import  xlrd
import requests
import json

def test():
 filename = 'F:\\MyProject\\test\\test.xls'
 book = xlrd.open_workbook(filename=filename)
 url = (book.sheet_by_index(0).cell(1,0)).value  #获取表格里的内容，
 requ = book.sheet_by_index(0).cell(1,1).value
 print(url,requ)
 r =  requests.get(url,params=requ)
 print('Search Response:\n', json.dumps(r.json(), ensure_ascii=False, indent=4))

test()

