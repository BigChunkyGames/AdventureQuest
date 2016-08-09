import random
#  TODO: consult other adventure games to see what a good attack:HP ratio is

class Combat():
    def enemy(self, biome, level):
        # List of bad guys
        if biome == "forest":
            enemieslist = ["Forest_Spooderman", "Forest_a Squidward", "Forest_mob1", "Forest_mob2"]
        elif biome == "plains":
            enemieslist = ["Plains_Spooderman", "Plains_mob1", "Plains_mob2", "Plains_mob3"]
        else:
            print("this area has no biome what the heck in the world")
        enemy = random.randrange(0, len(enemieslist))
        # TODO: May later be affected by level as well as biome
        return enemieslist[enemy]

    def enemyhp(self, level):
        # HP is between (level * 48) and (level * 52)
        return level*random.randint(48, 52)

    def enemyattack(self, level):
        # Attack is between (level * 10) and (level * 15)
        if level == 1:
            return 2
        else:
            return level * random.randint(10, 15)

    def dropchance(self, percent):
        dropchance = random.randint(1, 100)
        if dropchance <= percent:
            return True
        else:
            return False

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
