from source.lists import *
from source.item import generateRandomArmourOrWeapon

class Slots():

    def __init__(self, player):
        self.player = player
        self.freerun = False
        self.beginningmoney = self.player.money


    def playcheck(self): #return bool
        return not (self.player.money - 10) < 0


    def slot_machine(self):
        if not self.playcheck():
            show("You think about taking a spin on the slot machine, but "
                  "realize you don't have enough money.")
            return
        show("You take a seat at this dank slot machine. ")
        play = input("Give it a go? Press Enter to play (Pay 10 money), "
                         "or anything else to leave. \n").lower().strip()
        if play == "":
            self.slot_machine_play()
            netdoge = (self.player.money - self.beginningmoney)
            if netdoge > 0:
                show("You got lucky today, managing to walk away with "+str(netdoge)+" more money than you came in with.")
            elif netdoge < 0:
                show("Looks like today wasn't your lucky day, your pockets are "+str(netdoge)+" money lighter than they were when you walked in.") 
            elif netdoge == 0:
                show("You leave the machine, not having gained or lost any money. You're still luckier than most who try their hand at gambling!")
        else:
            show("You decide that you're too "+getRandomDankAdjective().lower()+" for this shit and peace right out of there.")


    def slot_machine_play(self):
        while True: 
            clear()
            if not self.playcheck():
                chance = random.randint(1, 3)
                if chance == 1:
                    show("You don't have enough money for another round on "
                          "the slot machine. You gently tip your fedora "
                          "before leaving.")
                elif chance == 2:
                    show("You don't have enough money for another round "
                          "on the slot machine, but you didn't even want "
                          "to play another round anyway. Psh.")
                elif chance == 3:
                    show("You don't have enough money for another round "
                          "on the slot machine. You don your shades and "
                          "peace right out of there.")
                return
            if self.freerun:
                self.freerun = False
            else:
                self.player.money -= 10
                print("(-10 money) ")
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
            print ("The rollers spin and land on \n")
            print (tiles[a] + " " + tiles[b] + " " + tiles[c] + "\n")
            # winnings
            if tiles[a] == tiles[b] == tiles[c] == "(weed)":
                # 1/24 chance
                mult = random.randrange(1, 11)
                win = 40 + mult*2
                self.player.money += win
                printc(getRandomDankAdjective() + ", you won @"+str(win)+" money@green@.")
            elif tiles[a] == tiles[b] == tiles[c] == "(hitmarker)":
                # 1/24 chance
                mult = random.randrange(1, 31)
                win = 20 + mult*3
                self.player.money += win
                printc(getRandomDankAdjective() + ", you won @"+str(win)+" money@green@.")
            elif tiles[a] == tiles[b] == tiles[c] == "(Sample Text)":
                # 1/72 chance
                mult = random.randrange(1, 11)
                win = 1 + (mult**2) * 3
                self.player.money += win
                printc(getRandomDankAdjective() + ", you won @"+str(win)+" money@green@. That's fuckin sick!") 
            elif tiles[a] == tiles[b] == tiles[c] == "(Mountain Dew)":
                # 1/72 chance
                print("A small buzzer goes off. The lights flash and the "
                      "machine chants, \"You are dank.\"")
                print("The machine starts to rumble and a steaming can of "
                      "Mountain Dew falls out.")
                print("In your state of euphoria you quickly chug the "
                      "entire can.")
                printc("@You have gained 420 dank points.@green@")
                print(" ")
                self.player.dankpoints += 420
            elif tiles[a] == tiles[b] == tiles[c] == "(Sniper Rifle)":
                # 1/72 chance
                i = generateRandomArmourOrWeapon(self.player, _type='weapon', rarity='epic')
                print("The machine explodes and in the crater you find "
                      "what you've needed all long. Its a")
                print("" + str(i.name()) + "!")
                self.player.addToInventory(i)
            elif tiles[a] == tiles[b] == tiles[c] == "(Doritos)":
                # 1/72 chance
                print("The machine rumbles and out comes a single Dorito "
                      "chip.")
                print("You gently bite off a single corner of the chip, "
                      "storing the rest in your pocket for later.")
                print("You have gained one Perk Point.")
                print("")
                self.player.perkpoints += 1
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Mountain Dew)":
                print("The single mountain dew in the third slot can only mean one thing...")
                print("This game is even danker than you thought. (Your next spin is free!)")
                self.freerun = True
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Sniper Rifle)":
                print("The intervention in the third slot can only mean one thing...")
                print("You're a fuckin sick quickscoper m8. (+5 money)")
                self.player.money += 5
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Doritos)":
                print("The single dorito in the third slot can only mean one thing...")
                print("You're gonna need some gamer fuel. (+15 money)")
                self.player.money += 5
            elif tiles[a] != "(weed)" and tiles[b] != "(weed)" and tiles[a] != tiles[b] and tiles[b] != tiles[c] and tiles[a] != tiles[c] and tiles[c] == "(Sample Text)":
                print("The Sample Text in the third slot can only mean one thing...")
                print("Sample Text")
                print("Sample Text")
                print("Sample Text (+20 money)")
                self.player.money += 20
            else:
                print("You didn't win anything this time.")
            if self.player.money == 420:
                print("You have 420 money. That's really fuckin "
                      "dank, m8.")
                print("You have earned 1 dank point.")
                self.player.dankpoints += 1
            print("Hit enter to play again, type anything to quit. (You "
                  "have "+str(self.player.money)+" money.)")
            again = input("")
            if again != "":
                if self.freerun == True:
                    print("Your next spin is free, are you sure you want to "
                          "leave and waste this opportunity?")
                else:
                    print("Are you sure you want to leave the slot machine?")
                if yesno(self.player):
                    return
                else:
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



