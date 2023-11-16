import json
import os
## Create Class for creating new dictionaries here
class Games:
    def Create(self):
        name=input("Enter the name of the game:")
        company=input("Enter the company that made the game:")
        year=input("Enter the year the game was made:")
        genre=input("Enter the main genre of the game:")
        rating=int(input("Enter a personal rating for said game:"))
        glist={'Name:':name,'Company:':company,'Year:':year,'Genre:':genre,'Rating:':rating}
        return(glist)
    def __str__(thing):
        return f"{thing.name}, {thing.company}"
s=True
while s==True:
    check=input("Would you like to add a game to the dictionary? Yes/No:")
    if check=="No":
        exit()
    with open("data.json", "r") as f:
        data = json.load(f)
        game= Games()
        glist=game.Create()
        data.append(glist)
    #given code below
    new_file = "updated.json"
    with open(new_file, "w") as f:
        json_string = json.dumps(data, indent=4)
        f.write(json_string)
    os.remove("data.json")
    os.rename(new_file, "data.json")