posx = 1
posy = 1

def room(x, y):
    global path, roomx, roomy
    path = []
    if x == 1 and y == 1 or x == 1 and y == 2 or x == 1 and y == 3 or x == 2 and y == 2 or x == 2 and y == 3:
        path.append('east')
    if x == 1 and y == 2 or x == 2 and y == 1 or x == 3 and y == 1 or x == 3 and y == 2:
        path.append('north')
    if x == 1 and y == 3 or x == 2 and y == 2 or x == 3 and y == 2 or x == 3 and y == 3:
        path.append('south')
    if x == 2 and y == 1 or x == 2 and y == 2 or x == 2 and y == 3 or x == 3 and y == 2 or x == 3 and y == 3:
        path.append('west')
    roomx = x
    roomy = y
    move()

def move():
    global posx, posy, path
    while posx == roomx and posy == roomy:
        direction = raw_input("Which way do you go? ")
        if direction in path and direction == 'east':
            posx += 1
        elif direction in path and direction == 'west':
            posx -= 1
        elif direction in path and direction == 'north':
            posy += 1
        elif direction in path and direction == 'south':
            posy -= 1
        else:
            print("That move isn't possible.")
    print("You move %s." % direction)

while True:
    room(posx, posy)
    print "You are now in room {0}, {1}".format(posx, posy)


#  The map looks like this
#  X-X-X
#  |   |
#  X-X-X
#    | |
#  X-X X
