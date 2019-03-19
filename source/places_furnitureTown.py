
from source.utils import *
from source.item import *
from source.lists import getRandomCouch, getRandomFeeling
salesGuySpeed = .01

def furnitureTown(player):
    
    show("You see furniture through the large windows of the building.")
    print("Go inside?")
    if not yesno(player):
        show("Not today.")
        return
    else:
        player.registerVisit("Furniture Town")
        show("The automatic sliding doors open and reveal a lavish world of furniture basking in flourecent light.")
        if 'talked to furniture tom' in player.history:
            insideFurnitureTown(player)
        show("Through the aisles of furniture, a sales person, pretending not to notice you, quickly places himself in your path.")
        print("Approach him?")
        if yesno(player):
            player.history.append("talked to furniture tom")
            printSlowly("Whoa hey there welcome to Furniture Town my name is Furniture Tom what brings you in today?!", secondsBetweenChars=salesGuySpeed)
            x = input('> ')
            printSlowly("Well that's great listen I have just have got to tell you about these great deals we're having today I mean they are seriously outragious and I'm sure you're not going to find any deals on furniture (especially furniture of this caliber) anywhere else in all of "+player.aspect['land']+".", secondsBetweenChars=salesGuySpeed)
            printSlowly("So, would you like to buy some furniture?", secondsBetweenChars=salesGuySpeed)
            if yesno(player):
                buyFurniture(player, 1999.99)
            else: # didnt want to buy furniture
                printSlowly("Ah man well that's just too bad because let me tell you, we have some seriously high quality furniture here I'm talkin BIG couches BIG loveseats I'm takin HUGE dining room chairs.", secondsBetweenChars=salesGuySpeed)   
                printSlowly("What is it the price? We can make something work. I can go lower. It's not my furniture! The lowest I can go is FIVE hundo. I don't make commission anyways.", secondsBetweenChars=salesGuySpeed)
                printSlowly("So what do you say?", secondsBetweenChars=salesGuySpeed)
                if yesno(player):
                    return buyFurniture(player, 499.99)
                else:
                    printSlowly("Alright well if you're seriously not going to buy any furniture I better help some legitimate customers.", secondsBetweenChars=salesGuySpeed)
                    show("Furniture Tom gives you his business card and walks away.")
                    player.addToInventory(Item(player, 'Furniture Tom\'s business card', customDescription='Hi my name is Furniture Tom and welcome to Furniture Town. If you want to buy some furniture just call 1-800-FRN-TOWN', _type='misc', sellValue=0))
        else: # didnt wantn to approach sales guy
            show("You squeeze through the gaps between a "+getRandomCouch()+" and a "+getRandomCouch()+".")
            return insideFurnitureTown(player)


def insideFurnitureTown(player): # offer places to go here (couchtown...)
    show("There is furniture on display in every direction.")
    show("You cannot see an end to the sea of furniture.")
    show("The furniture fades off into the horizon.")
    show("This is a really large store.")
    show("Hanging in the lights above you are signs indicating the different sections of Furniture Town. ")
    while True:
        printc("Would you like to go to @'sofa city'@yellow@, @'bed heaven'@yellow@, @'rug road'@yellow@, or @'employee's only'@yellow@?")
        x = player.getInput()
        if 'sofa' in x or 'city' in x or checkInput(x,'sofa city'):
            sofaCity(player)
        elif 'bed' in x or 'heaven' in x or checkInput(x,'bed heaven'):
            bedHeaven(player)
        elif 'rug' in x or 'road' in x or checkInput(x,'rug road'):
            rugRoad(player)
        elif 'employee' in x or 'only' in x or checkInput(x,"employee's only"):
            show("The sign points to a door that is prohibited to customers.")
            print("Open it?")
            if not yesno(player):
                show("Yeah, you probably shouldn't go in there anyway.")
            else:
                if player.equippedArmourChest.name == 'Furniture Town Employee Polo':
                    pass
                else:
                    show("You crack open the door and get a glimpse of an immense warehouse.")
                    show("A burly man in a Furniture Town polo notices you and and crosses his arms.")
                    show("You are obviously not welcome here.")
                    show("You close the door.")

