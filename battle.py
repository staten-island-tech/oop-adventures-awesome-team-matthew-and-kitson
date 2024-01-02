import json
import random
from moveeffects import effects
from decimal import Decimal
class battle():
    def fight(i):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
            x=round(Decimal(player['BaseHP:'])*Decimal(player['HpMultiplier:']))
            hplist=[x]
        with open("data.json", "r") as ejson:
            edata = json.load(ejson)
            enemy=edata[i]
            enemyhplist=[enemy['Hp:'], enemy['Hp:']]
        print("You encounter a", enemy['Name:'],'!')
        global burner
        burner=0
        global poison_dmg
        poison_dmg=0
        global summon
        summon=0
        global phase
        phase=0
        while hplist[0]>0 and enemyhplist[1]>0:
            print("Moves:", player['Moves:'])
            movecheck=True
            while movecheck==True:
                y=input("What move would you like to use? ")
                if y in player['Moves:']:
                    movecheck=False
                else:
                    print("INVALID MOVE")
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
            def EffectCheck(w):
                if y==w:
                    if y in player['Moves:']:
                            return(True)
                    else:
                        return(False)
                else:
                    return(False)       
            def PlayerAttack(x, w):
                if y==w:
                    if y in player['Moves:']:
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
            def BossMoves(dmg, name):
                hp=hplist[0]-dmg
                hplist.append(hp)
                hplist.remove(hplist[0])
                print(enemy['Name:'], "used", name, "!", player['PName:'], "has", hp, "HP!")
            #All Moves
            class playermoves(moves):
                def SwordAttack():
                    PlayerAttack(round(Decimal(25)*Decimal(player['DmgMultiplier:'])), "Sword Attack")
                SwordAttack()
                def MaceSwing():
                    PlayerAttack(round(Decimal(30)*Decimal(player['DmgMultiplier:'])), "Mace Swing")
                MaceSwing()
                def ShieldBash():
                    PlayerAttack(round(Decimal(30)*Decimal(player['DmgMultiplier:'])), "Shield Bash")
                ShieldBash()
                def MeteorShower():
                    PlayerAttack(round(Decimal(20)*Decimal(player['DmgMultiplier:'])), "Meteor Shower")
                MeteorShower()
                def Thunderbolt():
                    PlayerAttack(round(Decimal(25)*Decimal(player['DmgMultiplier:'])), "Thunderbolt")
                Thunderbolt()
                def StaffStab():
                    PlayerAttack(round(Decimal(15)*Decimal(player['DmgMultiplier:'])), "Staff Stab")
                StaffStab()
                def NormalArrow():
                    PlayerAttack(round(Decimal(20)*Decimal(player['DmgMultiplier:'])), "Normal Arrow")
                NormalArrow()
                def SlingshotFire():
                    PlayerAttack(round(Decimal(15)*Decimal(player['DmgMultiplier:'])), "Slingshot Fire")
                SlingshotFire()
            class playereffectmoves(moves):
                def Shield():
                    if EffectCheck("Shield")==True:
                        check=effects.shieldthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Shield!")
                    else:
                        return(False)
                def Block():
                    if EffectCheck("Block")==True:
                        check=effects.blockthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Block!")
                    else:
                        return(False)
                def Ice_Shard():
                    PlayerAttack(round(Decimal(25)*Decimal(player['DmgMultiplier:'])), "Ice Shard")
                    if EffectCheck("Ice Shard")==True:
                        check=effects.freeze()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Freeze!")
                    else:
                        return(False)
                def Protection_Spell():
                    if EffectCheck("Protection Spell")==True:
                        check=effects.protectionthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Protect!")
                    else:
                        return(False)
                def Summon():
                    if EffectCheck("Summon")==True:
                        return(True)
                    else:
                        return(False)
                def Fireball():
                    PlayerAttack(round(Decimal(30)*Decimal(player['DmgMultiplier:'])), "Fireball")
                    if EffectCheck("Fireball")==True:
                        check=effects.burning()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Burn!")
                    else:
                        return(False)
                def Heal(x, y):
                    if EffectCheck("Heal")==True:
                        x=effects.heal(x, y)
                        hplist.append(x)
                        hplist.remove(hplist[0])
                        print(player['PName:'], "Healed for", y, "HP!", player['PName:'], "has", x, "HP!")
                Heal(hplist[0], round(Decimal(15)*Decimal(player['HpMultiplier:'])))
                def FireArrow():
                    PlayerAttack(round(Decimal(20)*Decimal(player['DmgMultiplier:'])), "Fire Arrow")
                    if EffectCheck("Fire Arrow")==True:
                        check=effects.burning()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Burn!")
                    else:
                        return(False)
                def Ice_Arrow():
                    PlayerAttack(round(Decimal(20)*Decimal(player['DmgMultiplier:'])), "Ice Arrow")
                    if EffectCheck("Ice Arrow")==True:
                        check=effects.freeze()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Freeze!")
                    else:
                        return(False)
                shield=Shield()
                blocked=Block()
                freeze=Ice_Shard() or Ice_Arrow()
                protect=Protection_Spell()
                summmoning=Summon()
                if y=="Fireball" or "Fire Arrow":
                    burn=Fireball() or FireArrow()
            if not i==6 and not i==8 and not i==10:
                if enemyhplist[1]<0:
                    break
            def enemy_attack_check():
                e=playereffectmoves
                if e.shield==True:
                    print(enemy['Name:'], "'s Attack was Shielded!")
                    return(False)
                elif e.blocked==True:
                    print(enemy['Name:'], "'s Attack was Blocked!")
                    return(False)
                elif e.freeze==True:
                    print(enemy['Name:'], "is Frozen!")
                    return(False)
                elif e.protect==True:
                    print(enemy['Name:'], "'s Attack was Protected!")
                    return(False)
                else:
                    return(True)
            class basicenemymoves(moves):
                def goblinattack():
                    basicattack(0)
                if i==0:
                    if enemy_attack_check()==True:
                        goblinattack()
                def spiderattack():
                    basicattack(1)
                if i==1:
                    if enemy_attack_check()==True:
                        spiderattack()
                def slimeattack():
                    basicattack(2)
                if i==2:
                    if enemy_attack_check()==True:
                        slimeattack()
                def zombieattack():
                    basicattack(3)
                if i==3:
                    if enemy_attack_check()==True:
                        zombieattack()
            class bossmoves(moves):
                def GolemSlam():
                    BossMoves(55, "Golem Slam")
                def BoulderThrow():
                    BossMoves(45, "Boulder Throw")
                def GolemPunch():
                    BossMoves(50, "Golem Punch")
                def Roll():
                    BossMoves(40, "Roll") 
                def Poisoning():
                    BossMoves(0, "Poisoning")
                def DeathSpell():
                    BossMoves(60, "Death Spell")
                def FireBreath():
                    BossMoves(50, "Fire Breath")
                def ClawSlash():
                    BossMoves(45, "Claw Slash")
                def TailSwing():
                    BossMoves(40, "Tail Swing")
                def Fly():
                    BossMoves(35, "Fly")
                def BlueFireBreath():
                    BossMoves(60, "Blue Fire Breath")
                def Bite():
                    BossMoves(50, "Bite")
                def Slam():
                    BossMoves(55, "Slam")
                def SwordAttack():
                    BossMoves(50, "Sword Attack")
                def SwordSlam():
                    BossMoves(55, "Sword Slam")
                def CrownThrow():
                    BossMoves(45, "Crown Throw")
                def SwordSlash():
                    BossMoves(60, "Sword Slash")
                def JewelBash():
                    BossMoves(70, "Jewel Bash")
                def KingSlam():
                    BossMoves(65, "King Slam")
                def HydraBlast():
                    BossMoves(65, "Hydra Blast")
                def TripleAttack():
                    BossMoves(60, "Triple Attack")
                def HydraBite():
                    BossMoves(50, "Hydra Bite")
                def HydraBeam():
                    BossMoves(85, "Hydra Beam")
                def SkullFire():
                    BossMoves(80, "Skull Fire")
                def PoisonFire():
                    BossMoves(50, "Poison Fire")
                def TripleBlast():
                    BossMoves(100, "Triple Blast")
                def Regenerate():
                    if enemyhplist[1]+enemyhplist[0]//3>829:
                        enemyhplist.append(829)
                        enemyhplist.remove(enemyhplist[0])
                    else:
                        enemyhplist.append(effects.heal(enemyhplist[1], enemyhplist[0]//3))
                        enemyhplist.remove(enemyhplist[0])
                    print(edata[i]['Name:'], "used regenerate and healed", enemyhplist[0]-enemyhplist[1], "HP!")
                    enemyhplist.remove(enemyhplist[0])
                def OneHeadAttack():
                    BossMoves(120, "One Head Attack")
                def LastEffort():
                    BossMoves(150, "Last Effort")
            #boss-phase-hp-check
            if i==6 or i==8 and phase==1:
                if enemyhplist[1]<0:
                    break
            if i==10 and phase==2:
                if enemyhplist[1]<0:
                    bossmoves.LastEffort() #uses last effort when going to die
                    break
            #Mini/Final-Boss-Move-Selection
            b=bossmoves
            global Poison
            if i==4:
                moveint=random.randint(1,4)
                if enemy_attack_check()==True:
                    if moveint==1:
                        b.GolemSlam()
                    if moveint==2:
                        b.BoulderThrow()
                    if moveint==3:
                        b.GolemPunch()
                    if moveint==4:
                        b.Roll()
            if i==5:
                moveint=random.randint(1,2)
                if enemy_attack_check()==True:
                    if moveint==1:
                        b.Poisoning()
                        Poison=True
                    if moveint==2:
                        b.DeathSpell()
                        Poison=False
            if i==6:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(edata[7]["Hp:"])
                    enemyhplist.append(edata[7]["Hp:"])
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("Dragon is in Phase 2!")
                    phase=phase+1
                if phase==1:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.BlueFireBreath()
                        if moveint==2:
                            b.Bite()
                        if moveint==3:
                            b.Slam()
                else:
                    moveint=random.randint(1,4)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.FireBreath()
                        if moveint==2:
                            b.ClawSlash()
                        if moveint==3:
                            b.TailSwing()
                        if moveint==4:
                            b.Fly()
            if i==8:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(edata[9]["Hp:"])
                    enemyhplist.append(edata[9]["Hp:"])
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("King is in Phase 2!")
                    phase=phase+1
                if phase==1:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.SwordSlam()
                        if moveint==2:
                            b.JewelBash()
                        if moveint==3:
                            b.KingSlam()
                else:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.SwordAttack()
                        if moveint==2:
                            b.SwordSlam()
                        if moveint==3:
                            b.CrownThrow()
            if i==10:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(edata[11]["Hp:"])
                    enemyhplist.append(edata[11]["Hp:"])
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("First Head was Killed! Hydra is in Phase 2!")
                    phase=phase+1
                if enemyhplist[1]<0 and phase==1:
                    enemyhplist.append(edata[12]["Hp:"])
                    enemyhplist.append(edata[12]["Hp:"])
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("Second Head was Killed! Hydra is in Phase 3!")
                    phase=phase+1
                if phase==1:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.HydraBeam()
                            Poison=False
                        if moveint==2:
                            b.SkullFire()
                            Poison=False
                        if moveint==3:
                            b.HydraBite()
                            Poison=False
                elif phase==2:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.TripleBlast()
                            Poison=False                        
                        if moveint==2:
                            b.Regenerate()
                            Poison=False
                        if moveint==3:
                            b.OneHeadAttack()
                            Poison=False
                else:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.HydraBlast()
                            Poison=False
                        if moveint==2:
                            b.TripleAttack()
                            Poison=False
                        if moveint==3:
                            b.PoisonFire()
                            Poison=True
            #Effect-Checking
            if playereffectmoves.Summon()==True or summon==1:
                summon=1
                if len(enemyhplist)==1:
                    enemyhplist.append(enemyhplist[0])
                    hp=enemyhplist[1]
                else:
                    enemyhplist.remove(enemyhplist[0])
                    hp=enemyhplist[0]
                nhp=hp-round(Decimal(30)*Decimal(player['DmgMultiplier:']))
                enemyhplist.append(nhp)
                if len(enemyhplist)>2:
                    enemyhplist.remove(enemyhplist[0])
                print("Zombies attacked", enemy['Name:'], "!", enemy["Name:"], "took", x, "DMG!", enemy["Name:"], "has", enemyhplist[1], "HP!")
            if y=="Fireball" or "Fire Arrow":
                if playereffectmoves.burn==True and burner==0:
                    burner=burner+3
            if i==10 or i==5:
                if Poison==True:
                    if poison_dmg==0:
                        poison_dmg=poison_dmg+3
            if not burner==0:
                burner=burner-1
                if len(enemyhplist) ==1:
                    enemyhplist.append(enemyhplist[0])
                    hp=enemyhplist[1]
                else:
                    enemyhplist.remove(enemyhplist[0])
                    hp=enemyhplist[0]
                nhp=hp-10
                enemyhplist.append(nhp)
                if len(enemyhplist)>2:
                    enemyhplist.remove(enemyhplist[0])
                print(enemy["Name:"], "was Burned!", enemy["Name:"], "took", 10, "DMG!", enemy["Name:"], "has", enemyhplist[1], "HP!")
            if not poison_dmg==0:
                poison_dmg=poison_dmg-1
                hp=hplist[0]
                nhp=hp-45
                hplist.append(nhp)
                hplist.remove(hplist[0])
                print(player['PName:'], "is Poisoned!", player['PName:'], "has", nhp, "HP!")
        if hplist[0]<0:
            print(player['PName:'], 'Lost the Battle!')
            return(False)
        if enemyhplist[1]<0:
            print(player['PName:'], 'Won the Battle!')
            return(True)
battle.fight(0)