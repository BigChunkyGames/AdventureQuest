import random
from source.utils import show, clear
from source.lists import getRandomEnemyName, getRandomAttackVerb
from source.enemy import *
from source.combatUI import *
from source.item import tryForDrop, generateRandomArmourOrWeapon, generateRandomConsumable
#  TODO: consult other adventure games to see what a good attack:HP ratio is

class Combat:
    def __init__(self, player, biome=None, alert=True, enemy=None, enemyPowerLevel=0 ,startCombatNow=True):
        # will  use given enemy's power level over enemyPowerLevel
        self.player = player
        self.biome = biome
        self.song = self.getSong()
        self.result = None # win, escaped, lose
        if not enemy == None: # if giving enemy
            self.enemy = enemy
        else: 
            self.enemy = Enemy(player,biome, powerLevel=enemyPowerLevel) # make random enemy with given biome
        self.dropchance = 0 # TODO drops
        if alert: self.alert()
        if startCombatNow: self.startCombat()

        # TODO: May later be affected by level as well as biome

    def alert(self):
        # map.getTileDescription prints something about where you are.
        s = ''
        s += "From over your shoulder you notice " # TODO flavor
        s += self.enemy.name
        s += " attempting to " # TODO flavor text about realizing your're being attacked
        attack = getRandomAttackVerb() 
        if attack[-1] == "*": # if attack finishes the sentence
            s += attack[:-1] # remove *
        else :
            s += attack
            s += " you!"
        printc(s)
        show("@You're being attacked!@red@") 

    def startCombat(self, GivenCombatUI=None):
        self.player.inCombat = True
        if GivenCombatUI==None: 
            self.player.combatUI = CombatUI(self.player, self.enemy, song=self.song)
        else: 
            self.player.combatUI = GivenCombatUI
        self.player.combatUI.run()
        self.result = self.player.combatUI.result
        clear()
        if self.player.combatUI.result == "win":
            show("You defeated " + self.enemy.name + "!")
            self.player.gainXp(self.enemy.xpworth, scale=False) # xp already scales when creating enemy
            self.player.regenHealth()# gain health
            if tryForDrop(25): # TODO luck
                self.getLoot()
        elif self.player.combatUI.result == "lose":
            self.player.death()
        elif self.player.combatUI.result == "escaped":
            show("You escaped from " + self.enemy.name + "! That was a close one!")
        elif self.player.combatUI.result == 'inventory':
            self.player.openInventory()
            self.player.combatUI.resume()
            self.startCombat(self.player.combatUI)
        self.player.inCombat = False
        return

    def getLoot(self):
        rand = random.randint(0,2)
        bonus = self.enemy.powerLevel
        if rand <=1: # 2/3 chance
            item = generateRandomArmourOrWeapon(self.player, bonus=bonus)
        elif rand ==2:
            item = generateRandomConsumable(self.player, powerLevel=bonus)
        show("@You found "+item.name +".@green@")
        #self.player.addToInventory(item)
        self.player.inventory.insert(0, item)

    def getSong(self):
        if self.biome == 'desert':
            return 'Third Castle.wav'
        else:
            return 'worry 1.wav'

        


        
        
