import json
import os
import stuff
weaponlist=stuff.WeaponList
def bootsequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
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
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
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
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
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
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
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
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    selectweapon=None
    if player['Weapon2:']=="N/A":
        print(player['Inventory:'])
        weaponcheck=input("What weapon would you like to equip? ")
        if weaponcheck in player['Inventory:']:
            for i in range(len(weaponlist)):
                if weaponcheck == weaponlist[i].Name:
                    selectweapon=weaponlist[i]
            if not selectweapon == None and not selectweapon.Name==player['Weapon2:'] and not selectweapon.Name==player['Weapon1:']:
                player['Weapon2:']==selectweapon.Name
                print(selectweapon.Name, "was equipped!")
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
                print("Not a weapon/item or already equipped.")
        else:
                print("Not in inventory.")
    else:
                print("Max weapons already equipped.")
def bootsunequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    bootscheck=player['Boots:']
    if not bootscheck=="N/A":
        for i in range(len(stuff.BootsList)):
            if bootscheck in stuff.BootsList[i].Name:
                selectboots=stuff.BootsList[i]
        player['Boots:']="N/A"
        player['BaseHP:']=player['BaseHP:']-selectboots.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully unequipped!")
    else:
        print("Boots are not equipped.")
def leggingsunequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    leggingscheck=player['Leggings:']
    if not leggingscheck=="N/A":
        for i in range(len(stuff.LeggingsList)):
            if leggingscheck in stuff.LeggingsList[i].Name:
                selectleggings=stuff.LeggingsList[i]
        player['Leggings:']="N/A"
        player['BaseHP:']=player['BaseHP:']-selectleggings.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully unequipped!")
    else:
        print("Leggings are not equipped.")
def chestplateunequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    chestplatechcek=player['Chestplate:']
    if not chestplatechcek=="N/A":
        for i in range(len(stuff.ChestplateList)):
            if chestplatechcek in stuff.ChestplateList[i].Name:
                selectchestplate=stuff.ChestplateList[i]
        player['Chestplate:']="N/A"
        player['HpMultiplier:']=player['HpMultiplier:']-selectchestplate.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully unequipped!")
    else:
        print("Chestplate are not equipped.")
def helmetunequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    helmetcheck=player['Helmet:']
    if not helmetcheck=="N/A":
        for i in range(len(stuff.HelmetList)):
            if helmetcheck in stuff.HelmetList[i].Name:
                selecthelmet=stuff.HelmetList[i]
        player['Helmet:']="N/A"
        player['BaseHP:']=player['BaseHP:']-selecthelmet.HP
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully unequipped!")
    else:
        print("Helmet is not equipped.")
def weaponunequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    if not player['Weapon2:']=="N/A":
        weaponcheck=input("What weapon would you like to unequip? ")
        for i in range(len(weaponlist)):
            if weaponcheck in weaponlist[i].Name:
                selectweapon=weaponlist[i]
        for i in range(len(selectweapon.Moves)):
             if selectweapon.Moves[i] in player['Moves:']:
                player['Moves:'].remove(selectweapon.Moves[i])
        if weaponcheck==player['Weapon2:']:
            player['Weapon2:']="N/A"
        elif weaponcheck==player['Weapon1:']:
            player['Weapon1:']=player['Weapon2:']
            player['Weapon2:']="N/A"
        else:
            print("Not an equipped weapon.")
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
        print("Successfully unequipped!")
    else:
        print("You cannot unequip a weapon with only 1 weapon equipped.")
def equip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
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
def unequip():
    check=input("Would you like to unequip a Weapon or Armor? (Enter to go break) " )
    if check=="Armor":
        armorcheck=input("Would you like to unequip Boots, Leggings, a Chestplate, or a Helmet? ")
        if armorcheck=="Boots":
            bootsunequip()
        if armorcheck=="Leggings":
            leggingsunequip()
        if armorcheck=="Chestplate":
            chestplateunequip()
        if armorcheck=="Helmet":
            helmetunequip()
    elif check=="Weapon":
        weaponunequip()
def ultequip():
    y=True
    while y==True:
        checkequip=input("Would you like to Equip or Unequip an item? (Enter to break) ")
        if checkequip=="Equip":
            equip()
        elif checkequip=="Unequip":
            unequip()
        else:
            break