import random
import json
class moves():
    def __init__(self, player, enemy, damage):
        self.player = player
        self.enemy = enemy
        self.damage = damage
class playermoves(moves):
    def swordswing(y):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
            enemy=y
class playereffectmoves(moves):
      print("FILLLLEEEERRRR")
class basicenemymoves(moves):
    def goblinattack():
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
            with open("data.json", "r") as ejson:
                edata = json.load(ejson)
                enemy=edata[0]
                player['Modified:']=player['ModifiedHP:']-enemy['Dmg:']

class bossmoves(moves):
    print("FILLLLLLEEEERRRR")
e=basicenemymoves
e.goblinattack()