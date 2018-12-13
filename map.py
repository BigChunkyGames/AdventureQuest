# this is the constant map of the realm
# each index of the 2d array is a tile object

from tile import *



#TODO: make a function that customizes tiles even more, adding where to go in the code for towns and such
#TODO: make a "generate even" function in Tile that can be given to specific coordinates of the map


class Map:



    def __init__(self):
        self.map = [i[:] for i in [[None] * 16] * 17] # declare empty actual map 
        x = lambda x, y : self.addToMap(Tile(x,y,"impassible", None, None, 0))
        o = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "forest", 1) ) # havent coded yet
        f = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "forest", 1) )
        p = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "plains", 1) )
        d = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "desert", 1) )
        m = lambda x, y : self.addToMap(Tile(x,y,"wilderness", None, "mountains", 1) )
        t = lambda x, y : self.addToMap(Tile(x,y,"town", None, None, 0 ))
        self.INITIAL_MAP = [  # 16 x 17
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17
        [ x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x ],
        [ x, x, x, x, m, f, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, m, f, f, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, m, m, m, f, t, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, m, x, m, p, p, p, p, o, o, o, t, o, o, o, o, x ],
        # default village --v
        [ x, m, x, d, p, p, t, p, t, f, t, t, o, o, o, o, x ],
        [ x, m, x, d, p, p, p, p, o, o, o, o, o, o, o, o, x ],
        [ x, x, d, d, p, p, p, p, o, o, o, o, o, o, o, o, x ],
        [ x, t, d, d, d, t, p, p, o, o, o, o, o, o, o, o, x ],
        [ x, d, d, d, d, p, p, t, o, o, o, o, o, o, o, o, x ],
        [ x, x, d, d, d, f, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, x, d, f, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, x, x, f, f, f, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, x, x, x, x, x, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, x, x, x, x, x, o, o, o, o, o, o, o, o, x ],
        [ x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x ]
        ] 

    def addToMap(self, tile):
        self.map[tile.getX()][tile.getY()] = tile
        print self.map[tile.getX()][tile.getY()].getType()

    def initializeMap(self):
        for i in range(len(self.INITIAL_MAP)): # height
            for j in range(len(self.INITIAL_MAP[0])): # width
                self.INITIAL_MAP[i][j](i-1,j-1)

    def getTile(self,x ,y):
        return (self.map[x][y])


m = Map()
m.initializeMap()
# print m.getTile(4,4).getBiome()
# print m.getTile(7,7).getBiome()


