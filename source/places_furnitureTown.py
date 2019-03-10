
from source.utils import *
from source.item import *
salesGuySpeed = .01n

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
            printSlowly("Well that's great listen I have just have got to tell you about these great deals we're having today I mean they are seriously outragious and I'm sure you're not going to find any deals on furniture (especially furniture this high quality) anywhere else in this entire tile.", secondsBetweenChars=salesGuySpeed)
            printSlowly("So, would you like to buy some furniture?", secondsBetweenChars=salesGuySpeed)
            if yesno(player):
                buyFurniture(player, 1999.99)
            else: # didnt want to buy furniture
                printSlowly("Ah man well that's just too bad because let me tell you, we have some seriously high quality furniture here I'm takin BIG couches BIG loveseats I'm takin HUGE dining room chairs.", secondsBetweenChars=salesGuySpeed)   
                printSlowly("What is it the price? We can make something work. I can go lower. It's not my furniture! The lowest I can go is FIVE hundo. I don't make commission anyways.", secondsBetweenChars=salesGuySpeed)
                printSlowly("So what do you say?", secondsBetweenChars=salesGuySpeed)
                if yesno(player):
                    return buyFurniture(player, 499.99)
                else:
                    printSlowly("Alright well if you're seriously not going to buy any furniture I better help some legitimate customers.", secondsBetweenChars=salesGuySpeed)
                    show("Furniture Tom gives you his business card and walks away.")
                    player.addToInventory(Item(player, 'Furniture Tom\'s business card', customDescription='Hi my name is Furniture Tom and welcome to Furniture Town. If you want to buy some furniture just call 1-800-FRN-TOWN', _type='misc', sellValue=0))
                    






#  printSlowly("", secondsBetweenChars=salesGuySpeed)




        else:
            pass


def furnitureTown2(player): # offer places to go here (couchtown...)
    pass

def buyFurniture(player, price):
    printSlowly("GREAT we'll get this taken care of right away.", secondsBetweenChars=salesGuySpeed)
    show("@$"+price+" has been deducted from your bank account.@red@")
    player.money -= price
    printSlowly("Our guys will have this delivered faster than you can get home! Ahhahhhahhhhahh.", secondsBetweenChars=salesGuySpeed)
    printSlowly("Hey well thanks for stopping by but we've really got to close soon tah-tah!", secondsBetweenChars=salesGuySpeed)
    show("A burly man in a Furniture Town polo escorts you out of the store.")
    show("They are still clearly open.")
    print("Go back inside?")
    if yesno(player):
        return furnitureTown2(player)