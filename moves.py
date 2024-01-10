import stuff
from moveeffects import effects
class pmoves():
    def basicattack(x,y):
        hp=x[0]
        hp=hp-y.DMG
        x.append(hp)
        x.remove(x[0])
        print(y.Name, "attacked!", stuff.Hero.name, "has", hp, "HP!")      
    def BossMoves(x, y):
        moveslist=[stuff.GolemSlam, stuff.BoulderThrow, stuff.GolemPunch, stuff.Roll, stuff.Poisoning, stuff.DeathSpell, stuff.FireBreath, stuff.ClawSlash, stuff.TailSwing, stuff.Fly, stuff.BlueFireBreath, stuff.Bite, stuff.Slam, stuff.SwordAttackBoss, stuff.SwordSlam, stuff.CrownThrow, stuff.SwordSlash, stuff.JewelBash, stuff.KingSlam, stuff.HydraBlast, stuff.TripleAttack, stuff.HydraBite, stuff.HydraBeam, stuff.SkullFire, stuff.PoisonFire, stuff.FinalBlast, stuff.Regenerate, stuff.OneHeadAttack, stuff.LastEffort]
        for i in range(len(moveslist)):
            if x==moveslist[i]:
                move=moveslist[i]
                name=move.name
                dmg=move.damage
                hp=x[0]-dmg
                y.append(hp)
                y.remove(y[0])
                print(move.name, "used", name, "!", stuff.Hero.name, "has", hp, "HP!")
    def basicattack(x, y):
        hp=x[0]
        hp=hp-y.DMG
        x.append(hp)
        x.remove(x[0])
        print(y.Name, "attacked!", stuff.Hero.name, "has", hp, "HP!")     
    def EffectCheck(y, w):
        if y==w:
            if y in stuff.Hero.moves:
                return(True)
            else:
                return(False)
        else:
            return(False)       
    def PlayerAttack(y, w, z):
        moveslist=[stuff.SwordAttack, stuff.MaceSwing, stuff.ShieldBash, stuff.MeteorShower, stuff.IceShard, stuff.Fireball, stuff.Thunderbolt, stuff.StaffStab, stuff.NormalArrow, stuff.FireArrow, stuff.IceArrow, stuff.SlingshotFire]
        for i in range(len(moveslist)):
            if y==moveslist[i].name:
                damage=moveslist[i].damage
                if y in stuff.Hero.moves:
                    if len(w)==1:
                        w.append(w[0])
                        hp=w[1]
                    else:
                        w.remove(w[0])
                        hp=w[0]
                    nhp=hp-damage 
                    w.append(nhp)
                    if len(w)>2:
                        w.remove(w[0])
                    print(z.Name, "took", damage, "DMG!", z.Name, "has", w[1], "HP!") 
    def Regenerate(x, y):
        if x[1]+x[0]//3>829:
            x.append(829)
            x.remove(x[0])
        else:
            x.append(effects.heal(x[1], x[0]//3))
            x.remove(x[0])
        print(y.Name, "used regenerate and healed", x[0]-x[1], "HP!")
    def Shield(s):
        if pmoves.EffectCheck(s, "Shield")==True:
            check=effects.shieldthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Shield!")
                return(False)
        else:
            return(False)
    def Block(s):
        if pmoves.EffectCheck(s, "Block")==True:
            check=effects.blockthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Block!")
                return(False)
        else:
            return(False)
    def Ice_Shard(s):
        if pmoves.EffectCheck(s, "Ice Shard")==True:
            check=effects.freeze()
            if check == True:
                return(True)
            else:
                print("Failed to Freeze!")
                return(False)
        else:
            return(False)
    def Protection_Spell(s):
        if pmoves.EffectCheck(s, "Protection Spell")==True:
            check=effects.protectionthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Protect!")
                return(False)
        else:
            return(False)
    def Summon(s):
        if pmoves.EffectCheck(s, "Summon")==True:
            return(True)
        else:
            return(False)
    def Fireball(s):
        if pmoves.EffectCheck(s, "Fireball")==True:
            check=effects.burning()
            if check == True:
                return(True)
            else:
                print("Failed to Burn!")
                return(False)
        else:
            return(False)
    def Heal(s, x, y, z):
        if pmoves.EffectCheck(s, "Heal")==True:
            healing=effects.heal(x, y)
            z.append(healing)
            z.remove(z[0])
            print(stuff.Hero.name, "healed for", y, "HP!", stuff.Hero.name, "has", x, "HP!")
    def FireArrow(s):
        if pmoves.EffectCheck(s, "Fire Arrow")==True:
            check=effects.burning()
            if check == True:
                return(True)
            else:
                print("Failed to Burn!")
                return(False)
        else:
            return(False)
    def Ice_Arrow(s):
        if pmoves.EffectCheck(s, "Ice Arrow")==True:
            check=effects.freeze()
            if check == True:
                return(True)
            else:
                print("Failed to Freeze!")
                return(False)
        else:
            return(False)