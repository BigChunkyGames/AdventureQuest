from inspect import currentframe, getframeinfo  # Used for error messages
import os   # Used to clear terminal

# I have made a comment
# Your comments are lame

os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal
print("Welcome to ADVENTURE QUEST Version 0.00.20P! The P stands for python.")

aspect = {}  # Beginning inputs

# Define Functions

# Displays text, waits for 'enter' before continuing.
def show(text):
    print(text)
    raw_input("... ")

# User inputs

    # Name
def name():
    name = raw_input("Enter your hero's name: ").lower().strip().title()
    while name == "":
        name = raw_input("You must enter your hero's name: ").lower().strip().title()
    return name
aspect['name'] = name()

    # Gender
def gender():
    gender = raw_input("Enter your hero's gender, boy or girl: ").lower()
    while gender != "boy" and gender != "girl":
        gender = raw_input("Select boy or girl: ").lower()
    return gender

aspect['gender'] = gender()

        # Pronouns
def pronouns():
    if aspect['gender'] == "boy":
        heshe = "he"
        HeShe = "He"
        hisher = "his"
    elif aspect['gender'] == "girl":
        heshe = "she"
        HeShe = "She"
        hisher = "her"
    else:
        exit("Error on line %s: Program attempted to create pronouns, but characters gender is not 'boy' or 'girl'." % getframeinfo(currentframe()).lineno)
    return heshe, HeShe, hisher
aspect['heshe'], aspect['HeShe'], aspect['hisher'] = pronouns()

        # Improper Nouns
def improperNouns():
    nam = "n occupation"
    for x in xrange(0, 4):
        inp = raw_input("Enter the name of a" + nam + ": ").lower().strip()
        while inp == "":
            print("A" + nam + " can not be blank. ")
            inp = raw_input("Enter the name of a" + nam + ": ").lower().strip()
        if x == 0:
            occ = inp
            nam = " violent verb"
        elif x == 1:
            viverb = inp
            nam = " special skill"
        elif x == 2:
            skill1 = inp
            nam = "nother special skill"
        elif x == 3:
            skill2 = inp
        else:
            exit("Error on line %s: Program attempted to assign input to variable in category 'Improper Nouns', but variable was out of range." % getframeinfo(currentframe()).lineno)
    return occ, viverb, skill1, skill2
aspect['occ'], aspect['viverb'], aspect['skill1'], aspect['skill2'] = improperNouns()

    # Proper Nouns
def properNouns():
    nam = "town"
    for x in xrange(0, 2):
        inp = raw_input("Enter the name of the " + nam + ": ").lower().title().strip()
        while inp == "":
            print("The name of the " + nam + " can not be blank.")
            inp = raw_input("Enter the name of the " + nam + ": ").lower().title().strip()
        nam = "hills"
        if x == 0:
            town = inp
        elif x == 1:
            hills = inp
        else:
            exit("Error on line %s: Program attempted to assign input to variable in category 'Proper Nouns', but variable was out of range." % getframeinfo(currentframe()).lineno)
    return town, hills
aspect['town'], aspect['hills'] = properNouns()

    # Adjectives
def adjectives():
    while True:
        try:
            adjinput = raw_input("Enter five adjectives separated by commas: ").lower()
            adjinputlist = adjinput.split(',')            # creates list from input split by commas
            adjlist = [x.strip() for x in adjinputlist]   # creates another list, strips whitespace
            if adjlist[4]:
                pass
            try:
                if adjlist[5]:
                    pass
                print("Your list is too long.")
            except IndexError:
                if adjlist[0] and adjlist[1] and adjlist[2] and adjlist[3] and adjlist[4]:
                    return adjlist[:]
                    break
                else:
                    print("Adjective may not be blank.")
        except IndexError:
            print("Your list doesn't seem to be long enough, try again.")

aspect['adj1'], aspect['adj2'], aspect['adj3'], aspect['adj4'], aspect['adj5'] = adjectives()

# Introduction
def introduction():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal
    show("In a time before the world fell into the splitting fires of hell, we looked to the legends.")
    show("Only one true hero could save us from our arriving, inevitable fate. The legends spoke of a place long ago, before the fire.")
    print("Past the {0} hills of {1} was a town named {2}. Here resided the adventurer, {3}, a {4} and {5} {6}."
          ).format(aspect['adj1'], aspect['hills'], aspect['town'], aspect['name'], aspect['adj2'], aspect['adj3'], aspect['occ'])
    raw_input("... ")
    print "{0} was a {1} {2}, ready to {3} what evil would ever cross {4} path.".format(aspect['HeShe'], aspect['adj4'], aspect['occ'], aspect['viverb'], aspect['hisher'])
    raw_input("... ")
    print("")
    show("but first, %s was thirsty." % aspect['heshe'])
    print("")

introduction()

move = raw_input("Type 'Tavern' to go to the tavern. ").lower().strip()
while move != "tavern":
    move = raw_input("No, it's spelled t-a-v-e-r-n. ").lower().strip()

# Tavern
show("The tavern in %s is old and rugged. Beaten down by countless travelers, it has acquired quite the homey atmosphere." % aspect['town'])
print('You approach the bartender. "Ey, what\'le it be for ya?" he says.')
drink = raw_input("On the shelf is a bottle of rum and a can of Mountain Dew. Which do you choose? (rum, dew) ").lower()
while drink != "rum" and drink != "dew":
    drink = raw_input("Come on, 'rum' or 'dew'. ")
if drink == "rum":
    show("\"I'll 'ave the rum, sir,\" you say.")
elif drink == "dew":
    show('"Gimme dat dew," you say. "I knew you were a dank one," the bartender says knowingly. You tip your fedora gently to show how euphoric you are about this dew.')
    show('"XDDDDDDDDDD," says the bartender. You throw down a one dollar bill. "I think this will cover it."')
    print("")
    show('"Holy fucking shit!" exclaims the bartender. "Did you see that??????"')
    show('"Hold on m8," you say. "I need to take a closer look." You begin to examine the bill.')
    show('"There is something fishy about this bill... could it be?"')
    show("You connect the three sides of the strange shape on the back of the bill and realize what you had been missing all along.")
    show("The three sides would connect to form none other than the illumrunarti triange. Then everything goes black.")
    show('You wake up to find yourself in a green haze in an unreal dimension. Ahead of you a light begins to appear. "Who\'s there??" you ask.')
    show('"You know who I am," the voice says. A wave of euphoria rushes over you as Snoop Dogg steps into view.')
    show("\"And you know why you're here, for only you, %s, have the swagger dank enough to defeat the greatest enemy of all... the illum-\"" % aspect['name'])
    show('You wake up on the floor of the tavern covered in doritos and see the bartender standing over you. "I know what I must do," you say.')
    show("Looking into your eyes with a piercing stare, the bartender speaks the word that will change your life forever.")
    print("")
    show('"k."')
else:
    exit("Error on line %s: Program attempted to interpret variable 'drink', but variable was out of range." % getframeinfo(currentframe()).lineno)

print("That's the end of this version of the game.")
