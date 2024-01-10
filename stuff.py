import json
class items():
    def __init__(self, Name, Price):
        self.Name = Name
        self.Price = Price
class Moneyitem(items):
    def __init__(self, Name, Price):
        super().__init__(Name, Price)
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
    Gold_Band=Moneyitem("Gold Band", 30)
    Silver_Band=Moneyitem("Silver Band", 20)
    Gold_Bangle=Moneyitem("Gold Bangle", 25)
    Silver_Bangle=Moneyitem("Silver Bangle", 15)
    Diamond=Moneyitem("Diamond", 50)
    Ruby=Moneyitem("Ruby", 35)
    class Helmet(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            super().__init__(Name, Price)
            self.HP = HP
    LeatherHelmet=Helmet(["Healer", "SpellCaster"], "Leather Helmet", 7, 67)
    PlateHelmet=Helmet(["Knight", "Tank"], "Plated Helmet", 17, 89)
    ConeHat=Helmet(["Mage", "Necromancer", "Healer", "Spellcaster"], "Cone Hat", 13, 54)
    HelmetList=[ConeHat, PlateHelmet, LeatherHelmet]
    class Chestplate(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            super().__init__(Name, Price)
            self.HP = HP
    LeatherChestplate=Chestplate(["Healer", "SpellCaster"],"Leather Chestplate", .1, 64)
    MagicRobe=Chestplate(["Mage", "Necromancer"], "Magic Robe", .3, 43)
    PlateChest=Chestplate(["Knight", "Tank"], "Plated Chestplate", .5, 78)
    ChestplateList=[PlateChest, MagicRobe, LeatherChestplate]
    class Leggings(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            super().__init__(Name, Price)
            self.HP = HP
    Trousers=Leggings(["Mage", "Necromancer", "Knight"], "Trousers", 8, 43)
    LeatherLeggings=Leggings(["Healer", "SpellCaster"], "Leather Leggings", 10, 56)
    PlateLeggings=Leggings(["Knight", "Tank"], "Plated Leggings", 23, 86)
    LeggingsList=[PlateLeggings, LeatherLeggings, Trousers]
    class Boots(items):
        def __init__(self, Equipable, Name, HP, Price):
            self.Equipable=Equipable
            super().__init__(Name, Price)
            self.HP = HP
    LeatherBoots=Boots(["Mage", "Necromancer", "Knight"], "Leather Boots", 5, 12)
    HeavyBoots=Boots(["Healer", "SpellCaster"], "Heavy Boots", 11, 26)
    PlateBoots=Boots(["Knight", "Tank"], "Plated Boots", 19, 29)
    BootsList=[PlateBoots, HeavyBoots, LeatherBoots]
class Weapon(items):
    def __init__(self, Name, Moves, Price):
        super().__init__(Name, Price)
        self.Moves=Moves

Sword=Weapon("Sword", ["Sword Attack", "Shield"], 100)
Mace=Weapon("Mace", ["Mace Swing"], 70)
Shield=Weapon("Shield", ["Shield Bash", "Block"], 100)
Staff=Weapon("Staff", ["Meteor Shower", "Ice Shard", "Protection Spell"], 120)
Necromancer_Staff=Weapon("Necromancer Staff", ["Summon"], 70)
Magic_Book=Weapon("Magic_Book", ["Fireball", "Thunderbolt"], 100)
Healer_Staff=Weapon("Healer Staff", ["Heal", "Staff Stab"], 90)
Bow=Weapon("Bow", ["Normal Arrow", "Fire Arrow", "Ice Arrow"], 120)
Slingshot=Weapon("Slingshot", ["Slingshot Fire"], 70)
WeaponList=[Sword, Mace, Shield, Staff, Necromancer_Staff, Magic_Book, Healer_Staff, Bow, Slingshot]
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
        super().__init__(Name, Num, HP, "N/A", EXP, Gold)
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
Hero=BattleHero(player['PName:'], round(float(player['BaseHP:']*player['HpMultiplier:'])), player['HpMultiplier:'], player['DmgMultiplier:'], player['Moves:'])
class moves():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
SwordAttack=moves("Sword Attack", round(float(25)*float(Hero.damagemultiplier)))
Shield=moves("Shield", 0)
MaceSwing=moves("Mace Swing", round(float(30)*float(Hero.damagemultiplier)))
ShieldBash=moves("Shield Bash", round(float(30)*float(Hero.damagemultiplier)))
Block=moves("Block", 0)
MeteorShower=moves("Meteor Shower", round(float(20)*float(Hero.damagemultiplier)))
IceShard=moves("Ice Shard", round(float(25)*float(Hero.damagemultiplier)))
ProtectionSpell=moves("Protection Spell", 0)
Summon=moves("Summon", round(float(30)*float(Hero.damagemultiplier)))
Fireball=moves("Fireball", round(float(30)*float(Hero.damagemultiplier)))
Thunderbolt=moves("Thunderbolt", round(float(25)*float(Hero.damagemultiplier)))
Heal=moves("Heal", 0)
StaffStab=moves("Staff Stab", (round(float(15)*float(Hero.damagemultiplier))))
NormalArrow=moves("Normal Arrow", (round(float(20)*float(Hero.damagemultiplier))))
FireArrow=moves("Fire Arrow", round(float(20)*float(Hero.damagemultiplier)))
IceArrow=moves("Ice Arrow", round(float(20)*float(Hero.damagemultiplier)))
SlingshotFire=moves("Slingshot Fire", (round(float(25)*float(Hero.damagemultiplier))))
GolemSlam=moves("Golem Slam", 55)
BoulderThrow=moves("Boulder Throw", 45)
GolemPunch=moves("Golem Punch", 50)
Roll=moves("Roll", 40)
Poisoning=moves("Poisoning", 0)
DeathSpell=moves("Death Spell", 60)
FireBreath=moves("Fire Breath", 50)
ClawSlash=moves("Claw Slash", 45)
TailSwing=moves("Tail Swing", 40)
Fly=moves("Fly", 35)
BlueFireBreath=moves("Blue Fire Breath", 60)
Bite=moves("Bite", 50)
Slam=moves("Slam", 55)
SwordAttackBoss=moves("Sword Attack", 50)
SwordSlam=moves("Sword Slam", 55)
CrownThrow=moves("Crown Throw", 45)
SwordSlash=moves("Sword Slash", 60)
JewelBash=moves("Jewel Bash", 70)
KingSlam=moves("King Slam", 65)
HydraBlast=moves("Hydra Blast", 65)
TripleAttack=moves("Triple Attack", 60)
HydraBite=moves("Hydra Bite", 50)
HydraBeam=moves("Hydra Beam", 85)
SkullFire=moves("Skull Fire", 80)
PoisonFire=moves("Poison Fire", 50)
FinalBlast=moves("Final Blast", 100)
Regenerate=moves("Regenerate", 0)
OneHeadAttack=moves("One Head Attack", 120)
LastEffort=moves("Last Effort", 150)