
# import os,sys,inspect
# currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0,parentdir) 

from source.utils import *
from source.lists import *
from source.miniGames.RockPaperScissors import RPSGame
from source.world import *
from source.item import Item, generateRandomArmourOrWeapon
from source.shopUI import ShopUI
from source.shops import *
from source.SlotMachine import *


def maintown(player):
    townName = player.aspect['town']
    player.registerVisit(townName) # places inside of this here while loop return to the while loop when they are finished
    player.addToTeleportableAreas(townName, maintown)
    while True:
        print("You stand in the homey town of "+townName+", a lovely place.")
        printc("You could go @'home'@yellow@ and check that out.")
        printc("The @'tavern'@yellow@ is always a cool place to hang out.")
        printc("The @'store'@yellow@ is probably open at this time of day.")
        printc("The @'blacksmith'@yellow@ might be fun.")
        printc("Or you could always @'leave'@yellow@ your humble town to explore the world.")
        print("Where do you want to go?")
        place = getInput(player)
        if place == "home" or place == "h":
            home(player)
        elif place == "tavern" or place == "t":
            tavern(player)
        elif place == "store" or place == "s":
            store(player)
        elif place == "blacksmith" or place == "b":
            blacksmith(player)
        elif place == "leave" or place == "l":
            if player.getVisits(townName) == 1:
                show("Just before you set foot outside of "+townName+", mom catches up with you.")
                printSlowly('"Sweety I almost forgot!"', secondsBetweenChars=.05, initialWait=False)
                printSlowly('"While you\'re out would you mind taking this lasagna to Grandpa?"', secondsBetweenChars=.03) 
                i = Item(player, "Lasagna", customDescription='A steamy lasagna in a large plastic container. Mom said to take this to Grandpa. She also said that he lives to the East of ' + townName +'.', _type='consumable')
                i.customActivationFunction = lambda: i.consume(karma=-3) # TODO fix conumables lambdas are stupid
                player.addToInventory(i)
                printSlowly('"He lives to the East."', secondsBetweenChars=.03) 
                printSlowly('"You know the way."', secondsBetweenChars=.03) 
                printSlowly('"Come back soon sweety!"', secondsBetweenChars=.03) 
                show("And with that, you are finally free.")
                
            else:
                show("You decide to leave your home town for greener pastures.")
            # TODO wormhole
            world(player)
            return
        else:
            print(getInvalidOptionText() + '\n')

def home(player):
    show("You enter your house through the familiar front door, taking in "
         "the sights of your childhood abode, reminiscing about all the "
         "dank shit you did as a kid.")
    while True:
        printc("You could @'explore'@yellow@ your house some more, @'sleep'@yellow@, @'play'@yellow@ a console game, or just @'leave'@yellow@.")
        action = getInput(player)
        if action == "explore" or action == "e":
            if player.registerVisit("Explore House") == 1:
                show("You head upstairs to your room and look around for a bit. "
                     "You realize that you left your can of Mtn Dew laying on top "
                     "of your dresser.")
                show("You grab the can just in case you need it later.")
                i = Item(player, 'Mtn Dew', customDescription='Consume for a healthy, energetic boost.', _type='consumable')
                i.customActivationFunction=lambda:i.consume(heal=4)
                player.addToInventory(i)
                show("You take a look at the framed picture of your childhood dog on your bedside table.")
                show("Bud must be in a better place now.")
            else:
                show("You look around the house, but shockingly can't find anywhere you haven't already explored")
        elif action == "sleep" or action == "s":
            show("After a long day's work adventuring, you're tired. You decide to climb into your old childhood bed to get some rest.")
            show("Your mother tucks you in and kisses you on the forehead.")
            show('"Good night sweetie, don\'t let the bed bugs bite!"')
            player.sleep()
            show("You turn to leave. \"Bye sweetie, be home for dinner!\" your mother says.")
            show("You shoot her with the double finger guns and head out as she collapses to the floor.")
            break
        elif action == "play" or action == "p":
            password1 = "super secret password 10 million"# TODO password
            password2 = "super secret password 20 million" # TODO password 2
            player.registerVisit("House Console Game")
            if player.getVisits("House Console Game") == 1:
                show("You decide to kill some time by playing some Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version")
                show("After popping the disc into your GameSphere 420, you realize that it needs to install and update.")
                show("You watch the loading bar move at an astoundingly slow pace. This could take a while.")
                show("Standing up, you decide to do something fun in the mean time.")
            elif player.day > 6 and "entered first game password" not in player.choices:
                show("Finally! The game is finished installing!")
                show("You start the game and prepare to jump right into the beautiful world of Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version.")
                show("The game says that you need to log in.")
                print("Enter you password:")
                x = player.getInput()
                if x == password1 and "entered first game password" not in player.choices: 
                    player.choices.append("entered first game password")
                    show("You're logged in.")
                    show("Wait a minute, this isn't your account.")
                    show("You log out, switch GameSphere 420 accounts, and restart the game.")
                    show("The game isn't installed on this account. ")
                    show("You decide to come back when it's finished installing. ")
                else:
                    show("Huh... You can't seem to remember it.")
                    show("Oh well. I'm sure you'll remember eventually.")
            elif player.day > 23 and "entered first game password" in player.choices: 
                show("Finally! After waiting " +player.day+ " whole days, you are ready to play some good ol' fashioned Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version.")
                show("Bursting with excitement, you boot up the game. ")
                show("The game says that you need to log in.")
                print("Enter you password:")
                x = player.getInput()
                if x == password2: 
                    player.choices.append("entered first game password")
                    show("You're logged in.")
                    # TODO
                elif x == password1:
                    show("No, that's the password for the other account.")
                    show("You need the password for your account.")
                else:
                    show("Huh... You can't seem to remember it.")
                    show("Oh well. I'm sure you'll remember eventually.")
                show("You start the game and prepare to jump right into the beautiful world of Call of Duty: Black Ops 4: Pro Edition: Platinum Hits Version.")
                show("The game says that you need to log in.")
                print("Enter you password:")
            else:
                show("You walk over to your GameSphere 420 to see if your game is done installing.")
                show("Oh, look at that!")
                show("It isn't.")
                show("You decide to wait some more.")
        elif action == "leave" or action == "l":
            show("You look around your house for a bit, before deciding to leave.")
            print("Your mother looks up from the " + getRandomDankClothing()  + " she's knitting.")
            input("... ")
            printSlowly('"Bye sweetie, good luck on your adventures! Don\'t forget: ' + getMotherlyPlattitude() )
            break
        else:
            print("Please input a valid action.")
    # TODO: add more stuff to do in your house


