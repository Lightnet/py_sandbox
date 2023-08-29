

# https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
# https://pypi.org/project/psutil/
# 
# 
import os
# Importing the library
import psutil
# Calling psutil.cpu_precent() for 4 seconds
print('The CPU usage is: ', psutil.cpu_percent(4))

# Getting loadover15 minutes
load1, load5, load15 = psutil.getloadavg()
 
cpu_usage = (load15/os.cpu_count()) * 100
 
print("The CPU usage is : ", cpu_usage)
import os
 
# Getting all memory using os.popen()
#total_memory, used_memory, free_memory = map(
    #int, os.popen('free -t -m').readlines()[-1].split()[1:])
 
# Memory usage
#print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))

print("RAM memory % used:", psutil.virtual_memory().percent)

print("RAM memory % used:", psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)