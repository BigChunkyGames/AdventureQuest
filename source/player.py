# the player class holds all of the information about the player. This class also handles input for player information
from source.lists import *
from source.utils import *
from source.map import Map
from source.inventoryUI import *
from source.item import Item, Consumable, consume
from source.combat import Combat

class Player:

# this function gets called when the player is initialized (player = Player()) It stores class variables and sets default values. 
# Get their values in this class like this ex. self.clantags[]
# or in another file like this ex. player.clantags[]

    def __init__(self): 
        self.devmode = False
        # dicts
        self.aspect = {'name' : 'no name'}  # Beginning inputs (name, gender, etc) used in storytelling
        self.stats = {} # name : int
        self.visitedareas = {} # a dict of visited areas 'area name': times visited (int)
        self.teleportableAreas = {} # same as visitedareas but these are the places the wormhole can go to 
        # lists
        self.clantags = []
        self.history = [] # a list of things that happened, choices (strings) used to keep track of what the player did 
        # points
        self.money = 5
        self.dankpoints = 0 # TODO
        self.perkpoints = 0 # TODO
        self.xp = 0
        self.levelupxp = 10
        # stats
        self.hp = 10
        self.maxhp = 10
        self.strength = 1 # base attack
        self.level = 0
        self.healthRegen = 2
        self.karma=0 # keep track of how nice or evil player is
        # inventory
        self.inventory = [] # list of item objects
        self.equippedWeapon = None
        self.equippedArmourHead = None
        self.equippedArmourOffhand = None
        self.equippedArmourChest = None
        self.equippedArmourLegs = None
        self.equippedArmourFeet = None
        self.getInitialItems() # also equipps them
        self.shops=[] # list of shop objects
        # location
        self.currentLocationX = 6
        self.currentLocationY = 5 # maintown
        self.map = Map() # make a new map for the player. Yeah this is stored in the player class rather than the game class. Should make accessing the map easier
        self.day = 1
        # sound
        self.addMixers()
        # UI
        self.inCombat = False
        # misc
        setFolderLocations(self)

#### misc ##############################################

    def stopMusic(self):
        self.musicMixer.stop()

    def getInput(self, oneTry=False): # redundency for easier coding
        return getInput(self, oneTry)

    def scale(self, number, returnInt=True):
        factor = 1.15 # determines how fast all scaled values ramp with player level
        if returnInt: return int(number * (factor ** (self.level)))
        else: return number * (factor ** (self.level))
        # player max hp scales 10
        # next level xp scales 12
        # enemy damage scales 2
        # enemy hp scales 10
        # enemy xp worth scales 2-3
        # random armour or weapon attack/block scales with rarity (3 for common)
        # random consumable damage scales 3 
        # random consumable heal scales 3 
        # random consumable xp scales 3 

    def getName(self, includeClantags=True):
        s = self.aspect['name']
        if includeClantags:
            for c in self.clantags:
                s += " " + str(c)
        return s

    def addMixers(self):
        self.musicMixer = pygame.mixer
        self.musicMixer.pre_init(44100, -16, 1, 512)
        self.musicMixer.init()
        self.oneShotMixer = pygame.mixer
        self.oneShotMixer.pre_init(44100, -16, 8, 512)
        self.oneShotMixer.init()

    def removeMixers(self):
        self.musicMixer = None
        self.oneShotMixer = None

