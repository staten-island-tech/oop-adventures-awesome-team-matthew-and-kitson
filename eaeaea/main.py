from merchant import Merchant
from hero import Hero
import json

guy=Merchant("Name", ["ruby", "diamond", "silver_band", "gold_band"])
me=Hero("Me", 500, [])
guy.welcome

class merchant(): 

    with open("item.json", "r") as f:
    # Serialize the updated Python list to a JSON string
        data = json.load(f)
    guy=Merchant("Name", ["ruby", "diamond", "silver_band", "gold_band"])
    me=Hero("Me", 500, [])
    guy.welcome

    find = input("What Do you want to buy/sell: ").lower()
    if find in guy.product:
        print(True)



    item = None
 
    for i in (data): 
        if find in i['Name']:
            item = i['Name'] 
            me.inventory.append(item)
    if item == find:
        print("you have sold" item['Name:'] "for" item['Price:'])
    if item == None:
        print("you do not have this item or it is of no value")



