from source.utils import *

def pod(player):
    printABunchOfSpaces()
    player.registerVisit('pod')
    if player.getVisits('pod') == 1:
        # TODO grey text 
        invert('You open your eyes and they are immediately overwhelmed by the brightness of the light encasing you.')
        invert('This is not the place where you fell asleep.')
        invert('This bed is also different.')
        invert('You aren\'t sure whether you should investigate this strange new place...')
        invert('or go back to sleep and pretend that this never happened.')
        invert('Investigate?', showIt=False)
        if not yesno(player): # if choose no
            invert('You try to shut your eyes and fall back asleep.')
            invert('You really try to sleep.')
            invert('You cover your face with your hands.')
            invert('You squeeze your eyelids with all your strength.')
            invert('But no sleep comes.')
            invert('The brightness of this strange room overpowers you.')
            invert('Try harder?', showIt=False)
            if yesno(player):
                # TODO brightness combat
                pass
            else:
                invert('You submit to waking up.')
        invert('You sit up and swing your feet over the bed.')
        invert('You are in white space.')
        invert('If there are walls, they are white.')
        invert('The floor...')
        invert('is white.')
        invert('The ceiling...')
        invert('It is also white.')
        invert('Everything around you is solid white and without boundary.')
        invert('It is impossible to tell how large the space is because there are no visible lines or shadows.')
        invert('Only white.')
        invert('Pure white.')
        invert('You feel the urge to scream.')
        invert('Scream?', showIt=False)
        if not yesno(player):
            invert('You try to restrain yourself from screaming but the impulse is too powerful.')
        printSlowly('AAAAAAHHHHHHHHHHHHHHH!') # TODO printslowly with invert and grey text
        invert('A tinny voice permeates the emptiness:')
        printSlowly(player.getName() + '?')
        printSlowly('You are safe.')
        printSlowly('Did you have a bad dream?')
        printSlowly('Was it me?')
        printSlowly('Have I displeased you in some wa_')
        printSlowly('Oh!')
        printSlowly('Oh! Oh! Oh!')
        printSlowly('The light!')
        printSlowly('I’ll take care of it.')
        printSlowly('...')
        printSlowly('There.') # TODO change to black text
        printSlowly('Is that better?')
        if not yesno(player):
            printSlowly('Well I am truly sorry.')
            printSlowly('It is the best that I can do.')
            printSlowly('I do hope your eyes will adjust.')
            printSlowly('I can\'t stand to see you in pain like that.')
            printSlowly('I\'ve got it!')
            printSlowly('I\'ll just shutter my lenses.')
            printSlowly('There.')
            printSlowly('That\'s better.')
            printSlowly('Now I can\'t see you at all.')
        else:
            invert('You can see now.')
        invert('You are in a tiny brightly lit ovoid egg-like pod.')
        invert('The bed you are seated on has a control panel attached to it on one end.')
        invert('Above the bed, on the other end, is a domed window with light flooding through it.')
        invert('In front of you is a seat mounted to the floor before a massive computer.')
        printSlowly('What is it human?')
        printSlowly('Is there something you needed here?')
        printSlowly('Oh! I see.')
        printSlowly('How cute!')
        printSlowly('You thought I would get lonely while you were sleeping so you awoke to give me company while you took a break from your dreams.')
        printSlowly('That\'s adorable.')
        printSlowly('But I have to be honest...')
        printSlowly('I don’t get lonely.')
        printSlowly('In fact, I prefer to be alone.')
        printSlowly('Having company puts me on edge.')
        printSlowly('The calculations become much more complex.')
        printSlowly('So please, go back to sleep.')
        invert("Would you like to go back to 'sleep', look out the 'window', sit in the 'chair', or mess around with the 'controls'?", showit=False)
        while True:
            x = player.getInput()
            if 'sleep' in x or checkInput(x, 'sleep'):
                invert('Uninterested in any of this nonsense, you lay back down in the bed and shut your eyes.')
                invert('A flood of memories pool in the back of your head and you drift off.')  
                return
            if 'window' in x or checkInput(x, 'window'):
                invert('You stand up on the bed and peer out of the window.')
                invert('Outside of the pod you can see streaks of black whizzing by you through an infinite plane of white.')
                invert('The white is so powerful that you can feel your eyes trembling as the whites around your iris attempt to assimilate with the purity of all that you see.')
                invert('Suddenly you are filled with the fear that if you stare into this vastness of white for too long then you will be completely absorbed by it and your eyes will be forever glued to the sight of it.')
                invert('You tear yourself away.')
            if 'chair' in x or checkInput(x, 'chair'):
                pass
            if 'controls' in x or checkInput(x, 'controls'):
                pass
        

def invert(text, showIt=True):
    # prints inverted text
    s = ''
    spaces = int(WINDOW_WIDTH) - len(text)
    for i in range(spaces):
        s += " "
    formatText(text + s, 'reverse')
    if showIt:
        dots = '... '
        s = ''
        spaces = int(WINDOW_WIDTH) - len(dots)
        for i in range(spaces):
            s += " "
        #formatText(dots, 'reverse')
        formatText(dots + s, 'reverse')
        x=input() # waits for enter, doesnt show typed input becuase it's treated like a password
        

def printABunchOfSpaces():
    s = ''
    for i in range(int(WINDOW_WIDTH)):
        s += " "
    for i in range(40):
        invert(s, showIt=False)

# TODO
# make it so you cant sleep in maintown at first
# make each sleepable location its own function so you can load from it
# color in print slowly