#### inventory #########################################

    def getInitialItems(self):
        fists = Item(self, 'Fists', customDescription="Knuckle up!", rarity=None, _type='weapon', damage=2, sellValue=0 )
        self.addToInventory(fists, printAboutIt=False, activateNow = True) 
        self.equippedWeapon = fists
        hat = Item(self, 'Baseball Cap', customDescription="You got this when you joined the little league in 7th grade.\nIt's red and smells like dirt.", rarity=None, _type='armour', armourSlot='head', sellValue=1 )
        self.addToInventory(hat, printAboutIt=False, activateNow = True) 
        self.equippedArmourHead = hat
        tshirt = Item(self, 'T-Shirt', customDescription="A black T-Shirt with a cool skull on the front.\nYou can't remember the last time this was washed, but it smells fine to you.", rarity=None, _type='armour', armourSlot='chest', sellValue=1 )
        self.addToInventory(tshirt, printAboutIt=False, activateNow = True) 
        self.equippedArmourChest = tshirt
        pants = Item(self, 'Sweat Pants', customDescription="They make a nice 'swish' sound when you walk.", rarity=None, _type='armour', armourSlot='legs', sellValue=1 )
        self.addToInventory(pants, printAboutIt=False, activateNow = True) 
        self.equippedArmourLegs = pants
        shoes = Item(self, 'Old Tennis Shoes', customDescription="You can't remember buying these, but you've worn them every day since.", rarity=None, _type='armour', armourSlot='feet', sellValue=2 )
        self.addToInventory(shoes, printAboutIt=False, activateNow = True) 
        self.equippedArmourFeet =shoes

    def getAllInventoryItemsAsString(self,_type=None, showEquipped=True):
        '''Can specify all inventory items of type weapon, armour, consumable, or quest'''
        i = 0
        s = ''
        atLeastOne = False
        while i < len(self.inventory):
            if self.inventory[i].type == _type or _type==None:
                if atLeastOne: s += '\n'
                if showEquipped:
                    s += self.inventory[i].getName()
                else:
                    s += self.inventory[i].name 
                atLeastOne = True
            i = i + 1
        return s

    def getAllInventoryItemsAsObjectList(self,_type=None):
        '''Can specify all inventory items of type weapon, armour, consumable, or quest'''
        i = 0
        l = []
        while i < len(self.inventory):
            if self.inventory[i].type == _type or _type==None:
                l.append(self.inventory[i])
            i = i + 1
        return l

    def openInventory(self):
        ui = InventoryUI(self)
        ui.run()
        return ui.result

    def addToInventory(self, item, printAboutIt=True, activateNow=False):
        self.inventory.insert(0, item) # add to front of list so most recent items are in front
        if printAboutIt: show("@You have acquired " + item.name + "@green@.")
        if activateNow: self.activateItem(item)

    def removeFromInventory(self, nameOfItem, printAboutIt=True):
        for x in self.inventory:
            if x.name == nameOfItem:
                self.inventory.remove(x)
                show("@" + str(x.name) + " was removed from your inventory.@red@")
                return True
        return False

    def checkIfInInventory(self, nameOfItem):
        for i in self.inventory:
            if i.name == nameOfItem:
                return True
        return False


    '''equip weapons and armour, consume consumables, examine other things. unequips currently equipped items if armour or weapon slot is occupied.'''
    def activateItem(self, item):
        if item.type == 'consumable' and item.consumable != None: # if has custom function
            return consume(item)
        if item.equipped == True:
            item.toggleEquipped()
            return
        elif item.type == 'weapon':
            self.unequip(_type='weapon')
            self.equippedWeapon = item
            item.toggleEquipped()
        elif item.type == 'armour':
            if item.armourSlot == 'head':
                self.unequip(_type='armour', armourSlot='head')
                self.equippedArmourHead == item
            elif item.armourSlot == 'chest':
                self.unequip(_type='armour', armourSlot='chest')
                self.equippedArmourChest == item
            elif item.armourSlot == 'offhand':
                self.unequip(_type='armour', armourSlot='offhand')
                self.equippedArmourOffhand == item
            elif item.armourSlot == 'legs':
                self.unequip(_type='armour', armourSlot='legs')
                self.equippedArmourLegs == item
            elif item.armourSlot == 'feet':
                self.unequip(_type='armour', armourSlot='feet')
                self.equippedArmourFeet == item
            else:
                return False
            item.toggleEquipped()
        elif item.type == 'consumable':
            pass # TODO consumables
        elif item.type == 'quest':
            pass # TODO quest
        else:
            return False

    ''' sets item.equipped to false for all items of type. if type=None, unequip all items. pass an item to unequip all items of its type'''
    def unequip(self, _type = None, armourSlot = None, item=None):
        if not item == None: # if unequipping 1 item
            _type = item.type
            armourSlot = item.armourSlot
        for i in self.inventory:
            if _type == 'weapon' and i.type == 'weapon': # unequip all weapons
                i.equipped = False
                self.equippedWeapon == None
            elif _type == 'armour' and i.type == 'armour' and armourSlot == i.armourSlot:
                if i.armourSlot == "head":
                    self.equippedArmourHead = None
                    i.equipped = False
                elif i.armourSlot == "chest":
                    self.equippedArmourChest = None
                    i.equipped = False
                elif i.armourSlot == "offhand":
                    self.equippedArmourOffhand = None
                    i.equipped = False
                elif i.armourSlot == "legs":
                    self.equippedArmourLegs = None
                    i.equipped = False
                elif i.armourSlot == "feet":
                    self.equippedArmourFeet = None
                    i.equipped = False
            elif _type == None:
                i.equipped = False

    def restockShops(self):
        for s in self.shops:
            if s.visitedOnDay % 3 == 0:
                s.restock()


