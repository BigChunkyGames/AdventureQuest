from utils import *
from miniGames import RockPaperScissors
import sys
# sys.path.append('../') # this is unnecessary - see what I did above for an example of importing from sibling directories


def tavern(player):
    if player.getVisits("Main Town Tavern", "add") == 1:
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
    while True:
        print("You have a look around to see what's up:")
        print("In front of you lies a pretty dope looking 'slot' machine")
        print("You could 'ask' the bartender for some rumors")
        print("It looks like one of the patrons is challenging others to a 'game'")
        print("You could get a room to 'rest' for the night")
        print("Or you could just 'leave'.")
        action = input(player)
        if action == "slot" or action == "s":
            # Slots(player).slot_machine() TODO: fix this
            # until that gets fixed, run this line instead:
            show("You try your best at the slot machine, but it conveniently results in no net change of dogecoin for you.")
        elif action == "ask" or action == "a":
            show("You walk up to the bartender and ask for some rumors.")
            show("He lets you know that he hasn't heard anything since the last "
                 "time you asked.")
            # TODO: Rumors (random maybe?)
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
    print('"I\'ve been challenging travelers across these lands to the '
         'game of my people for many years. You think you\'ve got what '
         'it takes to beat me?" (y/n)')
    if yesno(player):
        show('"Hah! Let\'s see how good you really are!')
        show("The pirate cracks his knuckles and offers his hand to you "
             "for a friendly handshake.")
        show("You accept his offer, shaking his hand, when he suddenly "
             "grins at you.")
        show('"Hah, new to the game, are you? I can feel in your hand '
             'what you\'re about to play!"')
        show("You gulp nervously and ready your fist, mentally preparing "
             "yourself for the beginning of the match.")
        yourchoice, opchoice, outcome = RockPaperScissors.RPSGame().game()
        show('"Enough waiting around! Let\'s do this!"')
        while True:
          yourchoice, opchoice, outcome = RockPaperScissors.RPSGame().game()
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
                    "actually won!").format(yourchoice, opchoice)
               raw_input("... ")
               show("The pirate looks up at you, clearly impressed.")
               show('"Not many can beat me at this game. I think you deserve '
                    'to be in my clan, it houses only the best rock paper '
                    'scissors players in the entire world."')
               player.clantags.append("[Pyr8]")
               show("You have joined The Pirates' Clan! [Pyr8]")
               show("After your rousing game, you head back to the front of the tavern.")
               break
          elif outcome == 'tie':
               print("You look down into your own hand. Both of you played {0}! "
                    "It's a tie!").format(yourchoice)
               raw_input("... ")
               show('"What a match! It looks like we\'re fairly even in skill," the pirate says.')
               show('"Let\'s play again to settle who really is the better player!"')
          else:
               print("You look down into your own hand. {0} beats {1}! He beat "
                    "you!").format(opchoice.title(), yourchoice)
               raw_input("... ")
               show('"Heh heh, well that\'s alright. Not everybody has what '
                    'it takes to play with the best of them. Better luck next time!"')
               show("After your rousing game, you head back to the front of the tavern.")
               break
    else:
        show('"Just as I figured, maybe you can come back when you\'re not '
             'such a fuckin whimp lol')
        show("You're so upset by his unkind words that you don't even want "
             "to be here anymore.")

    print("")