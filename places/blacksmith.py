from utils import *

def blacksmith(player):
    show("You head over to the blacksmith's place to take a look at some "
         "quality goods.")
    show("You walk over to your town's forge and approach the blacksmith, "
         "she's 6'5\" and the strongest one in your town.")
    show('"Hello!" she reaches out to shake your hand and ends up hurting it '
         'slightly.')
    player.takeDamage(1)
    show("You look at the blacksmith's wares, but she doesn't have anything "
         "you need at the moment. You decide to head back into the town.")
    # TODO: blacksmith