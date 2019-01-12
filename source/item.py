
# generates items
import random
from lists import getRandomWeaponName, getRandomItemPrefix

class Item():
    def __init__(self, player, name, customDescription='', rarity = None, _type=None, armourSlot = None, damage=0, block=0, sellValue = None,  customActivationFunction=None):
        '''
        Rarities: None, common, rare, epic, legendary
        Types: weapon, armour, consumable, quest
        ArmourSlots: head, offhand, chest, legs, feet
        Set sellValue to None to generate a default value
        customActivationFunction gets called when item is activated (equipped)
        '''
        self.player = player
        self.name = name
        self.rarity = rarity 
        self.type = _type    
        self.damage = damage
        self.block = block
        self.customActivationFunction = customActivationFunction
        self.customDescription = customDescription
        self.equipped = False

        if self.type == 'armour': self.armourSlot = armourSlot
        else: self.armourSlot = None

        if sellValue == None: self.sellValue = self.generateSellValue() 
        else: self.sellValue = sellValue

        self.description = self.buildItemDescriptionString(custom=customDescription)

    def getName(self):
        '''changes return value if item is equipped'''
        if self.equipped:
            return self.name + ' (equipped)'
        else:
            return self.name
        
    def toggleEquipped(self):
        if not self.equipped:
            self.equipped = True
        else:
            self.equipped = False
        self.description = self.buildItemDescriptionString(custom=self.customDescription)
        
    def generateSellValue(self):
        mult =1
        if self.rarity == None: mult =1
        elif self.rarity == 'rare': mult =2
        elif self.rarity == 'epic': mult =3
        elif self.rarity == 'legendary': mult =4
        return int( random.randint(1+self.player.level,1+self.player.level * 2) * mult ) # SCALING

    def buildItemDescriptionString(self, custom=''):
        if self.equipped: equip = '(equipped)'
        else: equip = ''
        if not self.rarity == None: # if has a rarity
            s = self.name + ' [' + self.rarity.capitalize() + '] ' + equip + '\n'
        else: 
            s = self.name + ' ' + equip + '\n'
        s += '\n'
        if self.damage > 0:
            s += 'Damage: ' + str(self.damage) + '\n'
        if self.block > 0:
            s += 'Block:  ' + str(self.block) + '\n'
        if self.sellValue > 0:
            s += 'Value: $' + str(self.sellValue) +  '\n'
        s += custom
        return s
        # TODO: flavorize

def generateRandomWeapon(player, rarity = 'common', goodnessBoost=0, extreme=False, customDescription=''): 
    ''' goodnessBoost makes the weapon a lot better (or worse if neg)
    '''
    prefix = generatePrefix(player, goodnessBoost+3)
    name = prefix.adjective + " " + getRandomWeaponName(extreme) 
    damage = 3 * (2 ** (player.level)) + prefix.damageMod# SCALING
    block = prefix.blockMod

    i = Item(player, name, customDescription=customDescription, rarity=rarity, _type='weapon', damage=damage, block=block)
    i.description = i.buildItemDescriptionString()
    return i

def generateRandomArmour(player, rarity = 'common', armourSlot=None, goodnessBoost=0, extreme=False, customDescription=''): 
    ''' goodnessBoost makes the weapon a lot better (or worse if neg)
    '''
    
    if armourSlot == None: 
        pass

    prefix = generatePrefix(player, goodnessBoost+3)
    name = prefix.adjective + " " + getRandomWeaponName(extreme) 
    damage = 3 * (2 ** (player.level)) + prefix.damageMod# SCALING
    block = prefix.blockMod

    i = Item(player, name, customDescription=customDescription, rarity=rarity, _type='weapon', damage=damage, block=block)
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