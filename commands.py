import data as d
from print_text import *
import sys
from dialogue import *

def handle_go(direction):
    if direction in d.rooms[d.currentlocation]:
        if not direction in d.rooms[d.currentlocation]["locked doors"]:
            d.currentlocation = d.rooms[d.currentlocation][direction]
            print_dialogue("You moved to ", d.currentlocation)
        else:
            print_notif("The door is locked!")
    else:
        print_notif("There are no doors in that direction.")

def handle_take(targetItem):
    if "item" in d.rooms[d.currentlocation]:
        if targetItem in d.rooms[d.currentlocation]["item"]:
            print("Picked up ", targetItem)
            d.inventory.append(targetItem)
            d.rooms[d.currentlocation]["item"].remove(targetItem)
            print(d.inventory)
        else:
            print_notif("There is no", targetItem)
    else:
        print_notif("There are no items in this room.")

def handle_use(targetItem):
    if targetItem in d.inventory:
        itemUsed = False
        for interactable in d.rooms[d.currentlocation]["interactable"]:
            if (targetItem, interactable) in d.interactions:
                print(d.interactions[(targetItem, interactable)])
                if (targetItem, interactable) == ("key", "locked door"):
                    if d.rooms[d.currentlocation]["locked doors"] != "":
                        d.rooms[d.currentlocation]["locked doors"] = ""
                itemUsed = True
        if not itemUsed:
            print_dialogue("You can do nothing with this here.")
    else:
        print_dialogue("You don't have this item.")

def handle_dialogue(dialogue):
    current_segment = dialogue["start"]
    dialgue_ended = False
    while not dialgue_ended:
        for line in current_segment["lines"]:
            print_dialogue(line)
        if current_segment["options"] == []:
            dialgue_ended = True
        else:
            for choice in current_segment["options"]:
                print(choice, end= "    ")
            print("")
            dialogue_choice = input(">")
            while dialogue_choice not in current_segment["options"]:
                dialogue_choice = input(">")
            current_segment = dialogue[dialogue_choice]

def handle_quit():
    print("Quitting the game...")
    d.save_data()
    sys.exit()

