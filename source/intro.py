from source.utils import *
from source.item import *
from source.lists import getDifficulty, getRandomDankClothing, CURSES

def introduction(player): 
    clear()
    printSlowly("In the time before " +player.aspect['land']+" fell into the splitting fires of hell, we looked to the legends.", quotes=False)
    printSlowly("The elders spoke of a hero that could save us from our inevitable fate...", quotes=False)
    printSlowly("A hero with the courage, strength, experience, attack damage, and block high enough to defeat any foe...", quotes=False)
    printSlowly("A hero that would vanquish the evil that threatened to end everything.", quotes=False)
    printSlowly("But first, "+player.aspect['name']+" was thirsty.", quotes=False) 
    printc("Type @'tavern'@yellow@ to enter the tavern.")
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
            printc("Try typing @'tavern'@yellow@ and the pressing the enter button to enter the tavern. ")
        elif attempts == 2:
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
    clear()
    # Tavern in intro is different from tavern.py
    show("The tavern in %s is old and rugged. Beaten down by countless "
         "travelers, it's acquired a homey atmosphere." % player.aspect['town'])
    show('You approach the bartender.')
    printSlowly('"Ey '+player.aspect['name']+', what\'ll it be for ya?"')
    printc("On the shelf is a bottle of @'Rum'@yellow@ and a can of Mountain @'Dew'@yellow@.\nWhich do you choose?")
    while True:
        drink = player.getInput()
        if checkInput(drink, 'rum'):
            if player.aspect['age'] <21:
                printSlowly("You're not old enough to drink that!")
                continue
            show("The bartender shoots you a smug look and slides a brimful glass of rum your way.")
            player.history.append("got rum")
            break
        elif checkInput(drink, 'dew'):
            show("The bartender shoots you a smug look and slides a brimful glass of Mountain Dew your way.")
            player.history.append("got dew")
            break
        elif drink == 'neither':
            print("You've got to drink something. What'll it be? ")
        elif drink == 'both':
            if player.aspect['age'] <21:
                printSlowly("You're not old enough mix drinks like that!")
                continue
            player.history.append("got rum and dew")
            printSlowly("Ah, just like mother used to make.")
            show("The bartender make a Mountain Dew Rum suicide and slides the brimful glass your way.")
            break
        else:
            printc("Come on, @'Rum'@yellow@ or @'Dew'@yellow@. ")
    show("You catch it and down the whole thing.")
    show("The bar cheers.")
    show('You throw down a one dollar bill.')
    printSlowly("Hey don't worry about that.")
    printSlowly("For you, it's on the house.")
    show("Again the bar cheers.")
    show("You move to get up but stop yourself.")
    show("Something doesn't feel right...")
    printSlowly("What's that look on your face for?")
    printSlowly(player.aspect['name'] + "?")
    printSlowly("You don't ")
    printSlowly("seem ", secondsBetweenChars=.05)
    printSlowly("so ", secondsBetweenChars=.08)
    printSlowly("good... ", secondsBetweenChars=.1, skipable=False)
    clear()
    # TODO transition
    # TODO sound change to ehteral music
    show("The bar is gone.")
    show("You are gone.")
    show("You see nothing.")
    show("Then from behind you, just barely, you hear what sounds like people talking.")
    # TODO lore
    printSlowly("We'll just have to go back.", secondsBetweenChars=.08)
    printSlowly("No... We can hide it. Underground. Nobody will have to know.")
    printSlowly("The illuminati won't want to hear that.", secondsBetweenChars=.08)
    printSlowly("We've got to tell them something.")
    printSlowly("There! Someone!")
    printSlowly("What the? How the hell did you get in here?", secondsBetweenChars=.08)
    # TODO transition
    clear()
    show("You wake up and peel you face off of the sticky tavern floor.")
    printSlowly("Boy, you should take a little more time between sips!")
    show("The barmen chuckle.")
    show("You stand up and brush yourself off, trying to make sense of what just happened.")
    show("You decide to go back home.")
    # show('"Holy fucking shit!" exclaims the bartender. "Did you see '
    #      'that??????"')
    # show('"Hold on m8," you say. "I need to take a closer look." You '
    #      'begin to examine the bill.')
    # show('"There is something fishy about this bill... could it be?"')
    # show("You connect the three sides of the strange shape on the back "
    #      "of the bill and realize what you had been missing all along.")
    # show("The three sides would connect to form none other than the "
    #      "illumrunarti triange. Then everything goes black.")
    # show('You wake up to find yourself in a green haze in an unreal '
    #      'dimension. Ahead of you a light begins to appear. "Who\'s '
    #      'there??" you ask.')
    # show('"You know who I am," the voice says. A wave of euphoria '
    #      'rushes over you as Snoop Dogg steps into view.')
    # show("\"And you know why you're here, for only you, %s, have the "
    #      "swagger dank enough to defeat the greatest enemy of all... "
    #      "the illum-\"" % player.getName())
    # show('You wake up on the floor of the tavern covered in doritos '
    #      'and see the bartender standing over you. "I know what I must '
    #      'do," you say.')
    # show("Looking into your eyes with a piercing stare, the bartender "
    #      "speaks the word that will change your life forever.")
    # input(" ")
    # print("...")
    # input(" ")
    # print(". . .")
    # input(" ")
    # print(".    .    .")
    # input(" ")
    # printSlowly('"k."')
    # show("You sprint to your house to grab your shit.")
    print('You enter your house and exclaim to your mom about what just happend.')
    player.getInput()
    show('She looks up from the '+getRandomDankClothing()+' sock she\'s knitting.')
    # printSlowly("Alright sweetie, be safe! Here, take this.")
    # player.addToInventory(Item(player, 'Camera', customDescription='Mom got this for you.', _type='misc'))
    printSlowly("Oh sweety I'm glad you're alright!")
    printSlowly("Your grandpa used to pass out in bars all the time.")
    printSlowly("Maybe you should go and give him a visit.")
    printSlowly("Oh!")
    show("Your mom dashes to the kitchen and removes something from the oven.")
    printSlowly("I just baked a perfect "+player.aspect['pieFlavor']+" pie.")
    printSlowly("That should help you feel better.")
    show("You walk to the kitchen and grab a piece.")
    player.addToInventory(Item(player, 'Perfect Piece of '+player.aspect['pieFlavor']+' Pie', customDescription='Your favorite!', sellValue=0, _type='consumable', consumable=Consumable(player, consumableType='heal', consumeText='Oh man that hit the spot.', heal=10)))

    printc("Type @'inventory'@yellow@ any time you are prompted for input to open your inventory. Use the @'arrow keys'@yellow@ as well as @'enter'@yellow@ and @'escape'@yellow@ when in menus.")
    while True:
        x = input('> ').lower()
        if x == 'inventory' or x == 'inv':
            player.openInventory() # doing this manually so that usually opening inventory doesnt count as an input
            break
        else:
            printc("Come on now, you can just type @'inv'@yellow@ if you can't handle big words like @'inventory'@yellow@.") 

    show('You thank your mom and leave your house, ready to head into whatever building you choose.')

