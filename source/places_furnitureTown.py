
from source.utils import *
from source.item import *
from source.lists import getRandomCouch, getRandomFeeling
import random
salesGuySpeed = .01

def furnitureTown(player):
    
    show("You see furniture through the large windows of the building.")
    print("Go inside?")
    if not yesno(player):
        show("Not today.")
        
    else:
        player.registerVisit("Furniture Town")
        s = Sound(player, 'mall.wav')
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
                    buyFurniture(player, 499.99)
                else:
                    printSlowly("Alright well if you're seriously not going to buy any furniture I better help some legitimate customers.", secondsBetweenChars=salesGuySpeed)
                    show("Furniture Tom gives you his business card and walks away.")
                    player.addToInventory(Item(player, 'Furniture Tom\'s business card', customDescription='Hi my name is Furniture Tom and welcome to Furniture Town. If you want to buy some furniture just call 1-800-FRN-TOWN', _type='misc', sellValue=0))
        else: # didnt wantn to approach sales guy
            show("You squeeze through the gaps between a "+getRandomCouch()+" and a "+getRandomCouch()+".")
            insideFurnitureTown(player)
        s.stopSound()


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
                if player.equippedArmourChest.name == 'Furniture Town Employee Polo on day':
                    inflitrationQuest(player)
                else:
                    show("You crack open the door and get a glimpse of an immense warehouse.")
                    show("A burly man in a Furniture Town polo notices you and and crosses his arms.")
                    show("You are obviously not welcome here.")
                    show("You close the door.")

