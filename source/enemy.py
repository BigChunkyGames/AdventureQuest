# this class makes enemies! obviously!!!!!!!
import random
from lists import *

class Enemy:

    # biome options are plains, firest, desert, mountain
    # make sure not to misspell those
    def __init__(self, player, biome):
        self.player = player
        # traits
        self.biome = biome
        self.name = getRandomEnemyName(biome)
        # stats
        self.enemyLevel = player.level # for now enemies are always same level TODO should chnange based on difficulty of tile
        self.maxhp = self.setHP()
        self.hp = self.maxhp #max hp by default
        self.attack = self.setAttack()
        self.missChancePercent = self.setMissChancePercent()
        self.xpworth = self.setxpworth()
        self.listOfAttacks = None

    def setHP(self):
        return 5 + self.enemyLevel * self.enemyLevel + random.randint(self.player.level, self.player.level * 2)
        # 5 + the product of enemy and player levels + a random amount between player level and twice player level
        # this means that player's attack should scale close to the square of their level

    def setAttack(self):
        return 1 + self.enemyLevel * (self.player.level / 2) 
        # 1 + product of enemy level and half of player level 
        # so if levels are:
        # 0 and 0, attack = 1
        # 1 and 1, attack = 2
        # 2 and 2, attack = 3
        # 3 and 3, attack = 7
        
    def setxpworth(self):
        return random.randint(2,3) # with this it always takes about 4 encounters to level up

    # each level, enemies have 3% greater chance to hit starting at 60%
    def setMissChancePercent(self):
        return int(40 - (self.enemyLevel * 3) )

    def getRandomAttack(self):
        if self.listOfAttacks == None: return getRandomAttackVerb()  
        else: return getRandomIndex(self.listOfAttacks)

    def setName(self, text): # idk why i need this but e.name = ... doesnt work
        self.name = text
    def setListOfAttacks(self, listt):
        self.listOfAttacks= listt
        
# TODO: will have to playtest to see which functions are better for hp and attack        
    # def enemyhp(self, level):
    #     # HP is between (level * 48) and (level * 52)
    #     return level*random.randint(48, 52)

    # def enemyattack(self, level):
    #     # Attack is between (level * 10) and (level * 15)
    #     if level == 1:
    #         return 2
    #     else:
    #         return level * random.randint(10, 15)
