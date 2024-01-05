import json
import os
import stuff
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

def wave_2():
    if wave_1()==True:

def wave_3():
    if wave_2()==True:

def wave_4():
    if wave_3()==True:
        
def wave_5():
    if wave_4()==True:
        
def final_wave():
    if wave_5()==True:
        
ultbattle(stuff.goblin)