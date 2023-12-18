from merchant import Merchant
from hero import Hero
import json

guy=Merchant("Filler", ["1", "2", "3", "4"])
me=Hero("Me", 500, [])
guy.welcome




with open("item.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

find = input("What Do you want to buy/sell: ").capitalize()
List = []
money=len(data)


for i in range(money): 
    if find in data[i]['Name']:
        List.extend([data[i]])
if not List:
    print("No Value")
else:
    print() 