def blacksmith(player):
    if player.registerVisit("Main Town Blacksmith") == 1:
        show("You decide to take a look at the quality goods at your local blacksmith.")
        show("You walk over to your town's forge and approach the blacksmith, "
             "she's 6'5\" and the strongest one in your town.")
        printSlowly('"Hello!"', secondsBetweenChars=.1)
        show('She reaches out to shake your hand and ends up hurting it '
             'slightly.')
        player.takeDamage(1)
        show("You leave.") # TODO @ Erik
    else:
        show("You head over to the blacksmith's place to take a look at some "
             "quality goods.")
        # TODO crafting

def tavern(player):
    if player.registerVisit("Main Town Tavern") == 1:
        show("You walk into the old tavern, wanting to visit the old place "
             "once again.")
        show("As you walk in, several patrons of the bar turn around to look "
             "at you.")
        printSlowly('"Ah, it\'s you."',newline=False)
        show(" the bartender says. ")
        printSlowly('Make sure to watch how much Mtn Dew you have this time!') 
        show('Several of the bar\'s guests chuckle jovially.')
    else:
        show("You walk into the old tavern once again, determined to find some "
          "dank shit to do here or something.")
    while True:
        print("You have a look around to see what's up:")
        printc("In front of you lies a pretty dope looking @'slot'@yellow@ machine")
        printc("You could @'ask'@yellow@ the bartender for some rumors")
        printc("It looks like one of the patrons is challenging others to a @'game'@yellow@")
        printc("You could get a room to @'rest'@yellow@ for the night")
        printc("Or you could just @'leave'@yellow@.")
        action = getInput(player)
        if action == "slot" or action == "s":
            s = Slots(player)
            s.slot_machine()
            # until that gets fixed, run this line instead:
            show("You try your best at the slot machine, but it conveniently results in no net change of money for you.")
        elif action == "ask" or action == "a":
            show("You walk up to the bartender and ask for some rumors.")
            show("He lets you know that he hasn't heard anything since the last "
                 "time you asked.")
            # TODO quest Rumors (random maybe?)
        elif action == "game" or action == "g":
                tavernGame(player)
        elif action == "rest" or action =="r":
            pass # TODO
        elif action == "leave" or action == "l":
            show("You've had enough fun at the tavern for today, and decide to blow this popsicle stand.")
            break
        else:
            print("You need to choose something to do!")
            print("")
    show("You leave the tavern, heading outside to the rest of the town.")


