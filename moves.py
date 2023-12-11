import random
import json
from moveeffects import effects
#WILL BE TAKEN FROM SEPERATE SCRIPT/FUNCTION>>>
i=0
y="Sword Attack"
#WILL BE TAKEN FROM SEPERATE SCRIPT/FUNCTION^^^
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
    enemy=edata[i]
    enemyhplist=[enemy['Hp:']]
def basicattack(i):
    with open("data.json", "r") as ejson:
        edata = json.load(ejson)
        enemy=edata[i]
        hp=hplist[0]
        hp=hp-enemy['Dmg:']
        hplist.append(hp)
        hplist.remove(hplist[0])
        return(hplist[0])
def PlayerAttack(x):
    if y in player['Moves1:'] or y in player['Moves2:']:
        hp=enemyhplist[0]
        hp=hp-x
        enemyhplist.append(hp)
        enemyhplist.remove(enemyhplist[0])
        return(enemyhplist[0])
def BossMoves(y):
    hp=hplist[0]
    hp=hp-y
    hplist.append(hp)
    hplist.remove(hplist[0])
    print(hplist[0])
class playermoves(moves):
    list1=['SwordAttack', 'Parry', 'MaceSwing', 'ShieldBash', 'MeteorShower', 'Thunderbolt', 'StaffStab', 'NormalArrow', 'SlingshotFire']
    def SwordAttack():
        PlayerAttack(25)
    def Parry():
        #takes damage dealt into attack
        PlayerAttack()
    def MaceSwing():
        PlayerAttack(30)
    def ShieldBash():
        PlayerAttack(30)
    def MeteorShower():
        PlayerAttack(20)
    def Thunderbolt():
        PlayerAttack(25)
    def StaffStab():
        PlayerAttack(15)
    def NormalArrow():
        PlayerAttack(20)
    def SlingshotFire():
        PlayerAttack(15)
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
    def FireBreath():
        BossMoves(50)
    def ClawSlash():
        BossMoves(30)
    def TailSwing():
        BossMoves(40)
    def Fly():
        BossMoves(30)
    def BlueFireBreath():
        BossMoves(60)
    def Bite():
        BossMoves(35)
    def Slam():
        BossMoves(45)
    def SwordAttack():
        BossMoves(45)
    def SwordSlam():
        BossMoves(50)
    def CrownThrow():
        BossMoves(35)
e=bossmoves
e.FireBreath()