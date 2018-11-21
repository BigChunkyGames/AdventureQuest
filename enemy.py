# this class makes enemies! obviously!!!!!!!
import random
from lists import *

class Enemy:

    # biome options are plains, firest, desert, mountain
    # make sure not to misspell those
    def __init__(self, player, enemyLevel, biome):
        self.playerCopy = player
        # traits
        self.biome = biome
        self.name = self.setEnemyName(biome)
        # stats
        self.enemyLevel = enemyLevel # should not be negative
        self.hp = self.setHP()
        self.attack = self.setAttack()

    def setHP(self):
        return 5 + enemyLevel * playerCopy.level + random.randint(playerCopy.level, playerCopy.level * 2)
        # 5 + the product of enemy and player levels + a random amount between player level and twice player level
        # this means that player's attack should scale close to the square of their level

    def setAttack(self):
        return 1 + enemyLevel * (playerCopy.level / 2) 
        # 1 + product of enemy level and half of player level 
        # so if levels are 3 and 3, attack = 7
        # or 0 and 0, attack = 1

    def setEnemyName(self, biome):
        return getRandomEnemyName(biome)
        

