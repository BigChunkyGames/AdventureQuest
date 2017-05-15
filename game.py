import os   # Used to clear terminal
import random
from SlotMachine import Slots  # Slot machine from SlotMachine.py
from RockPaperScissors import RPSGame  # RPSGame from RockPaperScissors.py

os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal
print("Welcome to ADVENTURE QUEST Version 0.00.42P! The P stands for python.")


# Global Variables - Used by SlotMachine
dogecoin = 500
dankpoints = 0
perkpoints = 0


# Global Dictionaries and Variables
debug = 1
aspect = {}  # Beginning inputs (name, gender, etc) used in storytelling
visitedareas = {}
clantags = []

# Define Functions

def dankadjective():
    adjs = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
    return adjs[random.randint(0, len(adjs)-1)]

def show(text):
    #  Displays text, waits for 'enter' before continuing.
    print(text)
    raw_input("... ")

def yesno():
    #  Returns True if user input is yes, returns False if no.
    while True:
        userinput = raw_input("> ").lower().strip()
        if userinput == "yes" or userinput == "y":
            return True
        elif userinput == "no" or userinput == "n":
            return False
        else:
            print("You must choose 'yes' or 'no'.")

def dichotomy(option1, option2):
    # Returns True if user input is option1, returns False if option2.
    # Make sure the options are in stripped lowercase form
    while True:
        userinput = raw_input("> ").lower().strip()
        if userinput == option1:
            return True
        elif userinput == option2:
            return False
        else:
            print("You must choose 'yes' or 'no'.")

# Might be useful later in the game
def checklevel(xp):
    for x in range(1,10001):
        if xp < (x**1.68)*100:
            return x - 1


# Returns number of times visited, including current visit
def visited(area):
    #  Returns number of times visited
    try:
        if visitedareas[area]:
            visitedareas[area] += 1
            return visitedareas[area]
    except KeyError:
        visitedareas[area] = 1
        return 1


def name():  # Used in charCreation()
    charname = raw_input("Enter your hero's name: ").lower().strip().title()
    while charname == "":
        charname = raw_input("You must enter your hero's name: ")\
            .lower().strip().title()
    return charname


def gender():
    chargender = raw_input("Enter your hero's gender: 'boi' or "
                           "'gril': ").lower()
    while chargender != "boi" and chargender != "gril":
        chargender = raw_input("Select 'boi' or 'gril': ").lower()
    return chargender


def pronouns():
    if aspect['gender'] == "boi":
        return "he", "He", "his"
    elif aspect['gender'] == "gril":
        return "she", "She", "her"


def impropernouns():
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


def propernouns():
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


def adjectives():
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


def charcreation():
    aspect['name'] = name()
    aspect['gender'] = gender()
    aspect['heshe'], aspect['HeShe'], aspect['hisher'] = pronouns()
    aspect['occ'], aspect['viverb'], aspect['skill1'], aspect['skill2']\
        = impropernouns()
    aspect['town'], aspect['hills'] = propernouns()
    aspect['adj1'], aspect['adj2'], aspect['adj3'], aspect['adj4'], \
        aspect['adj5'] = adjectives()


