# https://www.tutorialspoint.com/python/python_sending_email.htm
# https://docs.python.org/3/library/smtplib.html
from smtplib import SMTP, SMTPException

def send_mail():
  try:
    clientMail = SMTP('localhost', 8025)
    clientMail.set_debuglevel(1)
    #clientMail.login('test','test')#test login for aiosmtpd > def authenticator 
    #clientMail.login('test','test2')#test fail
    clientMail.sendmail('test@example.com', ['bart@example.com'], """\
    From: test@example.com
    To: bart@example.com
    Subject: A test

    testing log
    """)
    clientMail.quit()
    print("Successfully sent email")
  except SMTPException:
    print("Error: unable to send email")

if __name__ == '__main__':
  send_mail()