from source.utils import *
from source.item import Item

def introduction(player): #TODO i think we should change the intro to be less demanding of the player first thing. maybe we can add an option to have the lore given to the player or if they player can write the lore themselves
    clear()
    saveGame(player)
    show("In a time before the world fell into the splitting fires of "
         "hell, we looked to the legends.")
    show("Only one true hero could save us from our seemingly "
         "inevitable fate. The legends spoke of a time long ago.")
    print("In the " + player.aspect['adj1']+ " land of "+player.aspect['land']+" was a town named "+player.aspect['town']+'. Here resided the adventurer, '+player.aspect['name']+', a '+player.aspect['adj2']+' and '+player.aspect['adj3']+' '+player.aspect['occ']+".")
    input("... ")  # TODO: Replace "a" with "an" when needed
    print (player.aspect['HeShe'].capitalize()+" was a "+player.aspect['adj4']+" "+player.aspect['occ']+", ready to "+player.aspect['viverb']+" any evil that would dare to cross "+player.aspect['hisher']+" path.")
    input("... ")
    show("But first, %s was thirsty." % player.aspect['heshe'])
    clear()    
    printc("You recognize your humble town's @'tavern'@yellow@ to the north.")
    print("Type 'tavern' to enter the tavern. ")
    attempts = 0
    dies = 0
    move = getInput(player)
    while not move == "t" and not move == 'tavern' :
        if move == "'tavern'":
            print ("Good job but you don't need to type the 'single quotes'.")
            break
        attempts = attempts +1
        if move == "house":
            print ("Calm down there m8, we'll get there later.")
        elif attempts ==1:
            print("Come on now, it's spelled t-a-v-e-r-n.")
        elif move == "die" and dies == 0:
            dies = dies +1
            show("Though extremely thirsty, you refuse to go to the tavern and drink.")
            printc("If you don't go to the @'tavern'@yellow@ soon, you really might keel over from dehydration.")
        elif move == "die" and dies > 0:
            dies = dies +1
            show("Your throat dries and cracks like splintering ice.")
            show("You feel the last bit of moisture leave your skin.")
            show("Your eyes are raisins.")
            player.death()
        else:
            printc("If you really don't want to go to the tavern you can always type @'die'@yellow@ to die of dehydration.")
            
        
        move = getInput(player)
    # Tavern in intro is different from tavern.py
    show("The tavern in %s is old and rugged. Beaten down by countless "
         "travelers, it's acquired a homey atmosphere." % player.aspect['town'])
    show('You approach the bartender.')
    show('"Ey, what\'ll it be for ya?"')
    printc("On the shelf is a bottle of @'Rum'@yellow@ and a can of Mountain @'Dew'@yellow@.\nWhich do you choose?")
    drink = input("> ").lower()
    while not checkInput(drink, 'rum') and not checkInput(drink, 'dew'):
        if drink == 'neither':
            print("You've got to drink something. What'll it be? ")
        else:
            printc("Come on, @'Rum'@yellow@ or @'Dew'@yellow@. ")
        drink = input("> ").lower()
    if checkInput(drink, 'rum'):
        show("You start to reach for the rum, and then realize that "
             "you're way too MLG for that weak shit.")
        show('"Gimme dat dew," you say, gently placing your fedora on '
             'your head.')
        show('"Wow, you really are as dank as you look." the bartender '
             'says, looking impressed.')
    elif  checkInput(drink, 'dew'):
        show('"Gimme dat dew," you say. "I knew you were a dank one," '
             'the bartender says knowingly.')
        show('You tip your fedora gently to show how euphoric you are '
             'about this dew. "XDDDDDDDD," says the bartender.')
    show('You throw down a one dollar bill. "I think this will cover '
         'it."')
    show('"Holy fucking shit!" exclaims the bartender. "Did you see '
         'that??????"')
    show('"Hold on m8," you say. "I need to take a closer look." You '
         'begin to examine the bill.')
    show('"There is something fishy about this bill... could it be?"')
    show("You connect the three sides of the strange shape on the back "
         "of the bill and realize what you had been missing all along.")
    show("The three sides would connect to form none other than the "
         "illumrunarti triange. Then everything goes black.")
    show('You wake up to find yourself in a green haze in an unreal '
         'dimension. Ahead of you a light begins to appear. "Who\'s '
         'there??" you ask.')
    show('"You know who I am," the voice says. A wave of euphoria '
         'rushes over you as Snoop Dogg steps into view.')
    show("\"And you know why you're here, for only you, %s, have the "
         "swagger dank enough to defeat the greatest enemy of all... "
         "the illum-\"" % player.aspect['name'])
    show('You wake up on the floor of the tavern covered in doritos '
         'and see the bartender standing over you. "I know what I must '
         'do," you say.')
    show("Looking into your eyes with a piercing stare, the bartender "
         "speaks the word that will change your life forever.")
    input(" ")
    print("...")
    input(" ")
    print(". . .")
    input(" ")
    print(".    .    .")
    input(" ")
    printSlowly('"k."')
    show("You sprint to your house to grab your shit.")
    print('You enter your house and exclaim to your mom about how you are going on an adventure.')
    player.getInput()
    show('She looks up from the dick sock she\'s knitting.')
    printSlowly("Alright sweetie, be safe! Here, take this.")
    player.addToInventory(Item(player, 'Camera', customDescription='Mom got this for you.', _type='misc'))
    printc("Type @'inventory'@yellow@ any time you are prompted for input to open your inventory. Use the @'arrow keys'@yellow@ as well as @'enter'@yellow@ and @'escape'@yellow@ when in menus.")
    while True:
        x = input('> ').lower()
        if x == 'inventory' or x == 'inv':
            player.openInventory() # doing this manually so that usually opening inventory doesnt count as an input
            break
        else:
            printc("Come on now, you can just type @'inv'@yellow@ if you can't handle big words like @'inventory'@yellow@.") 

    show('After taking the camera, you leave your house and walk into town, ready to head into whatever building you choose.')
