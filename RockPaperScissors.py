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
        return guess

    def aiguess(self, choice, luck, AlwaysPicksRock):
        if AlwaysPicksRock == "Only Rock":
            opchoice = 1
        else:
            if 100 * random.random() < (33.33333333 - (abs(50 - luck))*.66666666):
                opchoice = choice
            else:
                if random.randint(0, 99) >= luck:
                    if choice == 3:
                        opchoice = 1
                    else:
                        opchoice = choice + 1
                else:
                    if choice == 1:
                        opchoice = 3
                    else:
                        opchoice = choice - 1
        return opchoice

    def game(self, luck = 50, AlwaysPicksRock = "No"):
        choice = self.guess()
        opchoice = self.aiguess(choice, luck, AlwaysPicksRock)
        if opchoice == choice - 1 or opchoice == choice + 2:
            finaloutcome = "win"
        elif opchoice == choice + 1 or opchoice == choice - 2:
            finaloutcome = "loss"
        else:
            finaloutcome = "tie"
        return self.choicename(choice), self.choicename(opchoice), finaloutcome
