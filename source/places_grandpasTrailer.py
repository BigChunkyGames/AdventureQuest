from source.utils import *
from source.lists import CURSES
from source.enemy import *
from source.combat import *
import random
from source.places_maintown import *


def grandpasTrailer(player):
    gspeed = .07 # speed of grandpas text
    # show("Dense woods surround a path that leads into darkness.")
    # show("Carefully, you make your way down the dirt path.")
    # tryForCombat(player)
    # show("With powerful strides, you continue down the dirt path.")
    # tryForCombat(player)
    # show("The path stretches on into the darkness.")
    # tryForCombat(player)
    # show("Continuing down the path, you take note of the dirt and the darkness.")
    # tryForCombat(player)
    # show("The path continues, dark and dirty.")
    # tryForCombat(player)
    # show("Finally the path ends.")
    # show("There is a trailer beside a small pond.")
    # print("Enter the trailer?")
    # if yesno(player):
    #     player.registerVisit('grandpas trailer')
    #     if  player.getVisits('grandpas trailer')== 1: # only on first visit
    #         player.stats['relation with grandpa'] = 0
    #         show("Before you can reach the door a tiny robot opens it and looks at you.")
    #         printSlowly('"What the *beep* do you want?"',)
    #         x = player.getInput()
    #         if 'grandpa' in x.lower():
    #             printSlowly('"Grandpa? I don\'t know any grandpas."', )
    #         elif 'lasagna' in x.lower():
    #             printSlowly('Lasagna? I don\'t know any lasagnas.')
    #         elif x.lower() in CURSES:
    #             printSlowly('Whoa, watch your mouth around here.')
    #         else:
    #             printSlowly('"What are you talking about?"', )
    #         printSlowly('"I\'m TROG. This is my trailer. I\'ve been living here for years."', )
    #         printSlowly('"Isn\'t it just *bloop*ing beautiful?"', )
    #         printSlowly('"A tiny robot like myself, out in the wild with my own trailer."', )
    #         printSlowly('"People are just so open these days."', )
    #         printSlowly('"We live in an accepting world."', )
    #         printSlowly('"Even robots can own property."', )
    #         show("From inside the trailer you hear what sounds like someone stumbling.")
    #         printSlowly('"Damnit TROG, who\'s at the door?"', secondsBetweenChars=gspeed)
    #         show("From behind the the robot, your grandpa steps into view.")
    #         show("His long grey hair and stained lab coat, stir in the breeze.")
    #         printSlowly('"Oh it\'s you, ' + player.aspect['name'] + '!"', secondsBetweenChars=gspeed)
    #         printSlowly('"I was wondering when you\'d stop by."', secondsBetweenChars=gspeed)
    #         printSlowly('"Hey... is that lasagna I smell? "', secondsBetweenChars=gspeed)
    #         if yesno(player):
    #             player.choices.append("gave lasagna to grandpa")
    #             if player.removeFromInventory('Lasagna'):
    #                 player.stats['relation with grandpa'] += 1
    #                 printSlowly('"Your mother\'s lasagna always fills my belly right to the brim. "', secondsBetweenChars=gspeed)
    #             else:
    #                 printSlowly("Don't fool me like that, I'm hungry!", secondsBetweenChars=gspeed)
    #                 player.stats['relation with grandpa'] -= 1
    #         else:
    #             player.stats['relation with grandpa'] += -1
    #             printSlowly('"Well that\'s too bad."', secondsBetweenChars=gspeed)
    #             printSlowly('"Must be your breath I\'m smelling then."', secondsBetweenChars=gspeed)
    #         printSlowly('"Well come inside then."', secondsBetweenChars=gspeed)
    #         show("You step up into the trailer which is revealed to be cluttered with beakers and scientific equipment with no place to practice science.")
    #         if player.equippedArmourFeet != None:
    #             printSlowly('"You wanna take your shoes off? Looks like you got some dirt on \'em."', secondsBetweenChars=gspeed)
    #             if yesno(player):
    #                 player.stats['relation with grandpa'] += 1
    #                 shoes = player.equippedArmourFeet.name
    #                 player.unequip(_type='armour', armourSlot='feet')
    #                 print("Your " + shoes + " were unequipped." )
    #             else:
    #                 player.stats['relation with grandpa'] += -1
    #                 player.karma -= 1
    #         printSlowly('"Why don\'t you take a seat?"', secondsBetweenChars=gspeed)
    #         show("You move some scientific glassware off of an armchair and take a seat.")
    #         printSlowly('"Glad you made it here in one piece. That ol\' path can be pretty dark and dirty!"', secondsBetweenChars=gspeed)
    #         printSlowly('"Hey, you look like you could use a pick-me-up. Want a bottle of my special serum?"', secondsBetweenChars=gspeed)
    #         show("Your grandpa opens a high cubbord, knocking some vials onto the floor, the contents of which burn a smoldering hole in the floor.")
    #         show("He puts the jar of dark red serum into your hands.")
    #         print("Drink it?")
    if yesno(player):
        # player.stats['relation with grandpa'] += 1
        show("You down the entire jar of bubbly slush.")
        show("Tears well in your eyes as the intense flavor eats away at your taste buds.")
        show("You belch up a thick cloud of vapor as you feel it beginning to take effect.")
        show("A pain stronger than you've ever felt comes over you in a rush.")
        waitTime = 0.8
        while player.hp > 1:
            player.takeDamage(1)
            wait(float(waitTime))
            waitTime = waitTime*.93
        printSlowly('"You should see the look on your face! Just give it a moment."', secondsBetweenChars=gspeed, skipable=False)
        waitTime = 0.8
        while player.hp < player.maxhp:
            player.regenHealth(1)
            wait(float(waitTime))
            waitTime = waitTime*.93
        printSlowly('', secondsBetweenChars=gspeed)
        show("Suddenly you feel better than ever.")
    else:
        player.stats['relation with grandpa'] += -1
        printSlowly('"Oh... I\'ll just put this back then."', secondsBetweenChars=gspeed)
        show("Your grandpa takes a swig of the serum and puts it back in the cubbard.")
    printSlowly('"So what did you want to talk about?"', secondsBetweenChars=gspeed)
    x = player.getInput()
    if 'illum' in x or 'illuminati' in x or 'ilum' in x:
        printSlowly('"The illuminati?"', secondsBetweenChars=gspeed)
        printSlowly('"My, that takes me back."', secondsBetweenChars=gspeed)
        show("A visible wave of nostalgia comes over your grandpa and he looks away.")
        printSlowly('"What are you interested in them for?"', secondsBetweenChars=gspeed)
        x = player.getInput()
        if 'destroy' in x or 'kill' in x or 'defeat' in x or 'end' in x or 'quest' in x:
            printSlowly('"My my. You\'ve got your sights set then eh?"', secondsBetweenChars=gspeed)
        if 'join' in x:
            printSlowly('"Hah, if you can find them!"', secondsBetweenChars=gspeed)
        if 'snoop' in x or 'dog' in x or 'vision' in x or 'preminition' in x or 'dream' in x :
            printSlowly('"Oh dear. I had visions of Snoop Dogg back in my hay day. It was never a good sign."', secondsBetweenChars=gspeed)
        printSlowly('"Well I\'m not sure I can be of much more help to you."', secondsBetweenChars=gspeed)
        printSlowly('"Although... I once stumbled across a book in the Library of Bable on the subject."', secondsBetweenChars=gspeed)
        printSlowly('"I think it was in the restricted section."', secondsBetweenChars=gspeed)
        printSlowly('"If you really need to know more about them, then you should try to find it."', secondsBetweenChars=gspeed)
        printSlowly('"The library is south of here, you can\'t miss it."', secondsBetweenChars=gspeed)
        printSlowly('"Come back here soon! I\'ll have another potion for ya."', secondsBetweenChars=gspeed)



    # else:
    #     show("Yeah, not right now.")
    #     show("You turn around and follow the path back outside of the woods.")
    #     return

def tryForCombat(player): # TODO trailer park enemys
    if random.randint(0,100) <= 15:
        e = Enemy(player, 'spooky',  )
        c = Combat(player, enemy=e)


# TODO add block and attack to stats screen