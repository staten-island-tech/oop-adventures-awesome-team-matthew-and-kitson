import json
import random
from moveeffects import effects
#WILL BE TAKEN FROM SEPERATE SCRIPT/FUNCTION>>>
i=int(input("Number 0-12: "))

with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
    hplist=[player['ModifiedHP:']]
with open("data.json", "r") as ejson:
    edata = json.load(ejson)
    enemy=edata[i]
    enemyhplist=[enemy['Hp:']]
while hplist[0]>0 and enemyhplist[0]>0:
    y=input("What move would you like to use?")
    class moves():
        def __init__(self, player, enemy, damage):
            self.player = player
            self.enemy = enemy
            self.damage = damage
    def basicattack(i):
        with open("data.json", "r") as ejson:
            edata = json.load(ejson)
            enemy=edata[i]
            hp=hplist[0]
            hp=hp-enemy['Dmg:']
            hplist.append(hp)
            hplist.remove(hplist[0])
            return(hplist[0])
    def PlayerAttack(x, z):
        if y in player['Moves1:'][z]:
            hp=enemyhplist[0]
            hp=hp-x
            enemyhplist.append(enemyhplist[0])
            enemyhplist.append(hp)
            enemyhplist.remove(enemyhplist[0])
            print(enemy["Name:"], "took", x, "DMG!", enemy["Name:"], "has", enemyhplist[1], "HP!")
            return(enemyhplist[1])
        elif 'Moves2:' in player:
            if y in player['Moves2:'][z]:
                hp=enemyhplist[0]
                hp=hp-x
                enemyhplist.append(enemyhplist[0])
                enemyhplist.append(hp)
                enemyhplist.remove(enemyhplist[0])
                print(enemy["Name:"], "took", x, "DMG!", enemy["Name:"], "has", enemyhplist[1], "HP!")
                return(enemyhplist[1])
    def BossMoves(y):
        hp=hplist[0]
        hp=hp-y
        hplist.append(hp)
        hplist.remove(hplist[0])
        print(hplist[0])
    class playermoves(moves):
        def SwordAttack():
            PlayerAttack(25, 0)
        SwordAttack()
        def Parry():
            #takes damage dealt into attack
            PlayerAttack(30, 1)
        Parry()
        def MaceSwing():
            PlayerAttack(30, 2)
        MaceSwing()
        def ShieldBash():
            PlayerAttack(30, 0)
        ShieldBash()
        def MeteorShower():
            PlayerAttack(20, 0)
        MeteorShower()
        def Thunderbolt():
            PlayerAttack(25, 1)
        Thunderbolt()
        def StaffStab():
            PlayerAttack(15, 2)
        StaffStab()
        def NormalArrow():
            PlayerAttack(20, 0)
        NormalArrow()
        def SlingshotFire():
            PlayerAttack(15, 0)
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