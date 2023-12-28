import json

class items():
    def __init__(self, name):
        self.name = name.capitalize()
class Moneyitem(items):
    def __init__(self, name, Price):
        self.name = name.capitalize()
        self.price = Price.capitalize() 
with open("item.json", "r") as ijson:
    data=json.load(ijson)
    trinket=Moneyitem(data[12]["Name"], 19)
    gold_goblet=Moneyitem(data[13]["Name"], 43)
    silver_goblet=Moneyitem(data[14]["Name"], 18)
    gold_ring=Moneyitem(data[15]["Name"], 39)
    silver_ring=Moneyitem(data[16]["Name"], 13)
    gold_necklace=Moneyitem(data[17]["Name"], 37)
    silver_necklace=Moneyitem(data[18]["Name"], 23)
    gold_ring=Moneyitem(data[19]["Name"], 46)
    silver_ring=Moneyitem(data[20]["Name"], 25)
    gold_band=Moneyitem(data[21]["Name"], 29)
    silver_band=Moneyitem(data[22]["Name"])
    gold_bangle=Moneyitem(data[23]["Name"], 34)
    silver_bangle=Moneyitem(data[24]["Name"], 21)
    diamond=Moneyitem(data[25]["Name"], 47)
    ruby=Moneyitem(data[26]["Name"], 35)
    class helmet(items):
        def __init__(self, equipable, name, Hp, price):
            self.equipable=equipable
            self.name = name.capitalize()
            self.Hp = Hp
            self.price=price
    LeatherHelmet=helmet(["Healer", "SpellCaster"], data[0]["Name"], 7, 67)
    PlateHelmet=helmet(["Knight", "Tank"], data[1]["Name"], 17, 89)
    ConeHat=helmet(["Mage", "Necromancer"], data[2]["Name"], 13, 54)
    class Chestplate(items):
        def __init__(self, equipable, name, Hp, price):
            self.equipable=equipable
            self.name = name.capitalize()
            self.Hp = Hp
            self.price=price
    LeatherChestplate=Chestplate(["Healer", "SpellCaster"], data[3]["Name"], .1, 64)
    Robe=Chestplate(["Mage", "Necromancer"], data[4]["Name"], .3, 43)
    PlateChest=Chestplate(["Knight", "Tank"], data[5]["Name"], .5, 78)
    class leggings(items):
        def __init__(self, equipable, name, Hp, price):
            self.equipable=equipable
            self.name = name.capitalize()
            self.Hp = Hp
            self.price=price
    LeatherLeggings=leggings(["Healer", "SpellCaster"], data[6]["Name"], 10, 56)
    PlateLeggings=leggings(["Knight", "Tank"], data[7]["Name"], 23, 86)
    Trousers=leggings(["Mage", "Necromancer"], data[8]["Name"], 8, 43)
    class boots(items):
        def __init__(self, equipable, name, Hp, price):
            self.equipable=equipable
            self.name = name.capitalize()
            self.Hp = Hp
            self.price=price
    LeatherBoots=boots(["Mage", "Necromancer"], data[10]["Name"], 5, 12)
    HeavyBoots=boots(["Healer", "SpellCaster"], data[9]["Name"], 11, 26)
    PlateBoots=boots(["Knight", "Tank"], data[11]["Name"], 19, 29)
class Enemy():
    def __init__(self, name, json_num, Hp, dmg, exp):
        self.name = name.capitalize()
        self.json_num = json_num
        self.Hp = Hp
        self.dmg = dmg
        self.exp = exp
class Boss(Enemy):
    def __init__(self, name, json_num, Hp, exp):
        self.name = name.capitalize()
        self.json_num = json_num
        self.hp = Hp
        self.exp = exp
with open("data.json", "r") as djson:
    data = json.load(djson)
    goblin=Enemy(data[0]["Name"], 0, data[0]["Hp"], data[0]["Dmg"], 5)
    spider=Enemy(data[1]["Name"], 1, data[1]["Hp"], data[1]["Dmg"], 10)
    slime=Enemy(data[2]["Name"], 2, data[2]["Hp"], data[2]["Dmg"], 15)
    zombie=Enemy(data[3]["Name"], 3, data[3]["Hp"], data[3]["Dmg"], 20)
    Golem=Boss(data[4]["Name"], 4, data[4]["Hp"])
    Lich=Boss(data[5]["Name"], 5, data[5]["Hp"])
    Dragon=Boss(data[6]["Name"], 6, data[6]["Hp"])
    King=Boss(data[8]["Name"], 8, data[8]["Hp"]  )
    Hydra=Boss(data[10]["Name"], 10, data[10]["Hp"] )