import json
import os

## Create Class for creating new dictionaries here
class items():
    def __init__(self, name):
        self.name = name.capitalize()
    
with open("item.json", "r") as ijson:
    data=json.load(ijson)
    class helmet(items):
        def __init__(self, name,Hp, dmg):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
            self.dmg = dmg.capitalize
    class Chestplate(items):
    class leggings(items): 
    class boots(items):
    class gloves(items): 
        def __init__(self, name,Hp, dmg):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
            self.dmg = dmg.capitalize
with open("item.json", "r") as ijson:
    class leatherhelm(helmet):
        name = 
        hp = 
        dmg = 



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
        dmg = data[0]["Dmg"]
    class spider(Enemy):
        name = data[1]["Name"]
        role = data[1]["Role"]
        hp = data[1]["Hp"]
        dmg = data[1]["Dmg"]
    class slime(Enemy):
        name = data[2]["Name"]
        role = data[2]["Role"]
        hp = data[2]["Hp"]
        dmg = data[2]["Dmg"]
    class zombie(Enemy):
        name = data[3]["Name"]
        role = data[3]["Role"]
        hp = data[3]["Hp"]
        dmg = data[3]["Dmg"]
    class Golem(Enemy):
        name = data[4]["Name"]
        role = data[4]["Role"]
        hp = data[4]["Hp"]
    class litch(Enemy):
        name = data[5]["Name"]
        role = data[5]["Role"]
        hp = data[5]["Hp"]
    class Dragon(Enemy):
        name = data[6]["Name"]
        role = data[6]["Role"]
        hp = data[6]["Hp"]
    class Dragonphase2(Enemy):
        name = data[7]["Name"]
        role = data[7]["Role"]
        hp = data[7]["Hp"]  
    class King(Enemy):
        name = data[8]["Name"]
        role = data[8]["Role"]
        hp = data[8]["Hp"] 
    class KingPhase2(Enemy):
        name = data[9]["Name"]
        role = data[9]["Role"]
        hp = data[9]["Hp"] 
    class Hydra(Enemy):
        name = data[10]["Name"]
        role = data[10]["Role"]
        hp = data[10]["Hp"] 
    class Hydraphase2(Enemy):
        name = data[11]["Name"]
        role = data[11]["Role"]
        hp = data[11]["Hp"]
    class Hydraphase3(Enemy):
        name = data[12]["Name"]
        role = data[12]["Role"]
        hp = data[12]["Hp"]
with open("data.json", "r") as f:   
    data = json.load(f)





new_file = "updated.json"
with open(new_file, "w") as f:



    json_string = json.dumps(data, indent=4)


    f.write(json_string)


name = input("Name: ")
role = input("Role: ")
hp = input("Hp: ")
Dmg= input("Dmg: ")
class Enemys():
    def __init__(self, name, role, Hp, Dmg):
        self.name = name.capitalize()
        self.role = role.capitalize()
        self.Hp = Hp.capitalize()
        self.Dmg = Dmg.capitalize()
    def create(self):
        data.append({'Name': self.name, 'Role': self.role, 'Hp': self.Hp, 'Dmg': self.Dmg})


with open("data.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
     
    ##Call classes in here
    mobs = Enemys(f"{name}", f"{role}", f"{hp}", f"{Dmg}")
    mobs.create()


#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent=4)

    # Write the JSON string to the new JSON file
    f.write(json_string)

# Overwrite the old JSON file with the new one
os.remove("data.json")
os.rename(new_file, "data.json")





