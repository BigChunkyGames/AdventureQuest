from utils import *

def burntTown(player):
    if player.getVisits("burntTown", "add") ==1 :
        show("As you continue walking down the dusty road, you notice smoke rising in the distance.")
        show("You start to run.")
        show("The town has been burnt to the ground. Embers on ruined buildings are still burning. The fire was recent.")
        show("You walk to where the town square used to be. There is no one else in sight.")
        print("You can try to find your 'grandpa's house, or 'search' around for survivers.")
        while True:
            x = input(player)
            if (x == "grandpa" or x == "g"):
                show("You need to find out if your grandpa is alright. You start walking towards where you remember coming as a child so many times.")
                show("The buildings have all been charred by the fire. Most of them have caved in completely.")
                show("Ahead is your grandpa's house... what's left of it.")
                show("The house has been incinerated completely, but the door frame is still in tact.")
                show("You enter into the house and find it completely empty.")
                break
            elif (x == "search" or x == "s"):
                show("It's eerily quiet.")
                show("There is nothing around but charred wooden buildings that use to house the inhabitants of this place. The ground is still hot.")
                breakA
            else:
                print("'grandpa' or 'search' ")
        show("From somewhere behind you you can hear faint wimpering.")
        show("Famous basketball player Labron James is sitting with his back to the wall of a burnt building.")
        show("He lets out a cough, his body badly burned.")
        show("\"You... I've seen you before...\"")
        show("\"Your grandpa... They took him...\"")
        print("He waits for your response.")
        print("> ")
        #TODO add wait for 1 sec 
        show("It was... ")
        show("It was... ")
        show("The Shanghai Dragons")
        show("He slumps over and dies.")
        show("You recoil in fear.")
        show("The Shanghai Dragons...")
        show("After losing 40 consecutive tournament overwatch matches, the team must have lost their minds and burnt down the town.")
        show("But what do they want with your grandpa?")
        show("You take a moment to reminisce about all the great times you had with your grandpa as a child...")
        show("The time he taught you to no-scope...")
        show("The time he taught you to kickflip...")
        show("The time he showed you his emblem collection...")
        show("The time he taught you to dunk...")
        show("The time he let you be the getaway driver for that bank heist...")
        show("You look down at your hands.")
        show("They are wet from tears.")
        show('"No," you say.')
        show('"This is not the time for tears."')
        show('"This is the time for action."')
        show('"I am an adult now."')
        player.levelUp()


    while True:
        show("You look around at the burnt buildings and famous basketball player Labron James' corpse.")
        show("There is not much else to do here.")
        show("You decide to head out back into the world.")
        break

