
# generates items
import random
from lists import getRandomWeaponName, getRandomItemPrefix

class Item():
    def __init__(self, player, name, description="", rarity = 'common', _type=None, damage=0, block=0, sellValue = None):
        '''
        Rarities: common, rare, epic, legendary
        Types: weapon, armour, consumable, quest
        '''
        self.player = player
        self.name = name
        self.description = description
        self.rarity = rarity 
        self.type = _type    

        self.damage = damage
        self.block = block

        if sellValue == None: self.sellValue = self.getSellValue() 

    def getSellValue(self):
        mult =1
        if self.rarity == 'rare': mult =2
        if self.rarity == 'epic': mult =3
        if self.rarity == 'legendary': mult =4
        return int( random.randint(self.player.level,self.player.level * 2) * mult ) # SCALING

    def buildItemDescriptionString(self):
        s = self.name + '[' + self.rarity.capitalize() + ']' + '\n'
        if self.damage > 0:
            s += 'Damage: ' + str(self.damage) + '\n'
        if self.block > 0:
            s += 'Block:  ' + str(self.block) + '\n'
        if self.sellValue > 0:
            s += 'Value:  ' + str(self.sellValue) + '\n'
        return s

def generateRandomWeapon(player, rarity = 'common', goodnessBoost=0, extreme=False): 
    ''' goodnessBoost makes the weapon a lot better (or worse if neg)
    '''
    prefix = generatePrefix(player, goodnessBoost+3)
    name = prefix.adjective + " " + getRandomWeaponName(extreme) 
    damage = 3 * (2 ** (player.level)) + prefix.damageMod# SCALING
    block = prefix.blockMod

    i = Item(player, name, description='', rarity=rarity, _type='weapon', damage=damage, block=block)
    i.description = i.buildItemDescriptionString()
    return i




class ItemPrefix():
    def __init__(self, adjective, damageMod = 0, blockMod=0):
        self.adjective = adjective
        self.damageMod = damageMod
        self.blockMod = blockMod

def generatePrefix(player, _type='weapon', prefixLevelOutOf5 = 3):
    '''prefix level: 1 is shitty, 5 is really good'''
    i = ItemPrefix(getRandomItemPrefix(prefixLevelOutOf5))
    if _type == 'weapon':
        i.damageMod = player.level * (prefixLevelOutOf5-2) + random.randint(0, prefixLevelOutOf5) # SCALING
    elif _type == 'armour':
        i.blockMod = player.level * (prefixLevelOutOf5-2) + random.randint(0, prefixLevelOutOf5)# SCALING

    if i.damageMod<0: i.damageMod==0
    if i.blockMod<0: i.blockMod==0
    # TODO make more special
    return i

def tryForDrop(percent): # TODO drops
    dropchance = random.randint(1, 100)
    if dropchance <= percent:
        return True
    else:
        return False