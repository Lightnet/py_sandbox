# https://www.programiz.com/python-programming/datetime/strftime
# https://www.askpython.com/python/examples/capture-screenshots
# https://blog.finxter.com/how-to-get-a-windows-screenshot-in-python/
# 
#import pyautogui
import PIL.ImageGrab #built in?
from datetime import datetime # built in

now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y__%H_%M_%S")
#myScreenshot = pyautogui.screenshot()
#myScreenshot.save('{date_time}test.png')
print("DATE: ",date_time)
screenshot = PIL.ImageGrab.grab()
screenshot.show()
screenshot.save("date"+ date_time + "_desktop.jpg")