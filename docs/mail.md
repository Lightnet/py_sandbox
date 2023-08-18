# Information:
  Mail smtpd for server as python 3.12.0 remove for sync to aiosmtpd


  https://www.youtube.com/watch?v=1Uyo2c2GYKQ

```py
from aiosmtpd.smtp import AuthResult, LoginPassword

auth_db = {
    b"user1": b"password1",
    b"user2": b"password2",
    b"user3": b"password3",
}

# Name can actually be anything
def authenticator_func(server, session, envelope, mechanism, auth_data):
  # For this simple example, we'll ignore other parameters
  assert isinstance(auth_data, LoginPassword)
  username = auth_data.login
  password = auth_data.password
  # If we're using a set containing tuples of (username, password),
  # we can simply use `auth_data in auth_set`.
  # Or you can get fancy and use a full-fledged database to perform
  # a query :-)
  if auth_db.get(username) == password:
    return AuthResult(success=True)
  else:
    return AuthResult(success=False, handled=False)
```

```py
controller = Controller(
  handler,
  hostname='192.168.8.125',
  port=10025,
  authenticator=authenticator_func,  # i.e., the name of your authenticator function
  auth_required=True,  # Depending on your needs
)
# auth_require_tls=False #test...
```



 * https://code.tutsplus.com/sending-emails-in-python-with-smtp--cms-29975t

```py
from flask import Flask
from flask_mail import Mail
app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'email@gmail.com'
app.config['MAIL_PASSWORD'] = 'gmailpassword'

mail = Mail(app)

msg = Message('Introducing Haiku', sender =   'haiku@mail.io', recipients = ['your_gmail'])
msg.body = "Configuration Test message"
mail.send(msg)
```