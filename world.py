 # player comes here when they are not inside of a place or experiancing an event

from utils import *
from places.burntTown import *

def world(player):
    player.addVisit("world")
    while True:
        print("To the 'North' you can see a huge TODO sign")
        if player.getVisits("world") == 1:
            print("To the 'East' you can see your objective")
        print("Or you can 'travel' back to somewhere you've already been.")
        print("Which direction would you like to go?")
        x = input()
        if( x == "east" or x == "e"):
            #todo actually go east
            burntTown(player)
            break
        elif (x == "back" or x == "b" or x = "cancel" or x = "c"):
            return
        elif (x == "t" or x == "travel"):
            while True:
                print("You can travel to one of these places:")
                for i in player.teleportableAreas:
                    print(i)
                x = input()
                if x in player.teleportableAreas:
                    print("You decided to get back on your way to"),
                    print("%s." %x),
                    show("")
                    player.teleportableAreas[x](player) #teleport
                    break

                
            break