def tavernGame(player):
    # TODO: if you're in the pirates clan this guy respects you more
    show("You saunter up to the gentleman who seems to be looking for "
             "someone willing to play a game with him.")
    show("The old pirate sitting at the table looks up at you and takes a "
         "sip out of his flask.")
    printSlowly('"I\'ve been challenging travelers across these lands to the '
         'game of my people for many years. You think you\'ve got what '
         'it takes to beat me?" ')
    if yesno(player):
        printSlowly('"Hah! Let\'s see how good you really are!')
        show("The pirate cracks his knuckles and offers his hand to you "
             "for a friendly handshake.")
        show("You accept his offer, shaking his hand, when he suddenly "
             "grins at you.")
        printSlowly('"Heh, new to the game, are you? I can feel in your hand '
             'what you\'re about to play!"')
        show("You gulp nervously and ready your fist, mentally preparing "
             "yourself for the beginning of the match.")
        show('"Enough waiting around! Let\'s do this!"')
        while True:
          yourchoice, opchoice, outcome = RPSGame().game()
          show("The world seems to fade away around you as the only thing "
               "you focus on is your own hand and that of your opponent.")
          show("Over the rushing sound in your ears you hear the patrons of "
               "the bar chanting, your fist hitting your open hand.")
          printSlowly('"ROCK"', pause=.1)
          printSlowly('"PAPER"', pause=.1)
          printSlowly('"SCISSORS"', pause=.1)
          printSlowly('"SHOOT!"', pause=.1)
          if opchoice == 'rock':
               show("The pirate slams his closed fist down into his open "
                    "palm. He played rock!")
          else:
               print("The pirate opens his hand a split second before slamming "
                    "his fist into his open palm, revealing his true choice: "
                    "%s!" % opchoice)
               input("... ")
          show("The bar erupts in cheers when they see the outcome of your "
               "match.")
          if outcome == 'win':
               print("You look down into your own hand. "+yourchoice+" beats "+opchoice+"! You "
                    "actually won!")
               input("... ")
               show("The pirate looks up at you, clearly impressed.")
               if player.registerVisit('maintown_tavern_rps_win') == 1:
                    printSlowly('"Not many can beat me at this game. I think you deserve '
                         'to be in my clan, it houses only the best rock paper '
                         'scissors players in the entire world."')
                    player.clantags.append("[Pyr8]")
                    show("You have joined The Pirates' Clan! @[Pyr8]@magenta@")
               else:
                    printSlowly('"Again you have defeated me. You are truly are an RPS master and I am honored to have you in my clan!"')
               show("After your rousing game, you return to the front of the tavern.")
               break
          elif outcome == 'tie':
               print("You look down into your own hand. Both of you played "+yourchoice+"! "
                    "It's a tie!")
               input("... ")
               printSlowly('"What a match! It looks like we\'re fairly even in skill,"', newline=False)
               show(' the pirate says.')
               printSlowly('"Let\'s play again to settle who really is the better player!"')
          else:
               print("You look down into your own hand. "+opchoice.title()+" beats "+yourchoice+"! He beat "
                    "you!")
               input("... ")
               printSlowly('"Heh heh, well that\'s alright. Not everybody has what '
                    'it takes to play with the best of them. Better luck next time!"')
               show("After your rousing game, you head back to the front of the tavern.")
               break
    else:
        printSlowly('"Just as I figured, maybe you can come back when you\'re not '
             'such a fuckin whimp lol')
        show("You're so upset by his unkind words that you don't even want "
             "to be here anymore.")
    print("")

def store(player):
    show("You stride into the sedentary sales store supplementing the "
         "not-so-silent town of "+player.aspect['town']+", where succulent sweets and sundries "
         "are sold. ")
    show("You approach the shopkeeper, an old and wary gentleman with age on "
         "his face and experience in his eyes.")
    printSlowly('"What\'ll it be for ya today?"', pause=1.2)
    maintownShop(player)
    # show("You make a point of considering the shopkeeper's wares, but you're "
    #      "not in the market for anything he's selling at the moment.")
    # show("He looks a little irritated that you didn't buy anything as you "
    #      "head back to the town center, having accomplished nothing at all.")
    show("Satisfied with your transaction, you exit the shop.")

def maintownShop(player):
    if openIfExists(player, player.aspect['town'] + " Sales Supplies Limited"): return

    s = Shop(player, player.aspect['town'] + " Sales Supplies Limited")
    s.shopAsciiArt ="""
               ......               
            .:||||||||:.   how are ya      
           /            \           
          (   o      o   )          
--@@@@----------:  :----------@@@@--
"""

    inv = []

    i1 = Item(player, 'Lesser Health Potion', customDescription="A small glass vial filled with sparkly red liquid.", _type='consumable', sellValue=3)
    i1.customActivationFunction = lambda:i1.consume(heal=4)
    inv.append(i1) # CONSUMABLES MUST HAVE UNIQUE VAR NAME

    i2 = Item(player, 'Big Cheeseburger', customDescription="Oh man this big juicy cheeseburger just look's so delicious that you know it has to be worth the price.", _type='consumable', sellValue=8)
    i2.customActivationFunction = lambda:i2.consume(xpgain=int(player.levelupxp / 3))
    inv.append(i2)

    inv.append(Item(player, 'Salad Fork', damage=1, customDescription="It's plastic. Good for poking.", _type='weapon', sellValue=3))
    inv.append(Item(player, 'Fancy Butter Knife', damage=2, customDescription="It's made of clear accurately molded plastic.", _type='weapon', sellValue=5))

    inv.append(generateRandomArmourOrWeapon(player, _type='armour', rarity='common'))
    inv.append(generateRandomArmourOrWeapon(player, _type='armour', rarity='common'))
    inv.append(generateRandomArmourOrWeapon(player, _type='armour', rarity='common'))
    
    i = generateRandomArmourOrWeapon(player, _type='weapon', rarity='rare')
    inv.append(i)

    i = Item(player, 'Bent Piece of Metal', block=1, customDescription="I guess you could just hold this in your " + getOtherHand(player) + " hand.", _type='armour', sellValue=3, armourSlot='offhand')
    inv.append(i)

    s.originalInventory = inv
    s.restock()
    s.openUI()


