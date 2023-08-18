#!/usr/bin/python
# https://www.tutorialspoint.com/python/python_sending_email.htm
# https://realpython.com/python-send-email/#getting-started
# python built in mail
from smtplib import SMTP, SMTPException
import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
  #smtplib.SMTP('mail.your-domain.com', 25)
  smtpObj = smtplib.SMTP('localhost')
  smtpObj.sendmail(sender, receivers, message)         
  print("Successfully sent email")
except SMTPException:
  print("Error: unable to send email")