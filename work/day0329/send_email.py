# -*- coding:utf-8 -*-
# @Time:2019/3/30
# @Author:wangym
# @Email:123@qq.com
# @File:send_email


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from  email.mime.image import MIMEImage
from email.header import Header
from day0316.conf_class import cf_help


class SendEmail():

    def __init__(self):
        conf = cf_help("email.conf")
        self.sender = conf.get_str("email", "sender")
        password = conf.get_str("email", "password")
        self.receiver = eval(conf.get_str("email", "receiver"))
        self.server =smtplib.SMTP_SSL("smtp.qq.com",465)
        self.server.login(self.sender,password)

    def send_text(self,msg,subject):

        msgs=MIMEText(msg,"plain","utf-8")
        msgs["subject"]=Header(subject,"utf-8")
        self._sendemails(self.sender,self.receiver,msgs.as_string())
    def send_html(self,file,subject):
        fileread = open(file, "rb").read()
        msgfilehtml =MIMEMultipart()
        msgfilehtml["subject"] = Header(subject, "utf-8")
        msgfilehtml['From'] = "敏敏"  # 发件人昵称
        msgfilehtml['To'] = ";".join(self.receiver)
        msgs=MIMEText(fileread,"html","utf-8")
        msgfilehtml.attach(msgs)
        msgfile =MIMEApplication(file,"base64")
        msgfile.add_header("Content-Type","application/octet-stream")
        msgfile.add_header('Content-Disposition', 'attachment', filename='result.html')
        msgfilehtml.attach(msgfile)

        self._sendemails(self.sender,self.receiver,msgfilehtml.as_string())

    def send_file(self,filepath,subject):
        sendfile = open(filepath,"rb").read()
        msgfile = MIMEApplication(sendfile,"base64")
        msgfile["subject"]=subject
        msgfile.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
        self._sendemails(self.sender, self.receiver, msgfile.as_string())

    def send_image(self,file,subject):
        images= open(file, 'rb').read()
        msgimage = MIMEImage(images,"octet-stream")
        msgimage["subject"]=subject
        msgimage.add_header("Content-TD","<id1>")
        msgimage.add_header('Content-Disposition', 'attachment', filename='img.jpg')
        html = """
        <html>  
          <head></head>  
          <body>  
            <p>Hi!<br>  
               How are you?<br>  
               Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
               <img src="cid:id1">
            </p> 
          </body>  
        </html>  
        """
        text_html = MIMEText(html, 'html', 'utf-8')

        self._sendemails(self.sender, self.receiver,text_html.as_string())

    def send_images(self, file, subject):
        """正文加图片"""
        images = open(file, 'rb').read()
        msgg =MIMEMultipart()
        msgg["subject"] = subject
        msgimage = MIMEImage(images, "octet-stream")
        msgimage.add_header("Content-ID", "<image1>")
        msgimage.add_header('Content-Disposition', 'attachment', filename='img.jpg')
        msgg.attach(msgimage)
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
        msgg.attach(text_html)
        self._sendemails(self.sender, self.receiver, msgg.as_string())

    def _sendemails(self,sender,receiver,msg):
        self.server.sendmail(sender, receiver, msg)
        self.server.quit()



if __name__ == '__main__':
    senders=SendEmail()
    #senders.send_text("周五爬山","今天活动")
    #senders.send_file("day.txt","附件")
    #senders.send_images('F:\wjk.jpg',"图片")
    senders.send_html("F:\MyProject\work\day0321\\result.html","测试报告")



