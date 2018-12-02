# this is the constant map of the realm
# each index of the 2d array is a tile object

from tile import *

x = None # impassable
o = None # empty for now
# 16 x 16
THE_MAP = [
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x],
[ x, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, x]
]

def initializeMap():
    for i in range(len(THE_MAP)): # height
        for j in range(len(THE_MAP[0])): # width
            if THE_MAP[i][j] == o: # default
                THE_MAP[i][j] = Tile()
            elif THE_MAP[i][j] == x: # impassable
                THE_MAP[i][j] = Tile("impassable")

            THE_MAP[i][j].setLocation(i,j)
            print THE_MAP[i][j].type

initializeMap()


