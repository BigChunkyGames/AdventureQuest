 # player comes here when they are not inside of a place or experiancing an event

from source.utils import getInput, clear, show, printc, bug, yesno, checkForCancel
from source.lists import getInvalidOptionText

def world(player):
    player.registerVisit("world")
    
    while True:
        clear()
        # TODO: make seperate biome synomyms for this part
        printc("To the @'North'@blue@ you can see " + player.map.getTileDescription(player.currentLocationX , player.currentLocationY - 1)), 
        printc("To the @'East'@blue@  you can see " + player.map.getTileDescription(player.currentLocationX +1 , player.currentLocationY )), 
        printc("To the @'South'@blue@ you can see " + player.map.getTileDescription(player.currentLocationX , player.currentLocationY +1)),
        printc("To the @'West'@blue@  you can see " + player.map.getTileDescription(player.currentLocationX -1, player.currentLocationY )), 
        x = getInput(player)
        if( x == "north" or x == "n"):
            player.map.goTo(player.currentLocationX , player.currentLocationY - 1, player)
            
        elif( x == "east" or  x == "e"):
            player.map.goTo(player.currentLocationX +1 , player.currentLocationY , player)
            
        elif( x == "south" or x == "s"):
            player.map.goTo(player.currentLocationX , player.currentLocationY +1, player)
            
        elif( x == "west" or x == "w"):
            player.map.goTo(player.currentLocationX -1, player.currentLocationY, player)
            
        elif (checkForCancel(x)):
            show("You turn around, having not finished your time at " + player.map.getTile(player.currentLocationX,player.currentLocationY).description + ".")
            player.map.goTo(player.currentLocationX, player.currentLocationY , player)
            return
        else:
            clear()
            show(getInvalidOptionText(traveling=True))

            
def wormHole(player):
    while True:
        if len(player.teleportableAreas) == 0:
            bug(player)
        elif len(player.teleportableAreas) == 1:
            show("The only worm hole that's cleared right now goes to " + player.aspect['town'] + ".")
            print("Travel to " + player.aspect['town'] + "?")
            if yesno(player): return player.teleportableAreas[player.aspect['town']](player)
            else: 
                show("You decided to just go back outside.")
                return
        else:
            while True:
                print("The worm holes lead to ")
                count = 0
                max = len(player.teleportableAreas)
                s = ''
                for i in player.teleportableAreas:
                    count = count + 1
                    if count != max:
                        s += "@'" + i + "'@yellow@" + ", "
                    else: 
                        s += "and @'" + i + "'@yellow@."
                printc(s)
                x = getInput(player)
                if x in player.teleportableAreas:
                    show("You set out on your way towards " + x + ".")
                    show("Wow. That was fast.")
                    player.teleportableAreas[x](player) #teleport
                    return
                elif checkForCancel(x):
                    show("Just kidding.")
                    return world(player) 
                else:
                    show(getInvalidOptionText(traveling=True))