def rugRoad(player):
    show("You walk down the road of rugs.")
    show("There are rugs of all kinds, hung up and on the ground.")
    show("The rug road begins to incline, as you climb atop larger and larger rugs.")
    show("You make it to the top of a huge pile of rugs.")
    print("Try out one of the rugs?")
    if not yesno(player):
        show("You make your way down rug road and back to the entrance.")
        return
    show("You lie down on the nearest rug.")
    show("It feels "+getRandomFeeling()+".")
    player.sleep()
    show("You decide to head back to the entrance.")
    return

def bedHeaven(player):
    name = 'Alice'

    show("You head towards bed heaven.")
    show("The beds begin to get so tightly packed that you have to crawl over them.")
    if 'woke up '+name in player.history:
        show("You notice "+name+" still sleeping in the bed.")
    else:
        show("You stumble upon a girl sleeping in one of the beds.")
    print("Wake her up?")
    if not yesno(player):
        show("Yeah, that would be rude.")
        print("Try out one of the beds?")
        if not yesno(player):
            show("You decide to head back to the entrance.")
            return
        show("You lie down in the closest bed.")
        show("Wow, what a comfortable bed.")
        player.sleep()
        show("That was nice.")
        show("You decide to head back to the entrance.")
        return
    else: #waking her up
        printSlowly("Whhuuaa?", secondsBetweenChars=.2)
        if "woke up "+name in player.history:
            printSlowly('You again?')
            printSlowly("Are you going to help me get back at this place?")
        else:
            player.history.append("woke up "+name)
            show("The girl sits up in the bed and stretches her arms.")
            show("She is more beautiful than you realized.")
            printSlowly("Huh, I guess I dozed off.", secondsBetweenChars=.15)
            printSlowly("Who are you?", secondsBetweenChars=.1)
            playerName = getInput(player)
            playerName = playerName.title()
            printSlowly(playerName + "?")
            printSlowly("That's a weird name.")
            printSlowly("I'm "+name+".")
            show(name + " hops off of the bed and looks you in the eyes.")
            printSlowly("So, "+playerName+", you want to help me out?")
            printSlowly("This place has been ripping people off for forever.")
            printSlowly("I walked in here and talked to Furniture Tom and then next thing I knew I was completely broke.")
            printSlowly("I've got so much debt and I've got no where to go...")
            printSlowly("So I just live here.")
            printSlowly("They keep trying to kick me out, but this store is so large they can never find me.")
            printSlowly("It's time we get back at them.")
            printSlowly("I've been scheming about this for a while, but my plan requires two people.")
            printSlowly("Are you in?")
        if yesno(player):
            printSlowly("Great.")
            printSlowly("")
        else:
            printSlowly("Huh. Whatever.")
            show(name +" is done talking to you and gets back in the bed.")
            show("She immediately falls asleep.")
            show("You decided to head back to the entrance.")
            return



def sofaCity(player):
    show("You follow the path towards an endless display of couches and coffee tables.")
    print('Would you like to take a seat in one of the couches?')
    if yesno(player):
        couch(player)
    show("You decide to head back to the entrance.")

def couch(player):
    show("You plop into a " +getRandomCouch()+".")
    show("It feels "+getRandomFeeling()+".")
    printc("Type @'get up'@yellow@ to get up.")
    x = ''
    while x != 'get up':
        x = player.getInput()
    print("Try out another one?")
    if yesno(player):
        return couch(player)
    

def buyFurniture(player, price):
    printSlowly("GREAT we'll get this taken care of right away.", secondsBetweenChars=salesGuySpeed)
    show("@$"+str(price)+" has been deducted from your bank account.@red@")
    player.money -= price
    printSlowly("Our guys will have this delivered faster than you can get home! Ahhahhhahhhhahh.", secondsBetweenChars=salesGuySpeed)
    printSlowly("Well let me know if you want to buy any more furniture.")
    printSlowly("Feel free to browse around.")
    return insideFurnitureTown(player)
    
