#! /usr/bin/env python
# coding=utf-8
import time
import poplib
import smtplib
from datetime import datetime
import email
from email.mime.text import MIMEText
import re


def remove_values_from_list(the_list, val):
    while val in the_list:
        the_list.remove(val)


# 邮件发送函数
def send_mail(mail_host, mail_pass, to_list, sub, content):
    # print me
    msg = MIMEText(content, _subtype='plain')
    msg['Subject'] = sub
    msg['From'] = mail_host
    msg['To'] = ";".join(to_list)  # 将收件人列表以‘；’分隔
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)  # 连接服务器
        server.login(mail_host, mail_pass)  # 登录操作
        server.sendmail(mail_host, [to_list], msg.as_string())
        server.close()
        return True
    except Exception as e:
        # print e
        return False
    return False


# 邮件接收函数
def accpet_mail(accpet_host, accpet_user, accpet_pass):
    mail_list = []
    try:
        p = poplib.POP3(accpet_host, port=110)
        p.user(accpet_user)
        p.pass_(accpet_pass)
        (mail_count, mail_total_size) = p.stat()  # 返回一个元组:(邮件数,邮件尺寸)
        for i in range(mail_count):
            mail_map = {}
            # 邮件从1开始读取,retr方法返回一个元组:(状态信息,邮件,邮件尺寸)
            status_info, email_info, email_size = p.retr(str(i + 1))
            # print decode_header(email.message_from_string(str(email_info)))[0][0]
            # print email.message_from_string(str(email_info))
            message = {}
            last_email_item, append_flag = "", True
            # print str(decode_header(email_info)[0][0])
            remove_values_from_list(email_info, '')
            for j, email_item in enumerate(email_info):
                if j == len(email_info) - 1:
                    message["Content"] = email_item
                    break
                email_item_list = "".join(str(email_item, 'utf-8').split("\r\n")).split(": ")
                if len(email_item_list) != 2:
                    if append_flag == True:
                        message[last_email_item] = message.get(last_email_item) + email_item_list[0]
                        # print email_item_list[0]
                else:
                    if email_item_list[0] in message:
                        append_flag = False
                        continue
                    message[email_item_list[0]] = email_item_list[1]
                    last_email_item = email_item_list[0]
            if "Subject" not in message or "Content" not in message:
                p.dele(str(i + 1))
                continue
            # print i+1,message.get("Subject"),message.get("Content")
            content_match_list = re.findall(r"The sending time", str(message.get("Content"),'utf-8'))
            subject_match_list = re.findall(r"MAILVIEW", str(message.get("Subject"),'utf-8'))
            if subject_match_list == [] or content_match_list == []:
                p.dele(str(i + 1))
                # print i+1,message.get("Subject"),message.get("Content")
                # print "2:"+str(email_info)
                continue
            # print str(i+1)
            content_list = message.get("Content").split("#")
            send_list = content_list[0].split(":")
            # print "send_time" + str(datetime.strptime(send_list[1],'%Y%m%d%H%M%S'))
            # mail_map["send_time"] =str(datetime.strptime(send_list[1],'%Y%m%d%H%M%S'))
            # mail_map["recive_time"] =  str(datetime.strptime(message.get("Date"),'%a, %d %b %Y %H:%M:%S +0800'))
            sr_list = content_list[1].split("@")
            from_list = sr_list[0].split(":")
            to_list = sr_list[1].split(":")
            # print from_list[0] + ":" + from_list[1]
            mail_map[from_list[0]] = from_list[1]
            # print to_list[0] + ":" + to_list[1]
            mail_map[to_list[0]] = to_list[1]
            # print "recive_time:"+str(datetime.strptime(message.get("Date"),'%a, %d %b %Y %H:%M:%S +0800'))
            # Mon, 30 Mar 2015 14:20:58 +0800  '%a, %d %b %Y %H:%M:%S +0800'
            # mail_map["send_time"] =  str(datetime.strptime(message.get("Date"),'%a, %d %b %Y %H:%M:%S +0800'))
            # 从字符串读取信息-->解密邮件头-->字符串取[0][0]-->以"\n"分组-->取第一个-->替换字符串"From nobody "为空-->格式化为日期格式-->得到接收时间
            # mail_map["recive_time"] = str(datetime.strptime(str(decode_header(email.message_from_string(str(email_info)))[0][0]).split("\n")[0].replace("From nobody ",""),'%a %b %d %H:%M:%S %Y'))

            mail_map["send_time"] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(
                time.mktime(email.utils.parsedate(message.get('Date'))))))
            receive_time_list = message.get('Received').split(";")
            mail_map["recive_time"] = str(
                datetime.strptime(receive_time_list[len(receive_time_list) - 1].replace(" (CST)", "").lstrip(),
                                  '%a, %d %b %Y %H:%M:%S +0800'))
            # print message
            # print "send_time: %s" % mail_map.get('send_time')
            # print "recive_time: %s" %  mail_map.get('recive_time')
            # print "----------------------------------------------------------------"
            mail_list.append(mail_map)
            p.dele(str(i + 1))
        p.quit()
        return mail_list
    except poplib.error_proto as e:
        # print "Login failed:",e
        p.quit()
        return mail_list
        # sys.exit(1)
    return mail_list


# 运行当前文件时，执行sendmail和accpet_mail函数
if __name__ == "__main__":
    accpet_host = 'pop.126.com'
    accpet_user = 'chenmingrang@126.com'
    accpet_pass = input("pwd:")
    accpet_mail(accpet_host=accpet_host, accpet_user=accpet_user, accpet_pass=accpet_pass)