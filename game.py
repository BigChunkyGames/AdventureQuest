import random
from SlotMachine import Slots  # Slot machine from SlotMachine.py
from RockPaperScissors import RPSGame  # RPSGame from RockPaperScissors.py
from utils import * # import all functions from utils
from intro import *
from player import *
from places.maintown import *

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.")

#TODO: assuming new game each time. Should ask to load saved game data or start 
# new game. Below line creates a new player object but should load if loading saved game
player = Player() #make new player object in player.py



debug = 1



# Define Functions

def main():
    #intro()
    player.charcreation() 
    introduction(player)
    maintown(player)

if debug == 1:
    player.aspect['name'] = "name"
    player.aspect['gender'] = "boi"
    player.aspect['heshe'], player.aspect['HeShe'], player.aspect['hisher'] = "he", "He", "his"
    player.aspect['occ'], player.aspect['viverb'], player.aspect['skill1'], player.aspect['skill2'] = "fireman", "stab", "sewing", "rubiks cube solving"
    player.aspect['town'], player.aspect['hills'] = "Swagsburgh", "Peak's Hills"
    player.aspect['adj1'], player.aspect['adj2'], player.aspect['adj3'], player.aspect['adj4'], player.aspect['adj5'] = "cool", "neato", "sick nasty", "wiggity wiggity whack", "excellent"
    maintown(player)
else:
    main()
