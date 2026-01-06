from rich.console import Console
from rich.style import Style
import time
import art


console = Console()

dangerStyle = Style(color= "red", bold= True, bgcolor= "white")
dialogueStyle = Style(color= "blue")
instructionStyle = Style(color= "green")
notifStyle = Style(color= "magenta")


def print_title(message):
    art.tprint(message)

def slow_print(*message, delay, useStyle):
    for line in message:
        for char in line:
            console.print(char, end = "", style= useStyle)
            time.sleep(delay)
        console.print("", end = "")
    console.print("") 

def print_dialogue(*message):
    slow_print(message, delay = 0.15, useStyle = dialogueStyle)

def print_instruction(*message):
    slow_print(message, delay = 0.2, useStyle = instructionStyle)

def print_notif(*message):
    slow_print(message, delay = 0.1, useStyle = notifStyle)
    