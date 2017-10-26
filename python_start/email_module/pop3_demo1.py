#Python内置一个poplib模块，实现了POP3协议，可以直接用来收邮件。
"""
POP3协议收取的不是一个已经可以阅读的邮件本身，而是邮件的原始文本，这和SMTP协议很像，SMTP发送的也是经过编码后的一大段文本
要把POP3收取的文本变成可以阅读的邮件，还需要用email模块提供的各种类来解析原始文本，变成可阅读的邮件对象。
第一步：用poplib把邮件的原始文本下载到本地。
第二部：用email解析原始文本，还原为邮件对象。
"""

import poplib
from email.parser import Parser

email = "819718662@qq.com"
password = input('password:')
pop3_host = "pop.qq.com"

server = poplib.POP3(pop3_host, port=995)
server.set_debuglevel(1)
print(server.getwelcome().decode("utf-8"))

server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间:
print("numMessages: %s. sizeMessages:%s" % server.stat())
# list()返回所有邮件的编号:
response, mails, octets = server.list()
print(mails)

# 获取最新一封邮件, 注意索引号从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析出邮件:
msg = Parser().parsestr(msg_content)

#删除最后一封邮件
server.dele(index)
server.quit()

