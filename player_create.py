import json
import os
import random
PName=input("What is the player's name?")

class Player:
    Name=(PName)

class Warrior(Player):
    q=input("Do you want to be a Knight or Tank?")
#import
with open("data.json", "r") as f:
    data = json.load(f)

with open("data.json", "r") as f:
    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data, indent=4)
        f.write(json_string)
    os.remove("data.json")
    os.rename(new_file, "data.json")