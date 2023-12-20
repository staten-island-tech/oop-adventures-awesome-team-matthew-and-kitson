import json
import os
PName=input("What is the player's name? ")
def confirm(i):
    print("Congratulations, you have selected & became the class:", i)
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    class Player:
        def Create(self, i):
            PlayerName=PName
            Pclass=data[i]['Class']
            HP=data[i]['Hp']
            Weapon1=data[i]['Weapon1']
            Moves1=data[i]['Moves1']
            if "Weapon2" in data[i]:
                Weapon2=data[i]['Weapon2']
                Moves2=data[i]['Moves2']
                PValues={'PName:':PlayerName,'Class:':Pclass,'BaseHP:':HP, 'ModifiedHP:':HP, 'Weapon1:':Weapon1,'Moves1:':Moves1,'Weapon2:':Weapon2, 'Moves2':Moves2, 'Gold:': 0, "HpMultiplier:":1}
            else:
                PValues={'PName:':PlayerName,'Class:':Pclass,'BaseHP:':HP, 'ModifiedHP:':HP,'Weapon1:':Weapon1,'Moves1:':Moves1, 'Weapon2:':"N/A", 'Moves2':"N/A", 'Gold:': 0, "HpMultiplier:":1}
            return(PValues)
        def Create2(self, x):
            with open("player.json", "r") as pjson:
                data = json.load(pjson)
                P= Player()
                PValues=P.Create(x)
                data.append(PValues)
                new_file = "updated.json"
                with open(new_file, "w") as pjson:
                    json_string = json.dumps(data, indent=4)
                    pjson.write(json_string)
            os.remove("player.json")
            os.rename(new_file, "player.json")
P= Player()
e=True
while e ==True:
    Mainq=input("Which player type do you want to be; Warrior, Magical, or Archer? ")
    break
class Warrior(Player):
    if Mainq=="Warrior":
        x=True
        while x ==True:
            Wq=input("Do you want to be a Knight or Tank? ")
            if Wq=="Knight":
                P.Create2(0)
                confirm(Wq)
                break
            elif Wq=="Tank":
                P.Create2(1)
                confirm(Wq)
                break
            else:
                print("Error, please enter one of the options.")

class Magical(Player):
    if Mainq=="Magical":
        x=True
        while x ==True:
            Mq=input("Do you want to be a Mage, Necromancer, Spellcaster, or Healer? ")
            if Mq=="Mage":
                P.Create2(2)
                confirm(Mq)
                break
            elif Mq=="Necromancer":
                P.Create2(3)
                confirm(Mq)
                break
            elif Mq=="Spellcaster":
                P.Create2(4)
                confirm(Mq)
                break
            elif Mq=="Healer":
                P.Create2(5)
                confirm(Mq)
                break
            else:
                print("Error, please enter one of the options.")

class Archer(Player):
    if Mainq=="Archer":
        x=True
        while x ==True:
            Aq=input("Do you want to be a Archer or Slinger (Slingshot)? ")
            if Aq=="Archer":
                P.Create2(6)
                confirm(Aq)
                break
            elif Aq=="Slinger":
                P.Create2(7)
                confirm(Aq)
                break
            else:
                print("Error, please enter one of the options.")