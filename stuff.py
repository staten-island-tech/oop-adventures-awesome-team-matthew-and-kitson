import json
from decimal import Decimal
class items():
    def __init__(self, Name):
        self.Name = Name.capitalize()
class Moneyitem(items):
    def __init__(self, Name, Price):
        self.Name = Name.capitalize()
        self.Price = Price
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    player=data[8]
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
    Trousers=Leggings(["Mage", "Necromancer", "Knight"], "Trousers", 8, 43)
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
class Weapon(items):
    def __init__(self, Name, Moves):
        self.Name=Name
        self.Moves=Moves
Sword=Weapon("Sword")
Mace=Weapon("Mace")
Shield=Weapon("Shield")
Staff=Weapon("Staff")
Necromancer_Staff=Weapon("Necromancer Staff")
Magic_Book=Weapon("Magic_Book")
Healer_Staff=Weapon("Healer Staff")
Bow=Weapon("Bow")
Slingshot=Weapon
class Enemy():
    def __init__(self, Name, Num, HP, DMG, EXP, Gold):
        self.Name = Name.capitalize()
        self.Num = Num
        self.HP = HP
        self.DMG = DMG
        self.EXP = EXP
        self.Gold=Gold
class Boss(Enemy):
    def __init__(self, Name, Num, HP, EXP, Gold):
        self.Name = Name.capitalize()
        self.Num = Num
        self.HP = HP
        self.EXP = EXP
        self.Gold=Gold
goblin=Enemy("Goblin", 0, 32, 12, 5, 1)
spider=Enemy("Spider", 1, 24, 16, 10, 2)
slime=Enemy("Slime", 2, 12, 5, 15, 2)
zombie=Enemy("Zombie", 3, 43, 27, 20, 5)
Golem=Boss("Golem", 4, 238, 50, 50)
Lich=Boss("Lich", 5, 150, 70, 50)
Dragon=Boss("Dragon", 6, 534, 200, 100)
King=Boss("King", 8, 367, 250, 100)
Hydra=Boss("Hydra", 10, 462, 400, 200)
class BattleHero:
    def __init__(self, name, hp, hpmultiplier, damagemultiplier, moves):
        self.name = name
        self.hp = hp
        self.hpmultiplier=hpmultiplier
        self.damagemultiplier = damagemultiplier
        self.moves=moves
class Merchant:
    def __init__(self, products):
        self.products=products
    def sell(self, item):
        self.products.remove(item)
    def welcome(x):
        print(f"Welcome to my shop! You can buy items from my catalogue, or sell any sellable item here!")
Hero=BattleHero(player['PName:'], round(Decimal(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])