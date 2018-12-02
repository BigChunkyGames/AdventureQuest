# The purpose of this file is to hold lists like a list of all dank memes


import random
from utils import *
# from colorama import Fore
# from colorama import Style

def getWeaponPrefix():
    pass
    # TODO

def getRandomMemePeople():
    return getRandomIndex(DANKNAMES)

def getRandomDankAdjective():
    return getRandomIndex(DANKADJECTIVES)

def getRandomPainNoise():
    return getRandomIndex(PAIN_NOISES)

def getRandomDankClothing():
    return getRandomIndex(DANKCLOTHING)

def getMotherlyPlattitude():
    return getRandomIndex(MOTHERLYPLATITUDES)

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

DANKADJECTIVES = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
DANKNAMES = ["Caillou", "Gabe Newell", "Batman", "Sanic", "Peppa Pig", "Pepe", "Famous Basketball Player Shaquille O'Neal", "Big Man Tyrone", "Voiceover Pete", "Shrek", "Neil deGrasse Tyson", "Bill Nye the Science Guy", "xXx_Sinpars_xXx", "Nicholas Cage", "Sergei Rachmaninoff"]
DANKCLOTHING = ["dick sock", "red bandana", "blue bandana", "single sock", "ski mask", "Christmas stocking"]
MOTHERLYPLATITUDES = ["There's no 'I' in 'Team'!", "Everybody makes mistakes. Don't forget to save often!", "Time heals all wounds. If you're injured, find a place to sleep!", "Work smarter, not harder. A lot of times, you can just type the first letter of a choice instead of the whole word."]

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
