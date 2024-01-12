import json
import os
import player_create
def check():
    with open("player.json", "r") as pjson:
        data=json.load(pjson)
    if not len(data)==8:
        data.remove(data[8])
        new_file = "updated.json"
        with open(new_file, "w") as pjson:
            json_string = json.dumps(data, indent=4)
            pjson.write(json_string)
        os.remove("player.json")
        os.rename(new_file, "player.json")
    player_create.Player.ultcreate()