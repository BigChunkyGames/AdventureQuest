
from utils import *

def introduction(player):
    clear()
    show("In a time before the world fell into the splitting fires of "
         "hell, we looked to the legends.")
    show("Only one true hero could save us from our seemingly "
         "inevitable fate. The legends spoke of a time long ago, "
         "before the fire.")
    print("Past the {0} hills of {1} was a town named {2}. Here "
          "resided the adventurer, {3}, a {4} and {5} {6}."
          ).format(player.aspect['adj1'], player.aspect['hills'], player.aspect['town'],
                   player.aspect['name'], player.aspect['adj2'], player.aspect['adj3'],
                   player.aspect['occ'])
    raw_input("... ")  # TODO: Replace "a" with "an" when needed
    print "{0} was a {1} {2}, ready to {3} any evil that would dare " \
          "to cross {4} path.".format(player.aspect['HeShe'], player.aspect['adj4'],
                                      player.aspect['occ'], player.aspect['viverb'],
                                      player.aspect['hisher'])
    raw_input("... ")
    print("")
    show("but first, %s was thirsty." % player.aspect['heshe'])
    clear()    
    print("You recognize your humble town's tavern to the north.")
    move = raw_input("Type 'tavern' to enter the tavern. ").lower().strip()
    while move != "tavern":
        if move == "house":
            print "Calm down there m8, we'll get there later."
        move = raw_input("It's spelled t-a-v-e-r-n. ").lower().strip()
    # Tavern in intro is unique to tavern.py
    show("The tavern in %s is old and rugged. Beaten down by countless "
         "travelers, it's acquired a homey atmosphere." % player.aspect['town'])
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
         "the illum-\"" % player.aspect['name'])
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