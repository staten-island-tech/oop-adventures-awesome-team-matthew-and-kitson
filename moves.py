import stuff
import json
from moveeffects import effects
class pmoves():
    def basicattack(x,y):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        hp=x[0]
        hp=hp-y.DMG
        x.append(hp)
        x.remove(x[0])
        print(y.Name, "attacked!", Hero.name, "has", hp, "HP!")      
    def BossMoves(x, y):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        moveslist=[stuff.GolemSlam, stuff.BoulderThrow, stuff.GolemPunch, stuff.Roll, stuff.Poisoning, stuff.DeathSpell, stuff.FireBreath, stuff.ClawSlash, stuff.TailSwing, stuff.Fly, stuff.BlueFireBreath, stuff.Bite, stuff.Slam, stuff.SwordAttackBoss, stuff.SwordSlam, stuff.CrownThrow, stuff.SwordSlash, stuff.JewelBash, stuff.KingSlam, stuff.HydraBlast, stuff.TripleAttack, stuff.HydraBite, stuff.HydraBeam, stuff.SkullFire, stuff.PoisonFire, stuff.FinalBlast, stuff.Regenerate, stuff.OneHeadAttack, stuff.LastEffort]
        for i in range(len(moveslist)):
            if x==moveslist[i].name:
                move=moveslist[i]
                name=move.name
                dmg=move.damage
                hp=y[0]-dmg
                y.append(hp)
                y.remove(y[0])
                print(move.name, "used", name, "!", Hero.name, "has", hp, "HP!")
    def basicattack(x, y):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        hp=x[0]
        hp=hp-y.DMG
        x.append(hp)
        x.remove(x[0])
        print(y.Name, "attacked!", Hero.name, "has", hp, "HP!")     
    def EffectCheck(y, w):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        if y==w:
            if y in Hero.moves:
                return(True)
            else:
                return(False)
        else:
            return(False)       
    def PlayerAttack(y, w, z):
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        SwordAttack=stuff.moves("Sword Attack", Hero.calculate_damage(25))
        MaceSwing=stuff.moves("Mace Swing", Hero.calculate_damage(30))
        ShieldBash=stuff.moves("Shield Bash", Hero.calculate_damage(30))
        MeteorShower=stuff.moves("Meteor Shower", Hero.calculate_damage(20))
        IceShard=stuff.moves("Ice Shard", Hero.calculate_damage(25))
        Fireball=stuff.moves("Fireball", Hero.calculate_damage(30))
        Thunderbolt=stuff.moves("Thunderbolt", Hero.calculate_damage(25))
        StaffStab=stuff.moves("Staff Stab", Hero.calculate_damage(15))
        NormalArrow=stuff.moves("Normal Arrow", Hero.calculate_damage(20))
        FireArrow=stuff.moves("Fire Arrow", Hero.calculate_damage(20))
        IceArrow=stuff.moves("Ice Arrow", Hero.calculate_damage(20))
        SlingshotFire=stuff.moves("Slingshot Fire", Hero.calculate_damage(25))
        moveslist=[SwordAttack, MaceSwing, ShieldBash, MeteorShower, IceShard, Fireball, Thunderbolt, StaffStab, NormalArrow, FireArrow, IceArrow, SlingshotFire]
        for i in range(len(moveslist)):
            if y==moveslist[i].name:
                damage=moveslist[i].damage
                if y in Hero.moves:
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
        print(y.Name, "used regenerate and healed", x[1]-x[0], "HP!")
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
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        Hero=stuff.BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
        if pmoves.EffectCheck(s, "Heal")==True:
            healing=effects.heal(x, y)
            z.append(healing)
            z.remove(z[0])
            print(Hero.name, "healed for", y, "HP!", Hero.name, "has", x, "HP!")
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