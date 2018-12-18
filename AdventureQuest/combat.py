import random
from utils import show, clear
from lists import getRandomEnemyName, getRandomAttackVerb
from enemy import *
#  TODO: consult other adventure games to see what a good attack:HP ratio is

class Combat:
    def __init__(self, player, biome):
        self.player = player
        self.biome = biome
        self.enemy = Enemy(player,biome)
        self.dropchance = 0 # TODO drops
        self.alert()
        self.startCombat()

        # TODO: May later be affected by level as well as biome

    def tryForDrop(self, percent): # TODO drops
        dropchance = random.randint(1, 100)
        if dropchance <= percent:
            return True
        else:
            return False

    def alert(self):
        # map.getTileDescription prints something about where you are.
        print "From over your shoulder you notice",
        print self.enemy.name,
        print "attempting to", # TODO flavor text about realizing your're being attacked
        attack = getRandomAttackVerb() 
        if attack[-1] == "*": # if attack finishes the sentence
            print attack[:-1] # remove *
        else :
            print attack,
            print "you!"
        show("You're being attacked!") #TODO color

    def startCombat(self):
        # player goes first
        self.displayAttackOptions()
        
    def displayAttackOptions(self):
        while True:
            print(
        "test"  



            )
            break

