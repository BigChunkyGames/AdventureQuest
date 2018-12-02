from world import *
from utils import *
import sys
sys.path.append('../') # i dont really know whats going on here but it lets you import from sibling directories
from SlotMachine import *


def maintown(player):
    player.addVisit("maintown") # places inside of this here while loop return to the while loop when they are finished
    while True:
        print("You stand in the homey town of %s, a lovely place. Where do you "
              "want to go?") % player.aspect['town']
        print("You could go 'home' and check that out.")
        print("The 'tavern' is always a cool place to hang out.")
        print("The 'store' is probably open.")
        print("The 'blacksmith' might appreciate you buying something.")
        print("Or you could 'head out' into the world.")
        print("Where do you want to go?")
        place = input()
        while place == "":
            place = input()
        if place == "home":
            home(player)
        elif place == "tavern":
            tavern(player)
        elif place == "store":
            store(player)
        elif place == "blacksmith":
            blacksmith(player)
        elif place == "head out":
            if player.getVisits("maintown") == 1:
                show("Off to find your grandpa eh? Mom said to head " + Fore.YELLOW + "EAST.")
            world(player)
            break # this break right here is really important
        else:
            print("You've got to pick one of the places listed.")
            print("")

def home(player):
    show("for some reason your house just has a huge todo sign in front of it")
    #TODO

def blacksmith(player):
    show("You head over to the blacksmith's place to take a look at some "
         "quality goods.")
    show("You walk over to your town's forge and approach the blacksmith, "
         "she's 6'5\" and the strongest one in your town.")
    show('"Hello!" she reaches out to shake your hand and ends up hurting it '
         'slightly.')
    player.takeDamage(1)
    show("You look at the blacksmith's wares, but she doesn't have anything "
         "you need at the moment. You decide to head back into the town.")
    # TODO: blacksmith

def tavern(player):
    if player.getVisits("tavern") == 1:
        show("You walk into the old tavern, wanting to visit the old place "
             "once again.")
        show("As you walk in, several patrons of the bar turn around to look "
             "at you.")
        show('"Ah, it\'s you," the bartender says. "Make sure to watch how '
             'much Mtn Dew you have this time!" Several of the bar\'s guests '
             'chuckle jovially.')
    else:
        show("You walk into the old tavern once again, determined to find some "
          "dank shit to do here or something.")
    print("You have a look around to see what's up:")
    print("In front of you lies a pretty dope looking 'slot' machine")
    print("You could 'ask' the bartender for some rumors")
    print("It looks like one of the patrons is challenging others to a 'game'")
    print("Or you could just leave.")
    action = raw_input("> ").lower().strip()
    if action == "slot":
        Slots(player).slot_machine()
        show("After your exciting go on the slot machine, you decide you've "
             "had enough of the tavern for now.")
    elif action == "ask":
        show("You walk up to the bartender and ask for some rumors.")
        show("He lets you know that he hasn't heard anything since the last "
             "time you asked.")
        # TODO: Rumors (random maybe?)
    elif action == "game":
        show("You saunter up to the gentleman who seems to be looking for "
             "someone willing to play a game with him.")
        show("The old pirate sitting at the table looks up at you and takes a "
             "sip out of his flask.")
        print('"I\'ve been challenging travelers across these lands to the '
             'game of my people for many years. You think you\'ve got what '
             'it takes to beat me?" (y/n)')
        if yesno():
            show('"Hah! Let\'s see how good you really are!')
            show("The pirate cracks his knuckles and offers his hand to you "
                 "for a friendly handshake.")
            show("You accept his offer, shaking his hand, when he suddenly "
                 "grins at you.")
            show('"Hah, new to the game, are you? I can feel in your hand '
                 'what you\'re about to play!"')
            show("You gulp nervously and ready your fist, mentally preparing "
                 "yourself for the beginning of the match.")
            yourchoice, opchoice, outcome = RPSGame().game()
            show('"Enough waiting around! Let\'s do this!"')
            show("The world seems to fade away around you as the only thing "
                 "you focus on is your own hand and that of your opponent.")
            show("Over the rushing sound in your ears you hear the patrons of "
                 "the bar chanting, your fist hitting your open hand.")
            show('"ROCK"')
            show('"PAPER"')
            show('"SCISSORS"')
            show('"SHOOT!"')
            if opchoice == 'rock':
                show("The pirate slams his closed fist down into his open "
                     "palm. He played rock!")
            else:
                print("The pirate opens his hand a split second before slamming "
                     "his fist into his open palm, revealing his true choice: "
                     "%s!" % opchoice)
                raw_input("... ")
            show("The bar erupts in cheers when they see the outcome of your "
                 "match.")
            if outcome == 'win':
                print("You look down into your own hand. {0} beats {1}! You "
                     "actually beat him!").format(yourchoice, opchoice)
                raw_input("... ")
                show("The pirate looks up at you, clearly impressed.")
                show('"Not many can beat me at this game. I think you deserve '
                     'to be in my clan, it houses only the best rock paper '
                     'scissors players in the entire world."')
                clantags.append("[Pyr8]")
                show("You have joined The Pirates' Clan! [Pyr8]")
            else:
                show("You look down into your own hand. {0} beats {1}! He beat "
                     "you!").format(opchoice.title(), yourchoice)
                show('"Heh heh, well that\'s alright. Not everybody has what '
                     'it takes to play with the best of them."')
            show("After your rousing game, you decide you've had enough fun at the "
             "tavern for now.")
        else:
            show('"Just as I figured, maybe you can come back when you\'re not '
                 'such a fuckin whimp lol')
            show("You're so upset by his unkind words that you don't even want "
                 "to be here anymore.")
    show("You leave the tavern, heading outside to the rest of the town.")
    print("")

def store(player):
    show("You stride into the sedentary sales store supplementing the "
         "not-so-silent town of %s, where succulent sweets "
         "are sold. " % player.aspect['town'])
    show("You approach the shopkeeper, an old and wary gentleman with age on "
         "his face and experience in his eyes.")
    show('"What\'ll it be for ya today?"')
    show("You make a point of considering the shopkeeper's wares, but you're "
         "not in the market for anything he's selling at the moment.")
    show("He looks a little irritated that you didn't buy anything as you "
         "head back to the town center.")
    # TODO: add the shop