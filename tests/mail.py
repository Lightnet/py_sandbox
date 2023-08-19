# https://www.djangosnippets.org/snippets/96/
# https://stackoverflow.com/questions/2690965/a-simple-smtp-server-in-python
# https://stackoverflow.com/questions/32173803/sending-emails-in-python-via-loop
from datetime import datetime
#import asyncore
#from smtpd import SMTPServer
import smtplib

#!/usr/bin/python


def mail_send():
  sender = 'from@fromdomain.com'
  receivers = ['to@todomain.com']

  message = """From: From Person <from@fromdomain.com>
  To: To Person <to@todomain.com>
  Subject: SMTP e-mail test

  This is a test e-mail message.
  """

  try:
    smtpObj = smtplib.SMTP('localhost',25)
    smtpObj.sendmail(sender, receivers, message)         
    print("Successfully sent email")
  except smtplib.SMTPException:
    print("Error: unable to send email")

if __name__ == '__main__':
  mail_send()
	#run()