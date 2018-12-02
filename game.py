import random
from SlotMachine import Slots  # Slot machine from SlotMachine.py
from RockPaperScissors import RPSGame  # RPSGame from RockPaperScissors.py
from utils import * # import all funsctions from utils
from intro import *
from player import *
from places.maintown import *
from devMode import *

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.")

# Define Functions

class Game: # perhaps this is what should be saved
    def __init__(self):
        self.player= Player()
        self.devMode = 1 # on

    def getPlayer(self):
        return self.player

    def start():
        self.player.charcreation() 
        introduction(self.player)
        maintown(self.player)
        
#TODO: assuming new game each time. Should ask to load saved game data or start 
# new game. Below line creates a new game object but should load if loading saved game
g = Game()
if g.devMode==1: g.player = devMode(Player()) # make player into a god and teleport somehwere
print "1" + g.getPlayer().getName()
if g.devMode != 1 : g.start()

print "the end"
