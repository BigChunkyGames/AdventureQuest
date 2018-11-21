# The purpose of this file is to hold lists like a list of all dank memes

from utils import *
from colorama import Fore
from colorama import Style

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

#################### lists #############################################################
# these are constants. thats why they're all caps
# these list items should never have leading or trailing spaces and always have captial first letters of words ##########

DANKADJECTIVES = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]

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