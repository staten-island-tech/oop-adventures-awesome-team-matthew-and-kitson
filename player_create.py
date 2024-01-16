import json
import os
class Player:
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
    def confirm(i):
        print("Congratulations, you have selected & became the class:", i)
    def Create(self, i):
        PName=input("What is the player's name? ")
        Pclass=Player.data[i]['Class']
        HP=Player.data[i]['Hp']
        Weapon1=Player.data[i]['Weapon1']
        Moves=Player.data[i]['Moves']
        Weapon2=Player.data[i]['Weapon2']
        if not Weapon2 == "N/A":
            PValues={'PName:':PName,'Class:':Pclass,'BaseHP:':HP,'Weapon1:':Weapon1,'Weapon2:':Weapon2, 'Moves:': Moves, 'Gold:': [0], "HpMultiplier:":1, "DmgMultiplier:":1, "Inventory:": [Weapon1, Weapon2], "Helmet:": "N/A", "Chestplate:": "N/A", "Leggings:": "N/A", "Boots:": "N/A", "Level:": 0, "EXP:":0}
        else:
            PValues={'PName:':PName,'Class:':Pclass,'BaseHP:':HP,'Weapon1:':Weapon1,'Weapon2:':Weapon2, 'Moves:': Moves, 'Gold:': [0], "HpMultiplier:":1, "DmgMultiplier:":1, "Inventory:": [Weapon1], "Helmet:": "N/A", "Chestplate:": "N/A", "Leggings:": "N/A", "Boots:": "N/A", "Level:": 0, "EXP:":0}
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
    def info_check(self, x):
        P= Player()
        PValues=P.Create(x)
        print(PValues)
    def ultcreate():
        P= Player()
        e=True
        while e ==True:
            Mainq=input("Which player type do you want to be; Warrior, Magical, or Archer? Enter 'Info' for info on classes. ")
            if Mainq=='Info':
                with open("player.json", "r") as pjson:
                    data = json.load(pjson)
                    for i in range(len(data)):
                        print(data[i])
            elif Mainq=="Warrior":
                x=True
                while x ==True:
                    Wq=input("Do you want to be a Knight or Tank? ")
                    if Wq=="Knight":
                        P.Create2(0)
                        Player.confirm(Wq)
                        e=False
                        x=False
                    elif Wq=="Tank":
                        P.Create2(1)
                        Player.confirm(Wq)
                        e=False
                        x=False
                    else:
                        print("Error, please enter one of the options.")
            elif Mainq=="Magical":
                x=True
                while x ==True:
                    Mq=input("Do you want to be a Mage, Necromancer, Spellcaster, or Healer? ")
                    if Mq=="Mage":
                        P.Create2(2)
                        Player.confirm(Mq)
                        e=False
                        x=False
                    elif Mq=="Necromancer":
                        P.Create2(3)
                        Player.confirm(Mq)
                        e=False
                        x=False
                    elif Mq=="Spellcaster":
                        P.Create2(4)
                        Player.confirm(Mq)
                        e=False
                        x=False
                    elif Mq=="Healer":
                        P.Create2(5)
                        Player.confirm(Mq)
                        e=False
                        x=False
                    else:
                        print("Error, please enter one of the options.")
            elif Mainq=="Archer":
                x=True
                while x ==True:
                    Aq=input("Do you want to be a Archer or Slinger (Slingshot)? ")
                    if Aq=="Archer":
                        P.Create2(6)
                        Player.confirm(Aq)
                        e=False
                        x=False
                    elif Aq=="Slinger":
                        P.Create2(7)
                        Player.confirm(Aq)
                        e=False
                        x=False
                    else:
                        print("Error, please enter one of the options.")
            else:
                print("Enter a valid class.")
def check():
    with open("player.json", "r") as pjson:
        data=json.load(pjson)
    while not len(data)==8:
        data.remove(data[8])
    new_file = "updated.json"
    with open(new_file, "w") as pjson:
        json_string = json.dumps(data, indent=4)
        pjson.write(json_string)
    os.remove("player.json")
    os.rename(new_file, "player.json")
    Player.ultcreate()