from utils import *

def store(player):
    show("You stride into the sedentary sales store supplementing the "
         "not-so-silent town of %s, where succulent sweets "
         "are sold. " % player.aspect['town'])
    show("You approach the shopkeeper, an old and wary gentleman with age on "
         "his face and experience in his eyes.")
    show('"What\'ll it be for ya today?"')
    show("You make a point of considering the shopkeeper's wares, but you're "
         "not in the market for anything he's selling at the moment.")
    show("He looks a little irritated that you didn't buy anything as you "
         "head back to the town center.")
    # TODO: add the shop