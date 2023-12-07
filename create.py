import json
import os

## Create Class for creating new dictionaries here
class items():
    def __init__(self, name):
        self.name = name.capitalize()
    
with open("item.json", "r") as ijson:
    data=json.load(ijson)
    class Moneyitem(items):
        def __init__(self, name,Price):
            self.name = name.capitalize()
            self.price = Price.capitalize()
    class helmet(items):
        def __init__(self, name,Hp):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
    class Chestplate(items):
        def __init__(self, name,Hp):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
    class leggings(items):
        def __init__(self, name,Hp):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
    class boots(items):
        def __init__(self, name,Hp):
            self.name = name.capitalize()
            self.hp = Hp.capitalize()
with open("item.json", "r") as ijson:
    data = json.load(ijson)
    class leatherhelm(helmet):
        equipable = ["Healer", "SpellCaster"]
        name = data[0]["Name"]
        hp = 7
        price = 67
    class Platehelm(helmet):
        equipable = ["Knight", "Tank"]
        name = data[1]["Name"]
        hp = 17
        price = 89      
    class Conehat(helmet):
        equipable = ["Mage", "Necromancer"]
        name = data[2]["Name"]
        hp = 13
        price = 54
    class HeavyLeatherChest(Chestplate):
        equipable = ["Healer", "SpellCaster"]
        name = data[3]["Name"]
        hp = 15
        price = 64
    class Robe(Chestplate):
        equipable = ["Mage", "Necromancer"]
        name = data[4]["Name"]
        hp = 23
        price = 43
    class PlateChest(Chestplate):
        equipable = ["Knight", "Tank"]
        name = data[5]["Name"]
        hp = 64
        price = 78
    class HeavyLeatherlegs(leggings):
        equipable = ["Healer", "SpellCaster"]
        name = data[6]["Name"]
        hp = 10
        price = 56
    class Platelegs(leggings):
        equipable = ["Knight", "Tank"]
        name = data[7]["Name"]
        hp = 23
        price = 86
    class trousers(leggings):
        equipable = ["Mage", "Necromancer"]
        name = data[8]["Name"]
        hp = 9
        price = 43
    class Heavyboots(boots):
        equipable = ["Healer", "SpellCaster"]
        name = data[9]["Name"]
        hp = 11
        price = 26
    class Clothboots(boots):
        equipable = ["Mage", "Necromancer"]
        name = data[10]["Name"]
        hp = 5
        price = 12
    class Plateboots(boots):
        equipable = ["Knight", "Tank"]
        name = data[11]["Name"]
        hp = 19
        price = 29
    class trinket(Moneyitem):
        name = data[12]["Name"]
        price = 19
    class gold_goblet(Moneyitem):
        name = data[13]["Name"]
        Price = 43
    class silver_goblet(Moneyitem):
        name = data[14]["Name"]
        Price = 18
    class gold_ring(Moneyitem):
        name = data[15]["Name"]
        Price = 39
    class silver_ring(Moneyitem):
        name = data[16]["Name"]
        Price = 13
    class gold_necklace(Moneyitem):
        name = data[17]["Name"]
        Price = 37
    class silver_necklace(Moneyitem):
        name = data[18]["Name"]
        Price = 23
    class gold_ring(Moneyitem):
        name = data[19]["Name"]
        Price = 46
    class silver_ring(Moneyitem):
        name = data[20]["Name"]
        Price = 25
    class gold_band(Moneyitem):
        name = data[21]["Name"]
        Price = 29
    class silver_band(Moneyitem):
        name = data[22]["Name"]
        Price = 16
    class gold_bangle(Moneyitem):
        name = data[23]["Name"]
        Price = 34
    class silver_bangle(Moneyitem):
        name = data[24]["Name"]
        Price = 21
    class diamond(Moneyitem):
        name = data[25]["Name"]
        Price = 47
    class ruby(Moneyitem):
        name = data[26]["Name"]
        Price = 35
  


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

