### System 1 ### Includes working demo ###

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
        direction = raw_input("Which way do you go? ").lower()
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
    print "You are now in room {0}, {1}".format(posx, posy)  # should import rooms independently to avoid spaghetti


#  The map looks like this
#  X-X-X
#  |   |
#  X-X-X
#    | |
#  X-X X

### System 2 ###

posx = 1
posy = 1

def room(x, y, door1, door2 = 'none', door3 = 'none', door4 = 'none'):
    global path, roomx, roomy
    if door1 == 'all':
        door1 = 'north'
        door2 = 'south'
        door3 = 'east'
        door4 = 'west'
    path = [door1, door2, door3, door4]
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
    return posx, posy

while True:
    room(posx, posy, 'all')  # Input (room's X position, room's Y postiion, and directions (or the word 'all'))
    print "You are now in room {0}, {1}".format(posx, posy)

# This is better, still needs a lot of work - I'm holding off until we have a more concrete map.


# Make dictionary 'routes' of directions for rooms
routes = {}
room(posx, posy, routes)
