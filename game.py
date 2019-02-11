import random
from source.utils import * # import all functions from utils
from source.intro import *
from source.places_maintown import *
from source.player import *
from source.devMode import *
from source.world import *
from source.places_flowers import flowers
from source.places_wormHome import tea, wormHome
from source.places_dogeTown import dogeTown, bonysShop, getBook
from source.places_burntTown import burntTown
from source.shopUI import ShopUI
from source.combat import Combat
from source.enemy import Enemy
from source.SlotMachine import *
from source.places_grandpasTrailer import grandpasTrailer

clear() 
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.\n")

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
            #grandpasTrailer(self.player)
            #burntTown(self.player)
            
            #introduction(self.player)
            maintown(self.player)
            #bonysShop(self.player)
            #maintownShop(self.player)
            #dogeTown(self.player)

            #flowers(self.player)

            #self.player.choices.append('owns worm home')
            #wormHome(self.player)
            

            # lisht = []
            # lisht.append(i)
            # x = ShopUI(self.player, "name of shop", lisht, )
            # x.run()

            #c = Combat(self.player) # jump to combat

            #self.player.openInventory()
            
            #s = Slots(self.player)
            #s.slot_machine()

            world(self.player)
        
#TODO: assuming ne
# w game each time. Should
#  ask to load saved game data or start 
# new game. Below line creates a new game object but should
# \ load if loading saved" game
g = Game()
g.start()

print ("the end")

