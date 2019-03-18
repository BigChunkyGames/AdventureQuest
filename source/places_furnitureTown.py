
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
        show("The automatic sliding doors open and reveal a lavish world of furniture basking in flourecent light.")
        show("Through the aisles of furniture, a sales person, pretending not to notice you, quickly places himself in your path.")
        print("Approach him?")
        if yesno(player):
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
    show("There is furniture being displayed in every direction.")
    show("You look around and notice that there is furniture as far as the eye can see.")
    show("The furniture fades off into the horizon.")
    show("This is a really large store.")
    show("Hanging in the fluorescent lights above you are signs indicating the different sections of Furniture Town. ")
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
    show("You head towards bed heaven.")
    show("You begin to notice many more beds through the sea of furniture.")
    show("You stumble upon a woman sleeping in one of the beds.")
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
    
