def handle_go(location):
    direction = location
    global rooms
    global currentlocation
    if direction in rooms[currentlocation]:
        if not direction in rooms[currentlocation]["locked doors"]:
            currentlocation = rooms[currentlocation][direction]
            print("You moved to", currentlocation)
        else:
            print("The door is locked!")
    else:
        print("There are no doors in that direction.")

def handle_take(targetItem):
    global rooms
    global currentlocation
    global inventory
    if "item" in rooms[currentlocation]:
        if targetItem in rooms[currentlocation]["item"]:
            print("Picked up", targetItem)
            inventory.append(targetItem)
            rooms[currentlocation]["item"].remove(targetItem)
            print(inventory)
        else:
            print("There is no", targetItem)
    else:
        print("There are no items in this room.")