# The purpose of this file is to hold utility functions that are commonly used

import os   # Used to clear terminal
import random
# from colorama import *
import time
# init(autoreset=True) # init colors and reset to white each time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal

def show(text):
    #  Displays text, waits for 'enter' before continuing.
    print(text)
    input = raw_input("... ")
    from game import g #briefly import the player object
    if input == "i":
        g.getPlayer().openInventory()

def input(): # alwase use this unless you dont want the inventory to be able to be opened
    input = raw_input("> ").lower().strip()
    if input == "i":
        from game import g #briefly import the entire game object #FIXME
        g.getPlayer().openInventory()
    else:
        return input

def wait(seconds):
    time.sleep(seconds)

def yesno():
    #  Returns True if user input is yes, returns False if no.
    while True:
        userinput = raw_input("> ").lower().strip()
        if userinput == "yes" or userinput == "y":
            return True
        elif userinput == "no" or userinput == "n":
            return False
        else:
            print("You must choose 'yes' or 'no'.")

def dichotomy(option1, option2):
    # Returns True if user input is option1, returns False if option2.
    # Make sure the options are in stripped lowercase form
    while True:
        userinput = raw_input("> ").lower().strip()
        if userinput == option1:
            return True
        elif userinput == option2:
            return False
        else:
            print("You must choose 'yes' or 'no'.")

# Might be useful later in the game
def checklevel(xp):
    for x in range(1,10001):
        if xp < (x**1.68)*100:
            return x - 1

# takes an array returns a random index
def getRandomIndex(arr):
    return arr[random.randint(0, len(arr)-1)]
    
# HOW TO PRINT COLOR
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text') # doesnt work?