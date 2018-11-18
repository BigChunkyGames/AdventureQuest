from tavern import *
from blacksmith import *
from store import *


def maintown(player):
    while True:
        print("You stand in the homey town of %s, a lovely place. Where do you"
              "want to go?") % player.aspect['town']
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Where do you want to go?")
        place = raw_input("> ").lower().strip()
        while place == "":
            place = raw_input("> ").lower().strip()
        if place == "home":
            home(player)
        elif place == "tavern":
            tavern(player)
        elif place == "store":
            store(player)
        elif place == "blacksmith":
            blacksmith(player)
        else:
            print("You've got to pick one of the places listed.")
            print("")