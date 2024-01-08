import stuff
from moveeffects import effects
class moves():
    def EffectCheck(y, w):
        if y==w:
            if y in stuff.Hero.moves:
                return(True)
            else:
                return(False)
        else:
            return(False)       
    def PlayerAttack(y, x, w, z):
        moveslist=[stuff.SwordAttack, stuff.MaceSwing, stuff.ShieldBash, stuff.MeteorShower, stuff.IceShard, stuff.Fireball, stuff.Thunderbolt, stuff.StaffStab, stuff.NormalArrow, stuff.FireArrow, stuff.IceArrow, stuff.SlingshotFire]
        for i in range(len(moveslist)):
            if y==moveslist[i].Name:
                if y in stuff.Hero.moves:
                    if len(w)==1:
                        w.append(w[0])
                        hp=w[1]
                    else:
                        w.remove(w[0])
                        hp=w[0]
                    nhp=hp-x 
                    w.append(nhp)
                    if len(w)>2:
                        w.remove(w[0])
                    print(z.Name, "took", x, "DMG!", z.Name, "has", w[1], "HP!") 
    def Shield():
        if moves.EffectCheck("Shield")==True:
            check=effects.shieldthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Shield!")
                return(False)
        else:
            return(False)
    def Block():
        if moves.EffectCheck("Block")==True:
            check=effects.blockthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Block!")
                return(False)
        else:
            return(False)
    def Ice_Shard():
        if moves.EffectCheck("Ice Shard")==True:
            check=effects.freeze()
            if check == True:
                return(True)
            else:
                print("Failed to Freeze!")
                return(False)
        else:
            return(False)
    def Protection_Spell():
        if moves.EffectCheck("Protection Spell")==True:
            check=effects.protectionthingy()
            if check == True:
                return(True)
            else:
                print("Failed to Protect!")
                return(False)
        else:
            return(False)
    def Summon():
        if moves.EffectCheck("Summon")==True:
            return(True)
        else:
            return(False)
    def Fireball():
        if moves.EffectCheck("Fireball")==True:
            check=effects.burning()
            if check == True:
                return(True)
            else:
                print("Failed to Burn!")
                return(False)
        else:
            return(False)
    def Heal(x, y, z):
        if moves.EffectCheck("Heal")==True:
            x=effects.heal(x, y)
            z.append(x)
            z.remove(z[0])
            print(stuff.Hero.name, "Healed for", y, "HP!", stuff.Hero.name, "has", x, "HP!")
    def FireArrow():
        if moves.EffectCheck("Fire Arrow")==True:
            check=effects.burning()
            if check == True:
                return(True)
            else:
                print("Failed to Burn!")
                return(False)
        else:
            return(False)
    def Ice_Arrow():
        if moves.EffectCheck("Ice Arrow")==True:
            check=effects.freeze()
            if check == True:
                return(True)
            else:
                print("Failed to Freeze!")
                return(False)
        else:
            return(False)