def introduction():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal
    show("In a time before the world fell into the splitting fires of "
         "hell, we looked to the legends.")
    show("Only one true hero could save us from our seemingly "
         "inevitable fate. The legends spoke of a time long ago, "
         "before the fire.")
    print("Past the {0} hills of {1} was a town named {2}. Here "
          "resided the adventurer, {3}, a {4} and {5} {6}."
          ).format(aspect['adj1'], aspect['hills'], aspect['town'],
                   aspect['name'], aspect['adj2'], aspect['adj3'],
                   aspect['occ'])
    raw_input("... ")  # TODO: Replace "a" with "an" when needed
    print "{0} was a {1} {2}, ready to {3} any evil that would dare " \
          "to cross {4} path.".format(aspect['HeShe'], aspect['adj4'],
                                      aspect['occ'], aspect['viverb'],
                                      aspect['hisher'])
    raw_input("... ")
    print("")
    show("but first, %s was thirsty." % aspect['heshe'])
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You recognize your humble town's tavern to the north.")
    move = raw_input("Type 'tavern' to enter the tavern. ").lower().strip()
    while move != "tavern":
        if move == "house":
            print "Calm down there m8, we'll get there later."
        move = raw_input("It's spelled t-a-v-e-r-n. ").lower().strip()
    # Tavern
    show("The tavern in %s is old and rugged. Beaten down by countless "
         "travelers, it's acquired a homey atmosphere." % aspect['town'])
    print('You approach the bartender. "Ey, what\'ll it be for ya?" he '
          'says.')
    print("On the shelf is a bottle of rum and a can of Mountain Dew. "
          "Which do you choose? (rum, dew) ")
    drink = raw_input("> ").lower()
    while drink != "rum" and drink != "dew":
        if drink == 'neither':
            print("You've got to drink something. What'll it be? ")
        else:
            print("Come on, 'rum' or 'dew'. ")
        drink = raw_input("> ").lower()
    if drink == "rum":
        show("You start to reach for the rum, and then realize that "
             "you're way too MLG for that weak shit.")
        show('"Gimme dat dew," you say, gently placing your fedora on '
             'your head.')
        show('"Wow, you really are as dank as you look." the bartender '
             'says, looking impressed.')
    elif drink == "dew":
        show('"Gimme dat dew," you say. "I knew you were a dank one," '
             'the bartender says knowingly.')
        show('You tip your fedora gently to show how euphoric you are '
             'about this dew. "XDDDDDDDD," says the bartender.')
    show('You throw down a one dollar bill. "I think this will cover '
         'it."')
    show('"Holy fucking shit!" exclaims the bartender. "Did you see '
         'that??????"')
    show('"Hold on m8," you say. "I need to take a closer look." You '
         'begin to examine the bill.')
    show('"There is something fishy about this bill... could it be?"')
    show("You connect the three sides of the strange shape on the back "
         "of the bill and realize what you had been missing all along.")
    show("The three sides would connect to form none other than the "
         "illumrunarti triange. Then everything goes black.")
    show('You wake up to find yourself in a green haze in an unreal '
         'dimension. Ahead of you a light begins to appear. "Who\'s '
         'there??" you ask.')
    show('"You know who I am," the voice says. A wave of euphoria '
         'rushes over you as Snoop Dogg steps into view.')
    show("\"And you know why you're here, for only you, %s, have the "
         "swagger dank enough to defeat the greatest enemy of all... "
         "the illum-\"" % aspect['name'])
    show('You wake up on the floor of the tavern covered in doritos '
         'and see the bartender standing over you. "I know what I must '
         'do," you say.')
    show("Looking into your eyes with a piercing stare, the bartender "
         "speaks the word that will change your life forever.")
    print("")
    show('"k."')
    show("You sprint to your house to grab your shit.")
    print('Type "house" to go to your house.')
    move = raw_input("> ").lower().strip()
    while move != "house":
        if move == "tavern":
            print("You just came from there, you need to go to your "
                  "house.")
        else:
            print('No. Type "house"')
        move = raw_input("> ").lower().strip()
    show('You enter your house, hoping mum will get the camera. "Mom! I\'m '
         'going on an adventure!!1!!!!1one!!"')
    show('She looks up from the dick sock she\'s knitting. "Alright '
         'sweetie, be safe! Here, take this."')
    show('You have acquired the camera.')
    show('After taking the camera, you leave your house and walk into town, '
         'ready to head into whatever building you choose.')

def home():
    show("You enter your house through the familiar front door, taking in "
         "the sights of your childhood abode, reminiscing about all the "
         "dank shit you did as a kid.")
    show("You could 'look' around some more, or just leave.")
    action = raw_input("> ").lower().strip()
    while action != "leave" and action != "look":
        action = raw_input("> ")
    if action == "look":
        if visited("bedroom") == 1:
            show("You head upstairs to your room and look around for a bit. "
                 "You realize that you left your can of Mtn Dew laying on top "
                 "of your dresser.")
            show("You grab the can just in case you need it later.")
            # TODO: add the can to your inventory
        else:
            show("You look around your house for a bit, but there isn't much "
                 "to find that you haven't already.")
            # TODO: add more stuff to do in your house
    else:
        show("You figure that there isn't much to do here at the moment, "
             "so you turn 360 degrees and walk away.")

