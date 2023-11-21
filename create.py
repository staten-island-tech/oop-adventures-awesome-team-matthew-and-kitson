import json
import os

## Create Class for creating new dictionaries here

class Enemy():
    def __init__(self, name, role, Hp, dmg):
        self.name = name.capitalize()
        self.role = role.capitalize()
        self.hp = Hp.capitalize()
        self.dmg = dmg.capitalize
with open("data.json", "r") as djson:
    data = json.load(djson)
    class goblin(Enemy):
        name = data[0]["Name"]
        role = data[0]["Role"]
        hp = data[0]["Hp"]
       
    


with open("data.json", "r") as f:   
    data = json.load(f)





new_file = "updated.json"
with open(new_file, "w") as f:



    json_string = json.dumps(data, indent=4)


    f.write(json_string)


os.remove("data.json")
os.rename(new_file, "data.json")





