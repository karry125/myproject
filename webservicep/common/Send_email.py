# -*- coding:utf-8 -*-
# @Time:2019/4/25
# @Author:wangym
# @Email:123@qq.com
# @File:Send_email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from  email.mime.image import MIMEImage
from email.header import Header
from common.readconf import conf

class sendEmail:
    def __init__(self):
        self.sender = conf.getstr("email", "sender")
        password = conf.getstr("email", "password")
        self.receiver = eval(conf.getstr("email", "receiver"))
        self.server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        self.server.login(self.sender, password)

    def mail_msg(self,msg,type="html"):
        msg = MIMEText(msg,type,"utf-8")
        return msg

    def sender_mails(self,msg,files=None,type='plain',subject=""):
        total = MIMEMultipart()
        total["Subject"] = Header(subject, "utf-8")
        total['From'] = "敏敏"  # 发件人昵称
        total['To'] = ";".join(self.receiver)
        body = self.mail_msg(msg,type=type)
        total.attach(body)
        # 这个 files 是一个不为空的列表
        # 判断这个 files 首先不能为空， 不为空的列表
        if files :
            #for filename in files:
                file = MIMEApplication(open(files, 'rb').read())
                file.add_header("Content-Type","application/octet-stream")
                file.add_header('Content-Disposition', 'attachment', filename="result.html")
                # 附件摸快添加到总的里面
                total.attach(file)
        self.server.sendmail(self.sender,self.receiver,total.as_string())
        self.server.quit()


if __name__ == '__main__':
    send= sendEmail()
    msg =open("F:\MyProject\qianchengdai\\report\\2019-04-25-20_01_50.html","rb").read()
    send.sender_mails(msg,type="html",files="F:\MyProject\qianchengdai\\report\\2019-04-25-20_01_50.html",subject="测试报告")

