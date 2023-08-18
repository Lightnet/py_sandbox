# https://aiosmtpd.readthedocs.io/en/latest/controller.html
# https://github.com/aio-libs/aiosmtpd/blob/master/examples/basic/server.py
# https://stackoverflow.com/questions/66170956/python-aiosmtpd-server-with-basic-authentication
import asyncio

from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink

class ExampleHandler:
  async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
    print("address: ", address)
    if not address.endswith('@example.com'):
      return '550 not relaying to that domain'
    envelope.rcpt_tos.append(address)
    return '250 OK'

  async def handle_DATA(self, server, session, envelope):
    print('Message from %s' % envelope.mail_from)
    print('Message for %s' % envelope.rcpt_tos)
    print('Message data:\n')
    for ln in envelope.content.decode('utf8', errors='replace').splitlines():
      print(f'> {ln}'.strip())
    print()
    print('End of message')
    return '250 Message accepted for delivery'

async def amain(loop):
  #cont = Controller(Sink(), hostname='', port=8025)
  cont = Controller(ExampleHandler(), hostname='localhost', port=8025)
  cont.start()

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





"""
class CustomSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        myqueue.queue.put(envelope.content)
        return '250 OK'

handler = CustomSMTPHandler()
self.server = aiosmtpd.controller.Controller(handler)
self.server.start()
input("Server started. Press Return to quit.")
self.server.stop()
"""