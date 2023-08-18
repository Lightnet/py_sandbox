# https://www.djangosnippets.org/snippets/96/
# https://stackoverflow.com/questions/2690965/a-simple-smtp-server-in-python
# https://tutorialedge.net/python/concurrency/asyncio-event-loops-tutorial/


# oudate for mail server ??? 
from datetime import datetime
import asyncio
from smtpd import SMTPServer

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = '%s-%d.eml' % (datetime.now().strftime('%Y%m%d%H%M%S'),
                self.no)
        f = open(filename, 'w')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.no += 1

async def work():
    while True:
        await asyncio.sleep(1)
        #print("Task Executed")


loop = asyncio.get_event_loop()
def run():
    foo = EmlServer(('localhost', 25), None)
    try:
        asyncio.ensure_future(work())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()

if __name__ == '__main__':
	run()