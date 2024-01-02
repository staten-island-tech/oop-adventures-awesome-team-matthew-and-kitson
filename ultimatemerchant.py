from merchant import Merchant
import stuff
import json
import os
class ultmerchant:
    nonsellableitems=["Sword", "Mace", "Shield", "Staff", "Necromancer Staff", "Magic Book", "Healer Staff", "Bow", "Slingshot"]
    sellableitems=[stuff.Trinket, stuff.Gold_Goblet, stuff.Silver_Goblet, stuff.Gold_Ring, stuff.Silver_Ring, stuff.Gold_Necklace, stuff.Silver_Necklace, stuff.Gold_Band, stuff.Silver_Band, stuff.Gold_Bangle, stuff.Silver_Bangle, stuff.Diamond, stuff.Ruby, stuff.LeatherHelmet, stuff.PlateHelmet, stuff.ConeHat, stuff.LeatherChestplate, stuff.MagicRobe, stuff.PlateChest, stuff.Trousers, stuff.LeatherLeggings, stuff.PlateLeggings, stuff.LeatherBoots, stuff.HeavyBoots, stuff.PlateBoots]
    def buy(x):
        y=True
        while y==True:
            with open("player.json", "r") as pjson:
                data = json.load(pjson)
                goldnum=data[8]['Gold:'][0]
                print("Gold:", goldnum)
                for i in range(len(x.products)):
                    print(x.products[i].Name, ",", x.products[i].Price)
                find = input("What do you want to buy? If nothing, enter 'break': ")
                z=None
                if find=='break':
                    break
                productlist=x.products
                for i in range(len(productlist)):
                    if find in productlist[i].Name:
                        remover=productlist[i]
                        z=productlist[i].Price
                if not z == None:
                    if data[8]['Gold:'][0]>=z:
                        x.sell(remover)    
                        inventory=data[8]['Inventory:']
                        inventory.append(remover.Name)
                        goldlist=data[8]['Gold:']
                        ngold=goldnum-z
                        goldlist.append(ngold)
                        goldlist.remove(goldnum)
                        new_file = "updated.json"
                        with open(new_file, "w") as pjson:
                            json_string = json.dumps(data, indent=4)
                            pjson.write(json_string)
                        os.remove("player.json")
                        os.rename(new_file, "player.json")
                        print("You have bought", find)
                    else:
                        print("You do not have enough money to buy this item.")
                else:
                    print("Item not found in merchant and/or not an item.")
    def sell():
        item=None
        with open("player.json", "r") as pjson:
            data = json.load(pjson)
            inventory=data[8]['Inventory:']
            print(inventory)
            find = input("What do you want to Sell? ")
            if find in inventory and not find in ultmerchant.nonsellableitems:
                for i in range(len(ultmerchant.sellableitems)):
                    if find in ultmerchant.sellableitems[i].Name:
                        item=ultmerchant.sellableitems[i]
                        inventory.remove(find)
                        z=item.Price
                        goldnum=data[8]['Gold:'][0]
                        goldlist=data[8]['Gold:']
                        ngold=goldnum+z
                        goldlist.append(ngold)
                        goldlist.remove(goldnum)
                        new_file = "updated.json"
                        with open(new_file, "w") as pjson:
                            json_string = json.dumps(data, indent=4)
                            pjson.write(json_string)
                        os.remove("player.json")
                        os.rename(new_file, "player.json")
        if not item == None:
            print("You have sold", item.Name, "for", item.Price, "Gold!")
        else:
            print("You do not have this item or it is of no value. ")
    def buyingselling(items):
        guy=Merchant(items)
        guy.welcome()
        y=True
        while y==True:
            x=input('Do you want to Buy or Sell? If neither, just enter. ')
            if x=="Buy":
                ultmerchant.buy(guy)
            elif x=='Sell':
                ultmerchant.sell()
            else:
                break