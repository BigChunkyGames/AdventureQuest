# the player class holds all of the information about the player. This class also handles input for player information
from inventory import *
from lists import *
from utils import *
from map import *

class Player:

# this function gets called when the player is initialized (player = Player()) It stores class variables and sets default values. 
# Get their values in this class like this ex. self.clantags[]
# or in another file like this ex. player.clantags[]

    def __init__(self): 
         # lists
        self.aspect = {'name' : 'no name'}  # Beginning inputs (name, gender, etc) used in storytelling
        self.visitedareas = {} # a dict of visited areas
        self.teleportableAreas = {}
        self.clantags = []
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
        self.devmode = False
        
        self.inventory = Inventory(self) # this is kind of sketchy not sure if this will cause problems later

        self.currentLocationX = 6
        self.currentLocationY = 5 # maintown
        self.map = Map() # make a new map for the player. Yeah this is stored in the player class rather than the game class. Should make accessing the map easier

    def getTileAtCurrentLocation(self):
        return self.map.getTile(self.currentLocationX, self.currentLocationY)
        
    def getAspect(self, s):
        return self.aspect[s]

    def openInventory(self):
        self.inventory.open()

    # max hp inceases by 2
    # current hp increases by 2 unless greater than max
    # strength increases by 1
    # health regen increased by 1
    # xp needed for next level is  2^currentLevel
    def levelUp(self):
        while True:
            self.level = self.level + 1
            print("")
            print "You are now level ", 
            printWithColor(str(self.level), "magenta", after= "!")
            self.experiencepoints = self.experiencepoints - self.levelupxp
            if self.experiencepoints < 0:
                self.experiencepoints = 0
            self.strength = self.strength + 1
            print("You now have " + str(self.strength) + " strength!")

            self.maxhp = self.maxhp + 2
            self.hp = self.hp + 2
            if self.hp > self.maxhp: self.hp = self.maxhp
            print("You now have " + str(self.maxhp) + " maximum HP!")

            self.healthRegen = self.healthRegen + 1
            print("You now regenerate " + str(self.healthRegen) + " after each battle!")

            self.levelupxp = (2 ** (self.level)) * 10
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

    def death(self):
        show("You fall to your knees, then the ground, clutching at your chest as your last thought passes through your mind:")
        show('*I think I left the oven on at home*')
        show("With that, everything goes dark.")
        print(""); print(""); print("")
        show("You're dead. You should feel pretty lucky that death doesn't have an effect yet.")
        print("Anyway, on with the game... ")
        # TODO
    
    def regenHealth(self, r = None):
        if r == None:
            self.hp = self.hp + self.healthRegen
            print "You regained ",
            printWithColor(str(self.healthRegen) + " HP", "green", after = "!")
        else:
            self.hp = self.hp + r
            print "You regained ",
            printWithColor(str(r) + " HP", "green", after = "!")
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        show("You now have " + str(self.hp) + "/" + str(self.maxhp) + " HP.")

    def sleep(self):
        self.hp = self.maxhp
        print("After a long night's rest, you feel reinvigorated and ready to start a new day.")
        show("@Your HP has been restored to full!@green@")

    def charcreation(self):
        while True:
            print("Would you like to 'create' your own character or 'roleplay' one created for you?")
            dec = getInput(self) # TODO handle inventory 
            if dec == "create" or dec == "c":
                self.aspect['name'] = self.name()
                self.aspect['gender'] = self.gender()
                self.aspect['heshe'], self.aspect['HeShe'], self.aspect['himher'], self.aspect['hisher'] = self.pronouns()
                self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], self.aspect['skill2'] = self.impropernouns()
                self.aspect['town'], self.aspect['hills'] = self.propernouns()
                self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], self.aspect['adj4'], self.aspect['adj5'] = self.adjectives()
                break
            elif dec == "roleplay" or dec == "r":
                self.aspect['name'] = "Michael"
                self.aspect['gender'] = "boi"
                self.aspect['heshe'], self.aspect['HeShe'], self.aspect['hisher'] = "he", "He", "his"
                self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], self.aspect['skill2'] = "fireman", "evicerate", "sewing", "rubiks cube solving"
                self.aspect['town'], self.aspect['hills'] = "Swagsburgh", "Peak's Summit"
                self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], self.aspect['adj4'], self.aspect['adj5'] = "impressive", "well liked", "sick nasty", "wiggity wiggity whack", "excellent"
                break
            else:
                pass
        
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
        hills = raw_input("Enter the name of the hills: ").lower().title().strip()
        while hills == "":
            print("The name of the hills can not be blank.")
            hills = raw_input("Enter the name of the hills: ").lower().title().strip()
        return town, hills

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
