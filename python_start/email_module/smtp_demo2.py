from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def format_addr(s):
    name, addr = parseaddr(s)
    #经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input("From:")
pwd = input("PWD:")
to_addr = "819718662@qq.com"

msg = MIMEText(_text='hello, this msg send by Python...', _charset='utf-8')
msg["From"] = format_addr('python爱好者<%s>' % from_addr)
# msg["From"] = 'python爱好者' 发送失败
#msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可。
msg["To"] = format_addr('管理员<%s>' % to_addr)
#如果包含中文，需要通过Header对象进行编码
msg["Subject"] = Header("来自火星的问候。。。", 'utf-8').encode()

server = smtplib.SMTP('smtp.126.com', 25)
server.set_debuglevel(1)
server.login(from_addr, pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()