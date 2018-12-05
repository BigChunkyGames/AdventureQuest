from utils import *
from lists import *


def home(player):
    show("You enter your house through the familiar front door, taking in "
         "the sights of your childhood abode, reminiscing about all the "
         "dank shit you did as a kid.")
    while True:
        print("You could 'explore' your house some more, 'sleep', 'play' a console game, or just 'leave'.")
        action = input(player)
        if action == "explore" or action == "e":
            if player.getVisits("Explore House", "add") == 1:
                show("You head upstairs to your room and look around for a bit. "
                     "You realize that you left your can of Mtn Dew laying on top "
                     "of your dresser.")
                show("You grab the can just in case you need it later.")
                # TODO: add the can to your inventory
            else:
                show("You look around the house, but shockingly can't find anywhere you haven't already explored")
        elif action == "sleep" or action == "s":
            show("After a long day's work adventuring, you're tired. You decide to climb into your old childhood bed to get some rest.")
            show("Your mother tucks you in and kisses you on the forehead.")
            show("Good night sweetie, don't let the bed bugs bite!")
            player.sleep()
            show("You turn to leave. \"Bye sweetie, be home for dinner!\" your mother says.")
            show("You shoot her with the double finger guns and head out as she collapses to the floor.")
            break
        elif action == "play" or action == "p":
            player.addVisit("House Console Game")
            if player.getVisits("House Console Game") == 1:
                show("You decide to kill some time by playing some Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version")
                show("After popping the disc into your GameSphere 420, you realize that it needs to install.")
                show("You watch the loading bar move at an astoundingly slow pace. This could take a while.")
                show("Standing up, you decide to do something fun in the mean time.")
            else:
                show("You walk over to your GameSphere 420 to see if your game is done installing.")
                show("Oh, look at that!")
                show("It isn't.")
                show("You decide to wait some more.")
        elif action == "leave" or action == "l":
            show("You look around your house for a bit, before deciding to leave.")
            print("Your mother looks up from the " + getRandomDankClothing()  + " she's knitting.")
            raw_input("... ")
            show('"Bye sweetie, good luck on your adventures! Don\'t forget to remember: ' + getMotherlyPlattitude() )
            break
        else:
            print("Please input a valid action.")
    # TODO: add more stuff to do in your house
