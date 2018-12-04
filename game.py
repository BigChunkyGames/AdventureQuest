import random
from utils import * # import all functions from utils
from intro import *
from player import *
from places.maintown import *
from devMode import *

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.43P!")

# Define Functions

def start():
    if not player.devmode:
        player.charcreation() 
        introduction(player)
    maintown(player)
    show("NOW LOADING: literally the entire world")
    world(player)

# TODO: Ask to load saved game data or start new game

# if newgame:
player = Player() #make new player object in player.py
devMode(player) # make player into a god and teleport somehwere

start()

print "the end"
