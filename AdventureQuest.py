# -*- coding: utf-8 -*-

print('loading...')
# try:
import threading
import random
from source.utils import Sound, show , wait 
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
from source.places_furnitureTown import *
# except Exception as e:
#     print(e)
#     print('Failed to do initial import.')
#     input('dang it')



clear() 


class Game:
    def __init__(self):
        self.player= Player()
        self.player.devMode = True 

    def start(self):
        if not self.player.devMode: # not dev mode
            # FIXME animation started not wokring????????
            setConsoleWindowSize(WINDOW_WIDTH, 16) # set dimensions of window (imported from utils)
            Animation('introAnimation')
            n = newOrLoad(self.player) # loads or returns true
            setConsoleWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
            if n == True: 
                charCreation(self.player) 
                introduction(self.player)
                maintown(self.player)
        else: # dev mode
            devMode(self.player)
            setConsoleWindowSize(WINDOW_WIDTH, 14) # so i can see it in vs code

            # self.player.die()





            furnitureTown(self.player)
            #inflitrationQuest(self.player)
            


            #Sound(self.player, 'yes.wav')
            # self.player.sleep()


            # saveGame(self.player, printAboutIt=True)
            #loadGame(self.player)

            #yesno(self.player)
            
            # places 

            #pod(self.player)
            # i = Item(self.player, "Lasagna", customDescription='A steamy lasagna in a large plastic container. Mom said to take this to Grandpa. She also said that he lives to the East of ', _type='consumable', consumable=Consumable(self.player, heal=10, karma=-3, consumeText='Hope Grandpa won\'t be mad that you ate his lasagna!'))
            # self.player.addToInventory(i)
            # grandpasTrailer(self.player)
            #burntTown(self.player)
            #babel(self.player)
            #introduction(self.player)
            # maintown(self.player)
            
            #dogeTown(self.player)
            #flowers(self.player)
            #self.player.history.append('owns worm home')
            #wormHome(self.player)

            # ui

            # bonysShop(self.player)
            # maintownShop(self.player)
            

            # lisht = []
            # lisht.append(i)
            # x = ShopUI(self.player, "name of shop", lisht, )
            # x.run()

            # c = Combat(self.player, biome='plains') # jump to combat

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



theEnd(g.player)

