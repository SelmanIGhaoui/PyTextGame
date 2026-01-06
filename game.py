import os
import rich

from print_text import *
import data as d
import commands as cmd

slow_print("Welcome to...", delay = 0.25, useStyle=dangerStyle)
print_title("The Horror Manor!")

print_instruction("Do you want to load a previous save? (y/n)")
loadChoice = input(">")

while loadChoice.lower() not in ["y", "n"]:
    print_instruction("Do you want to load a previous save? (y/n)")
    loadChoice = input(">")

if loadChoice.lower() == "y":
        d.load_data()    

while True:
    print_dialogue("You are in the ", d.currentlocation)
    print_instruction("What do you do?")
    action = input(">")

    os.system('cls' if os.name == 'nt' else 'clear')

    actionList = action.split(" ", 1)

    if actionList[0] == "go":
        cmd.handle_go(actionList[1])
    
    if actionList[0] == "take":
        cmd.handle_take(actionList[1])

    if actionList[0] == "use":
        cmd.handle_use(actionList[1])

    if actionList[0] == "talk":
        cmd.handle_dialogue(cmd.d1)

    if actionList[0] == "quit":
        cmd.handle_quit()

    if d.currentlocation == "garden" and "key" in d.inventory:
        print("You have found the exit and also have the key to escape!")
        print("Congratulatlions! You won!")
        break

    if "monster" in d.rooms[d.currentlocation]["item"]:
        print("You see a monster!")
        if "kitchen knife" in d.inventory:
            print("You stab the monster with the knife!")
            print("The evil has been defeated! You win!")
            break
        else:
            print("It kills you mercielessly! You lose!")
            break



print("GAME OVER!")