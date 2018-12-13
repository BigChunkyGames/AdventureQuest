import random
from utils import * # import all functions from utils
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

    def start(self):
        if not player.devmode:
            player.charcreation() 
            introduction(player)
        maintown(player)
        show("NOW LOADING: literally the entire world")
        world(player)

    def start():
        self.player.charcreation() 
        introduction(self.player)
        maintown(self.player)
        
#TODO: assuming new game each time. Should ask to load saved game data or start 
# new game. Below line creates a new game object but should load if loading saved game
g = Game()
g.start()


print "the end"
