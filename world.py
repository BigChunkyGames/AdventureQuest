 # player comes here when they are not inside of a place or experiancing an event

from utils import input, clear, show

def world(player):
    player.addVisit("world")
    
    while True:
        # print player.currentLocationX
        # print player.currentLocationY 
        print("To the 'North' you can see" ),
        print player.map.getTileDescription(player.currentLocationX , player.currentLocationY - 1)
        print("To the 'East'  you can see"),
        print player.map.getTileDescription(player.currentLocationX +1 , player.currentLocationY )
        print("To the 'South' you can see"),
        print player.map.getTileDescription(player.currentLocationX , player.currentLocationY +1)
        print("To the 'West'  you can see"),
        print player.map.getTileDescription(player.currentLocationX -1, player.currentLocationY )
        print("Or you can 'travel' back to somewhere you've already been.")
        x = input()
        if( x == "north" or x == "n"):
            player.map.goTo(player.currentLocationX , player.currentLocationY - 1, player)
            
        elif( x == "east" or  x == "e"):
            player.map.goTo(player.currentLocationX +1 , player.currentLocationY , player)
            
        elif( x == "south" or x == "s"):
            player.map.goTo(player.currentLocationX , player.currentLocationY +1, player)
            
        elif( x == "west" or x == "w"):
            player.map.goTo(player.currentLocationX -1, player.currentLocationY, player)
            
        elif (x == "back" or x == "b" or x == "cancel" or x == "c"):
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
                elif x == "cancel" or x == "c" or x == "escape" or x == "e" or x == "back" or x == "b":
                    break 
            break
        else:
            clear()
            print "I'm really sorry but that's just not a valid option.\n" #TODO falvor text
            # you tried to go that way but it didn't make any sense
            # uou went that way but ended up right back where you started
            
