import random
import json
i=0
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
    hplist=[player['ModifiedHP:']]
with open("data.json", "r") as ejson:
    edata = json.load(ejson)
    enemy=edata[i]
    enemyhplist=[enemy['Hp:']]
class effects:
    def __init__(self, player, enemy, damage):
        self.player = player
        self.enemy = enemy
        self.damage = damage
    def block():
        print("e")
    def burn():
        if random.randint(0,1) == 0:
            hplist=hplist-10
    def heal(x, y):
        x=x+y