def charCreation(player):
    player.aspect['name'] = name(player)
    player.aspect['age'] = age(player)
    player.aspect['pieFlavor'] = pie(player)
    player.aspect['difficulty'] = difficulty(player)
    player.aspect['hand'] = hand(player)
    player.aspect['town'], player.aspect['land'] = propernouns(player)
    
def name(player):
    print("What is your name?")
    while True:
        x= player.getInput() 
        if len(x) > 40:
            print("Could you shorten that? It's a bit wordy.")
        else:
            return x.title()

def age(player):
    print("What is your age?")
    while True:
        age = player.getInput()
        try:
            age1 = int(age)
            return age1
        except ValueError:
            print("Your age must be a number.")

def pie(player):
    print("What is your favorite flavor of pie?")
    return player.getInput()

def difficulty(player):
    i = 0
    while True:
        dif = getDifficulty(i)
        if dif == 'Lose':
            player.death()
        print("Would you like the difficulty, " + dif + "?")
        if yesno(player):
            return dif 
        i += 1

def hand(player):
    printc("Which is your dominant hand, @'right'@yellow@ or @'left'@yellow@?")
    x = player.getInput()
    if checkInput(x, "right"): return "right"
    elif checkInput(x, "left"): return "left"
    else: return hand(player)

def propernouns(player):
    print('What is the name of your home town?')
    town = player.getInput()
    print("What is the name of the land?")
    land = player.getInput()
    return town, land

