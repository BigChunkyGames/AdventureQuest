import os   # Used to clear terminal
os.system('cls' if os.name == 'nt' else 'clear')  # Clears terminal
print("Welcome to ADVENTURE QUEST Version 0.00.24P! The P stands for "
      "python.")

# Global Dictionaries
aspect = {}  # Beginning inputs (name, gender, etc) used in storytelling
visitedareas = {}

# Define Functions


def show(text):  # Displays text, waits for 'enter' before continuing.
    print(text)
    raw_input("... ")


# Returns number of times visited, including current visit
def visited(area):
    try:
        if visitedareas[area]:
            visitedareas[area] += 1
            return visitedareas[area]
    except KeyError:
        visitedareas[area] = 1
        return 1


def name():  # Used in charCreation()
    charname = raw_input("Enter your hero's name: ").lower().strip()\
        .title()
    while charname == "":
        charname = raw_input("You must enter your hero's name: ")\
            .lower().strip().title()
    return charname


def gender():
    chargender = raw_input("Enter your hero's gender, 'boy' or "
                           "'girl': ").lower()
    while chargender != "boy" and chargender != "girl":
        chargender = raw_input("Select 'boy' or 'girl': ").lower()
    return chargender


def pronouns():
    if aspect['gender'] == "boy":
        return "he", "He", "his"
    elif aspect['gender'] == "girl":
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
        adjinput = raw_input("Enter five adjectives separated by "
                             "commas: ").lower()
        adjinputlist = adjinput.split(',')
        adjlist = [x.strip() for x in adjinputlist]
        if len(adjlist) == 5:
            return adjlist
        elif len(adjlist) > 5:
            print("Your list is too long.")
        elif len(adjlist) < 5:
            print("Your list isn't long enough.")


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
    move = raw_input("Type 'tavern' to enter the tavern. ").lower()\
        .strip()
    while move != "tavern":
        move = raw_input("No, it's spelled t-a-v-e-r-n. ").lower()\
            .strip()
    # Tavern
    show("The tavern in %s is old and rugged. Beaten down by countless "
         "travelers, it's acquired a homey atmosphere." %
         aspect['town'])
    print('You approach the bartender. "Ey, what\'le it be for ya?" he '
          'says.')
    drink = raw_input("On the shelf is a bottle of rum and a can of "
                      "Mountain Dew. Which do you choose? (rum, dew) ")\
        .lower()
    while drink != "rum" and drink != "dew":
        if drink == 'neither':
            drink = raw_input("You've got to drink something. What'll "
                              "it be? ")
        else:
            drink = raw_input("Come on, 'rum' or 'dew'. ")
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
    move = raw_input('Type "house" to go to your house.').lower()\
        .strip()
    while move != "house":
        if move == "tavern":
            print("You just came from there, you need to go to your "
                  "house.")
            move = raw_input('Type "house" to go to your house.')\
                .lower().strip()
        else:
            move = raw_input('No. Type "house" ')
    show('You enter your house, hoping mum will get the camera. "Mom! '
         'I\'m going on an adventure!!1!!!!1one!!"')
    show('She looks up from the dick sock she\'s knitting. "Alright '
         'sweetie, be safe! Here, take this."')
    print('You have acquired the camera. Press "i" to access your '
          'inventory. ')
    # TODO: add this ability
    # TODO: add initial story


def main():
    charcreation()
    introduction()

main()
print("That's the end of this version of the game.")
