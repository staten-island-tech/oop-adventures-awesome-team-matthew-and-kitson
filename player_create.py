import json
import os
import random
PName=input("What is the player's name? ")
Attributes={"Player Name": PName}
Mainq=input("Which player type do you want to be; Warrior, Magical, or Archer?")
class Warrior():
    if Mainq=="Warrior":
        Wq=input("Do you want to be a Knight or Tank?")
        if Wq=="Knight":
            with open("class.json", "r") as f:
                data = json.load(f)
                print(data[1])
                KAppend=data[1]
                Attributes.append{KAppend}
                data.append(Attributes)
        elif Wq=="Tank":
            print("e")
        else:
            print("Error")
#import
with open("class.json", "r") as f:
    data = json.load(f)
    data.append(Attributes)

with open("class.json", "r") as f:
    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data, indent=4)
        f.write(json_string)
    os.remove("class.json")
    os.rename(new_file, "class.json")