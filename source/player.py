# the player class holds all of the information about the player. This class also handles input for player information
from lists import *
from utils import *
from map import Map
from inventoryUI import *
from item import Item

class Player:

# this function gets called when the player is initialized (player = Player()) It stores class variables and sets default values. 
# Get their values in this class like this ex. self.clantags[]
# or in another file like this ex. player.clantags[]

    def __init__(self): 
        self.devmode = False
        # dicts
        self.aspect = {'name' : 'no name'}  # Beginning inputs (name, gender, etc) used in storytelling
        self.counters = {} # name : int
        self.visitedareas = {} # a dict of visited areas 'area name': times visited (int)
        self.teleportableAreas = {} # same as visitedareas but these are the places the wormhole can go to 
        # lists
        self.clantags = []
        self.choices = [] # a list of choices (strings) used to keep track of what the player did (should probably be called player history)
        # points
        self.dogecoin = 5
        self.dankpoints = 0
        self.perkpoints = 0
        self.experiencepoints = 0
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
        self.getInitialItems()
        # location
        self.currentLocationX = 6
        self.currentLocationY = 5 # maintown
        self.map = Map() # make a new map for the player. Yeah this is stored in the player class rather than the game class. Should make accessing the map easier

#### misc ##############################################

    def getInput(self): # redundent
        return getInput(self)

#### inventory #########################################

    def getInitialItems(self): # TODO Flavorize

        fists = Item(self, 'Fists', customDescription="Knuckle up!", rarity=None, _type='weapon', damage=2, sellValue=0 )
        self.addToInventory(fists, printAboutIt=False, activateNow = True) 

        hat = Item(self, 'Baseball Cap', customDescription="You got this when you joined the little league in 7th grade.\nIt's red and smells like dirt.", rarity=None, _type='armour', armourSlot='head', sellValue=1 )
        self.addToInventory(hat, printAboutIt=False, activateNow = True) 

        tshirt = Item(self, 'T-Shirt', customDescription="A black T-Shirt with a cool skull on the front.\nYou can't remember the last time this was washed, but it smells fine to you.", rarity=None, _type='armour', armourSlot='chest', sellValue=1 )
        self.addToInventory(tshirt, printAboutIt=False, activateNow = True) 

        pants = Item(self, 'Sweat Pants', customDescription="They make a nice 'swish' sound when you walk.", rarity=None, _type='armour', armourSlot='legs', sellValue=1 )
        self.addToInventory(pants, printAboutIt=False, activateNow = True) 

        shoes = Item(self, 'Old Tennis Shoes', customDescription="You can't remember buying these, but you've worn them every day since.", rarity=None, _type='armour', armourSlot='feet', sellValue=2 )
        self.addToInventory(shoes, printAboutIt=False, activateNow = True) 

    def getAllInventoryItemsAsString(self,_type=None, showEquipped=True):
        '''Can specify all inventory items of type weapon, armour, consumable, or quest'''
        i = 0
        s = ''
        while i < len(self.inventory):
            if self.inventory[i].type == _type or _type==None:
                if showEquipped:
                    s += self.inventory[i].getName() + '\n'
                else:
                    s += self.inventory[i].name + '\n'
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
        x = InventoryUI(self)
        x.run()
        return x.result

    def addToInventory(self, item, printAboutIt=True, activateNow=False):
        self.inventory.insert(0, item) # add to front of list so most recent items are in front
        if printAboutIt: show(item.name + " was added to your inventory!")
        if activateNow: self.activateItem(item)

    '''equip weapons and armour, consume consumables, examine other things. unequips currently equipped items if armour or weapon slot is occupied.'''
    def activateItem(self, item):
        if not item.customActivationFunction == None:
            return item.customActivationFunction()

        if item.equipped == True:
            item.toggleEquipped()
            return

        elif item.type == 'weapon':
            self.unequipAll(_type='weapon')
            self.equippedWeapon = item
            item.toggleEquipped()
        elif item.type == 'armour':
            if item.armourSlot == 'head':
                self.unequipAll(_type='armour', armourSlot='head')
                self.equippedArmourHead == item
            elif item.armourSlot == 'chest':
                self.unequipAll(_type='armour', armourSlot='chest')
                self.equippedArmourChest == item
            elif item.armourSlot == 'offhand':
                self.unequipAll(_type='armour', armourSlot='offhand')
                self.equippedArmourOffhand == item
            elif item.armourSlot == 'legs':
                self.unequipAll(_type='armour', armourSlot='legs')
                self.equippedArmourLegs == item
            elif item.armourSlot == 'feet':
                self.unequipAll(_type='armour', armourSlot='feet')
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

    ''' sets item.equipped to false for all items of type'''
    def unequipAll(self, _type = None, armourSlot = None):
        for i in self.inventory:
            if _type == 'weapon' and i.type == 'weapon':
                i.equipped = False
            elif _type == 'armour' and i.type == 'armour':
                if i.armourSlot == armourSlot:
                    i.equipped = False
            else:
                i.equipped = False

