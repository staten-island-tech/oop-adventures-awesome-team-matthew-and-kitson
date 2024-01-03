import json
def check():
    with open("player.json", "r") as pjson:
        data=json.load(pjson)
        while len(data)==8:
            from player_create import Player
            Player.ultcreate()
check()