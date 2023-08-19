# mail local server

#import asyncio
import datetime
from aiosmtpd.controller import Controller
from aiosmtpd.smtp import AuthResult, LoginPassword
from aiosmtpd.smtp import SMTP as Server, syntax
import sqlalchemy as db

engine = db.create_engine("sqlite:///maildb.sqlite")
conn = engine.connect() 
metadata = db.MetaData() #extracting the metadata

User = db.Table('User', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('alias', db.String(255), nullable=False),
  db.Column('passphrase', db.String(255), nullable=False),
  db.Column('pass_hash', db.String(255)),
  db.Column('role', db.String(32), default="member"),
  db.Column('status', db.String(16), default="offline"),
  db.Column('groupid', db.String(16), default="default"),
  db.Column('ban', db.Boolean(), default=False),
  db.Column('created_at', db.types.DateTime(timezone=True), default=datetime.datetime.utcnow)
)

EMail = db.Table('EMail', metadata,
  db.Column('Id', db.Integer(),primary_key=True),
  db.Column('sender', db.String(255), nullable=False),
  db.Column('receivers', db.String(255), nullable=False),
  db.Column('content', db.String()),
  db.Column('message', db.String()),
  db.Column('isread', db.Boolean(), default=False),
  db.Column('dir', db.String(255), default="inbox"),
  db.Column('created_at', db.types.DateTime(timezone=True), default=datetime.datetime.utcnow)
)

metadata.create_all(engine)

auth_db = {
  b"test": b"test",
  b"user1": b"password1",
  b"user2": b"password2",
  b"user3": b"password3",
}

# Name can actually be anything
def authenticator_func(server, session, envelope, mechanism, auth_data):
  # For this simple example, we'll ignore other parameters
  assert isinstance(auth_data, LoginPassword)
  username = auth_data.login.decode('utf-8')#convert b"" to string
  password = auth_data.password.decode('utf-8')#convert b"" to string
  # If we're using a set containing tuples of (username, password),
  # we can simply use `auth_data in auth_set`.
  # Or you can get fancy and use a full-fledged database to perform
  # a query :-)
  query = User.select().where(User.columns.alias == username)
  output = conn.execute(query)
  result = output.fetchone()
  print("AUTH:: ", username)
  #print("username: ", username)
  #print("password: ", password)
  #print("result: ", result)
  if result == None:
    print("NONE USER AUTH: ")
    return AuthResult(success=False, handled=False)
  else:
    if password == result[2]:
      print("PASS: ", result[2])
      return AuthResult(success=True)  
    else:
      print("BAD PASS: ", result[2])
      return AuthResult(success=False, handled=False)

  # simple test
  """
  if auth_db.get(username) == password:
    return AuthResult(success=True)
  else:
    return AuthResult(success=False, handled=False)
  """

class MailHandler:
  async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
    if not address.endswith('@example.com'):
      return '550 not relaying to that domain'
    envelope.rcpt_tos.append(address)
    return '250 OK'

  async def handle_DATA(self, server, session, envelope):
    print('Message from %s' % envelope.mail_from)
    print('Message for %s' % envelope.rcpt_tos)
    print("envelope.content: ", envelope.content)

    print('Message data:\n')
    for ln in envelope.content.decode('utf8', errors='replace').splitlines():
      print(f'> {ln}'.strip())
    print()
    print('End of message')
    return '250 Message accepted for delivery'


class EMailServer(Server):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)#need this

  @syntax('PING [ignored]')
  async def smtp_PING(self, arg):
    print("client ping...")
    await self.push('259 Pong')

# https://github.com/aio-libs/aiosmtpd/blob/master/aiosmtpd/tests/test_server.py
# https://github.com/aio-libs/aiosmtpd/issues/198
# 
class MyController(Controller):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)#need this

  #def factory(self):
    #return EMailServer(self.handler)
  def factory(self):
    #super().factory(self)
    print("FACTORY:: ")
    #self.smtpd = EMailServer(self.handler,auth_callback=authenticator_func)
    self.smtpd = EMailServer(
      self.handler,
      #hostname='localhost',
      #port=8025,
      #authenticator=authenticator_func,
      #auth_required=True,  # Depending on your needs
      #auth_require_tls=False
    )
    #self.smtpd = EMailServer(self.handler)
    return self.smtpd

async def amain(loop):
  #print("loop???")
  #cont = Controller(Sink(), hostname='', port=8025)
  #cont = Controller(
  cont = MyController(
    MailHandler(),
    hostname='localhost',
    port=8025,
    authenticator=authenticator_func,  # i.e., the name of your
    auth_required=True,  # Depending on your needs
    auth_require_tls=False
  )
  print("PORT:",cont.port)
  print("HOST:",cont.hostname)
  cont.start()

"""
if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  loop.create_task(amain(loop=loop))
  try:
    print("init mail test server...")
    loop.run_forever()
  except KeyboardInterrupt:
    print("User abort indicated")
    loop.close()
  finally:
    loop.close()
"""