#### map ######################################################

    def getTileAtCurrentLocation(self):
        return self.map.getTile(self.currentLocationX, self.currentLocationY)
        
#### player history ######################################################

    def getAspect(self, s):
        return self.aspect[s]

    def addToTeleportableAreas(self, placeName, function):
        if placeName not in self.teleportableAreas:
            self.teleportableAreas[placeName.lower().strip()] = function

    def addVisit(self, area):
        if area in self.visitedareas:
            self.visitedareas[area] += 1
        else :
            self.visitedareas[area] = 1

    def getVisits(self, area, add = ""):
        #  Returns number of times visited
        if add == "add":
            self.addVisit(area)
        if area in self.visitedareas:
            return self.visitedareas[area] # return amount of times visited including this time if added
        else:
            return 0

    def countOf(self, name, increment=False): self.count(name,increment)
    def count(self, name, increment=False):
        # returns number of counts for a given name and adds 1 first if increment. if name not found, adds it to self.counters
        if not name in self.counters:
            self.counters[name] = 0
        if increment==True:
            self.counters[name] = self.counters[name] + 1
        return self.counters[name]


#### leveling ####################################################

    def levelUp(self):
        while True:
            self.level = self.level + 1
            print("")
            print "You are now level ", 
            printWithColor(str(self.level), "magenta", after= "!")
            self.experiencepoints = self.experiencepoints - self.levelupxp
            if self.experiencepoints < 0:
                self.experiencepoints = 0
            
            # strength
            self.strength = self.strength + 1
            print("You now have " + str(self.strength) + " strength!")

            # max hp
            self.maxhp = 10 * (2 ** (self.level)) # SCALING
            print("You now have " + str(self.maxhp) + " maximum HP!")

            # regain all health
            gain = self.maxhp - self.hp
            printc("You have regained @" + str(gain) + " HP!@green@")
            self.hp = self.maxhp # SCALING

            # health regen
            self.healthRegen = (2 ** (self.level)) # SCALING
            print("You now regain " + str(self.healthRegen) + " after each battle!")

            # next level xp
            self.levelupxp = 10 * (2 ** (self.level)) # SCALING
            if self.experiencepoints >= self.levelupxp:
                print("You have enough XP to level up again!")
            else:
                print("You'll need " + str(self.levelupxp) + " XP to level up again.")
                break
        print("")
        #TODO italisize

    def addExperience(self, xp, scale = True):
        if scale:
            xp = xp * (2 ** (self.level)) # gain xp based on base xp * 2^level
        self.experiencepoints = self.experiencepoints + xp
        if self.experiencepoints < self.levelupxp:
            printc("You have gained @" + str(xp) + " XP!@yellow@")
            printc("You now have " + str(self.experiencepoints) + "/" + str(self.levelupxp) + " needed to level up.")
        else:
            printc("You have gained " + str(xp) + " experience! That's enough to level up!")
            raw_input("... ")
            self.levelUp()
        raw_input("... ")

#### Combat ##########################################

    def takeDamage(self, d):
        self.hp = self.hp - d
        if self.hp <= 0:
            hp = 0
            print("You take "),
            printWithColor(str(d) + " damage", "red", after=", leaving you unable to stand any longer.")
            raw_input("... ")
            self.death()
        else:
            print("You took "),
            printWithColor(str(d) + " damage", "red", after="!")
            print(getRandomPainNoise())
            print("You now have " + str(self.hp) + " HP.")
            print("")

    def die(self): self.death()
    def death(self):
        show("You fall to your knees, then the ground, clutching at your chest as your last thought passes through your mind:")
        show('*I think I left the oven on at home*')
        show("With that, everything goes dark.")
        print(""); print(""); print("")
        show("You're dead. You should feel pretty lucky that death doesn't have an effect yet.")
        print("Anyway, on with the game... ")
        # TODO
    
    def regenHealth(self, health = None, returnString=False, showCurrentHealth=True):
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
            show(text)

    def sleep(self, customText=None):
        self.hp = self.maxhp
        if customText == None: 
            print("After a long night's rest, you feel reinvigorated and ready to start a new day.")
        else:
            print customText
        # TODO flavorize
        show("@Your HP has been restored to full!@green@")

