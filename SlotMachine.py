# Slot machine to be added in the arcade, or something.
import random
dogecoin = 500
dankpoints = 0
perkpoints = 0

def dankadjective():
    adjs = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
    return adjs[random.randint(0, len(adjs)-1)]


# dont include that ^

class Slots():

    def playcheck(self):
        global dogecoin
        return not (dogecoin - 10) < 0


    def slot_machine(self):
        global dogecoin
        if not self.playcheck():
            print("You think about taking a spin on the slot machine, but "
                  "realize you don't have enough money.")
            return
        print("You take a seat at this dank slot machine. ")
        play = raw_input("Give it a go? Press P to play (Pay 10 Dogecoin), "
                         "or anything else to leave. \n").lower().strip()
        if play == "p":
            beginningdogecoin = dogecoin
            self.slot_machine_play()
            netdoge = (dogecoin - beginningdogecoin)
            if netdoge > 0:
                print("You got lucky today, managing to walk away with %s more dogecoin than you came in with.") % netdoge
            elif netdoge < 0:
                print("Looks like today wasn't your lucky day, your pockets are %s dogecoin lighter than they were when you walked in.") % abs(netdoge)
            elif netdoge == 0:
                print("You leave the machine, not having gained or lost any dogecoin. You're still luckier than most who try their hand at gambling!")
        else:
            print("You decide that you're too %s for this shit and peace "
                  "right out of there.") % dankadjective().lower()


    def slot_machine_play(self):
        global dogecoin, perkpoints, dankpoints
        while True:
            if not self.playcheck():
                chance = random.randint(1, 3)
                if chance == 1:
                    print("You don't have enough money for another round on "
                          "the slot machine. You gently tip your fedora "
                          "before leaving.")
                elif chance == 2:
                    print("You don't have enough money for another round "
                          "on the slot machine, but you didn't even want "
                          "to play another round anyway. Psh.")
                elif chance == 3:
                    print("You don't have enough money for another round "
                          "on the slot machine. You don your shades and "
                          "peace right out of there.")
                return
            try:
                if freerun:
                    freerun = False
                else:
                    dogecoin -= 10
            except NameError:
                freerun = False
                dogecoin -= 10
            # 13.8% win chance
            tiles = ["(weed)", "(weed)", "(weed)", "(weed)",
                     "(hitmarker)", "(hitmarker)", "(hitmarker)",
                     "(Sample Text)", "(Sample Text)", "(Mountain Dew)",
                     "(Sniper Rifle)", "(Doritos)"]
            a = random.randrange(0, 12)  # 0-11, Does not include 12
            b = random.randrange(0, 12)
            c = random.randrange(0, 12)
            autowin = random.randrange(0, 30)
            if autowin == 0:
                a = random.randrange(6, 12)
                c = b = a
            # cheater
            # a=b=c= 0
            print ("(-10 Dogecoin) The rollers spin and land on \n")
            print tiles[a], " ", tiles[b], " ", tiles[c], "\n"
            # winnings
            if tiles[a] == tiles[b] == tiles[c] == "(weed)":
                # 1/24 chance
                mult = random.randrange(1, 11)
                win = 40 + mult*2
                dogecoin += win
                print(dankadjective() + ", you won %s Dogecoin.") % win
            elif tiles[a] == tiles[b] == tiles[c] == "(hitmarker)":
                # 1/24 chance
                mult = random.randrange(1, 31)
                win = 20 + mult*3
                dogecoin += win
                print(dankadjective() + ", you won %s Dogecoin.") % win
            elif tiles[a] == tiles[b] == tiles[c] == "(Sample Text)":
                # 1/72 chance
                mult = random.randrange(1, 11)
                win = 1 + (mult**2) * 3
                dogecoin += win
                print(dankadjective() + ", you won %s Dogecoin. That's fuckin sick!") % win
            elif tiles[a] == tiles[b] == tiles[c] == "(Mountain Dew)":
                # 1/72 chance
                print("A small buzzer goes off. The lights flash and the "
                      "machine chants, \"You are dank.\"")
                print("The machine starts to rumble and a steaming can of "
                      "Mountain Dew falls out.")
                print("In your state of euphoria you quickly chug the "
                      "entire can.")
                print("You have gained 420 dank points.")
                print(" ")
                dankpoints += 420
            elif tiles[a] == tiles[b] == tiles[c] == "(Sniper Rifle)":
                # 1/72 chance
                print("The machine explodes and in the crater you find "
                      "what you've needed all long. Its a"),
                print(self.randomweapon() + "!")
            elif tiles[a] == tiles[b] == tiles[c] == "(Doritos)":
                # 1/72 chance
                print("The machine rumbles and out comes a single Dorito "
                      "chip.")
                print("You gently bite off a single corner of the chip, "
                      "storing the rest in your pocket for later.")
                print("You have gained one Perk Point.")
                print("")
                perkpoints += 1
                # TODO: Add perkpoint(self)
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Mountain Dew)":
                print("The single mountain dew in the third slot can only mean one thing...")
                print("This game is even danker than you thought. (Your next spin is free!)")
                freerun = True
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Sniper Rifle)":
                print("The intervention in the third slot can only mean one thing...")
                print("You're a fuckin sick quickscoper m8. (+5 dogecoin)")
                dogecoin += 5
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Doritos)":
                print("The single dorito in the third slot can only mean one thing...")
                print("You're gonna need some gamer fuel. (+15 dogecoin)")
                dogecoin += 5
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Sample Text)":
                print("The Sample Text in the third slot can only mean one thing...")
                print("Sample Text")
                print("Sample Text")
                print("Sample Text (+20 dogecoin)")
                dogecoin += 20
            else:
                print("You didn't win anything this time.")
            if dogecoin == 420:
                print("You have 420 dogecoin. That's really fuckin "
                      "dank, m8.")
                print("You have earned 1 dank point.")
                dankpoints += 1
            print("Hit enter to play again, type anything to quit. (You "
                  "have %s Dogecoin.)") % dogecoin
            again = raw_input("").lower().strip()
            if again == "":
                pass
            else:
                if freerun == True:
                    print("Your next spin is free, are you sure you want to "
                          "leave and waste this opportunity? (y/n)")
                    while True:
                        usercontinue = raw_input("> ").lower().strip()
                        if usercontinue == "n":
                            playagain = True
                            break
                        elif usercontinue == "y":
                            playagain = False
                            break
                        else:
                            print("Please enter 'y' or 'n'")
                else:
                    print("Are you sure you want to leave the slot machine? (y/n)")
                    while True:
                        usercontinue = raw_input("> ").lower().strip()
                        if usercontinue == "n":
                            playagain = True
                            break
                        elif usercontinue == "y":
                            playagain = False
                            break
                        else:
                            print("Please enter 'y' or 'n'")
                if not playagain:
                    chance = random.randint(1, 4)
                    if chance == 1:
                        print("After a while, you decide that you're too MLG "
                              "for this game made for casuals. ")
                    elif chance == 2:
                        print("After a while, you decide that you're too much "
                              "of a nice guy to play this game. You don your "
                              "fedora before leaving. ")
                    elif chance == 3:
                        print("After a while, you decide you've got way cooler "
                              "things to do than play this game. You put on "
                              "your shades and backflip away.")
                    else:
                        print("After a while, you decide that you never even "
                              "wanted to play this game anyway. You turn 360 "
                              "degrees and walk away.")
                    break


    def randomweapon(self):
        return "random weapon (not implemented)"

Slots().slot_machine()