# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send():
    sender = '1126191425@qq.com'
    receivers = '2031510010@qq.com'
    message =  MIMEMultipart('related')
    subject = '终于能发图片了'
    message['Subject'] = subject
    message['From'] = _format_addr(sender)
    message['To'] = receivers
    content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>','html','utf-8')
    message.attach(content)

    file=open(r'F:\wjk.jpg', "rb")
    img_data = file.read()
    file.close()

    img = MIMEImage(img_data)
    img.add_header('Content-ID', 'imageid')
    message.attach(img)

    try:
        server=smtplib.SMTP_SSL("smtp.qq.com",465)
        server.login(sender,"akkiyxgwaqlnifji")
        server.sendmail(sender,receivers,message.as_string())
        server.quit()
        print ("邮件发送成功")
    except smtplib.SMTPException as e:
        print(e)
send()
