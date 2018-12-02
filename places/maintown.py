from tavern import *
from blacksmith import *
from store import *
from home import *
from world import *
from utils import *


def maintown(player):
    player.addVisit(player.aspect['town']) # places inside of this here while loop return to the while loop when they are finished
    player.addToTeleportableAreas(player.aspect['town'], maintown)
    while True:
        print("You stand in the homey town of {0}, just passed the hills of {1}, a lovely place. Where do you "
              "want to go?").format(player.aspect['town'] , player.aspect['hills'])
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open at this time of day.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Or you could always 'leave' your humble town to explore the world.")
        print("Where do you want to go?")
        place = input()
        while place == "":
            place = input()
        if place == "home" or place == "h":
            home(player)
        elif place == "tavern" or place == "t":
            tavern(player)
        elif place == "store" or place == "s":
            store(player)
        elif place == "blacksmith" or place == "b":
            blacksmith(player)
        elif place == "leave" or place == "l":
            if player.getVisits("maintown") == 1:
                show("Off to find your grandpa eh? Mom said to head EAST.")
            world(player)
            break # this break right here is really important
        else:
            print("You've got to pick one of the places listed.")
            print("")