import random
from source.lists import FOREST_SYNONYMS,PLAINS_SYNONYMS,DESERT_SYNONYMS,MOUNTAINS_SYNONYMS,TRANSIT_SYNONYMS
from source.utils import *
from source.tile import *
from source.combat import * 
# this is going to need to import all places
from source.places_maintown import maintown
from source.places_burntTown import burntTown
from source.places_dogeTown import dogeTown
from source.places_flowers import flowers
from source.places_grandpasTrailer import grandpasTrailer

class Map:

    def __init__(self):
        self.map = [i[:] for i in [[None] * 17] * 16] # declare empty actual map. makes a 15 col 16 row emtpy 2d list
        x = lambda x, y : self.addToMap(Tile(x,y,"impassible", None, None, 0, None))
        o = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "forest", .5, None) ) # havent coded yet
        f = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "forest", .5, None) )
        p = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "plains", .5, None) )
        d = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "desert", .5, None) )
        m = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "mountains", .5, None) )
        t = lambda x, y : self.addToMap(Tile(x,y,"town", None, None, 0 , None))
        # this is the constant map of the realm
        # each index of the 2d array is a tile object
        self.INITIAL_MAP = [  # 16 x 17
        # 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 X
        [ x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x ], # 0 
        [ x, x, x, x, m, f, f, t, m, x, t, m, x, x, x, x, x ], # 1 
        [ x, x, x, m, f, f, f, f, f, f, f, f, m, x, x, x, x ], # 2
        [ x, m, m, m, f, t, f, f, p, p, f, f, f, t, x, x, x ], # 3
        [ x, m, x, m, p, p, p, p, p, p, t, f, f, m, m, x, x ], # 4
        # default village --v           v-- burnt town
        [ x, m, x, d, p, p, t, p, t, p, t, f, f, m, m, m, x ], # 5 
        [ x, m, x, d, p, p, p, p, p, p, f, f, f, m, m, m, x ], # 6
        [ x, x, d, d, p, p, p, p, p, p, f, f, f, m, m, t, x ], # 7
        [ x, t, d, d, d, t, p, p, p, t, p, f, t, m, m, m, x ], # 8
        [ x, d, d, d, d, p, p, t, f, f, p, f, f, m, m, m, x ], # 9
        [ x, x, d, d, d, f, f, f, f, f, f, t, f, m, m, m, x ], # 10
        [ x, x, x, x, d, f, f, f, t, f, f, f, f, m, m, x, x ], # 11
        [ x, x, x, x, x, f, f, f, f, f, f, f, x, x, x, x, x ], # 12
        [ x, x, x, x, x, x, x, x, f, f, t, x, x, x, x, x, x ], # 13
        [ x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x ]  # 15 Y
        ] 
        self.initializeMap() # sets self.map to be a new INITIAL_MAP
        self.initializeTileAttributes()

        

    def addToMap(self, tile):
        self.map[tile.x][tile.y] = tile

    def initializeMap(self):
        for i in range(0,len(self.INITIAL_MAP)): # height
            for j in range(0,len(self.INITIAL_MAP[0])): # width
                self.INITIAL_MAP[i][j](i,j)
                #print self.getTileDescription(i,j)

    def getTile(self,x ,y): # i literally made this function just so i can use x y instead of y x
        return (self.map[y][x]) # it took me so fucking long to realize this needed to be y x not x y

    def getTileDescription(self, x, y):
        if not self.getTile(x,y).description == None: # if description exists
            return self.getTile(x,y).description # return it
        elif not self.getTile(x,y).getBiome() == None: #elif biome exists
            return self.getTile(x,y).getBiome()
            
        elif self.getTile(x,y).type == "town":
            return "a town." # shoould never see this, only will if a town has not been given a description
        elif self.getTile(x,y).type == "impassible":
            return "a cliff off the edge of the world." #TODO add a bunch of things it can say as descriptions for impassible areas (random each time)
        else:
            return "nothing at all don't even worry about it." # if you see this it means a place was not given a description

    def makeWildernessEvent(self, x,y):
        s = ''
        s+=getRandomIndex(TRANSIT_SYNONYMS) + " "
        if self.getTile(x,y).getBiome() == "forest":
            s+=getRandomIndex(FOREST_SYNONYMS) + "." 
        elif self.getTile(x,y).getBiome() == "plains":
            s+= getRandomIndex(PLAINS_SYNONYMS) + "."
        elif self.getTile(x,y).getBiome() == "desert":
            s+= getRandomIndex(DESERT_SYNONYMS) + "."
        elif self.getTile(x,y).getBiome() == "mountains":
            s+= getRandomIndex(MOUNTAINS_SYNONYMS) + "."
        else:
            s+="nothing don't even worry about it"
        show(s)

    def initializeTileAttributes(self):
        #TODO: add description for each town ie to the north you see ...
        #TODO: add place functions too
        # try to keep these organized by y then x (top to bottom)

        #            x,y
        self.getTile(7,1).description = "a number of cute doggos prancing about."
        self.getTile(7,1).placeFunction = lambda player: dogeTown(player) 

        self.getTile(10,4).description = "Grandpa's trailer."
        self.getTile(10,4).placeFunction = lambda player: grandpasTrailer(player)

        self.getTile(6,5).description = "your home town." # maintown
        self.getTile(6,5).placeFunction = lambda player: maintown(player) 

        self.getTile(7,5).fightChance = 0 # tile to right of hometown

        self.getTile(8,5).description = "a beautiful field of flowers." # maintown
        self.getTile(8,5).placeFunction = lambda player: flowers(player)

        self.getTile(10,5).description = "smoke billowing from over the hills."
        self.getTile(10,5).placeFunction = lambda player: burntTown(player) 
        

    def goTo(self,x,y, player):
        clear()
        if self.getTile(x,y).type == "impassible":
            print( "you can't go that way.") #TODO flavor add flavor text
            return
        player.currentLocationX = x
        player.currentLocationY = y
        if not (self.getTile(x,y).placeFunction):
            # no interesting thing at this tile,
            self.makeWildernessEvent(x,y)
            if self.getTile(x,y).fightChance > random.uniform(0, 1):
                # if chance of fight is greater than ranom float 
                Combat(player, self.getTile(x,y).getBiome())
                return
        else:
            self.getTile(x,y).placeFunction(player)