def inflitrationQuest(player):
    show("A burly man in a Furniture Town polo notices you and crosses his arms.")
    show('His name tag says, "Hank".')
    printSlowly("I don't remember seeing you around here.")
    printSlowly("What's your name again?")
    nameTagName = player.getInput()
    printSlowly(nameTagName.title() + "?")
    printSlowly("Well put on a name tag so people don't have to ask.")
    item = Item(player, 'Name Tag', customDescription="It says \"My name is "+nameTagName+".\" The safety pin part looks kind of sharp.", _type="weapon", damage=1, scale=False)
    player.addToInventory(item)
    player.equippedWeapon == item
    show("@You equipped the name tag.@green@")
    printSlowly("Oh and by the way there's a stack of EP500's on floor 10 and they need processing.")
    printSlowly("Get on that would you?")
    show('Hank goes back to staring at the door with his arms crossed.')
    show("You take a look around the warehouse and find that it too is tremendously large.")
    show("The broken and used furniture is piled to the ceiling.")
    show("You walk around a bit and find an elevator.")
    show("You press the button and wait.")
    printSlowly("5")
    printSlowly("4")
    printSlowly("3")
    printSlowly("2")
    printSlowly("1")
    Sound(player,'elevator_ding.wav', loop=0)
    show("The elevator arrives and 4 huge burly men in Furniture Town Polos walk out.")
    show("You step inside the elevator and examine the array of buttons.")
    show("The buttons stretch from the floor to the ceiling and range from @1@yellow@ to @112@yellow@.")
    show("There is also a button labled @'Directory'@yellow@.")
    currentFloor = 1
    total = 0
    while True:
        print("Which button do you press?")
        floor = player.getInput()
        if checkInput(floor, 'Directory'):
            directory(currentFloor)
            continue
        else:
            try:
                floor = int(floor)
                assert floor >0
                assert floor < 113
            except Exception:
                print("That is not one of the buttons.")
                continue
            currentFloor = floor
            printSlowly(". . .", quotes=False)
            Sound(player,'elevator_ding.wav', loop=0)
            o = "The doors open and"
            if floor == 1:
                show(o+" you are back in the warehouse.")
                if 'Got the money from furniture town' not in player.history:
                    show("You can't go back to Alice empty-handed...")
                    show("You get back in the elevator.")
                else:
                    return part2(player,total, nameTagName)
            elif floor == 2:
                show(o+" you see an office of men that all look exactly like Furniture Tom filing papers and making small talk by the watercooler.")
            elif floor == 3:
                show(o+' you enter a triangular room with a pedestal in the center.')
                show("There is a triangle shaped hole in the pedestal.")
                show("You look around and see something shining in the corner of the room.")
                print("Check it out?")
                if yesno(player):
                    show("You walk over a find a square shaped key.")
                    print("Try it in the hole?")
                    if yesno(player):
                        show("It obviously doesn't fit.")
                    show("You toss it on the ground and get back into the elevator.")
                    continue
                show("You step back into the elevator.")
            elif floor == 4:
                show(o+" you are immediately bombarded by intense radiation.")
                show("You can feel the cancer developing in your small intestine.")
                player.takeDamage(1)
                show("You hit the close door button as fast as you can.")
            elif floor == 5:
                show(o+' a blast of humid sweaty air accompanied by relaxing zen music rushes into the elevator.')
                if 'yoga floor' in player.history:
                    show("Though the scent of yoga is alluring, you decided to go to a different floor.")
                else:
                    player.history.append("yoga floor")                
                    show("You see someone walking towards the elevator.")
                    printSlowly("Hey hold the door for me!")
                    print("Hold the door for them?")
                    if yesno(player):
                        show("You hold the door for the person.")
                        show('Their name tag says, "Jebra".')
                        printSlowly("Thanks!")
                        show("Jebra lays down in the corner of the elevator and quickly falls asleep.")
                    else:
                        printSlowly("What the f...")
            elif floor == 6:
                show(o+" there is blood all over the floor.")
                show("A large alligator-camel hybrid with a disconcerting smirk is galloping towards the elevator door.")
                printc("Mash the door close button by typing, @'Close the door'@yellow@ as fast as you can!")
                while True:
                    x = player.getInput()
                    if x == 'close the door':
                        break
                    else:
                        printc("It's getting closer!")
            elif floor == 7:
                show(o+" you are dazzled by the brilliant amorphous triangles that float about the room." )
                show("You stare at their geometric wonders and begin to lose track of time and space.")
            elif floor == 8:
                show(o+" the room is completely empty.")
                show("There is nothing in it.")
            elif floor == 9:
                show(o+" there you are.")
                show("It's you, standing just a few feet ahead.")
                show("You look at yourself, face to face.")
                show("You feel a confused horror but the face you see has a look of calm contentment.")
                show("You begin to speak but...")
            elif floor == 10:
                show(o+" you walk down a hallway looking for where the money might be.")
                show('You turn the corner and see a door labled, "Capital Storage".')
                show("You start to turn the handle but suddenly you hear a scolding voice from behind you.")
                show("An angry woman in a manager's outfit is pointing her finger at your pants.")
                show("Her name tag says, \"Loreen\".")
                printSlowly("What the heck are you doing?")
                x = player.getInput()
                printSlowly("I don't want to hear it!")
                printSlowly("You can't wear those "+str(player.equippedArmourLegs.name)+" around here!")
                printSlowly("Think of the customers!")
                printSlowly("Go into that storage room and change into some slacks this instant!")
                show("You hang your head low and enter the storage room across the hall.")
                show("You open a box labled, \"SLACKS\" and find some slacks that are your size.")
                slacks = Item(player, 'Slacks', 'You found these in a box labled, "SLACKS".', _type='Armour', armourSlot='legs')
                player.addToInventory(slacks)
                print("Put them on?")
                if yesno(player):
                    show("@You put on the slacks.@green@")
                else:
                    show("@You put on the slacks even though you don't want to.@green@")
                player.equippedArmourLegs = slacks
                show('You exit the storage room and try the handle to the door labled, "Capital Storage".')
                show("It's locked.")
                show("Loreen appears behind you.")
                printSlowly("Oh now I've got you!")
                printSlowly("And I assume you've misplaced your master key as well?")
                printSlowly("Don't you know some crook could be trying to steal our money and all he would need is that key.")
                printSlowly("This is going on your permanent record, "+nameTagName.title()+".")
                printSlowly("I'll open this for you now, but if you don't have that key by tomorrow there will be serious consequences.")
                printSlowly("What do you need in here anyways?")
                print("> ")
                wait(1)
                printSlowly("Actually don't answer that. I don't care.")
                printSlowly("Just get back to work.")
                show("Loreen opens the door for you and you go inside.")
                show("The door closes behind you and you turn on the lights.")
                show('In front of you there is a huge safe with a complicated looking keypad.')
                print("Enter password?")
                while True:
                    if yesno(player):
                        print("The computer terminal is awaiting input:")
                        pw = player.getInput()
                        if pw == '123':
                            player.history.append("Got the money from furniture town")
                            show("Click.")
                            show("The safe opens and a huge amount of money spills out onto the ground.")
                            show("You begin stuffing as much of it as you can into your pants, but your "+str(player.equippedArmourLegs.name)+" have shallow pockets.")
                            player.addMoney(5035)
                            total = 5035
                            while True:
                                print("Grab some more?")
                                if yesno(player):
                                    show("You stuff some more money in your pants.")
                                    show("They are bulging at the seams.")
                                    r = random.randint(98, 432)
                                    player.addMoney(r)
                                    total+=r
                                else:
                                    break
                            show("You exit the room and make a break for the elevator.")
                            break
                        else:
                            show("The safe beeps angrily.")
                            show("Wrong password.")
                    else:
                        show('You look around the room for a hint.')
                        show('On the wall next to the safe is a sticky note with the numbers, "1 2 3" on it.')
                    print("Try again?")
            else:
                show("The computerized voice comes over the speakers.")
                printSlowly("That floor is on lockdown.")
                printSlowly("Thank you.")
                continue
            show("The elevator doors slowly close.")
            
