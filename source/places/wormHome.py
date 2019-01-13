from source.utils import *
from source.lists import getInvalidOptionText


def wormHome(player):

    print("There are a few things to do inside of the quaint worm abode.")
    while(True):
        
        printc("You could watch some @'Worm TV'@yellow@.")
        printc("There is a worm and cozy @'bed'@yellow@.")
        printc("There is a @'Tape-Worm'@yellow@ system beside the TV.")
        printc("You could investigate the @'tunnels'@yellow@.")
        printc("Or you could @'leave'@yellow@.")

        x = player.getInput()
        if checkInput(x, "Worm TV"):
            pass
        elif checkInput(x, 'bed'):
            show("You continue into the next room.")
            show("It used to be Angry Worm Poet’s bedroom.")
            show("A worm and cozy bed is pushed to one corner.")
            show("It is now yours. You may sleep in it whenever you wish.")
            player.sleep(customText="You lay down in the worm and cozy bed. The wormth pushes you immediately into a deep sleep.")
            show("After that delightful nap you are again faced with a choice.")
        elif checkInput(x, 'Tape-Worm'):
            pass
        elif checkInput(x, 'tunnels'):
            pass
        elif checkInput(x, 'leave'):
            pass
        else:
            print(getInvalidOptionText())
