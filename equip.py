import json
import os
import stuff
with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
weaponlist=stuff.WeaponList
def bootsequip():
    for i in range(len(stuff.BootsList)):
        print(stuff.BootsList[i].Name, " ", stuff.BootsList[i].Equipable)
    bootscheck=input("What boots would you like to equip? ")
    for i in range(len(stuff.BootsList)):
        if bootscheck in stuff.BootsList[i].Name:
            selectboots=stuff.BootsList[i]
    if bootscheck in player['Inventory:'] and player['Boots:'] == "N/A" and player['Class:'] in selectboots.Equipable:
        player['Boots:']=selectboots.Name
        player['BaseHP:']=player['BaseHP:']+selectboots.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully equipped!")
    else:
        print("Boots already equipped, not in inventory, or unequipable for your class.")
def leggingsequip():
    for i in range(len(stuff.LeggingsList)):
        print(stuff.LeggingsList[i].Name, " ", stuff.LeggingsList[i].Equipable)
    leggingscheck=input("What leggings would you like to equip? ")
    for i in range(len(stuff.LeggingsList)):
            if leggingscheck in stuff.LeggingsList[i].Name:
                selectleggings=stuff.LeggingsList[i]
    if leggingscheck in player['Inventory:'] and player['Leggings:'] == "N/A" and player['Class:'] in selectleggings.Equipable:
        player['Leggings:']=selectleggings.Name
        player['BaseHP:']=player['BaseHP:']+selectleggings.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully equipped!")
    else:
        print("Leggings already equipped, not in inventory, or unequipable for your class.")
def chestplateequip():
    for i in range(len(stuff.ChestplateList)):
        print(stuff.ChestplateList[i].Name, " ", stuff.ChestplateList[i].Equipable)
    chestplatecheck=input("What chestplate would you like to equip? ")
    for i in range(len(stuff.ChestplateList)):
            if chestplatecheck in stuff.ChestplateList[i].Name:
                selectchestplate=stuff.ChestplateList[i]
    if chestplatecheck in player['Inventory:'] and player['Chestplate:'] == "N/A" and player['Class:'] in selectchestplate.Equipable:
        player['Chestplate:']=selectchestplate.Name
        player['HpMultiplier:']=player['HpMultiplier:']+selectchestplate.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully equipped!")
    else:
        print("Chestplate already equipped, not in inventory, or unequipable for your class.")
def helmetequip():
    for i in range(len(stuff.HelmetList)):
        print(stuff.HelmetList[i].Name, " ", stuff.HelmetList[i].Equipable)
    helmetcheck=input("What helmet would you like to equip? ")
    for i in range(len(stuff.HelmetList)):
        if helmetcheck in stuff.HelmetList[i].Name:
            selecthelmet=stuff.HelmetList[i]
    if helmetcheck in player['Inventory:'] and player['Helmet:'] == "N/A" and player['Class:'] in selecthelmet.Equipable:
        player['Helmet:']=selecthelmet.Name
        player['BaseHP:']=player['BaseHP:']+selecthelmet.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully equipped!")
    else:
        print("Helmet already equipped, not in inventory, or unequipable for your class.")
def weaponequip():
    selectweapon=None
    if player['Weapon2:']=="N/A":
        print(player['Inventory:'])
        weaponcheck=input("What weapon would you like to equip? ")
        if weaponcheck in player['Inventory:']:
            for i in range(len(weaponlist)):
                if weaponcheck in weaponlist[i].Name:
                    selectweapon=weaponlist[i]
            if not selectweapon == None:
                player['Weapon2:']=selectweapon.Name
                print(player['Weapon2:'], "was equipped!")
                for i in range(len(selectweapon.Moves)):
                    player['Moves:'].append(selectweapon.Moves[i])
                new_file = "updated.json"
                with open(new_file, "w") as pjson:
                    json_string = json.dumps(data, indent=4)
                    pjson.write(json_string)
                os.remove("player.json")
                os.rename(new_file, "player.json")
                print("Successfully equipped!")
            else:
                print("Not a weapon/item.")
        else:
                print("Not in inventory.")
    else:
                print("Max weapons already equipped.")
def equip():
    check=input("Would you like to equip a Weapon or Armor? (Enter to go break) " )
    if check=="Armor":
        print(player['Inventory:'])
        armorcheck=input("Would you like to equip Boots, Leggings, a Chestplate, or a Helmet? ")
        if armorcheck=="Boots":
            bootsequip()
        if armorcheck=="Leggings":
            leggingsequip()
        if armorcheck=="Chestplate":
            chestplateequip()
        if armorcheck=="Helmet":
            helmetequip()
    elif check=="Weapon":
        weaponequip()