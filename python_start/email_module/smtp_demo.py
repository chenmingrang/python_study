#SMTP是发送邮件的协议，Python内置对SMTP的支持，可以发送纯文本邮件、HTML邮件以及带附件的邮件。
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件。

from email.mime.text import MIMEText
from email.header import Header

#构造一个最简单的纯文本邮件('text/plain')
msg = MIMEText('hello, use Python send', 'plain', 'utf-8')
msg['Subject'] = Header("hello world", 'utf-8')
msg['From'] = 'chenmingrang@126.com>'
msg['To'] = "819718662@qq.com"

from_addr = input('From:')
passwd = input("Passwd:")
smtp_server = "smtp.126.com"

to_addr = "819718662@qq.com"

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

