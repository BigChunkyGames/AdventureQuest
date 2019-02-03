from source.utils import *

def grandpasTrailer(player):
    show("Dense woods surround a path that leads into darkness.")
    show("Carefully, you make your way down the dirt path.")
    show("Finally the path ends.")
    show("There is a trailer beside a small pond.")
    print("Enter the trailer?")
    if yesno(player):
        show("Before you can reach the door a tiny robot opens it and looks at you.")
        printSlowly('"What the heck do you want?"',)
        x = player.getInput()
        if 'grandpa' in x:
            printSlowly('"Grandpa? I don\'t know any grandpas."', )
            # TODO robot bragging
            printSlowly('"You must have the wrong address. Bye bye."', )
            show("The robot slams the door.")
    else:
        show("Yeah, not right now.")
        show("You turn around and follow the path back outside of the woods.")
        return