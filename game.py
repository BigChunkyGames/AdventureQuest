print('loading...')

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
from source.places_babel import babel


clear() 

class Game: # perhaps this is what should be saved
    def __init__(self):
        self.player= Player()
        self.player.devMode = False 

    def start(self):
        #os.system('mode con: cols='+WINDOW_WIDTH+' lines='+WINDOW_HEIGHT) # set dimensions of window (imported from utils)
        if not self.player.devMode: # not dev mode
            Animation('introAnimation')
            if newOrLoad(self.player): # loads or returns true
                self.player.charcreation() 
                introduction(self.player)
                maintown(self.player)
        else: # dev mode
            devMode(self.player)
            #Sound('worry 1.mp3')
            #loadGame(self.player)
            #grandpasTrailer(self.player)
            #burntTown(self.player)
            #babel(self.player)
            #introduction(self.player)
            #maintown(self.player)
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

            c = Combat(self.player) # jump to combat

            self.player.openInventory()
            
            #s = Slots(self.player)
            #s.slot_machine()

            world(self.player)

g = Game()
try:
    g.start()
except Exception as e:
    if g.player.devMode:
        printException()
    else:
        bug(g.player, assertFalse=False)
        printException()
    while True: input('')



printSlowly("The End", secondsBetweenChars=.4)
Animation('credits')

