from source.utils import *
from source.lists import CURSES
from source.enemy import *
from source.combat import *
import random
from source.places_maintown import *


def grandpasTrailer(player):
    gspeed = .07 # speed of grandpas text
    show("Dense woods surround a path that leads into darkness.")
    show("Carefully, you make your way down the dirt path.")
    tryForCombat(player)
    show("With powerful strides, you continue down the dirt path.")
    tryForCombat(player)
    show("The path stretches on into the darkness.")
    tryForCombat(player)
    show("Continuing down the path, you take note of the dirt and the darkness.")
    tryForCombat(player)
    show("The path continues, dark and dirt.")
    tryForCombat(player)
    show("Finally the path ends.")
    show("There is a trailer beside a small pond.")
    print("Enter the trailer?")
    if yesno(player):
        show("Before you can reach the door a tiny robot opens it and looks at you.")
        printSlowly('"What the heck do you want?"',)
        x = player.getInput()
        if 'grandpa' in x.lower():
            printSlowly('"Grandpa? I don\'t know any grandpas."', )
        elif 'lasagna' in x.lower():
            printSlowly('Lasagna? I don\'t know any lasagnas.')
        elif x.lower() in CURSES:
            printSlowly('Whoa, watch your mouth around here.')
        else:
            printSlowly('"I am TROG."', )
        printSlowly('"This is my trailer. I\'ve been living here for years."', )
        printSlowly('"Isn\'t it just beautiful?"', )
        printSlowly('"A tiny robot like myself, out in the wild with my own trailer. "', )
        printSlowly('"People are just so open these days."', )
        printSlowly('"We live in an accepting world."', )
        printSlowly('"Even robots can own property."', )
        show("From inside the trailer you hear what sounds like someone stumbling.")
        printSlowly('"Damnit TROG, who\'s at the door?"', secondsBetweenChars=gspeed)
        show("From behind the the robot, your grandpa steps into view.")
        show("His long grey hair and stained lab coat, stir in the breeze.")
        printSlowly('"Oh it\'s you, ' + player.aspect['name'] + '!"', secondsBetweenChars=gspeed)
        printSlowly('"I was wondering when you\'d stop by."', secondsBetweenChars=gspeed)
        printSlowly('"Hey... is that lasagna I smell? "', secondsBetweenChars=gspeed)
        if yesno(player):
            player.removeFromInventory('Lasagna')
            printSlowly('"Your mother\'s lasagna always fills my belly right to the brim. "', secondsBetweenChars=gspeed)
        else:
            printSlowly('"Well that\'s too bad."', secondsBetweenChars=gspeed)
            printSlowly('"Must be your breath I\'m smelling then."', secondsBetweenChars=gspeed)
        printSlowly('"Well come inside then."', secondsBetweenChars=gspeed)
        show("You step up into the trailer which is revealed to be much larger than it seemed from the outside.")

        show("Suddenly you don't feel right.")
        show("There's something wrong here.")
        show("Wait a minute, is that...")
        printSlowly('The end of the demo?', secondsBetweenChars=.1)
        show("Yes.")
        show("It is.")
        show("You jolt upright in bed.")
        show("Huh, what a strange dream.")
        show("You walk down stairs and eat a piece of toast.")
        show("Deciding you better start your day, you make your way outside.")
        return maintown(player)


        
        
    else:
        show("Yeah, not right now.")
        show("You turn around and follow the path back outside of the woods.")
        return

def tryForCombat(player):
    if random.randint(0,100) <= 15:
        e = Enemy(player, 'spooky',  )
        c = Combat(player, enemy=e)


# TODO add block and attack to stats screen