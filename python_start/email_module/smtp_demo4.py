from email import encoders
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

def format_addr(s):
    name, addr = parseaddr(s)
    #经过Header对象编码的文本，包含utf-8编码信息和Base64编码的文本
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = "chenmingrang@126.com"
pwd = input("PWD:")
to_addr = "819718662@qq.com"

msg = MIMEMultipart()
msg["From"] = format_addr('python爱好者<%s>' % from_addr)
msg["To"] = format_addr('管理员<%s>' % to_addr)
msg["Subject"] = Header("来自火星的问候。。。", 'utf-8').encode()
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

with open("201710.doc", 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('application', 'msword', filename="201710.doc")
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='cmr.doc')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')

    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP('smtp.126.com', 25)
server.set_debuglevel(1)
server.login(from_addr, pwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()