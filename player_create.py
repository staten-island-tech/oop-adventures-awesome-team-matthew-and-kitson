import json
import os
abv=0
PName=input("What is the player's name? ")
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    class Player:
        def Create(self, i):
            PlayerName=PName
            HP=data[i]['Hp']
            Weapon1=data[i]['Weapon1']
            Moves1=data[i]['Moves1']
            if "Weapon 2" in data[i]:
                Weapon2=data[i]['Weapon2']
                Moves2=data[i]['Moves2']
                PValues={'PName:':PlayerName,'HP:':HP,'Weapon1:':Weapon1,'Moves1:':Moves1,'Weapon2:':Weapon2, 'Moves2':Moves2}
            else:
                PValues={'PName:':PlayerName,'HP:':HP,'Weapon1:':Weapon1,'Moves1:':Moves1}
            return(PValues)

Mainq=input("Which player type do you want to be; Warrior, Magical, or Archer?")
class Warrior(Player):
    if Mainq=="Warrior":
        Wq=input("Do you want to be a Knight or Tank?")
        if Wq=="Knight":
            abv+0
        elif Wq=="Tank":
            abv+1
        else:
            print("Error")

class Magical(Player):
    if Mainq=="Magical":
        Mq=input("Do you want to be a Mage, Necromancer, Spellcaster, or Healer?")
        if Mq=="Mage":
            abv+2
        elif Mq=="Necromancer":
            abv+3
        elif Mq=="Spellcaster":
            abv+4
        elif Mq=="Healer":
            abv+5
        else:
            print("Error")

class Archer(Player):
    if Mainq=="Archer":
        Aq=input("Do you want to be a Archer or Slinger (Slingshot)?")
        if Aq=="Archer":
            abv+6
        elif Aq=="Slinger":
            abv+7
        else:
            print("Error")

with open("player.json", "r") as pjson:
    data = json.load(pjson)
    P= Player()
    PValues=P.Create(abv)
    data.append(PValues)    

new_file = "updated.json"
with open("player.json", "r") as pjson:
    with open(new_file, "w") as pjson:
        json_string = json.dumps(data, indent=4)
        pjson.write(json_string)
os.remove("player.json")
os.rename(new_file, "player.json")