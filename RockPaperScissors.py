class RPSGame():

    def choicename(self, int):
        if int == 1:
            return "rock"
        elif int == 2:
            return "paper"
        elif int == 3:
            return "scissors"

    def guess(self):
        guess = int(raw_input("play 1 for rock, 2 for paper, and 3 for "
                              "scissors. "))
        while guess != 1 and guess != 2 and guess != 3:
            guess = int(raw_input("Either pick 1 (rock,) 2 (paper,) "
                                  "or 3 (scissors.) "))
        print("You chose %s!" % self.choicename(guess))
        return guess

    def aiguess(self):
        opponent = random.randint(1,3)
        print("I picked %s." % self.choicename(opponent))
        return opponent

    def game(self):
        choice = self.guess()
        opchoice = self.aiguess()
        if opchoice == choice - 1 or opchoice == choice + 2:
            print ("{} beats {}! You win!").format(self.choicename(choice),
                                                   self.choicename(opchoice))
        elif opchoice == choice + 1 or opchoice == choice - 2:
            print ("{} beats {}! You lost!").format(self.choicename(opchoice)
                                                     .title(),
                                                     self.choicename(choice))
        elif opchoice == choice:
            print("We tied!")
