# the player class holds all of the information about the player. This class also handles input for player information
class Player:

# this function gets called when the player is initialized (player = Player()) It stores class variables and sets default values. 
# Get their values in this class like this ex. self.clantags[]
# or in another file like this ex. player.clantags[]
    def __init__(self): 
        self.aspect = {}  # Beginning inputs (name, gender, etc) used in storytelling
        self.visitedareas = {} # a dict of visited areas
        self.clantags = []
        self.dogecoin = 500
        self.dankpoints = 0
        self.perkpoints = 0
        self.hp = 10

    def charcreation(self):
        self.aspect['name'] = self.name()
        self.aspect['gender'] = self.gender()
        self.aspect['heshe'], self.aspect['HeShe'], self.aspect['hisher'] = self.pronouns()
        self.aspect['occ'], self.aspect['viverb'], self.aspect['skill1'], self.aspect['skill2']\
            = self.impropernouns()
        self.aspect['town'], self.aspect['hills'] = self.propernouns()
        self.aspect['adj1'], self.aspect['adj2'], self.aspect['adj3'], self.aspect['adj4'], \
            self.aspect['adj5'] = self.adjectives()

    def name(self):  # Used in charCreation()
        charname = raw_input("Enter your hero's name: ").lower().strip().title()
        while charname == "":
            charname = raw_input("You must enter your hero's name: ")\
                .lower().strip().title()
        return charname

    def pronouns(self):
        charpronouns = raw_input("Enter your three pronouns (e.g. 'he him his'): ")
        while 1:
            charpronouns = charpronouns.split(" ")
            if len(charpronouns) != 3:
                charpronouns = raw_input("Make sure to enter 3 pronouns: ")
            else:
                return charpronouns[0], charpronouns[1], charpronouns[2]

    def gender(self):
        chargender = raw_input("Enter your hero's gender (e.g. 'boi' or 'gril'): ")\
            .lower()
        return chargender

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
    
        # Returns number of times visited, including current visit
    def getTimesVisited(self, area):
        #  Returns number of times visited
        # FIXME: this function checks times visited but also incriments times visited. So if you check multiple times it still incriments which could be bad.
        try:
            if self.visitedareas[area]:
                self.visitedareas[area] += 1
                return self.visitedareas[area]
        except KeyError:
            self.visitedareas[area] = 1
            return 1
