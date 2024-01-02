import json
class items():
    def __init__(self, Name):
        self.Name = Name.capitalize()
class Moneyitem(items):
    def __init__(self, Name, Price):
        self.Name = Name.capitalize()
        self.Price = Price
with open("item.json", "r") as ijson:
    data=json.load(ijson)
    Trinket=Moneyitem("Trinket", 19)
    Gold_Goblet=Moneyitem("Gold Goblet", 43)
    Silver_Goblet=Moneyitem("Silver Goblet", 18)
    Gold_Ring=Moneyitem("Gold Ring", 39)
    Silver_Ring=Moneyitem("Silver Ring", 13)
    Gold_Necklace=Moneyitem("Gold Necklace", 37)
    Silver_Necklace=Moneyitem("Silver Necklace", 23)
    Gold_Band=Moneyitem("Gold Band", 29)
    Silver_Band=Moneyitem("Silver Band", 20)
    Gold_Bangle=Moneyitem("Gold Bangle", 34)
    Silver_Bangle=Moneyitem("Silver Bangle", 21)
    Diamond=Moneyitem("Diamond", 47)
    Ruby=Moneyitem("Ruby", 35)
    class Helmet(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            self.Name = Name
            self.HP = HP
            self.Price=Price
    LeatherHelmet=Helmet(["Healer", "SpellCaster"], "Leather Helmet", 7, 67)
    PlateHelmet=Helmet(["Knight", "Tank"], "Plated Helmet", 17, 89)
    ConeHat=Helmet(["Mage", "Necromancer", "Healer", "Spellcaster"], "Cone Hat", 13, 54)
    HelmetList=[ConeHat, PlateHelmet, LeatherHelmet]
    class Chestplate(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            self.Name = Name
            self.HP = HP
            self.Price=Price
    LeatherChestplate=Chestplate(["Healer", "SpellCaster"],"Leather Chestplate", .1, 64)
    MagicRobe=Chestplate(["Mage", "Necromancer"], "Magic Robe", .3, 43)
    PlateChest=Chestplate(["Knight", "Tank"], "Plated Chestplate", .5, 78)
    ChestplateList=[PlateChest, MagicRobe, LeatherChestplate]
    class Leggings(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            self.Name = Name
            self.HP = HP
            self.Price=Price
    Trousers=Leggings(["Mage", "Necromancer"], "Trousers", 8, 43)
    LeatherLeggings=Leggings(["Healer", "SpellCaster"], "Leather Leggings", 10, 56)
    PlateLeggings=Leggings(["Knight", "Tank"], "Plated Leggings", 23, 86)
    LeggingsList=[PlateLeggings, LeatherLeggings, Trousers]
    class Boots(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            self.Name = Name
            self.HP = HP
            self.Price=Price
    LeatherBoots=Boots(["Mage", "Necromancer", "Knight"], "Leather Boots", 5, 12)
    HeavyBoots=Boots(["Healer", "SpellCaster"], "Heavy Boots", 11, 26)
    PlateBoots=Boots(["Knight", "Tank"], "Plated Boots", 19, 29)
    BootsList=[PlateBoots, HeavyBoots, LeatherBoots]
class Enemy():
    def __init__(self, Name, JSON_Num, HP, DMG, EXP, Gold):
        self.name = Name.capitalize()
        self.JSON_Num = JSON_Num
        self.HP = HP
        self.DMG = DMG
        self.EXP = EXP
        self.Gold=Gold
class Boss(Enemy):
    def __init__(self, Name, JSON_num, HP, EXP, Gold):
        self.Name = Name.capitalize()
        self.JSON_num = JSON_num
        self.HP = HP
        self.EXP = EXP
        self.Gold=Gold
with open("data.json", "r") as djson:
    data = json.load(djson)
    goblin=Enemy(data[0]["Name:"], 0, data[0]["Hp:"], data[0]["Dmg:"], 5, 1)
    spider=Enemy(data[1]["Name:"], 1, data[1]["Hp:"], data[1]["Dmg:"], 10, 2)
    slime=Enemy(data[2]["Name:"], 2, data[2]["Hp:"], data[2]["Dmg:"], 15, 2)
    zombie=Enemy(data[3]["Name:"], 3, data[3]["Hp:"], data[3]["Dmg:"], 20, 5)
    Golem=Boss(data[4]["Name:"], 4, data[4]["Hp:"], 50, 50)
    Lich=Boss(data[5]["Name:"], 5, data[5]["Hp:"], 70, 50)
    Dragon=Boss(data[6]["Name:"], 6, data[6]["Hp:"], 200, 100)
    King=Boss(data[8]["Name:"], 8, data[8]["Hp:"], 250, 100)
    Hydra=Boss(data[10]["Name:"], 10, data[10]["Hp:"], 400, 200)