import os
import smtplib

from celery import Celery

celery = Celery('flcelery',
                broker='redis://localhost:6379/0',
                backend='redis://localhost:6379/0')


@celery.task
def send_email(receiver_address, subject, body=None):
    if not body:
        body = subject
        subject = 'No Subject'
    user = os.environ['MAIL_ADDRESS']
    password = os.environ['MAIL_PASSWORD']
    sent_from = user
    to = [receiver_address]
    email_text = """
    From: %s
    To: %s
    Subject: %s%s
    """ % (sent_from, ", ".join(to), subject, body)
    server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_text)
    server.close()
