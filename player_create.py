import json
import os
import random
PName=input("What is the player's name? ")
Attributes={"Player Name": PName}
print(Attributes)


with open("class.json", "r") as f:
    data = json.load(f)
    class Player:
        def Create(self, i):
            PName=data[i]
            HP=
            Weapon1=
            Moves1=
            Weapon2=
            Moves2=
            if "Weapon 2" in data[i]:
                PValues={'PName:':PName,'HP:':HP,'Weapon1:':Weapon1,'Moves1:':Moves1,'Rating:':rating}
            else:
                PValues={'PName:':PName,'HP:':HP,'Weapon1:':Weapon1,'Moves1:':Moves1}
            return(PValues)
    def __str__(thing):
        return f"{thing.name}, {thing.company}"
with open("player.json", "r") as f:
    data = json.load(f)
    P= Player()
    PValues=P.Create()
    data.append(PValues)

with open("player.json", "r") as f:
    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data, indent=4)
        f.write(json_string)
    os.remove("player.json")
    os.rename(new_file, "player.json")


Mainq=input("Which player type do you want to be; Warrior, Magical, or Archer?")
class Warrior():
    if Mainq=="Warrior":
        Wq=input("Do you want to be a Knight or Tank?")
        if Wq=="Knight":
            print("e")
        elif Wq=="Tank":
            print("e")
        else:
            print("Error")
#import

