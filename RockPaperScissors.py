from random import randint

def choicename(int):
    if int == 1:
        return "rock"
    elif int == 2:
        return "paper"
    elif int == 3:
        return "scissors"

def guess():
    print("Let's play rock paper scissors!")
    guess = int(raw_input("play 1 for rock, 2 for paper, and 3 for "
                          "scissors. "))
    while guess != 1 and guess != 2 and guess != 3:
        guess = int(raw_input("Either pick 1 (rock,) 2 (paper,) "
                              "or 3 (scissors.) "))
    print("You chose %s!" % choicename(guess))
    return guess

def aiguess():
    opponent = randint(1,3)
    print("I picked %s." % choicename(opponent))
    return opponent

def game():
    choice = guess()
    opchoice = aiguess()
    if opchoice == choice - 1 or opchoice == choice + 2:
        print ("{} beats {}! You win!").format(choicename(choice),
                                               choicename(opchoice))
    elif opchoice == choice + 1 or opchoice == choice - 2:
        print ("{} beats {}! You lost!").format(choicename(opchoice)
                                                 .title(),
                                                 choicename(choice))
    elif opchoice == choice:
        print("We tied!")

game()
