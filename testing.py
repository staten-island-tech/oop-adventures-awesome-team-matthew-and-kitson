import os
import time
import random


s=random.randit(0,10)

while s<=60:
    os.system('cls')
    print (s, 'Seconds')
    time.sleep(1)
    s+=1
    if s==0:
        print("Failed to Block")
        break
   