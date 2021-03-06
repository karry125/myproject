

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.application import MIMEApplication

# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.qq.com'
username = '1126191425@qq.com'
password = 'akkiyxgwaqlnifji'
sender = '1126191425@qq.com'
# receiver='XXX@126.com'
# 收件人为多个收件人
receiver = ['2031510010@qq.com']

subject = 'Python email test 你好'
# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
# subject=Header(subject, 'utf-8').encode()

# 构造邮件对象MIMEMultipart对象，含不同部分
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = Header(subject,'utf-8').encode()
msg['From'] =  Header("下雪",'utf-8')  #发件人昵称注：如果包含中文，需要通过Header对象进行编码
msg['To'] = '2031510010@qq.com'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
#msg['To'] = ";".join(receiver)
# msg['Date']='2012-3-16'

# 构造文字内容
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
text_plain = MIMEText(text, 'plain', 'utf-8')
#加到邮件的主要对象
msg.attach(text_plain)

# 构造图片链接
sendimagefile = open(r'F:\wjk.jpg', 'rb').read()#读取文件
image = MIMEImage(sendimagefile,_subtype="octet-stream")#图片格式
image.add_header('Content-ID', '<image1>')# 定义图片ID
#image["Content-Disposition"] = 'attachment; filename="testimage.png"'
image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
msg.attach(image)

# 构造html
# 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
html = """
<html>  
  <head></head>  
  <body>  
    <p>Hi!<br>  
       How are you?<br>  
       Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
       <img src="cid:image1">
    </p> 
  </body>  
</html>  
"""
text_html = MIMEText(html, 'html', 'utf-8')
#text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
msg.attach(text_html)

# 构造附件
sendfile = open(r'f:\test.xlsx', 'rb').read()
text_att = MIMEText(sendfile, 'base64', 'utf-8')
text_att["Content-Type"] = 'application/octet-stream'
# 以下附件可以重命名成aaa.txt
# text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
# 另一种实现方式头信息
text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
# 以下中文测试不ok
# text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
msg.attach(text_att)

f = MIMEApplication(sendfile)#这个也可以附件

# 发送邮件
#smtp = smtplib.SMTP()
#邮件服务器，ssl加密
smtp=smtplib.SMTP_SSL("smtp.qq.com",465)
#smtp.connect('smtp.qq.com')
# 我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
# smtp.set_debuglevel(1)
#登陆
smtp.login(username, password)
#对象要转换成文本 asstring，不混合传，直接单个类型传
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()