#### map ######################################################

    def getTileAtCurrentLocation(self):
        return self.map.getTile(self.currentLocationX, self.currentLocationY)
        
#### player history ######################################################

    def getAspect(self, s):
        return self.aspect[s]

    def addToTeleportableAreas(self, placeName, function):
        if placeName not in self.teleportableAreas:
            self.teleportableAreas[placeName.lower().strip()] = function

    def registerVisit(self, area):
        # increments visits here or creates it if it doesn't already exist
        # returns visits + this one
        if area in self.visitedareas:
            self.visitedareas[area] += 1
        else :
            self.visitedareas[area] = 1
        return self.visitedareas[area]

    def getVisits(self, area):
        #  Returns number of times visited
        if area in self.visitedareas:
            return self.visitedareas[area]
        else:
            return 0

    def countOf(self, name, increment=False): self.count(name,increment)
    def count(self, name, increment=False):
        # returns number of counts for a given name and adds 1 first if increment. if name not found, adds it to self.stats
        if not name in self.stats:
            self.stats[name] = 0
        if increment==True:
            self.stats[name] = self.stats[name] + 1
        return self.stats[name]


#### leveling ####################################################

    def levelUp(self, printAboutIt=True, sound=True):
        if sound==True: Sound(self, 'achieve.wav')
        while True:
            self.level = self.level + 1
            if printAboutIt:printWithColor(str(self.level), before='\nYou are now level ', color="magenta", after= "!")
            self.xp = self.xp - self.levelupxp
            if self.xp < 0:
                self.xp = 0
            
            # strength
            self.strength = self.strength + 1
            if printAboutIt: print("You now have " + str(self.strength) + " strength!")

            # max hp
            self.maxhp = self.scale(10) # SCALING
            if printAboutIt:print("You now have " + str(self.maxhp) + " maximum HP!")

            # regain all health
            gain = self.maxhp - self.hp
            if printAboutIt:printc("You have regained @" + str(gain) + " HP!@green@")
            self.hp = self.maxhp # SCALING

            # health regen
            self.healthRegen = self.scale(1) # SCALING
            if printAboutIt:print("You now regain " + str(self.healthRegen) + " after each battle!")

            # next level xp
            self.levelupxp = self.scale(12) # SCALING
            if self.xp >= self.levelupxp:
                if printAboutIt:print("You have enough XP to level up again!")
            else:
                if printAboutIt:print("You'll need " + str(self.levelupxp) + " XP to level up again.")
                break
        if printAboutIt:print("")
        #TODO italisize

    def gainXp(self, xp, scale = True, returnString=False):
        Sound( self,'etheral_unlock_1.mp3')
        if scale:
            xp = self.scale(xp) # gain xp based on base xp * 2^level
        self.xp = self.xp + xp
        if not returnString:
            if self.xp < self.levelupxp:
                show("You have gained @" + str(xp) + " XP@yellow@!")
            else:
                show("You have gained @" + str(xp) + " XP@yellow@! That's enough to level up!")
                self.levelUp()
        else: 
            s = ''
            if self.xp < self.levelupxp:
                s += "You have gained " + str(xp) + " XP!"
            else:
                self.levelUp(printAboutIt=False)
                s += "You have gained " + str(xp) + " XP! That's enough to level up!\nYou are now level " + str(self.level) +"!"
            return s

