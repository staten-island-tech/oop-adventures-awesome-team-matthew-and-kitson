from moves import moves
from moves import playermoves
with open("player.json", "r") as pjson:
    input=input("What move would you like to use? ")
    for i in range(len(pjson[8]['Moves1:'])):
        if pjson[8]['Moves1:']==input:
            if 