import random
import json
with open("player.json", "r") as pjson:
    data = json.load(pjson)
    def swordswing(x, y):
        player=data[8]
        enemy=y
        
