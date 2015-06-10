import random


class Combat():
    def enemy(self, biome, level):
        # List of bad guys
        if biome == "forest":
            enemieslist = ["Forest_Spooderman", "Forest_a Squidward", "Forest_mob1", "Forest_mob2"]
        elif biome == "plains":
            enemieslist = ["Plains_Spooderman", "Plains_mob1", "Plains_mob2", "Plains_mob3"]
        else:
            print("this area has no biome what the jizz")
        enemy = random.randrange(0, len(enemieslist))
        # TODO: May later be affected by level as well as biome
        return enemieslist[enemy]

    def enemyhp(self, level):
            # HP is between (level * 2) and (level * 3)
        enemyHP = level*2 + random.randrange(0, level)
        return enemyHP

    def enemyattack(self, level):
            # Attack is between (1 + level( and (1 + level * 1.5)
        enemyAttack = 1 + level + random.randrange(0, level/2)
        return enemyAttack

    def dropchance(self, percent):
        dropchance = random.randint(1, 100)
        if dropchance <= percent:
            drop = True
        else:
            drop = False
        return drop

combat = Combat()
# Variables
if random.randint(0,1) == 0:  # Random for testing purposes
    biome = 'forest'
else:
    biome = 'plains'
level = random.randint(1,10)  # Random for testing purposes TODO: enemy level based on biome and player level
enemy = combat.enemy(biome, level)
print("You're in the {biome}").format(biome = biome)
print("You enter the room and find holy shit its {enemy}.").format(enemy = enemy)
    # Assign base stats to variables to potentially be changed (ex. enemyHP will be changed by player damage, enemyAttack could be changed by weakness potions, etc)
enemyHP = combat.enemyhp(level)
enemyAttack = combat.enemyattack(level)
print("The enemy is a level {level} with {enemyhp} HP and {enemyattack} attack.").format(level = level, enemyhp = str(enemyHP), enemyattack = str(enemyAttack))
#print(drop)
if combat.dropchance(50) == True:
    print("Its gonna drop something.")
else:
    print("Its not gonna drop something.")
