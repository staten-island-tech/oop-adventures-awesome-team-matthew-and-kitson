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
            player['Inventory:'].append(y)
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string) 
        os.remove("player.json")
        os.rename(new_file, "player.json") 
    def menu():
        x=True
        while x==True:
            y=input("This is the menu. Would you like to Equip/Unequip (enter 'Equip') or view player info (enter 'Info')? (Enter to break) ")
            if y=='Equip':
                ultequip()
            elif y=='Info':
                print("Name:", player['PName:'], "Class:", player['Class:'], "BaseHP:", player['BaseHp'], "Weapons:", player['Weapon1'], player['Weapon2'], "Moves:", player['Moves:'], "Gold:", player['Gold:'], "HP Multiplier:", player['HpMultiplier:'], "Damage Multiplier", player['DmgMultiplier:'], "Inventory: ", player['Inventory:'], "Armor:", player['Helmet:'], player['Chestplate:'], player['Leggings:'], player['Boots:'], "Level:", player['Level:'], "EXP:", player['EXP:'])
            else:
                x=False
    def ultbattle(x):
        if battle.fight(x)==True:
            playerlevel=player['Level:']
            player['EXP:']=player['EXP:']+x.EXP
            if player['EXP:']>calculator(player['Level:']):
                playerlevel=player['Level:']+1
                player['EXP:']=0
            print(player['PName:'], "got", x.Gold, "Gold!", "\n", player['PName:'], "got", x.EXP, "EXP!")
            if not player['Level:']==playerlevel:
                print(player['PName:'], "is Level", playerlevel, "!")
            thing=player['Gold:'][0]+x.Gold
            player['Gold:'].append(thing)
            player['Gold:'].remove(player['Gold:'][0])
            player['Level:']=playerlevel    
            player['DmgMultiplier:']=multiplier_calc(1, playerlevel)
            player['HpMultiplier:']=multiplier_calc(1, playerlevel)
            new_file = "updated.json"
            with open(new_file, "w") as pjson:
                json_string = json.dumps(data, indent=4)
                pjson.write(json_string) 
            os.remove("player.json")
            os.rename(new_file, "player.json")
            return True
        else:
            return False
    def loss():
        print("You have lost. You need to restart this wave.")
        return(False)
wave1=[stuff.goblin, stuff.spider, stuff.slime, stuff.zombie]
wave2=[]
wave3=[]
wave4=[]
wave5=[]
wave6=[]
itemlst1=[]
itemlst2=[]
itemlst3=[]
itemlst4=[]
itemlst5=[]
itemlst6=[]
def wavefunc(y, x):
    if bool(gameplay.ultbattle(y[0]))==True:
        gameplay.menu()
        if bool(gameplay.ultbattle(y[1]))==True:
            gameplay.menu()
            if bool(gameplay.ultbattle(y[2]))==True:
                gameplay.menu()
                if bool(gameplay.ultbattle(y[3]))==True:
                    gameplay.menu()
                    print("(This is a merchant. You can sell sellable items here or buy from the merchants catalog.)")
                    ultmerchant.buyingselling(x)
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
def singlewavereplay(x, y):
    if x==False:
        bq=input("What battle # would you like to replay? (1-4)")
        if bq==1:
            gameplay.ultbattle(y[0])
        if bq==2:
            gameplay.ultbattle(y[1])
        if bq==3:
            gameplay.ultbattle(y[2])
        if bq==4:
            gameplay.ultbattle(y[3])
def replay(w1, w2, w3, w4, w5, w6):
    waveq=input("Which wave would you like to replay a battle from?")
    if waveq=="Wave1":
        singlewavereplay(w1, wave1)
    if waveq=="Wave2":
        singlewavereplay(w2, wave2)
    if waveq=="Wave3":
        singlewavereplay(w3, wave3)
    if waveq=="Wave4":
        singlewavereplay(w4, wave4)
    if waveq=="Wave5":
        singlewavereplay(w5, wave5)
    if waveq=="Wave6":
        singlewavereplay(w6, wave6)
    else:
        print("Not a valid wave.")
def final_wave():
    x=True
    WaveCheck1=False
    WaveCheck2=False
    WaveCheck3=False
    WaveCheck4=False
    WaveCheck5=False
    WaveCheck6=False
    while x==True:
        if wavefunc(wave1, itemlst1)==True:
            print('Wave 1 Completed!')
            if wavefunc(wave2, itemlst2)==True:
                print('Wave 2 Completed!')
                if wavefunc(wave3, itemlst3)==True:
                    print('Wave 3 Completed!')
                    if wavefunc(wave4, itemlst4)==True:
                        print('Wave 4 Completed!')
                        if wavefunc(wave5, itemlst5)==True:
                            print('Wave 5 Completed! Final Wave!')
                            if wavefunc(wave6, itemlst6)==True:
                                print('Final Wave Completed!')
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
    x=True
final_wave()