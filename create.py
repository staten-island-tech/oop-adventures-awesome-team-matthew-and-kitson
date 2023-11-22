import json
import os

## Create Class for creating new dictionaries here

<<<<<<< Updated upstream
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


=======
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
>>>>>>> Stashed changes
os.remove("data.json")
os.rename(new_file, "data.json")





