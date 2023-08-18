from ptpmail import amain
import asyncio

if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  try:
    loop.create_task(amain(loop=loop))
    print("init mail test server...")
    loop.run_forever()
  except KeyboardInterrupt:
    print("User abort indicated")
  finally:
    print("Closing Loop")
    loop.close()