
# generates items
import random
from source.lists import getRandomWeaponName, getRandomItemPrefix, getRandomArmourSlot, getRandomArmourName

class Item():
    def __init__(self, player, name, customDescription='', rarity = None, _type=None, armourSlot = None, damage=0, block=0, sellValue = None,  customActivationFunction=None):
        '''
        Rarities: None, common, rare, epic, legendary
        Types: weapon, armour, consumable, quest, 
        ArmourSlots: head, offhand, chest, legs, feet
        Set sellValue to None to generate a default value
        customActivationFunction is a lambda that gets called when item is activated (equipped)
        '''
        self.player = player
        self.name = name
        self.rarity = rarity 
        self.type = _type    
        self.damage = damage
        self.block = block
        self.equipped = False
        self.customActivationFunction = customActivationFunction
        self.customDescription = customDescription

        if self.type == 'armour': self.armourSlot = armourSlot
        else: self.armourSlot = None

        if sellValue == None: self.sellValue = self.generateSellValue() 
        else: self.sellValue = sellValue

        self.description = self.buildItemDescriptionString()

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
        self.description = self.buildItemDescriptionString()
        
    def generateSellValue(self):
        mult =1
        if self.rarity == None: mult =1
        elif self.rarity == 'rare': mult =2
        elif self.rarity == 'epic': mult =3
        elif self.rarity == 'legendary': mult =4
        return int( random.randint(1+self.player.level,1+self.player.level * 2) * mult ) # SCALING

    def buildItemDescriptionString(self): # used in UIs
        s = ''
        if not self.rarity == None: # if has a rarity
            s += ' [' + self.rarity.capitalize() + '] ' + '\n'
        elif self.type == 'weapon' or self.type == 'armour':
            s += ' [Common] ' + '\n'
        if self.sellValue > 0:
            s += 'Value: $' + str(self.sellValue) +  '\n'
        if self.damage > 0:
            s += 'Damage: ' + str(self.damage) + '\n'
        if self.block > 0:
            s += 'Block:  ' + str(self.block) + '\n'
        if not self.customDescription == "" and not self.customDescription == None:
            s += "\n" + self.customDescription
        if self.equipped: s += '\n' + "You're " + self.whereIsIt()
        elif self.type == 'weapon' or self.type =='armour': s+= '\n' + self.whereDoesItGo()
        return s.strip()
        # TODO: flavorize

    def whereIsIt(self):
        hand = self.player.aspect["hand"]
        if hand == 'right': otherhand='left'
        else: otherhand='right'
        if self.type ==  "weapon":
            return "holding this in your " + hand + " hand."
        elif self.armourSlot == "head":
            return "wearing this on your head."
        elif self.armourSlot == "chest":
            return "wearing this."
        elif self.armourSlot == "feet" or self.armourSlot == "legs":
            return "wearing these."
        elif self.armourSlot == "offhand":
            return "holding this in your " + otherhand + " hand."

    def whereDoesItGo(self):
        hand = self.player.aspect["hand"]
        if hand == 'right': otherhand='left'
        else: otherhand='right'
        if self.type ==  "weapon":
            return "Weapon"
        elif self.armourSlot == "head":
            return "This goes on your head head."
        elif self.armourSlot == "chest":
            return "This goes on your chest."
        elif self.armourSlot == "legs":
            return "This goes on your legs."
        elif self.armourSlot == "feet":
            return 'This goes on your feet.'
        elif self.armourSlot == "offhand":
            return "This goes in your " + otherhand + " hand."
        return "You can't hold this."

    def consume(self, text=None, heal=None, xpgain=None):
        ''' returns string about what happened after consumption (because consumption is only possible form inventory menu). '''
        # TODO make lots of effects
        if self.type == 'consumable':
            if text == None:
                text = "You ate the " + self.name + ".\n It was delicious.\n"
            if heal:
                self.player.regenHealth(health = heal, returnString=False, showCurrentHealth=False)
                text += "\nYou regained " + heal + " HP!"
            if xpgain:
                text += '\n' + self.player.gainXp(xpgain, returnString=True)
            self.player.inventory.remove(self)
        else:
            text = "You can't eat that!"
        return text

    def scale(self):
        '''change an items stats to scale with player level'''
        self.damage = self.player.scale(self.damage)
        self.block = self.player.scale(self.block)
        self.sellValue = self.sellValue + self.player.level # TODO not sure about this

def generateRandomArmourOrWeapon(player, _type='armour',rarity = 'common', armourSlot=None, goodnessBoost=0, extreme=False, customDescription='', prefix=True, scale=True): 
    ''' goodnessBoost makes the weapon a lot better (or worse if neg)'''
    goodnessBoost += getNumberBasedOnRarity(rarity)
    if prefix == True: prefix = generatePrefix(player, _type=_type ,prefixLevelOutOf5=goodnessBoost+2)
    if _type == 'armour':
        if armourSlot == None: armourSlot = getRandomArmourSlot()
        damage = 0
        block = prefix.blockMod
        name = prefix.adjective + " " + getRandomArmourName(armourSlot)
    else:
        _type = 'weapon'
        damage = prefix.damageMod
        block = 0
        name = prefix.adjective + " " + getRandomWeaponName(extreme) 
    i = Item(player, name, customDescription=customDescription, rarity=rarity, _type=_type, armourSlot = armourSlot, damage=damage, block=block)
    i.description = i.buildItemDescriptionString()
    if scale: i.scale()
    return i

def getNumberBasedOnRarity(rarity):
    if rarity == None or rarity == 'common':
        return 0
    if rarity == 'rare':
        return 1
    if rarity == 'epic':
        return 2
    if rarity == 'legendary':
        return 3


class ItemPrefix():
    def __init__(self, adjective, damageMod = 0, blockMod=0):
        self.adjective = adjective
        self.damageMod = damageMod
        self.blockMod = blockMod

def generatePrefix(player, _type='weapon', prefixLevelOutOf5 = 3):
    '''prefix level: 1 is shitty, 5 is really good'''
    i = ItemPrefix(getRandomItemPrefix(prefixLevelOutOf5))
    if _type == 'weapon':
        i.damageMod = prefixLevelOutOf5
    elif _type == 'armour':
        i.blockMod = prefixLevelOutOf5

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