import MySQLdb



tpl = '''<html>
<head><title>{title}</title></head>
<body>
<h1>{title}</h1>
<table border=1px>
    <tr>
        <th>序号</th>
        <th>用例</th>
        <th>结果</th>
    </tr>
    {trs}
</table>
</body>
</html>
'''

tr = '''<tr><td>{sn}</td>
<td>{case_name}</td>
<td>{result}</td>
'''

title = "自动化测试报告"
case_results = [("1", "test_add_normal", "PASS"), ("2", "test_add_negative", "PASS"), ("3", "test_add_float", "FAIL")]

trs = ''
for case_result in case_results:
    tr_format = tr.format(sn=case_result[0], case_name=case_result[1], result=case_result[2])
    trs += tr_format

html = tpl.format(title=title, trs=trs)

f = open("report.html", "w")
f.write(html)
f.close()

