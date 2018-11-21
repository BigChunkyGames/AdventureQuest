import random
from SlotMachine import Slots  # Slot machine from SlotMachine.py
from RockPaperScissors import RPSGame  # RPSGame from RockPaperScissors.py
from utils import * # import all functions from utils
from intro import *
from player import *
from places.maintown import *
from devMode import *

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.")

#TODO: assuming new game each time. Should ask to load saved game data or start 
# new game. Below line creates a new player object but should load if loading saved game

player = Player() #make new player object in player.py
debug = 1
if debug==1: devMode(player) # make player into a god and teleport somehwere

# Define Functions

def start():
    player.charcreation() 
    introduction(player)
    maintown(player)
    
if debug != 1 : start()

print "the end"
