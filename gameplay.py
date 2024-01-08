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
    y=input("This is the menu. Would you like to Equip/Unequip (enter 'Equip') or view player info (enter 'Info')? (Enter to break) ")
    x=True
    while x==True:
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
        player['Level:']=playerlevel    
        player['DmgMultiplier:']=multiplier_calc(1, playerlevel)
        player['HpMultiplier:']=multiplier_calc(1, playerlevel)
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string) 
        os.remove("player.json")
        os.rename(new_file, "player.json") 
def wave_1():
    print("Wave 1 started!")
    ultbattle(stuff.goblin)
    menu()
    ultbattle(stuff.spider)
    menu()
    ultbattle(stuff.slime)
    menu()
    ultbattle(stuff.zombie)
    menu()
    print("(This is a merchant. You can sell sellable items here or buy from the merchants catalog.)")
    ultmerchant.buyingselling([stuff.LeatherBoots, stuff.LeatherHelmet, stuff.Mace])
def wave_2():
    if wave_1()==True:
        print("Wave 2 started!")
        ultbattle(stuff.zombie)
        menu()
def wave_3():
    if wave_2()==True:
        print("Wave 3 started!")
def wave_4():
    if wave_3()==True:
        print("Wave 4 started!")
def wave_5():
    if wave_4()==True:
        print("Wave 5 started!")
def final_wave():
    if wave_5()==True:
        print("Final wave started!")