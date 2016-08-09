# Slot machine to be added in the arcade, or something.
import random
dogecoin = 500
dankpoints = 0
perkpoints = 0
# dont include that ^


def dankadjective():
    adjs = ["Dank", "Sick", "MLG", "Nice"]
    return adjs[random.randint(0, 3)]


def playcheck():
    global dogecoin
    return not (dogecoin - 10) < 0


def slot_machine():
    global dogecoin
    if not playcheck():
        print("You think about taking a spin on the slot machine, but "
              "realize you don't have enough money.")
        return
    print("You take a seat at this dank slot machine. ")
    play = raw_input("Give it a go? Press P to play (Pay 10 Dogecoin), "
                     "or anything else to leave. \n").lower().strip()
    if play == "p":
        slot_machine_play()
    else:
        print("You decide that you're too MLG for this shit and peace "
              "right out of there.")


def slot_machine_play():
    global dogecoin, perkpoints, dankpoints
    while True:
        if not playcheck():
            chance = random.randint(1, 3)
            if chance == 1:
                print("You don't have enough money for another round on"
                      "the slot machine. You gently tip your fedora "
                      "before leaving.")
            elif chance == 2:
                print("You don't have enough money for another round "
                      "on the slot machine, but you didn't even want "
                      "to play another round anyway. Psh.")
            elif chance == 3:
                print("You don't have enough money for another round "
                      "on the slot machine. You don your shades and "
                      "leave.")
            return
        dogecoin -= 10
        # 13.8% win chance TODO: increase win chance for more fun
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
            print(dankadjective() + ", you won %s Dogecoin.") % win
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
            print(randomweapon() + "!")
        elif tiles[a] == tiles[b] == tiles[c] == "(Doritos)":
            # 1/72 chance
            print("The machine rumbles and out comes a single Dorito "
                  "chip.")
            print("You gently bite off a single corner of the chip, "
                  "storing the rest in your pocket for later.")
            print("You have gained one Perk Point.")
            print("")
            perkpoints += 1
            # perkpoint() TODO: Add perkpoint()
        else:
            print("You didn't win anything this time.")
            if dogecoin == 420:
                print("You have 420 dogecoin. That's really fuckin "
                      "dank, m8.")
                print("You earned 1 dank point.")
                dankpoints += 1
        print("Hit enter to play again, type anything to quit. (You "
              "have %s Dogecoin.)") % dogecoin
        again = raw_input("").lower().strip()
        if again == "":
            pass
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


def randomweapon():
    return "random weapon (not implemented)"

slot_machine()
