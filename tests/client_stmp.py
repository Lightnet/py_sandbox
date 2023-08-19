from smtplib import SMTP as Client, SMTPException

def send_mail():
  try:
    client = Client('localhost', 8025)
    code, message = client.docmd('PING')
    print("code: ", code)
    print("message: ", message)
    client.close()
    print("Successfully sent data")
  except SMTPException:
    print("Error: unable to send data")

    
if __name__ == '__main__':
  send_mail()