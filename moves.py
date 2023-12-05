import random
import json
class moves():
    def __init__(self, player, enemy, damage):
        self.player = player
        self.enemy = enemy
        self.damage = damage
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
    hplist=[player['ModifiedHP:']]
with open("data.json", "r") as ejson:
    edata = json.load(ejson)
    filler=edata[i]
    enemyhplist=[filler['Hp:']]
def basicattack(i):
    with open("data.json", "r") as ejson:
        edata = json.load(ejson)
        enemy=edata[i]
        hp=hplist[0]
        hp=hp-enemy['Dmg:']
        hplist.append(hp)
        hplist.remove(hplist[0])
        print(hplist[0])
class playermoves(moves):
    def SwordAttack(y):
        if "Sword Attack" in player['Moves1:'] or "Sword Attack" in player['Moves2:']:
            hp=enemyhplist[0]
            hp=hp-30
            enemyhplist.append(hp)
            enemyhplist.remove(enemyhplist[0])
            print(enemyhplist[0])
class playereffectmoves(moves):
      print("FILLLLEEEERRRR")
class basicenemymoves(moves):
    def goblinattack():
        basicattack(0)
    def spiderattack():
        basicattack(1)
    def slimeattack():
        basicattack(2)
    def zombieattack():
        basicattack(3)
class bossmoves(moves):
    print("FILLLLLLEEEERRRR")
e=basicenemymoves
e.goblinattack()