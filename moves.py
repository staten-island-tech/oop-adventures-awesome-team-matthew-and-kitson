import random
import json

class moves():
    def __init__(self, php, enemy, damage):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        self.php = player['ModifiedHP']
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
                basicenemymoves.php=player['ModifiedHP:']-enemy['Dmg:']
                print(player['Modified:'])

class bossmoves(moves):
    print("FILLLLLLEEEERRRR")
e=basicenemymoves
e.goblinattack()
e.goblinattack()