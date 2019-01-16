from source.utils import *
from source.lists import getInvalidOptionText,getConversationResponse
from source.world import wormHole
from source.item import Item

def wormHome(player):

    if "owns worm home" in player.choices:
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
                show("It used to be Angry Worm Poet's bedroom.")
                show("A worm and cozy bed is pushed to one corner.")
                show("It is now yours. You may sleep in it whenever you wish.")
                player.sleep(customText="You lay down in the worm and cozy bed. The wormth pushes you immediately into  a deep sleep.")
                show("After that delightful nap you are again faced with a choice.")
            elif checkInput(x, 'Tape-Worm'):
                pass
            elif checkInput(x, 'tunnels'):
                pass
            elif checkInput(x, 'leave'):
                pass
            else:
                print(getInvalidOptionText())
    elif True: # visit before submitting poem # TODO set a player choice after submitting poem
        show('Andy Worm Poet is extremely excited to see you again.')
        show('"Hey there friend!"')
        print('"Would you care for some tea?"')
        if yesno(player): tea(player)
        show('"Things are really looking up for me, friend!"')
        show('"I\'m really feeling good these days!"')
        show('"But I talk too much."')
        print('"Tell me about yourself!"')
        for i in range(getRandInt(min=2, max=3)):
            x = input(player)
            print(getConversationResponse(getRandInt(min=1, max=3)))
        show('Andy Worm Poet gets distracted from your conversation.')
        show('He looks at you after staring at a wall for a few minutes.')
        print('"Did you need to use my wormholes to go somewhere?"')
        x = yesno(player)
        show("Okay, see you again soon!")
        if x: return wormHole(player)
        else: return

def tea(player): 
    player.count("tea from andy", increment=True)
    while(True):
        if player.counters["tea from andy"]==1:
            tea1 = "Chamomile"
            tea2 = "Lavender"
        elif player.counters("tea from andy")==2:
            tea1 = "Oolong"
            tea2 = "Kombucha"
        elif player.counters("tea from andy")==3:
            tea1 = "Sencha"
            tea2 = "Matcha"
        elif player.counters("tea from andy")>3:
            show("Oh, I don't have any more tea. Sorry about that.")
            break
        else: bug(player)

        printc("@'"+ tea1 +"'@yellow@ or @'"+ tea2 +"'@yellow@?")
        x = getInput(player)
        if checkInput(x, tea1):
            show("Andy pours you a cup of "+ tea1 +" tea.")
            tea = tea1
            break
        elif checkInput(x, tea2):
            show("Andy pours you a cup of "+ tea2 +" tea.")
            tea = tea2
            break
        else:
            print("Which tea do you want?")
    receiveTea(player, tea)

def receiveTea(player, tea):
    i = Item(player, tea + ' tea', customDescription="Andy Worm Poet gave you this cup of tea. It's still warm and smells delicious.", _type='consumable', sellValue=5)
    i.customActivationFunction = lambda:i.consume(heal=3)
    player.addToInventory(i)
            