def part2(player, total, name):
    show("You quickly head towards the exit of the Employee's Only area.")
    show("Hank steps in your path and crosses his arms.")
    printSlowly("Huh. I remember you looking skinnier.")
    printSlowly("Have you put on some weight?")
    printSlowly("You must just look fat in those "+player.equippedArmourLegs+".")
    printSlowly("Well anyways, thanks for sorting out all those issues with the EP500's.")
    printSlowly("It's nice to know someone around here has my back.")
    printSlowly("Now get back out there and sell some furniture!")
    show("Hank gives you a shove through the exit.")
    show("It doesn't take you long to find Alice.")
    show("She is sleeping on a "+getRandomCouch()+".")
    print("Wake her up?")
    if not yesno(player):
        show("Your deliberation wakes Alice.")
    printSlowly("Whhhuuaaa?", secondsBetweenChars=.1)
    printSlowly(name +)


def directory(floor):
    show("A computerized voice begins listing the floor names:")
    printSlowly("You are on floor "+str(floor)+".")
    printSlowly("Floor 1: Warehouse")
    printSlowly("Floor 2: Sales")
    printSlowly("Floor 3: Administration")
    printSlowly("Floor 4: Bio-Waste")
    printSlowly("Floor 5: Yoga Club")
    printSlowly("Floor 6: DNA Sequencing Lab")
    printSlowly("Floor 7: Triangles")
    printSlowly("Floor 8: Nothing")
    printSlowly("Floor 9: Chamber of Retroflection")
    printSlowly("Floor 10: EP500 Realignment Facility")
    printSlowly("All other floors are on lockdown.")
    printSlowly("Thank you.")



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
            printSlowly("Huh, I guess I dozed off.", secondsBetweenChars=.1)
            printSlowly("Who are you?", secondsBetweenChars=.1)
            playerName = getInput(player)
            playerName = playerName.title()
            printSlowly(playerName + "?")
            printSlowly("That's a weird name.")
            printSlowly("I'm "+name+".")
            show(name + " hops off of the bed and looks you in the eyes.")
            printSlowly("So, "+playerName+", you want to help me out?")
            printSlowly("This place has been ripping people off for forever.")
            printSlowly("I walked in here and talked to Furniture Tom and then next thing I knew I was completely broke.", secondsBetweenChars=.02)
            printSlowly("I've got so much debt and I've got no where to go...")
            printSlowly("So I just live here.")
            printSlowly("They keep trying to kick me out, but this store is so large they can never find me.")
            printSlowly("It's time we get back at them.")
            printSlowly("I've been scheming about this for a while, but my plan needs two people.")
            printSlowly("Are you in?")
        if yesno(player):
            printSlowly("Great!")
            printSlowly("Come with me.")
            show(name +' grabs your hand and runs to a door marked "Employee\'s Only".')
            printSlowly("I found this. I need you to put it on.")
            item = Item(player, 'Furniture Town Employee Polo')
            player.addToInventory(item)
            while True:
                print("Put it on?")
                if yesno(player):
                    player.equippedArmourChest = item
                    show("@You equipped the Polo.@green@")
                    break
                else:
                    printSlowly("What the heck I need you to put this on!")
            printSlowly("Yes! You look just like one of them!")
            printSlowly("Now I need you to sneak into the back of this place and find out where they keep the money.")
            printSlowly("When you find it, grab as much as you can and then come back here.")
            printSlowly("But don't let anyone see you while you're doing that.")
            printSlowly("Got it!?")
            x = player.getInput()
            printSlowly("Great!")
            show(name + " shoves you through the doorway into the Employee's Only section.")
            return inflitrationQuest(player)

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
    show("Furniture Tom walks off into the distance.")
    return insideFurnitureTown(player)
    
