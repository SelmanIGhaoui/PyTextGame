import rich
from interactions import *
from print_text import *

slow_print("Welcome to...", delay = 0.25, useStyle=dangerStyle)
print_title("The Horror Manor Modified!")


currentlocation = "entrance"

inventory = []



rooms = {
    "entrance": {
        "east" : "saloon",
        "item" : [],
        "interactable" : [],
        "locked doors" : ""
    },
    "saloon" : {
        "south" : "kitchen",
        "east" : "workshop",
        "west" : "entrance",
        "item" : [],
        "interactable" : [],
        "locked doors" : ""
    },
    "kitchen" : {
        "north" : "saloon",
        "east" : "garden",
        "item" : ["kitchen knife", "key"],
        "interactable" : ["locked door"],
        "locked doors" : "east"
    },
    "garden" : {
        "west" : "kitchen",
        "north" : "workshop",
        "item" : ["shovel"],
        "interactable" : ["grave"],
        "locked doors" : ""
    },
    "workshop" : {
        "west" : "saloon",
        "south" : "garden",
        "item" : ["hammer", "screw", "monster"],
        "interactable" : [],
        "locked doors" : ""
    }
}

while True:
    print_dialogue("You are in the ", currentlocation)
    print_instruction("What do you do?")
    action = input(">")

    actionList = action.split(" ", 1)

    if actionList[0] == "go":
        direction = actionList[1]
        if direction in rooms[currentlocation]:
            if not direction in rooms[currentlocation]["locked doors"]:
                currentlocation = rooms[currentlocation][direction]
                print_dialogue("You moved to ", currentlocation)
            else:
                print_notif("The door is locked!")
        else:
            print_notif("There are no doors in that direction.")
    
    if actionList[0] == "take":
        targetItem = actionList[1]
        if "item" in rooms[currentlocation]:
            if targetItem in rooms[currentlocation]["item"]:
                print("Picked up ", targetItem)
                inventory.append(targetItem)
                rooms[currentlocation]["item"].remove(targetItem)
                print(inventory)
            else:
                print_notif("There is no", targetItem)
        else:
            print_notif("There are no items in this room.")

    if actionList[0] == "use":
        usedItem = actionList[1]
        if usedItem in inventory:
            itemUsed = False
            for interactable in rooms[currentlocation]["interactable"]:
                if (usedItem, interactable) in interactions:
                    print(interactions[(usedItem, interactable)])
                    if (usedItem, interactable) == ("key", "locked door"):
                        if rooms[currentlocation]["locked doors"] != "":
                            rooms[currentlocation]["locked doors"] = ""
                    itemUsed = True
            if not itemUsed:
                print_dialogue("You can do nothing with this here.")
        else:
            print_dialogue("You don't have this item.")

    if currentlocation == "garden" and "key" in inventory:
        print("You have found the exit and also have the key to escape!")
        print("Congratulatlions! You won!")
        break

    if "monster" in rooms[currentlocation]["item"]:
        print("You see a monster!")
        if "kitchen knife" in inventory:
            print("You stab the monster with the knife!")
            print("The evil has been defeated! You win!")
            break
        else:
            print("It kills you mercielessly! You lose!")
            break



print("GAME OVER!", 0.3)