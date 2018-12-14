class Tile:
                # BIOMES: plains, forest, desert, mountains, 
                # TYPE: town, wilderness, impassible
                # NOTE: towns are anywhere the player can interact with something besides an enemy and they dont have to specifically be towns like the fountain of hope is considered a town even though there is no town involved with the fountain of hope
    def __init__(self, x, y, type_, event , biome , fightChance, description ): 
        self.x = x
        self.y = y
        self.type = type_ # type is a key word in python
        self.event = event
        self.biome = biome
        self.fightChance = fightChance
        self.description = description # a town's name or what it looks like. if null use biome
        self.placeFunction = None # none should default to combat potential if fight chance > 0

    def getBiome(self):
        return self.biome
    def getType(self):
        return self.type

