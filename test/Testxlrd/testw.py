import xlrd,xlwt




sheen = xlrd.open_workbook(r'E:/q.xlsx','w+b')
table = sheen.sheet_by_index(0)
trow = table.nrows
tcol = table.ncols
for  i in range(1,trow):
    for j in range(0,tcol):
        print(table.cell(i,j).value)
print(table.row_values(1)[1])
result = [("王某", "1375000571",), ("王某某", "13750005271")]
print(len(result))
print(trow)