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
        self.enemyLevel = player.level # for now enemies are always same level TODO
        self.hp = self.setHP()
        self.attack = self.setAttack()

    def setHP(self):
        return 5 + self.enemyLevel * self.enemyLevel + random.randint(self.player.level, self.player.level * 2)
        # 5 + the product of enemy and player levels + a random amount between player level and twice player level
        # this means that player's attack should scale close to the square of their level

    def setAttack(self):
        return 1 + self.enemyLevel * (self.player.level / 2) 
        # 1 + product of enemy level and half of player level 
        # so if levels are 3 and 3, attack = 7
        # or 0 and 0, attack = 1
        

        
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