#### Combat ##########################################

    def getTotalAttackPower(self):
        damage = self.strength
        if self.equippedWeapon: damage += self.equippedWeapon.damage
        if self.equippedArmourChest: damage += self.equippedArmourChest.damage
        if self.equippedArmourFeet: damage += self.equippedArmourFeet.damage
        if self.equippedArmourHead: damage += self.equippedArmourHead.damage
        if self.equippedArmourLegs: damage += self.equippedArmourLegs.damage
        if self.equippedArmourOffhand: damage += self.equippedArmourOffhand.damage
        return damage

    def getTotalBlock(self):
        block = 0
        if self.equippedWeapon: block += self.equippedWeapon.block
        if self.equippedArmourChest: block += self.equippedArmourChest.block
        if self.equippedArmourFeet: block += self.equippedArmourFeet.block
        if self.equippedArmourHead: block += self.equippedArmourHead.block
        if self.equippedArmourLegs: block += self.equippedArmourLegs.block
        if self.equippedArmourOffhand: block += self.equippedArmourOffhand.block
        return block

    def takeDamage(self, d):
        self.hp = self.hp - d
        s = ''
        if self.hp <= 0:
            hp = 0
            printWithColor(str(d) + " damage",  "red", before="You take ",after=", leaving you unable to stand any longer.")
            input("... ")
            self.death()
        else:
            s += "You took @"
            s +=str(d) + " damage@red@! "
            s += getRandomPainNoise()
            s +="\nYou now have " + str(self.hp) + " HP."
            printc(s)

    def die(self, customText=None): self.death(customText)
    def death(self, customText=None):
        Sound(self, 'etheral plunge.wav')
        if customText:
            printSlowly(str(customText), skipable=False)
        else:
            printSlowly("Suddenly the clouds crack and rain begins to pour.", skipable=False)
            printSlowly("You fall to your knees, then the ground, clutching at your chest as your last thought passes through your mind:", skipable=False)
            printSlowly(getRandomFinalThought(), skipable=False) # TODO flavor
        printSlowly("With that, everything goes dark.", skipable=False)
        printSlowly('...')
        show("@YOU ARE DEAD@red@")
        theEnd(self)

    
    def regenHealth(self, health = None, returnString=False, showCurrentHealth=True, showText=True):
        ''' set health to None for regen health like at end of combat'''
        if health == None:
            health = self.healthRegen
            self.hp = self.hp + self.healthRegen
        else:
            self.hp = self.hp + health
        text = "You regained @" + str(health) + " HP@green@!"
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        if showCurrentHealth:
            text += "\nYou now have " + str(self.hp) + "/" + str(self.maxhp) + " HP."
        if returnString:
            return text
        else:
            if showText:
                show(text)
            else:
                printc(text)

    def sleep(self, customText=None):
        self.hp = self.maxhp
        if customText == None: 
            print("After a long night's rest, you are rejuvenated.")
        else:
            print (customText)
        # TODO flavorize
        self.day += 1
        self.restockShops()
        show("@Your HP has been restored to full!@green@")

    