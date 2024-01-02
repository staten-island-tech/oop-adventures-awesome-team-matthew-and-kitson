import random
import time
from decimal import Decimal
class effects:
    def blockthingy():
        t_time = random.randint(1, 2)
        t1 = time.time()
        while True:
            user_input = input("Enter 'Block': ")
            t2 = time.time()
            t3 = t2 - t1
            if user_input == "Block" and t3<=t_time:
                return(True)
            if t3 >= t_time:
                return(False)
    def shieldthingy():
        t_time = random.randint(2, 4)
        t1 = time.time()
        while True:
            user_input = input("Enter 'Shield': ")
            t2 = time.time()
            t3 = t2 - t1
            if user_input == "Shield" and t3<=t_time:
                return(True)
            if t3 >= t_time:
                return(False)
    def protectionthingy():
        t_time = random.randint(2, 4)
        t1 = time.time()
        while True:
            user_input = input("Enter 'Spell': ")
            t2 = time.time()
            t3 = t2 - t1
            if user_input == "Spell" and t3<=t_time:
                return(True)
            if t3 >= t_time:
                return(False)
    def freeze():
        if random.randint(1,3)==1:
            return(True)
        else:
            return(False)
    def burning():
        if random.randint(1,2) == 1:
            return(True)
        else:
            return(False)
    def heal(x, y):
        z=Decimal(x)+Decimal(y)
        return(Decimal(z))