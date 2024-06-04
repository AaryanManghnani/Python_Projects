import time
import os

while True:
    current_time = time.gmtime()
    clock = time.strftime("%H:%M:%S", current_time)
    print(clock)
    time.sleep(1)
    os.system('cls')
    
