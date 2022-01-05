# encoding:utf-8
import os
import yagmail


def sendBy163(to, subject, body, attachments=None, html="", user="Mr_Qian_Ives@163.com",
              password=os.environ["pass163"],
              host="smtp.163.com",
              port=465):
    # 示例
    # sendBy163(["990509820@qq.com"], "看到请回复", "请查看系统日志", ["1.jpg", "2.jpg"])
    # to="990509820@qq.com"
    # to=["990509820@qq.com"]
    # subject = 'This is obviously the subject'
    # body = 'This is obviously the body'
    # html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
    # attachments = ['path/to/attachment1.png', 'path/to/attachment2.pdf', 'path/to/attachment3.zip']
    yag = yagmail.SMTP(user, password, host, port)
    yag.send(to=to, subject=subject, contents=[body, html], attachments=attachments)


def sendByQQ(to, subject, body, attachments=None, html="", user="1356227919@qq.com",
             password=os.environ["passqq"],
             host="smtp.qq.com",
             port=465):
    # 示例
    # sendByQQ(["990509820@qq.com"], "看到请回复", "请查看系统日志", ["1.jpg", "2.jpg"])
    # to="990509820@qq.com"
    # to=["990509820@qq.com"]
    # subject = 'This is obviously the subject'
    # body = 'This is obviously the body'
    # html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
    # attachments = ['path/to/attachment1.png', 'path/to/attachment2.pdf', 'path/to/attachment3.zip']
    yag = yagmail.SMTP(user, password, host, port)
    yag.send(to=to, subject=subject, contents=[body, html], attachments=attachments)

# demo
# sendByQQ(["990509820@qq.com"], "看到请回复", "请查看系统日志", ["1.jpg", "2.jpg"])