#### INTRO STUFF #################################################

    def charcreation(self):
        while True:
            printc("Would you like to @'create'@yellow@ your own character or @'roleplay'@yellow@ one created for you?\n(") # TODO have this 
            dec = getInput(self) 
            if dec == "create" or dec == "c":
                self.aspect['name'] = self.name()
                self.aspect['gender'] = self.gender()
                self.aspect['heshe'], self.aspect['HeShe'], self.aspect['himher'], self.aspect['hisher'] = self.pronouns()
                self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], self.aspect['skill2'] = self.impropernouns()
                self.aspect['town'], self.aspect['land'] = self.propernouns()
                self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], self.aspect['adj4'], self.aspect['adj5'] = self.adjectives()
                break
            elif dec == "roleplay" or dec == "r":
                self.generateAspects()
                break
            else:
                pass

    def generateAspects(self):
        self.aspect['name'] = "Michael"
        self.aspect['gender'] = "boi"
        self.aspect['heshe'], self.aspect['HeShe'], self.aspect['hisher'] = "he", "He", "his"
        self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], self.aspect['skill2'] = "fireman", "evicerate", "sewing", "rubiks cube solving"
        self.aspect['town'], self.aspect['land'] = "your home town", "Flat Earth"
        self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], self.aspect['adj4'], self.aspect['adj5'] = "impressive", "well liked", "sick nasty", "wiggity wiggity whack", "excellent"
    
        
    def name(self):
        charname = raw_input("Enter your hero's name: ").lower().strip().title()
        while charname == "":
            charname = raw_input("Your hero may not be nameless: ")\
                .lower().strip().title()
        return charname

    def gender(self):
        chargender = raw_input("Enter your hero's gender (e.g. 'boi' or 'gril'): ")\
            .lower()
        return chargender

    def pronouns(self):
        charpronouns = raw_input("Enter your three pronouns (e.g. 'he him his'): ")
        while 1:
            charpronouns = charpronouns.split(" ")
            if len(charpronouns) != 3:
                charpronouns = raw_input("Make sure to enter 3 pronouns separated by a single space each: ")
            else:
                return charpronouns[0], charpronouns[0].title(), charpronouns[1], charpronouns[2]

    def impropernouns(self):
        occ = raw_input("Enter the name of your hero's occupation (e.g. 'firefighter'): ").lower().strip()
        while occ == "":
            print("Your occupation can not be blank. ")
            occ = raw_input("Enter the name of your hero's occupation: ").lower().strip()
        viverb = raw_input("Enter the name of a violent verb: ").lower().strip()
        while viverb == "":
            print("The verb can not be blank. ")
            viverb = raw_input("Enter the name of a violent verb: ").lower().strip()
        skill1 = raw_input("Enter the name of a special skill: ").lower().strip()
        while skill1 == "":
            print("The special skill can not be blank. ")
            skill1 = raw_input("Enter the name of a special skill: ").lower().strip()
        skill2 = raw_input("Enter the name of a second special skill: ").lower().strip()
        while skill2 == "":
            print("The special skill can not be blank. ")
            skill2 = raw_input("Enter the name of a second special skill: ").lower().strip()
        return occ, viverb, skill1, skill2

    def propernouns(self):
        town = raw_input("Enter the name of the town: ").lower().title().strip()
        while town == "":
            print("The name of the town can not be blank.")
            town = raw_input("Enter the name of the town: ").lower().title().strip()
        land = raw_input("Enter the name of the land: ").lower().title().strip()
        while land == "":
            print("The name of the land can not be blank.")
            land = raw_input("Enter the name of the land: ").lower().title().strip()
        return town, land

    def adjectives(self):
        while True:
            try:
                adjinput = raw_input("Enter five adjectives separated by commas: ").lower()
                adjinputlist = adjinput.split(',')
                # creates list from input split by commas
                adjlist = [x.strip() for x in adjinputlist]
                # creates another list, strips whitespace
                if adjlist[4]:
                    pass
                try:
                    if adjlist[5]:
                        pass
                    print("Your list is too long.")
                except IndexError:
                    if adjlist[0] and adjlist[1] and adjlist[2] and adjlist[3] and adjlist[4]:
                        return adjlist[:]
                    else:
                        print("Adjective may not be blank.")
            except IndexError:
                print("Your list doesn't seem to be long enough, try again.")
