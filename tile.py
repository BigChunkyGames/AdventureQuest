class Tile:

    def __init__(self, type_ = "wilderness", event = None, biome = None, fightChance = 0,): 
        self.type = type_ # type is a key word in python
        self.x = None
        self.y = None

    def setLocation(self, x,y):
        self.x = x
        self.y = y

    def getLocation(self):
        return (self.x,self.y)

