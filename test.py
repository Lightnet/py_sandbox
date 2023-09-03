#!python
import time
from enum import Enum
#print("test shebang")

if __name__ == "__main__":
  print("test script")
  Color = Enum('Color', ['RED', 'GREEN', 'BLUE'])
  print(Color)
  color = Color.BLUE
  print("ECOLOR: ",color)
  
  #time.sleep(2.4)#delay when it close