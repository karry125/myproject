# -*- coding:utf-8 -*-
# @Time:2019/3/29
# @Author:wangym
# @Email:123@qq.com
# @File:email_send


import smtplib
from day0316.conf_class import cf_help
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from  email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
#
conf=cf_help("email.conf")
sender =conf.get_str("email","sender")
password =conf.get_str("email","password")
receiver =eval(conf.get_str("email","receiver"))
username =conf.get_str("email","username")
msg = MIMEMultipart('mixed')
msg["Subject"]="周五"
msg['From'] = "敏敏"  #发件人昵称
msg['To'] = ";".join(receiver)
text="你好正文"

msgtext =MIMEText(text,"plain","utf-8")
msg.attach(msgtext)
# 构造图片链接
sendimagefile = open(r'F:\wjk.jpg', 'rb').read()
image = MIMEImage(sendimagefile,"octet-stream")
image.add_header('Content-ID', '<image1>')# 定义图片ID
#image["Content-Disposition"] = 'attachment; filename="testimage.png"'
image.add_header('Content-Disposition', 'attachment', filename='img.jpg')
msg.attach(image)
sendfile = open("day.txt","rb").read()
file =MIMEApplication(sendfile,"base64")
file.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
msg.attach(file)


#邮件服务器
server =smtplib.SMTP_SSL("smtp.qq.com",465)
print(password)
server.login(sender,password)

server.sendmail(sender,receiver,msg.as_string())
server.quit()