import stuff
import json
import random
from moveeffects import effects
from decimal import Decimal
class battle():
    def fight(enemy):
        hplist=[stuff.Hero.hp]
        enemyhplist=[enemy.HP, enemy.HP]
        print("You encounter a", enemy.Name,'!')
        global burner
        burner=0
        global poison_dmg
        poison_dmg=0
        global summon
        summon=0
        global phase
        phase=0
        while hplist[0]>0 and enemyhplist[1]>0:
            print("Moves:", stuff.Hero.moves)
            movecheck=True
            while movecheck==True:
                y=input("What move would you like to use? ")
                if y in stuff.Hero.moves:
                    movecheck=False
                else:
                    print("INVALID MOVE")
            class moves():
                def __init__(self, enemy, damage):
                    self.enemy = enemy
                    self.damage = damage
                def basicattack():
                    hp=hplist[0]
                    hp=hp-enemy.DMG
                    hplist.append(hp)
                    hplist.remove(hplist[0])
                    print(enemy.Name, "attacked!", stuff.Hero.name, "has", hp, "HP!")      
                def EffectCheck(w):
                    if y==w:
                        if y in stuff.Hero.moves:
                            return(True)
                        else:
                            return(False)
                    else:
                        return(False)       
                def PlayerAttack(x, w):
                    if y==w:
                        if y in stuff.Hero.moves:
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
                            print(enemy.Name, "took", x, "DMG!", enemy.Name, "has", enemyhplist[1], "HP!") 
                def BossMoves(dmg, name):
                    hp=hplist[0]-dmg
                    hplist.append(hp)
                    hplist.remove(hplist[0])
                    print(enemy.Name, "used", name, "!", stuff.Hero.name, "has", hp, "HP!")
            #All Moves
            class playermoves(moves):
                def __init__(self, damage):
                    self.enemy=enemy
                    self.damage=damage
                def SwordAttack():
                    moves.PlayerAttack(round(Decimal(25)*Decimal(stuff.Hero.damagemultiplier)), "Sword Attack")
                SwordAttack()
                def MaceSwing():
                    moves.PlayerAttack(round(Decimal(30)*Decimal(stuff.Hero.damagemultiplier)), "Mace Swing")
                MaceSwing()
                def ShieldBash():
                    moves.PlayerAttack(round(Decimal(30)*Decimal(stuff.Hero.damagemultiplier)), "Shield Bash")
                ShieldBash()
                def MeteorShower():
                    moves.PlayerAttack(round(Decimal(20)*Decimal(stuff.Hero.damagemultiplier)), "Meteor Shower")
                MeteorShower()
                def Thunderbolt():
                    moves.PlayerAttack(round(Decimal(25)*Decimal(stuff.Hero.damagemultiplier)), "Thunderbolt")
                Thunderbolt()
                def StaffStab():
                    moves.PlayerAttack(round(Decimal(15)*Decimal(stuff.Hero.damagemultiplier)), "Staff Stab")
                StaffStab()
                def NormalArrow():
                    moves.PlayerAttack(round(Decimal(20)*Decimal(stuff.Hero.damagemultiplier)), "Normal Arrow")
                NormalArrow()
                def SlingshotFire():
                    moves.PlayerAttack(round(Decimal(15)*Decimal(stuff.Hero.damagemultiplier)), "Slingshot Fire")
                SlingshotFire()
            class playereffectmoves(moves):
                def Shield():
                    if moves.EffectCheck("Shield")==True:
                        check=effects.shieldthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Shield!")
                    else:
                        return(False)
                def Block():
                    if moves.EffectCheck("Block")==True:
                        check=effects.blockthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Block!")
                    else:
                        return(False)
                def Ice_Shard():
                    moves.PlayerAttack(round(Decimal(25)*Decimal(stuff.Hero.damagemultiplier)), "Ice Shard")
                    if moves.EffectCheck("Ice Shard")==True:
                        check=effects.freeze()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Freeze!")
                    else:
                        return(False)
                def Protection_Spell():
                    if moves.EffectCheck("Protection Spell")==True:
                        check=effects.protectionthingy()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Protect!")
                    else:
                        return(False)
                def Summon():
                    if moves.EffectCheck("Summon")==True:
                        return(True)
                    else:
                        return(False)
                def Fireball():
                    moves.PlayerAttack(round(Decimal(30)*Decimal(stuff.Hero.damagemultiplier)), "Fireball")
                    if moves.EffectCheck("Fireball")==True:
                        check=effects.burning()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Burn!")
                    else:
                        return(False)
                def Heal(x, y):
                    if moves.EffectCheck("Heal")==True:
                        x=effects.heal(x, y)
                        hplist.append(x)
                        hplist.remove(hplist[0])
                        print(stuff.Hero.name, "Healed for", y, "HP!", stuff.Hero.name, "has", x, "HP!")
                Heal(hplist[0], round(Decimal(15)*Decimal(stuff.Hero.hpmultiplier)))
                def FireArrow():
                    moves.PlayerAttack(round(Decimal(20)*Decimal(stuff.Hero.damagemultiplier)), "Fire Arrow")
                    if moves.EffectCheck("Fire Arrow")==True:
                        check=effects.burning()
                        if check == True:
                            return(True)
                        else:
                            print("Failed to Burn!")
                    else:
                        return(False)
                def Ice_Arrow():
                    moves.PlayerAttack(round(Decimal(20)*Decimal(stuff.Hero.damagemultiplier)), "Ice Arrow")
                    if moves.EffectCheck("Ice Arrow")==True:
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
            if not enemy.Num==6 and not enemy.Num==8 and not enemy.Num==10:
                if enemyhplist[1]<0:
                    break
            def enemy_attack_check():
                e=playereffectmoves
                if e.shield==True:
                    print(enemy.Name, "'s Attack was Shielded!")
                    return(False)
                elif e.blocked==True:
                    print(enemy.Name, "'s Attack was Blocked!")
                    return(False)
                elif e.freeze==True:
                    print(enemy.Name, "is Frozen!")
                    return(False)
                elif e.protect==True:
                    print(enemy.Name, "'s Attack was Protected!")
                    return(False)
                else:
                    return(True)
            #basic-enemy
            if enemy.Num<4:
                moves.basicattack()
            #bosses
            class bossmoves(moves):
                def GolemSlam():
                    moves.BossMoves(55, "Golem Slam")
                def BoulderThrow():
                    moves.BossMoves(45, "Boulder Throw")
                def GolemPunch():
                    moves.BossMoves(50, "Golem Punch")
                def Roll():
                    moves.BossMoves(40, "Roll") 
                def Poisoning():
                    moves.BossMoves(0, "Poisoning")
                def DeathSpell():
                    moves.BossMoves(60, "Death Spell")
                def FireBreath():
                    moves.BossMoves(50, "Fire Breath")
                def ClawSlash():
                    moves.BossMoves(45, "Claw Slash")
                def TailSwing():
                    moves.BossMoves(40, "Tail Swing")
                def Fly():
                    moves.BossMoves(35, "Fly")
                def BlueFireBreath():
                    moves.BossMoves(60, "Blue Fire Breath")
                def Bite():
                    moves.BossMoves(50, "Bite")
                def Slam():
                    moves.BossMoves(55, "Slam")
                def SwordAttack():
                    moves.BossMoves(50, "Sword Attack")
                def SwordSlam():
                    moves.BossMoves(55, "Sword Slam")
                def CrownThrow():
                    moves.BossMoves(45, "Crown Throw")
                def SwordSlash():
                    moves.BossMoves(60, "Sword Slash")
                def JewelBash():
                    moves.BossMoves(70, "Jewel Bash")
                def KingSlam():
                    moves.BossMoves(65, "King Slam")
                def HydraBlast():
                    moves.BossMoves(65, "Hydra Blast")
                def TripleAttack():
                    moves.BossMoves(60, "Triple Attack")
                def HydraBite():
                    moves.BossMoves(50, "Hydra Bite")
                def HydraBeam():
                    moves.BossMoves(85, "Hydra Beam")
                def SkullFire():
                    moves.BossMoves(80, "Skull Fire")
                def PoisonFire():
                    moves.BossMoves(50, "Poison Fire")
                def FinalBlast():
                    moves.BossMoves(100, "Final Blast")
                def Regenerate():
                    if enemyhplist[1]+enemyhplist[0]//3>829:
                        enemyhplist.append(829)
                        enemyhplist.remove(enemyhplist[0])
                    else:
                        enemyhplist.append(effects.heal(enemyhplist[1], enemyhplist[0]//3))
                        enemyhplist.remove(enemyhplist[0])
                    print(enemy.Name, "used regenerate and healed", enemyhplist[0]-enemyhplist[1], "HP!")
                    enemyhplist.remove(enemyhplist[0])
                def OneHeadAttack():
                    moves.BossMoves(120, "One Head Attack")
                def LastEffort():
                    moves.BossMoves(150, "Last Effort")
            #boss-phase-hp-check
            if enemy.Num==6 or enemy.Num==8 and phase==1:
                if enemyhplist[1]<0:
                    break
            if enemy.Num==10 and phase==2:
                if enemyhplist[1]<0:
                    bossmoves.LastEffort() #uses last effort when going to die
                    break
            #Mini/Final-Boss-Move-Selection
            b=bossmoves
            global Poison
            if enemy.Num==4:
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
            if enemy.Num==5:
                moveint=random.randint(1,2)
                if enemy_attack_check()==True:
                    if moveint==1:
                        b.Poisoning()
                        Poison=True
                    if moveint==2:
                        b.DeathSpell()
                        Poison=False
                else:
                    Poison=False
            if enemy.Num==6:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(947)
                    enemyhplist.append(947)
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
            if enemy.Num==8:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(552)
                    enemyhplist.append(552)
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
            if enemy.Num==10:
                if enemyhplist[1]<0 and phase==0:
                    enemyhplist.append(623)
                    enemyhplist.append(623)
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("First Head was Killed! Hydra is in Phase 2!")
                    phase=phase+1
                if enemyhplist[1]<0 and phase==1:
                    enemyhplist.append(829)
                    enemyhplist.append(829)
                    enemyhplist.remove(enemyhplist[0])
                    enemyhplist.remove(enemyhplist[1])
                    print("Second Head was Killed! Hydra is in Phase 3!")
                    phase=phase+1
                if phase==1:
                    moveint=random.randint(1,3)
                    Poison=False
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.HydraBeam()          
                        if moveint==2:
                            b.SkullFire()
                        if moveint==3:
                            b.HydraBite()
                elif phase==2:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            b.FinalBlast()
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
                    else:
                        Poison=False
            #Effect-Checking
            if playereffectmoves.Summon()==True or summon==1:
                summon=1
                if len(enemyhplist)==1:
                    enemyhplist.append(enemyhplist[0])
                    hp=enemyhplist[1]
                else:
                    enemyhplist.remove(enemyhplist[0])
                    hp=enemyhplist[0]
                nhp=hp-round(Decimal(30)*Decimal(stuff.Hero.damagemultiplier))
                enemyhplist.append(nhp)
                if len(enemyhplist)>2:
                    enemyhplist.remove(enemyhplist[0])
                print("Zombies attacked", enemy.Name, "!", enemy.Name, "took", round(Decimal(30)*Decimal(stuff.Hero.damagemultiplier)), "DMG!", enemy.Name, "has", enemyhplist[1], "HP!")
            if y=="Fireball" or "Fire Arrow":
                if playereffectmoves.burn==True and burner==0:
                    burner=burner+3
            if enemy.Num==10 or enemy.Num==5:
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
                print(stuff.Hero.name, "is Poisoned!", stuff.Hero.name, "has", nhp, "HP!")
        if hplist[0]<0:
            print(stuff.Hero.name, 'Lost the Battle!')
            return(False)
        if enemyhplist[1]<0:
            print(stuff.Hero.name, 'Won the Battle!')
            return(True)
battle.fight(stuff.Hydra)