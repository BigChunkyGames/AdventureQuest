import random

class Combat():
    def enemy(self, biome, level):
        #list of bad guys
        if biome == "forest":
            enemysList = ["Spooderman", "a Squidward", "(weed)", "(hitmarker)", "(hitmarker)", "(weed)", "(hitmarker)", "(Sample Text)", "(Sample Text)", "(Mountain Dew)", "(Sniper Rifle)", "(Doritos)"]
            x = 10 #total number of types of bad guy (not gonna be ten)
        elif biome == "planes":
            enemysList = ["Spooderman", "(weed)", "(weed)", "(hitmarker)", "(hitmarker)", "(weed)", "(hitmarker)", "(Sample Text)", "(Sample Text)", "(Mountain Dew)", "(Sniper Rifle)", "(Doritos)"]
            x = 10
        else:
            print("this area has no biome what the jizz")
        enemy = random.randrange(0, x)
        #may later be affected by level as well as biome
        return enemysList[enemy]

    def EnemyHP(self, level):
    #math used to find enemy stats
            #HP is between level *2 and level *3
        enemyHP = level*2 + random.randrange(0, level)
        return enemyHP

    def EnemyAttack(self, level):
            #attack is btween 1+level and 1+level * 1.5
        enemyAttack = 1 + level + random.randrange(0, level/2)
        return enemyAttack

    def Dropchance(self):
            #some math about drop chances
            #2 increasing chances from 40 and if one is maybe 4 or less drop = true
            #this is kind of crazy but we'll wait to playtest before changing
        dropchance1 = random.randrange(0, 40)
        #print (dropchance1)
        dropchance2 = random.randrange(0, dropchance1+1)
        #print (dropchance2)
        dropchance3 = random.randrange(0, 3)
       # print (dropchance3)
        dropchance = dropchance2 - dropchance3
        #print (dropchance)
        if dropchance <= 0:
            drop = True
        else:
            drop = False
        return drop

combat = Combat() #declare var combat a class
print("You're in the forest or something")
#stuff that will change somehow
biome = "forest"
level = 5
    #go gets what the enemy is based on just biome so far
enemy = combat.enemy(biome, level)
print("You enter the room and find holy shit its " + enemy + ".")
    #go find stuff about enemy stats
enemyHP = combat.EnemyHP(level)
enemyAttack = combat.EnemyAttack(level)
drop = combat.Dropchance()
print("The enemy has " + str(enemyHP) + " HP and " + str(enemyAttack) + " attack.")
#print(drop)
if drop == True:
    print("Its gonna drop something. ")
    #drop stuff function for items and/or weapons
else:
    print("Its not gonna drop something. ")

