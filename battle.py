import json
import random
from moveeffects import effects
class battle():
    def fight(i):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
            hplist=[player['ModifiedHP:']]
        with open("data.json", "r") as ejson:
            edata = json.load(ejson)
            enemy=edata[i]
            enemyhplist=[enemy['Hp:'], enemy['Hp:']]
        print("You encounter a", enemy['Name:'],'!')
        while hplist[0]>0 and enemyhplist[1]>0:
            y=input("What move would you like to use? ")
            if not 'Moves2:' in player:
                if y in player['Moves1:']:         
                    print("VALID MOVE!")
            elif 'Moves2:' in player:
                if y in player['Moves2:']:
                    print("VALID MOVE!")
            else:
                print("INVALID MOVE")
            blocked=False
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
                    print(enemy['Name:'], "attacked!", player['PName:'], "has", hp, "HP!")
                    return(hplist[0])      
            def EffectCheck(w, z):
                if not 'Moves2:' in player:
                    if y in player['Moves1:'][z]:
                        if y == w:
                            return(True)
                elif 'Moves2:' in player:
                    if y in player['Moves2:'][z]:
                        if y ==w:
                            return(True)
                else:
                    return(False)       
            def PlayerAttack(x, w, z):
                if not 'Moves2:' in player:
                    if y in player['Moves1:'][z]:
                        if y == w:
                            if len(enemyhplist) ==1:
                                enemyhplist.append(enemyhplist[0])
                                hp=enemyhplist[1]
                            else:
                                enemyhplist.remove(enemyhplist[0])
                                hp=enemyhplist[0]
                            nhp=hp-x 
                            enemyhplist.append(nhp)
                            if len(enemyhplist)>2:
                                enemyhplist.remove(enemyhplist[0])
                            print(enemy["Name:"], "took", x, "DMG!", enemy["Name:"], "has", enemyhplist[1], "HP!")
                            return(enemyhplist[1])
                elif 'Moves2:' in player:
                    if y in player['Moves2:'][z]:
                        if y ==w:
                            if len(enemyhplist) ==1:
                                enemyhplist.append(enemyhplist[0])
                                hp=enemyhplist[1]
                            else:
                                enemyhplist.remove(enemyhplist[0])
                                hp=enemyhplist[0]
                            nhp=hp-x 
                            enemyhplist.append(nhp)
                            if len(enemyhplist)>2:
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
                    PlayerAttack(25, "Sword Attack", 0)
                SwordAttack()
                def Parry():
                    #takes damage dealt into attack
                    PlayerAttack(30, "Parry", 2)
                Parry()
                def MaceSwing():
                    PlayerAttack(30, "Mace Swing", 0)
                MaceSwing()
                def ShieldBash():
                    PlayerAttack(30, "Shield Bash", 0)
                ShieldBash()
                def MeteorShower():
                    PlayerAttack(20, "Meteor Shower", 0)
                MeteorShower()
                def Thunderbolt():
                    PlayerAttack(25, "Thunder Bolt", 1)
                Thunderbolt()
                def StaffStab():
                    PlayerAttack(15, "Staff Stab", 2)
                StaffStab()
                def NormalArrow():
                    PlayerAttack(20, "Normal Arrow", 0)
                NormalArrow()
                def SlingshotFire():
                    PlayerAttack(15, "Slingshot Fire", 0)
                SlingshotFire()
            class playereffectmoves(moves):
                def Shield():
                    if EffectCheck==True:
                        effects.blockthingy()
                        if effects.blockthingy() == True:
                            blocked==True
                    else:
                        return(False)
                Shield()
            class basicenemymoves(moves):
                def goblinattack():
                    basicattack(0)
                if i==0:
                    if blocked==True:
                        print(enemy['Name:'], "'s Attack was Blocked!")
                    else:
                        goblinattack()
                def spiderattack():
                    basicattack(1)
                if i==1:
                    if blocked==True:
                        print(enemy['Name:'], "'s Attack was Blocked!")
                    else:
                        spiderattack()
                def slimeattack():
                    basicattack(2)
                if i==2:
                    if blocked==True:
                        print(enemy['Name:'], "'s Attack was Blocked!")
                    else:
                        slimeattack()
                def zombieattack():
                    basicattack(3)
                if i==3:
                    if blocked==True:
                        print(enemy['Name:'], "'s Attack was Blocked!")
                    else:
                        zombieattack()
            class bossmoves(moves):
                random.randint(1,4)
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
battle.fight(0)