def tavern():
    if visited("tavern") == 1:
        show("You walk into the old tavern, wanting to visit the old place "
             "once again.")
        show("As you walk in, several patrons of the bar turn around to look "
             "at you.")
        show('"Ah, it\'s you." The bartender says. "Make sure to watch how '
             'much Mtn Dew you have this time!" Several of the bar\'s guests '
             'chuckle jovially.')
    else:
        show("You walk into the old tavern once again, determined to find some "
          "dank shit to do here or something.")
    print("You have a look around to see what's up:")
    print("In front of you lies a pretty dope looking 'slot' machine")
    print("You could 'ask' the bartender for some rumors")
    print("It looks like one of the patrons is challenging others to a 'game'")
    print("Or you could just leave.")
    action = raw_input("> ").lower().strip()
    if action == "slot":
        Slots().slot_machine()
        show("After your exciting go on the slot machine, you decide you've "
             "had enough of the tavern for now.")
    elif action == "ask":
        show("You walk up to the bartender and ask for some rumors.")
        show("He lets you know that he hasn't heard anything since the last "
             "time you asked.")
        # TODO: Rumors (random maybe?)
    elif action == "game":
        show("You saunter up to the gentleman who seems to be looking for "
             "someone willing to play a game with him.")
        show("The old pirate sitting at the table looks up at you and takes a "
             "sip out of his flask.")
        print('"I\'ve been challenging travelers across these lands to the '
             'game of my people for many years. You think you\'ve got what '
             'it takes to beat me?" (y/n)')
        if yesno():
            show('"Hah! Let\'s see how good you really are!')
            show("The pirate cracks his knuckles and offers his hand to you "
                 "for a friendly handshake.")
            show("You accept his offer, shaking his hand, when he suddenly "
                 "grins at you.")
            show('"Hah, new to the game, are you? I can feel in your hand '
                 'what you\'re about to play!"')
            show("You gulp nervously and ready your fist, mentally preparing "
                 "yourself for the beginning of the match.")
            yourchoice, opchoice, outcome = RPSGame().game()
            show('"Enough waiting around! Let\'s do this!"')
            show("The world seems to fade away around you as the only thing "
                 "you focus on is your own hand and that of your opponent.")
            show("Over the rushing sound in your ears you hear the patrons of "
                 "the bar chanting, your fist hitting your open hand.")
            show('"ROCK"')
            show('"PAPER"')
            show('"SCISSORS"')
            show('"SHOOT!"')
            if opchoice == 'rock':
                show("The pirate slams his closed fist down into his open "
                     "palm. He played rock!")
            else:
                print("The pirate opens his hand a split second before slamming "
                     "his fist into his open palm, revealing his true choice: "
                     "%s!" % opchoice)
                raw_input("... ")
            show("The bar erupts in cheers when they see the outcome of your "
                 "match.")
            if outcome == 'win':
                print("You look down into your own hand. {0} beats {1}! You "
                     "actually beat him!").format(yourchoice, opchoice)
                raw_input("... ")
                show("The pirate looks up at you, clearly impressed.")
                show('"Not many can beat me at this game. I think you deserve '
                     'to be in my clan, it houses only the best rock paper '
                     'scissors players in the entire world."')
                clantags.append("[Pyr8]")
                show("You have joined The Pirates' Clan! [Pyr8]")
            else:
                show("You look down into your own hand. {0} beats {1}! He beat "
                     "you!").format(opchoice.title(), yourchoice)
                show('"Heh heh, well that\'s alright. Not everybody has what '
                     'it takes to play with the best of them."')
            show("After your rousing game, you decide you've had enough fun at the "
             "tavern for now.")
        else:
            show('"Just as I figured, maybe you can come back when you\'re not '
                 'such a fuckin whimp lol')
            show("You're so upset by his unkind words that you don't even want "
                 "to be here anymore.")
    show("You leave the tavern, heading outside to the rest of the town.")
    print("")

def store():
    show("You stride into the sedentary sales store supplementing the "
         "not-so-silent town of %s, where succulent sweets "
         "are sold. " % aspect['town'])
    show("You approach the shopkeeper, an old and wary gentleman with age on "
         "his face and experience in his eyes.")
    show('"What\'ll it be for ya today?"')
    show("You make a point of considering the shopkeeper's wares, but you're "
         "not in the market for anything he's selling at the moment.")
    show("He looks a little irritated that you didn't buy anything as you "
         "head back to the town center.")
    # TODO: add the shop

def blacksmith():
    show("You head over to the blacksmith's place to take a look at some "
         "quality goods.")
    show("You walk over to your town's forge and approach the blacksmith, "
         "she's 6'5\" and the strongest one in your town.")
    show('"Hello!" she reaches out to shake your hand and ends up hurting it '
         'slightly.')
    show("You have lost 1 HP")  # TODO: lose 1 hp
    show("You look at the blacksmith's wares, but she doesn't have anything "
         "you need at the moment. You decide to head back into the town.")
    # TODO: blacksmith

def maintown():
    while True:
        print("You stand in the homey town of %s, a lovely place. Where do you"
              "want to go?") % aspect['town']
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Where do you want to go?")
        place = raw_input("> ").lower().strip()
        while place == "":
            place = raw_input("> ").lower().strip()
        if place == "home":
            home()
        elif place == "tavern":
            tavern()
        elif place == "store":
            store()
        elif place == "blacksmith":
            blacksmith()
        else:
            print("You've got to pick one of the places listed.")
            print("")

def main():
    charcreation()
    introduction()
    maintown()

if debug == 1:
    aspect['name'] = "name"
    aspect['gender'] = "boi"
    aspect['heshe'], aspect['HeShe'], aspect['hisher'] = "he", "He", "his"
    aspect['occ'], aspect['viverb'], aspect['skill1'], aspect['skill2'] = "fireman", "stab", "sewing", "rubiks cube solving"
    aspect['town'], aspect['hills'] = "Swagsburgh", "Peak's Hills"
    aspect['adj1'], aspect['adj2'], aspect['adj3'], aspect['adj4'], aspect['adj5'] = "cool", "neato", "sick nasty", "wiggity wiggity whack", "excellent"
    maintown()
else:
    main()
