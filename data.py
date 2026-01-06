from interactions import *
import json

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

def save_data():
    full_data = {
    "location": currentlocation,
    "inventory": inventory,
    "rooms": rooms
    }

    data_string = json.dumps(full_data, indent=4)

    f = open("savefile.json", "w")
    f.write(data_string)

    f.close()

def load_data():

    try:
        f = open("savefile.json", "r")

    except:
        print("No save file found!")
        return
    
    full_data = json.load(f)
    
    global currentlocation
    currentlocation = full_data["location"]
    global inventory
    inventory = full_data["inventory"]
    global rooms
    rooms = full_data["rooms"]

    f.close()