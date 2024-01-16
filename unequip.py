import json
import os
import stuff
weaponlist=stuff.WeaponList
def unequip():
    with open("player.json", "r") as pjson:
        data = json.load(pjson)
        player=data[8]
    check=input("Would you like to unequip a Weapon or Armor? (Enter to go break) " )
    if check=="Armor":
        armorcheck=input("Would you like to unequip Boots, Leggings, a Chestplate, or a Helmet? ")
        if armorcheck=="Boots":
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
        if armorcheck=="Leggings":
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
        if armorcheck=="Chestplate":
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
        if armorcheck=="Helmet":
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
    elif check=="Weapon":
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