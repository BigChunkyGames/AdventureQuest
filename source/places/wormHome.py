from source.utils import *
from source.lists import getInvalidOptionText,getConversationResponse, getRandomTVShow
from source.world import wormHole
from source.item import Item

def wormHome(player):

    if "owns worm home" in player.choices:
        print("There are a few things to do inside of the quaint worm abode.")
        while(True):
            printc("There is a @'Worm TV'@yellow@ at the other end of the room.")
            printc("There is a @'Tape-Worm'@yellow@ system beside the TV.")
            printc("There is a worm and cozy @'bed'@yellow@.")
            printc("You could investigate the @'worm holes'@yellow@.")
            printc("Or you could @'leave'@yellow@.")

            x = player.getInput()
            if checkInput(x, "Worm TV"):
                show("You put Tubeworms in your eyes, sit back, and watch some T.V.")
                for i in range(20):
                    wait(1, ". ")
                    if i == 10:
                        print getRandomTVShow()
                show("Your entire day is wasted.")
                show("After a few too many hours, you stand up, lethargic and groggy, and try to regain your wasted time.")
                show("But it is lost forever.")
            elif checkInput(x, 'bed'):
                show("You continue into the next room.")
                show("It used to be Angry Worm Poet's bedroom.")
                show("A worm and cozy bed is pushed to one corner.")
                show("It is now yours. You may sleep in it whenever you wish.")
                player.sleep(customText="You lay down in the worm and cozy bed. The wormth pushes you immediately into  a deep sleep.")
                show("After that delightful nap you are again faced with a choice.")
            elif checkInput(x, 'Tape-Worm') or checkInput(x, "tape worm"):
                show("You place the Tape-Worms in your ears.")
                # TODO music sound
            elif checkInput(x, 'worm holes') or checkInput(x, 'worm') or checkInput(x, 'worm hole'):
                return wormHole(player)
            elif checkInput(x, 'leave'):
                show("You crawl back out of the hole.")
                return
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
            x = getInput(player)
            print(getConversationResponse( responses = getRandInt(min=1, max=3)))
        show('Andy Worm Poet gets distracted from your conversation.')
        show('He looks at you after staring at a wall for a few minutes.')
        print('"Did you need to use my wormholes to go somewhere?"')
        x = yesno(player)
        show('"Okay, see you again soon!"')
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
            
