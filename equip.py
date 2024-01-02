import json
import os
import stuff
def equip():
    y=True
    while y==True:
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            player=data[8]
        with open("weapondata.json", "r") as wjson:
            weaponlist = json.load(wjson)
        equip=input("Would you like to Equip or Unequip an item? (Enter to break) ")
        if equip=="Equip":
            check=input("Would you like to equip a Weapon or Armor? (Enter to go break) " )
            if check=="Armor":
                print(player['Inventory:'])
                armorcheck=input("Would you like to equip Boots, Leggings, a Chestplate, or a Helmet? ")
                if armorcheck=="Boots":
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
                    else:
                        print("Boots already equipped, not in inventory, or unequipable for your class.")
                if armorcheck=="Leggings":
                    for i in range(len(stuff.LeggingsList)):
                        print(stuff.LeggingsList[i].Name, " ", stuff.LeggingsList[i].Equipable)
                    leggingscheck=input("What leggings would you like to equip? ")
                    for i in range(len(stuff.LeggingsList)):
                            if leggingscheck in stuff.LeggingsList[i].Name:
                                selectleggings=stuff.LeggingsList[i]
                    if leggingscheck in player['Inventory:'] and player['Legging:'] == "N/A" and player['Class:'] in selectleggings.Equipable:
                        player['Leggings:']=selectleggings.Name
                        player['BaseHP:']=player['BaseHP:']+selectleggings.HP
                        new_file = "updated.json"
                        with open(new_file, "w") as pjson:
                            json_string = json.dumps(data, indent=4)
                            pjson.write(json_string)
                        os.remove("player.json")
                        os.rename(new_file, "player.json")
                    else:
                        print("Leggings already equipped, not in inventory, or unequipable for your class.")
                if armorcheck=="Chestplate":
                    for i in range(len(stuff.ChestplateList)):
                        print(stuff.ChestplateList[i].Name, " ", stuff.ChestplateList[i].Equipable)
                    chestplatecheck=input("What chestplate would you like to equip? ")
                    for i in range(len(stuff.ChestplateList)):
                            if chestplatecheck in stuff.ChestplateList[i].Name:
                                selectchestplate=stuff.ChestplateList[i]
                    if chestplatecheck in player['Inventory:'] and player['Chesplate:'] == "N/A" and player['Class:'] in selectchestplate.Equipable:
                        player['Chestplate:']=selectchestplate.Name
                        player['HpMultiplier:']=player['HpMultiplier:']+selectchestplate.HP
                        new_file = "updated.json"
                        with open(new_file, "w") as pjson:
                            json_string = json.dumps(data, indent=4)
                            pjson.write(json_string)
                        os.remove("player.json")
                        os.rename(new_file, "player.json")
                    else:
                        print("Chestplae already equipped, not in inventory, or unequipable for your class.")
                if armorcheck=="Helmet":
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
                    else:
                        print("Helmet already equipped, not in inventory, or unequipable for your class.")
            elif check=="Weapon":
                if player['Weapon2:']=="N/A":
                    print(player['Inventory:'])
                    weaponcheck=input("What weapon would you like to equip? ")
                    if weaponcheck in player['Inventory:']:
                        for i in range(len(weaponlist)):
                            if weaponcheck in weaponlist[i]["Name"]:
                                selectweapon=weaponlist[i]
                        player['Weapon2:']=selectweapon['Name']
                        print(player['Weapon2:'], "was equipped!")
                        for i in range(len(weaponlist[i]['Moves'])):
                            player['Moves:'].append(selectweapon['Moves'][i])
                        new_file = "updated.json"
                        with open(new_file, "w") as pjson:
                            json_string = json.dumps(data, indent=4)
                            pjson.write(json_string)
                        os.remove("player.json")
                        os.rename(new_file, "player.json")
                    else:
                        print("Max weapons already equipped.")
        elif equip=="Unequip":
            check=input("Would you like to unequip a Weapon or Armor? (Enter to go break) " )
            if check=="Armor":
                armorcheck=input("Would you like to unequip Boots, Leggings, a Chestplate, or a Helmet? ")
            elif check=="Weapon":
                if not player['Weapon2:']=="N/A":
                    weaponcheck=input("What weapon would you like to unequip? ")
                    for i in range(len(weaponlist)):
                        if weaponcheck in weaponlist[i]["Name"]:
                            selectweapon=weaponlist[i]
                    print(selectweapon['Name'], "was unequipped!")
                    for i in range(len(selectweapon['Moves'])):
                         if selectweapon['Moves'][i] in player['Moves:']:
                            player['Moves:'].remove(selectweapon['Moves'][i])
                    if weaponcheck==player['Weapon2:']:
                        player['Weapon2:']="N/A"
                    elif weaponcheck==player['Weapon1:']:
                        player['Weapon1']=player['Weapon2']
                        player['Weapon2:']="N/A"
                    else:
                        print("Not an equipped weapon.")
                    new_file = "updated.json"
                    with open(new_file, "w") as pjson:
                        json_string = json.dumps(data, indent=4)
                        pjson.write(json_string)
                    os.remove("player.json")
                    os.rename(new_file, "player.json")
                else:
                    print("You cannot unequip a weapon with only 1 weapon equipped.")
        else:
            break
equip()