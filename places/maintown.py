from tavern import *
from blacksmith import *
from store import *
from world import *
from utils import *


def maintown(player):
    player.addVisit("maintown") # places inside of this here while loop return to the while loop when they are finished
    while True:
        print("You stand in the homey town of %s, a lovely place. Where do you "
              "want to go?") % player.aspect['town']
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Or you could 'head out' into the world.")
        print("Where do you want to go?")
        place = input()
        while place == "":
            place = input()
        if place == "home":
            home(player)
        elif place == "tavern":
            tavern(player)
        elif place == "store":
            store(player)
        elif place == "blacksmith":
            blacksmith(player)
        elif place == "head out":
            if player.getVisits("maintown") == 1:
                show("Off to find your grandpa eh? Mom said to head " + Fore.YELLOW + "EAST.")
            world(player)
            break # this break right here is really important
        else:
            print("You've got to pick one of the places listed.")
            print("")