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

room(1, 1, 'all')  # Input (room's X position, room's Y postiion, and directions (or the word 'all'))
print "You are now in room {0}, {1}".format(posx, posy)