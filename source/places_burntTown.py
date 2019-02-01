from source.utils import show, getInput, printc, printSlowly, wait

def burntTown(player):
    NAME = "Famous basketball player Labron James" # dying person # TODO
    if player.registerVisit("burntTown") ==1 :
        show("As you continue walking down the dusty road, you notice smoke rising in the distance.")
        show("You start to run.")
        show("The town has been burnt to the ground. Embers on ruined buildings are still burning. The fire was recent.")
        show("You walk to where the town square used to be. There is no one else in sight.")
        printc("You can try to find your @'grandpa'@yellow@s house, or @'search'@yellow@ around for survivers.")
        while True:
            x = getInput(player)
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
                show("A half burned flyer is pinned to the door of what used to be a library.")
                show('It says,')
                show("Poetry Contest!", dots=False)
                show("Compete with your best poems!", dots=False)
                show("Win awesome prizes!", dots=False) # no one will notice that this is a haiku
                show("The rest of the flyer is destroyed, except for the list of participating libraries, which is more libraries than you have ever been to.")
                break
        show("From somewhere behind you you can hear faint wimpering.")
        show(NAME + " is sitting with his back to the wall of a burnt building.")
        show("He lets out a cough, his body badly burned.")
        printSlowly("\"You... I've seen you before...\"", secondsBetweenChars=.1, pause=.3)
        printSlowly("\"Your grandpa... \"", secondsBetweenChars=.1, pause=.3)
        printSlowly("\"That... \"", secondsBetweenChars=.1, pause=.3)
        printSlowly("\"That... \"", secondsBetweenChars=.1, pause=.3)
        wait(1.4)
        printSlowly("\"MANIAC\"", secondsBetweenChars=.25)
        printSlowly("\"I bet he caused this whole fire!\"", secondsBetweenChars=.1)
        printSlowly("\"Come to think of it, that explosion came from right around his house!\"", secondsBetweenChars=.08)
        printSlowly("\"He probably had this whole thing planned out and then fled to his trailer North of town.\"", secondsBetweenChars=.06)
        printSlowly("\"That bastard.\"", secondsBetweenChars=.1)
        show("He slumps over and dies.")
        show("You grandpa's reputation around here has never been great, but you doubt he is capable of destroying an entire city.")
        show("You really should go see him.")
        

    show("You look around at the burnt buildings and "+NAME +"'s corpse.")
    show("There is not much else to do here.")
    show("You decide to head out back into the world.")
    return

