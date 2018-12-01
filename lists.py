# The purpose of this file is to hold lists like a list of all dank memes


import random
from utils import *
from colorama import Fore
from colorama import Style

def getWeaponPrefix

def getRandomMemePeople():
    return getRandomIndex(DANKNAMES)

def getRandomDankAdjective():
    return getRandomIndex(DANKADJECTIVES)

def getRandomPainNoise():
    return getRandomIndex(PAIN_NOISES)

def getRandomEnemyName(biome):
    if biome == "plains":
        return getRandomIndex(ENEMYNAMES_PLAINS)
    if biome == "forest":
        return getRandomIndex(ENEMYNAMES_FOREST)
    if biome == "desert":
        return getRandomIndex(ENEMYNAMES_DESERT)
    if biome == "mountain":
        return getRandomIndex(ENEMYNAMES_MOUNTAIN)
    else:
        return "Void Creature"

def getReaction(reactionlevel):
    reaction = []
    if reactionlevel == 1:
        reaction = ["ehh", "pff"]
    elif reactionlevel == 2:
        reaction = ["oh cool", "neat"]
    elif reactionlevel == 3:
        reaction = ["whoa dude", "that was sick"]
    return reaction[random.randint(0, len(reaction)-1)]

#################### lists #############################################################
# these are constants. thats why they're all caps
# these list items should never have leading or trailing spaces and always have captial first letters of words ##########

DANKADJECTIVES = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
DANKNAMES = ["Caillou", "Gabe Newell", "Batman", "Sanic", "Peppa Pig", "Pepe", "Famous Basketball Player Shaquille O'Neal", "Big Man Tyrone", "Voiceover Pete", "Shrek", "Neil deGrasse Tyson", "Bill Nye the Science Guy", "xXx_Sinpars_xXx", "Nicholas Cage", "Sergei Rachmaninoff"]

# these can have duplicate names for different biomes and even duplicates within biome
# format like... "A wild [Shrek] appeared!" or "[Big huge rat monster] attacked and did 3 damage!"
ENEMYNAMES_PLAINS = ["FaZe Fanboy", "Sonic", "Tails", "Knuckles", "Ciallou", ]
ENEMYNAMES_FOREST = ["Shrek", "Donkey", "Big Huge Rat Monster",  ]
ENEMYNAMES_DESERT = ["Huge Fucking Scorpion"]
ENEMYNAMES_MOUNTAIN = ["Baby Dinosour"]

ATTACK_VERBS = ["scratch", "bite", "punch", "insult", "kick", "lick", "attack", "assult", "elbow", "curb-stomp"]
ATTACK_VERBS_EXTREME = ["nuke", "fireblast", "falcon punch", "no-scope", "ult"]

PAIN_NOISES = ["Youch!", "Oof!", "Ouch!", "Owwee!", "That has got to hurt.", "Should have dodged that.", 
    "That looked like it hurt!", "Dang!", "Ooch!", "Ow!", "~ouch~"]

# ex.
#print "look out! here comes a " + getRandomDankAdjective() + " " + getRandomEnemyName("forest")
