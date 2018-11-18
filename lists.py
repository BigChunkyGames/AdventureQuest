# The purpose of this file is to hold lists like a list of all dank memes

import random

def getRandomDankAdjective():
    adjs = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity"]
    return adjs[random.randint(0, len(adjs)-1)]

def getWeaponPrefix

def getRandomMemePeople():
    names = ["Caillou", "Gabe Newell", "Batman", "Sanic", "Peppa Pig", "Pepe", "Famous Basketball Player Shaquille O'Neal", "Big Man Tyrone", "Voiceover Pete", "Shrek", "Neil deGrasse Tyson", "Bill Nye the Science Guy", "xXx_Sinpars_xXx", "Nicholas Cage", "Sergei Rachmaninoff"]
    return names[random.randint(0, len(names)-1)]

def getReaction(reactionlevel):
    reaction = []
    if reactionlevel == 1:
        reaction = ["ehh", "pff"]
    elif reactionlevel == 2:
        reaction = ["oh cool", "neat"]
    elif reactionlevel == 3:
        reaction = ["whoa dude", "that was sick"]
    return reaction[random.randint(0, len(reaction)-1)]