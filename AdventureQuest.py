# -*- coding: utf-8 -*-

print('loading...')
import random
from source.utils import Sound, show , wait # import all functions from utils
from source.intro import charCreation, introduction
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
import sys
from source.places_pod import pod

clear() 


class Game:
    def __init__(self):
        self.player= Player()
        self.player.devMode = True 

    def start(self):
        if not self.player.devMode: # not dev mode
            # FIXME animation started not wokring????????
            setConsoleWindowSize(WINDOW_WIDTH, 15) # set dimensions of window (imported from utils)
            Animation('introAnimation')
            setConsoleWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
            if newOrLoad(self.player): # loads or returns true
                charCreation(self.player) 
                introduction(self.player)
                maintown(self.player)
        else: # dev mode
            devMode(self.player)
            #Sound(self.player, 'yes.wav')
            #saveGame(self.player, printAboutIt=True)
            #loadGame(self.player)

            
            #yesno(self.player)
            
            # places 

            #pod(self.player)
            #grandpasTrailer(self.player)
            #burntTown(self.player)
            #babel(self.player)
            #introduction(self.player)
            #maintown(self.player)
            
            #dogeTown(self.player)
            #flowers(self.player)
            #self.player.history.append('owns worm home')
            #wormHome(self.player)

            # ui

            #bonysShop(self.player)
            #maintownShop(self.player)
            

            # lisht = []
            # lisht.append(i)
            # x = ShopUI(self.player, "name of shop", lisht, )
            # x.run()

            #c = Combat(self.player, biome='plains') # jump to combat

            #self.player.openInventory()
            
            #s = Slots(self.player)
            #s.slot_machine()

        while True:
            world(self.player)

g = Game()
# try:
g.start()
# except Exception as e:
#     if g.player.devMode:
#         print(e)
#         print('\nand the other exception text: \n')
#         printException()
#     else:
#         bug(g.player, assertFalse=False)
#         printException()
#     while True: input('')



printSlowly("The End", secondsBetweenChars=.4)
#Animation('credits')

