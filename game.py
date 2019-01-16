import random
from source.utils import * # import all functions from utils
from source.intro import *
from source.places.maintown import maintown
from source.player import *
from source.devMode import *
from source.world import *
from source.places.flowers import flowers
from source.places.wormHome import tea

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.")

# Define Functions

class Game: # perhaps this is what should be saved
    def __init__(self):
        self.player= Player()
        self.player.devMode = True 

    def getPlayer(self):
        return self.player

    def start(self):
        if not self.player.devMode: 
            self.player.charcreation() 
            introduction(self.player)
            maintown(self.player)
        else: # dev mode
            devMode(self.player)

            flowers(self.player)

            #c = Combat(self.player,Enemy(self.player, "forest")) # jump to combat
            x = InventoryUI(self.player)
            x.run()
            print x.result
            #maintown(self.player)

            #world(self.play
            # er)
        
#TODO: assuming new game each time. Should ask to load saved game data or start 
# new game. Below line creates a new game object but should
# \ load if loading saved game
g = Game()
g.start()



print "the end"



''' tests



'''