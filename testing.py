import os
import time
import random

s=random.randint(1,3)
e=input("ENTER Block:")
while s<=60:
    print (s, 'Seconds')
    time.sleep(1)
    print ("\033[A                             \033[A")
    s-=1
    if s==0:
        print("Failed to Block")
        break
    if e=="Block":
        print("Blocked!")
        break