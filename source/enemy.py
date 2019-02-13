# this class makes enemies! obviously!!!!!!!
import random
from source.lists import *

class Enemy:

    # 
    # make sure not to misspell those
    def __init__(self, player, biome, powerLevel=0):
        '''biome options are plains, firest, desert, mountain'''
        self.player = player
        # traits
        self.biome = biome
        self.powerLevel = powerLevel # can be a float, casted to int during scaling, between -inf and 3
        self.name = getRandomEnemyName(biome)
        # stats
        self.maxhp = self.setHP()
        self.hp = self.maxhp #max hp by default
        self.attack = self.setAttack()
        self.missChancePercent = self.setMissChancePercent()
        self.xpworth = self.setxpworth()
        self.listOfAttacks = None

    def setHP(self): 
        return self.player.scale(10+self.powerLevel) # SCALING

    def setAttack(self):
        return self.player.scale(2+self.powerLevel) # SCALING
        
    def setxpworth(self):
        return self.player.scale(random.randint(2+self.powerLevel,3+self.powerLevel))  # SCALING
    
    def setMissChancePercent(self):
        return int(40 - 2*self.powerLevel) # SCALING

    def getRandomAttack(self):
        if self.listOfAttacks == None: return getRandomAttackVerb()  
        else: return getRandomIndex(self.listOfAttacks)

    def setName(self, text): # idk why i need this but e.name = ... doesnt work
        self.name = text

    def setListOfAttacks(self, listt):
        self.listOfAttacks= listt
        
