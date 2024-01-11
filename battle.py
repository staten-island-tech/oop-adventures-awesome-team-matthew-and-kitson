import stuff
import random
from moves import pmoves
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
            pmoves.PlayerAttack(y, enemyhplist, enemy)
            pmoves.Heal(y, hplist[0], round(float(20)*float(stuff.Hero.hpmultiplier)), hplist)
            shield=pmoves.Shield(y)
            blocked=pmoves.Block(y)
            freeze=pmoves.Ice_Shard(y) or pmoves.Ice_Arrow(y)
            protect=pmoves.Protection_Spell(y)
            summmoning=pmoves.Summon(y)
            if y=="Fireball" or "Fire Arrow":
                burn=pmoves.Fireball(y) or pmoves.FireArrow(y)
            if not enemy.Num==6 and not enemy.Num==8 and not enemy.Num==10:
                if enemyhplist[1]<=0:
                    break
            def enemy_attack_check():
                if shield==True:
                    print(enemy.Name, "'s Attack was Shielded!")
                    return(False)
                elif blocked==True:
                    print(enemy.Name, "'s Attack was Blocked!")
                    return(False)
                elif freeze==True:
                    print(enemy.Name, "is Frozen!")
                    return(False)
                elif protect==True:
                    print(enemy.Name, "'s Attack was Protected!")
                    return(False)
                else:
                    return(True)
            if enemy.Num<4:
                if enemy_attack_check()==True:
                    pmoves.basicattack(hplist, enemy)
            if enemy.Num==6 or enemy.Num==8 and phase==1:
                if enemyhplist[1]<0:
                    break
            if enemy.Num==10 and phase==2:
                if enemyhplist[1]<0:
                    pmoves.BossMoves("Last Effort", hplist)
                    break
            global Poison
            if enemy.Num==4:
                moveint=random.randint(1,4)
                if enemy_attack_check()==True:
                    if moveint==1:
                        pmoves.BossMoves("Golem Slam", hplist)
                    if moveint==2:
                        pmoves.BossMoves("Boulder Throw", hplist)
                    if moveint==3:
                        pmoves.BossMoves("Golem Punch", hplist)
                    if moveint==4:
                        pmoves.BossMoves("Roll", hplist)
            if enemy.Num==5:
                moveint=random.randint(1,2)
                if enemy_attack_check()==True:
                    if moveint==1:
                        pmoves.BossMoves("Poisoning", hplist)
                        Poison=True
                    if moveint==2:
                        pmoves.BossMoves("Death Spell", hplist)
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
                            pmoves.BossMoves("Blue Fire Breath", hplist)
                        if moveint==2:
                            pmoves.BossMoves("Bite", hplist)
                        if moveint==3:
                            pmoves.BossMoves("Slam", hplist)
                else:
                    moveint=random.randint(1,4)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            pmoves.BossMoves("Fire Breath", hplist)
                        if moveint==2:
                            pmoves.BossMoves("Claw Slash", hplist)
                        if moveint==3:
                            pmoves.BossMoves("Tail Swing", hplist)
                        if moveint==4:
                            pmoves.BossMoves("Fly", hplist)
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
                            pmoves.BossMoves("Sword Slash", hplist)
                        if moveint==2:
                            pmoves.BossMoves("Jewel Bash", hplist)
                        if moveint==3:
                            pmoves.BossMoves("King Slam", hplist)
                else:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            pmoves.BossMoves("Sword Attack", hplist)
                        if moveint==2:
                            pmoves.BossMoves("Sword Slam", hplist)
                        if moveint==3:
                            pmoves.BossMoves("Crown Throw", hplist)
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
                            pmoves.BossMoves("Hydra Beam", hplist)        
                        if moveint==2:
                            pmoves.BossMoves("Skull Fire", hplist)
                        if moveint==3:
                            pmoves.BossMoves("Hydra Bite", hplist)
                elif phase==2:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            pmoves.BossMoves("Final Blast", hplist)
                            Poison=False                        
                        if moveint==2:
                            pmoves.Regenerate(enemyhplist, enemy)
                            Poison=False
                        if moveint==3:
                            pmoves.BossMoves("One Head Attack", hplist)
                            Poison=False
                else:
                    moveint=random.randint(1,3)
                    if enemy_attack_check()==True:
                        if moveint==1:
                            pmoves.BossMoves("Hydra Blast", hplist)
                            Poison=False
                        if moveint==2:
                            pmoves.BossMoves("Triple Attack", hplist)
                            Poison=False
                        if moveint==3:
                            pmoves.BossMoves("Poison Fire", hplist)
                            Poison=True
                    else:
                        Poison=False
            if summmoning==True or summon>0:
                summon+1
                if len(enemyhplist)==1:
                    enemyhplist.append(enemyhplist[0])
                    hp=enemyhplist[1]
                else:
                    enemyhplist.remove(enemyhplist[0])
                    hp=enemyhplist[0]
                nhp=hp-round(float(30)*float(stuff.Hero.damagemultiplier))
                enemyhplist.append(nhp)
                if len(enemyhplist)>2:
                    enemyhplist.remove(enemyhplist[0])
                print("Zombies attacked", enemy.Name, "!", enemy.Name, "took", round(float(30)*float(stuff.Hero.damagemultiplier)), "DMG!", enemy.Name, "has", enemyhplist[1], "HP!")
            if y=="Fireball" or "Fire Arrow":
                if burn==True and burner==0:
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
            return False
        if enemyhplist[1]<=0:
            print(stuff.Hero.name, 'Won the Battle!')
            return True