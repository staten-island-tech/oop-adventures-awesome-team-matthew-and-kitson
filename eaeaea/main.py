from merchant import Merchant
from hero import Hero
import json

guy=Merchant("Name", ["ruby", "diamond", "silver_band", "gold_band"])
me=Hero("Me", 500, [])
guy.welcome

find = input("What Do you want to buy/sell: ")
if find in guy.product:
    print(True)


with open("item.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)





 
for i in (data): 
    if find in i['Name']:
        data.append(i[data])
if not data:
    print("No Value")
else:
    print("You have Sold 'Name' for 'Price'") 

