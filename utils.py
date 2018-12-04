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
    raw_input("... ")

def wait(seconds):
    time.sleep(seconds)

def yesno(player):
    #  Returns True if user input is yes, returns False if no.
    while True:
        userinput = input(player)
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

def input(player):
    while True:
        inp = raw_input("> ").lower().strip()
        if player.devmode and inp == "damage":
            player.takeDamage(int(raw_input("How much damage? : ")))
        elif inp == "hp":
            print("You have " + str(player.hp) + " out of " + str(player.maxhp) +  " HP. "),
            print("("),
            print(str(int(round(float(player.hp)/float(player.maxhp), 2) * 100))),
            print("% )")
        elif inp == "i" or inp == "inventory":
            print("Your inventory is currently not implemented.")
        elif inp == "me":
            print("You are a level " + str(player.level) + " " + player.aspect['occ'] + " with " + str(player.dogecoin) + " dogecoin to your name.")
        else:
            return inp
    
# HOW TO PRINT COLOR
#print(Fore.RED + 'some red text')
#print(Back.GREEN + 'and with a green background')
#print(Style.DIM + 'and in dim text') # doesnt work?