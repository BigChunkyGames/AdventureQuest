# the player class holds all of the information about the player. This class also handles input for player information


from lists import *
class Player:

# this function gets called when the player is initialized (player = Player()) It stores class variables and sets default values. 
# Get their values in this class like this ex. self.clantags[]
# or in another file like this ex. player.clantags[]

    def __init__(self): 
         # lists
        self.aspect = {}  # Beginning inputs (name, gender, etc) used in storytelling
        self.visitedareas = {} # a dict of visited areas
        self.teleportableAreas = {}
        self.clantags = []
        # points
        self.dogecoin = 500
        self.dankpoints = 0
        self.perkpoints = 0
        # stats
        self.hp = 10
        self.maxhp = 10

        self.strength = 1 # base attack
        self.level = 0

        self.currentLocation = [0,0] # set this before saving (coordinates of tile)

    def levelUp(self):
        self.level = self.level +1
        show("You leveled up!") #TODO italisize

    def addToTeleportableAreas(self, placeName, function):
        if placeName not in self.teleportableAreas:
            self.teleportableAreas[placeName.lower().strip()] = function

    def addVisit(self, area):
        if area in self.visitedareas:
            self.visitedareas[area] += 1
        else :
            self.visitedareas[area] = 1

    def getVisits(self, area):
        #  Returns number of times visited
        if area in self.visitedareas:
            return self.visitedareas[area]
        else:
            return 0

    def takeDamage(self, d):
        self.hp = self.hp - d
        print "You took",
        print (str(d) + " damage!")
        show(getRandomPainNoise())
        print("You now have " + str(self.hp) + " HP.")
        if self.hp <= 0:
            print "you dead" # TODO

    def sleep(self):
        self.hp = self.maxhp
        print("After a long night's rest, you feel reinvigorated and ready to start a new day.")
        show("Your HP has been restored to full!")


    def charcreation(self):
        self.aspect['name'] = self.name()
        self.aspect['gender'] = self.gender()
        self.aspect['heshe'], self.aspect['HeShe'], self.aspect['himher'], \
        self.aspect['hisher'] = self.pronouns()
        self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], \
        self.aspect['skill2'] = self.impropernouns()
        self.aspect['town'], self.aspect['hills'] = self.propernouns()
        self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], \
        self.aspect['adj4'], self.aspect['adj5'] = self.adjectives()

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
                charpronouns = raw_input("Make sure to enter 3 pronouns: ")
            else:
                return charpronouns[0], charpronouns[0].title(), charpronouns[1], charpronouns[2]

    def impropernouns(self):
        occ = raw_input("Enter the name of your hero's occupation: ")\
            .lower().strip()
        while occ == "":
            print("Your occupation can not be blank. ")
            occ = raw_input("Enter the name of your hero's occupation: ")\
                .lower().strip()
        viverb = raw_input("Enter the name of a violent verb: ").lower()\
            .strip()
        while viverb == "":
            print("The verb can not be blank. ")
            viverb = raw_input("Enter the name of a violent verb: ")\
                .lower().strip()
        skill1 = raw_input("Enter the name of a special skill: ").lower()\
            .strip()
        while skill1 == "":
            print("The special skill can not be blank. ")
            skill1 = raw_input("Enter the name of a special skill: ")\
                .lower().strip()
        skill2 = raw_input("Enter the name of a second special skill: ")\
            .lower().strip()
        while skill2 == "":
            print("The special skill can not be blank. ")
            skill2 = raw_input("Enter the name of a second special "
                               "skill: ").lower().strip()
        return occ, viverb, skill1, skill2

    def propernouns(self):
        town = raw_input("Enter the name of the town: ").lower().title()\
            .strip()
        while town == "":
            print("The name of the town can not be blank.")
            town = raw_input("Enter the name of the town: ").lower()\
                .title().strip()
        hills = raw_input("Enter the name of the hills: ").lower().title()\
            .strip()
        while hills == "":
            print("The name of the hills can not be blank.")
            hills = raw_input("Enter the name of the hills: ").lower()\
                .title().strip()
        return town, hills

    def adjectives(self):
        while True:
            try:
                adjinput = raw_input("Enter five adjectives separated by commas: ")\
                    .lower()
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
                    if adjlist[0] and adjlist[1] and adjlist[2] and adjlist[3]\
                            and adjlist[4]:
                        return adjlist[:]
                    else:
                        print("Adjective may not be blank.")
            except IndexError:
                print("Your list doesn't seem to be long enough, try again.")
