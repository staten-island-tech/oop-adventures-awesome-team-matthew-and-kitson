import json
import os
import stuff
import random
from ultequip import ultequip
from battle import battle
from ultimatemerchant import ultmerchant
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
class gameplay():
    def calculator(x):
        return(round((x*1.1)*3))
    def multiplier_calc(x, y):
        z=y-x
        returner=1+(z*.1)
        return(returner)
    def item_dropper(x,y):
        z=random.randint(0, x)
        if z==0:
            print("Item dropped from enemy: ", y.Name)
            player['Inventory:'].append(y.Name)
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string) 
        os.remove("player.json")
        os.rename(new_file, "player.json")
    wave1=[stuff.goblin, stuff.spider, stuff.slime, stuff.zombie]
    wave2=[stuff.zombie, stuff.slime, stuff.zombie, stuff.Lich]
    wave3=[stuff.goblin, stuff.spider, stuff.spider, stuff.Golem]
    wave4=[stuff.spider, stuff.spider, stuff.zombie, stuff.Dragon]
    wave5=[stuff.spider, stuff.slime, stuff.slime, stuff.King]
    wave6=[stuff.zombie, stuff.zombie, stuff.zombie, stuff.Hydra]
    itemlst1=[stuff.LeatherBoots, stuff.Mace, stuff.ConeHat]
    itemlst2=[stuff.Slingshot, stuff.Trousers, stuff.HeavyBoots]
    itemlst3=[stuff.LeatherLeggings, stuff.LeatherHelmet, stuff.LeatherChestplate]
    itemlst4=[stuff.MagicRobe, stuff.Healer_Staff, stuff.Necromancer_Staff]
    itemlst5=[stuff.Sword, stuff.Shield, stuff.Bow]
    itemlst6=[stuff.PlateChest, stuff.PlateBoots, stuff.PlateHelmet, stuff.PlateLeggings, stuff.Staff, stuff.Magic_Book]
    WaveCheck1=False
    WaveCheck2=False
    WaveCheck3=False
    WaveCheck4=False
    WaveCheck5=False
    WaveCheck6=False
    def singlewavereplay(x, y, z):
        if x==True:
            bq=input("What battle # would you like to replay? (1-4, enter 'Merchant' to buy from the merchant from said Wave.) ")
            if bq=="1":
                gameplay.ultbattle(y[0])
            if bq=="2":
                gameplay.ultbattle(y[1])
            if bq=="3":
                gameplay.ultbattle(y[2])
            if bq=="4":
                gameplay.ultbattle(y[3])
            if bq=='Merchant':
                ultmerchant.buyingselling(z)
    def replay():
        waveq=input("Which wave would you like to replay a battle from? ")
        if waveq=="Wave 1":
            gameplay.singlewavereplay(gameplay.WaveCheck1, gameplay.wave1, gameplay.itemlst1)
        if waveq=="Wave 2":
            gameplay.singlewavereplay(gameplay.WaveCheck2, gameplay.wave2, gameplay.itemlst2)
        if waveq=="Wave 3":
            gameplay.singlewavereplay(gameplay.WaveCheck3, gameplay.wave3, gameplay.itemlst3)
        if waveq=="Wave 4":
            gameplay.singlewavereplay(gameplay.WaveCheck4, gameplay.wave4, gameplay.itemlst4)
        if waveq=="Wave 5":
            gameplay.singlewavereplay(gameplay.WaveCheck5, gameplay.wave5, gameplay.itemlst5)
        if waveq=="Wave 6":
            gameplay.singlewavereplay(gameplay.WaveCheck6, gameplay.wave6, gameplay.itemlst6)
        else:
            print("Not a valid wave or not completed.") 
    def menu():
        x=True
        while x==True:
            y=input("This is the menu. Would you like to Equip/Unequip (enter 'Equip') or view player info (enter 'Info')? You can also replay battles from waves you have cleared to increase your level! (Enter 'Replay')(Enter to break) ")
            if y=='Equip':
                ultequip()
            elif y=='Info':
                with open("player.json", "r") as pjson:
                    data = json.load(pjson)
                    player=data[8]
                print("Name:", player['PName:'], "Class:", player['Class:'], "BaseHP:", player['BaseHP:'], "Weapons:", player['Weapon1:'], player['Weapon2:'], "Moves:", player['Moves:'], "Gold:", player['Gold:'], "HP Multiplier:", player['HpMultiplier:'], "Damage Multiplier", player['DmgMultiplier:'], "Inventory: ", player['Inventory:'], "Armor:", player['Helmet:'], player['Chestplate:'], player['Leggings:'], player['Boots:'], "Level:", player['Level:'], "EXP:", player['EXP:'])
            elif y=='Replay':
                gameplay.replay()
            else:
                x=False
    def ultbattle(x):
        if battle.fight(x)==True:
            if x.Num==0:
                gameplay.item_dropper(10, stuff.Trinket)
            if x.Num==1:
                gameplay.item_dropper(5, stuff.Trinket)
            if x.Num==2:
                gameplay.item_dropper(4, stuff.Trinket)
            if x.Num==3:
                gameplay.item_dropper(3, stuff.Trinket)
            if x.Num==4:
                gameplay.item_dropper(1, stuff.Trinket)
                gameplay.item_dropper(5, stuff.Ruby)
            if x.Num==5:
                gameplay.item_dropper(1, stuff.Trinket)
                gameplay.item_dropper(2, stuff.Silver_Band)
            if x.Num==6:
                gameplay.item_dropper(2, stuff.Silver_Band)
                gameplay.item_dropper(2, stuff.Silver_Bangle)
                gameplay.item_dropper(2, stuff.Silver_Band)
            if x.Num==8:
                gameplay.item_dropper(2, stuff.Gold_Ring)
                gameplay.item_dropper(2, stuff.Gold_Bangle)
                gameplay.item_dropper(2, stuff.Gold_Necklace)
                gameplay.item_dropper(2, stuff.Gold_Band)
                gameplay.item_dropper(2, stuff.Gold_Goblet)
            if x.Num==10:
                gameplay.item_dropper(1, stuff.Diamond)
                gameplay.item_dropper(1, stuff.Ruby)
            playerlevel=player['Level:']
            player['EXP:']=player['EXP:']+x.EXP
            if player['EXP:']>gameplay.calculator(player['Level:']):
                playerlevel=player['Level:']+1
                player['EXP:']=0
            print(player['PName:'], "got", x.Gold, "Gold!", "\n", player['PName:'], "got", x.EXP, "EXP!")
            if not player['Level:']==playerlevel:
                print(player['PName:'], "is Level", playerlevel, "!")
            thing=player['Gold:'][0]+x.Gold
            player['Gold:'].append(thing)
            player['Gold:'].remove(player['Gold:'][0])
            player['Level:']=playerlevel    
            player['DmgMultiplier:']=gameplay.multiplier_calc(1, playerlevel)
            player['HpMultiplier:']=gameplay.multiplier_calc(1, playerlevel)
            new_file = "updated.json"
            with open(new_file, "w") as pjson:
                json_string = json.dumps(data, indent=4)
                pjson.write(json_string) 
            os.remove("player.json")
            os.rename(new_file, "player.json")
            return True
        else:
            return False
    def wavefunc(y, x):
        if bool(gameplay.ultbattle(y[0]))==True:
            gameplay.menu()
            if bool(gameplay.ultbattle(y[1]))==True:
                gameplay.menu()
                if bool(gameplay.ultbattle(y[2]))==True:
                    gameplay.menu()
                    print("(This is a merchant. You can sell sellable items here or buy from the merchants catalog.)")
                    ultmerchant.buyingselling(x)
                    gameplay.menu()
                    if bool(gameplay.ultbattle(y[3]))==True:
                        gameplay.menu()
                        return(True)
                    else:
                        return(gameplay.loss())
                else:
                    return(gameplay.loss())
            else:
                return(gameplay.loss())
        else:
            return(gameplay.loss())
    def loss():
        print("You have lost. You need to restart all battles.")
        return(False)
def final_wave():
    x=True
    while x==True:
        if gameplay.wavefunc(gameplay.wave1, gameplay.itemlst1)==True:
            print('Wave 1 Completed!')
            gameplay.WaveCheck1=True
            if gameplay.wavefunc(gameplay.wave2, gameplay.itemlst2)==True:
                print('Wave 2 Completed!')
                gameplay.WaveCheck2=True
                if gameplay.wavefunc(gameplay.wave3, gameplay.itemlst3)==True:
                    print('Wave 3 Completed!')
                    gameplay.WaveCheck3=True
                    if gameplay.wavefunc(gameplay.wave4, gameplay.itemlst4)==True:
                        gameplay.WaveCheck4=True
                        if gameplay.wavefunc(gameplay.wave5, gameplay.itemlst5)==True:
                            gameplay.WaveCheck5=True
                            if gameplay.wavefunc(gameplay.wave6, gameplay.itemlst6)==True:
                                gameplay.WaveCheck6=True
                                return(True)
                            else:
                                x=False
                        else:
                            x=False
                    else:
                        x=False
                else:
                    x=False
            else:
                x=False
        else:
            x=False