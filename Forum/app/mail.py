from flask import current_app, render_template
from app.extensions import mail
from flask_mail import Message
from threading import Thread


def async_send_mail(app, msg):
    # 发送邮件需要程序上下文
    with app.app_context():
        mail.send(msg)


# 封装函数发送邮件
def send_mail(to, subject, template, **kwargs):
    # 该函数不在manage.py中
    # 从代理对象中获取原始对象
    app = current_app._get_current_object()
    # 准备邮件内容
    msg = Message(subject=subject,
                  recipients=[to],
                  sender=app.config['MAIL_USERNAME'])
    # 添加HTML内容，通过浏览器查看邮件
    msg.html = render_template('mail/' + template + '.html', **kwargs)
    # 添加body内容，命令行接收邮件
    msg.body = render_template('mail/' + template + '.txt', **kwargs)

    # 创建线程
    thr = Thread(target=async_send_mail, args=[app, msg])
    # 启动线程
    thr.start()
    return thr