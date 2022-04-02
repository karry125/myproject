import xlrd,xlwt

try:
    sheen = xlrd.open_workbook(r'E:/q.xlsx','w+b')
    table = sheen.sheet_by_index(0)
    trow = table.nrows
    tcol = table.ncols
    for  i in range(1,len(trow)+1):
        for j in range(0,len(tcol)):
            print(table.cell(i,j,u"%s"%table.cell(i,j).value))
    print(table.row_values(1)[1])
except:
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(u"第一个")
    fname = [u"姓名", u"手机号"]
    for f in range(0, len(fname)):
        sheet.write(0, f, fname[f])

    result = [("王某", "1375000571",), ("王某某", "13750005271")]

    for row in range(1, len(result) + 1):
        for col in range(0, len(fname)):
            sheet.write(row, col, "%s" % result[row - 1][col])
    workbook.save("E:/q.xlsx")


