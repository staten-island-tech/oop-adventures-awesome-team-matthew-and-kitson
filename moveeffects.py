import random
import json
import time

  
i=0
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
    x=player['BaseHP:']*player['HpMultiplier:']
    hplist=[x]
with open("data.json", "r") as ejson:
    edata = json.load(ejson)
    enemy=edata[i]
    enemyhplist=[enemy['Hp:']]
class effects:
    def __init__(self, player, enemy, damage):
        self.player = player
        self.enemy = enemy
        self.damage = damage
    def blockthingy():
        t_time = random.randint(1, 3)
        t1 = time.time()
        while True:
            user_input = input("Enter 'Block': ")
            t2 = time.time()
            t3 = t2 - t1
            if user_input == "Block" and t3<=t_time:
                return(True)
            if t3 >= t_time:
                return(False)
    def burn():
        if random.randint(0,1) == 0:
            hplist=hplist-10
    def heal(x, y):
        x=x+y
