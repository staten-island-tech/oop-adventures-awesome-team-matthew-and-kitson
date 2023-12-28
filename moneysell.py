from merchant import Merchant
from hero import Hero
import json

guy=Merchant("Name", ["ruby", "diamond", "silver_band", "gold_band"])
player=Hero("Me", 500, [])
def buy(x):
    y=True
    while y==True:
        find = input("What Do you want to Buy? If nothing, enter 'break':").lower()
        z=x.products.price
        if find in guy.product:
            if player.money>z:
                x.sell()
                print("You have bought", find)
def buyingselling(x):
    x.welcome()
    y=True
    while y==True:
        x=input('Do you want to Buy or Sell? If neither, just enter. ')
        if x=="Buy":
            number=int(input("How many items do you want to buy?"))
            for i in range(number):
                buy()
        elif x=='Sell':
            item=None
            find = input("What Do you want to Sell? ").lower()
            if find in player.inventory:
                item=find
                player.inventory.append(item)
            if item == find:
                print("You have sold", item[0], "for", item['Price:'])
            if item == None:
                print("You do not have this item or it is of no value")
        else:
            break