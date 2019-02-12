# -*- coding: utf-8 -*-
# # The purpose of this file is to hold utility functions that are commonly used

from __future__ import unicode_literals, print_function
import os   # Used to clear terminal
import random
# from colorama import *
import time
import pickle 
# init(autoreset=True) # init colors and reset to white each time
from prompt_toolkit import print_formatted_text, HTML
import getpass
import logging
import sys
import msvcrt
import threading
### sounds
import contextlib
with contextlib.redirect_stdout(None): # prevents console ouput during import
    import pygame
import pygame.mixer
###

#### console / user input #############################################

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # Clears terminal

def show(text, dots=True):
    #  Displays text, waits for 'enter' before continuing.
    printc(text)
    if dots: text='... '
    else: text = ''
    x=getpass.getpass(text) # waits for enter, doesnt show typed input becuase it's treated like a password

# more ansi colors: https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/examples/print-text/ansi-colors.py
# prints colored text. if more=true, will return s
def printWithColor(text, color, before="", after="", more=False):
    s = before
    if color == "red":
        s +=  '<ansired>' + text + '</ansired>'
    elif color == "green":
        s +=  '<ansigreen>' + text + '</ansigreen>'
    elif color == "yellow":
        s +=  '<ansiyellow>' + text + '</ansiyellow>'
    elif color == "blue":
        s +=  '<ansiblue>' + text + '</ansiblue>'
    elif color == "magenta":
        s +=  '<ansimagenta>' + text + '</ansimagenta>'
    elif color == "cyan":
        s +=  '<ansicyan>' + text + '</ansicyan>'
    else:
        s +=  '<ansiwhite>' + text + '</ansiwhite>'
    s += after
    if more:
        return s
    print_formatted_text(HTML(s))

def printc(text, stringList=False): # now supports multiple colors per call
    #  Given syntax like "this word is @colored@yellow@" will color all text between first two @'s. ie colored becomes yellow
    if not stringList: # if stringlist false
        t = text.split('@')
    else:
        t=stringList
    if len(t) == 1: #no @ in string
        print(text)
    elif (len(t)%3) -1 == 0: # has right amount of @'s
        if len(t) == 4:
            if stringList: # if using stringlist
                printWithColor(t[1],t[2], before=text + t[0], after = t[3])
            else: 
                printWithColor(t[1],t[2], before=t[0], after = t[3])
        else: 
            if stringList:
                s = text+ printWithColor(t[1],t[2], before=t[0], after = "", more=True)
            else:
                s = printWithColor(t[1],t[2], before=t[0], after = "", more=True)
            printc( s, stringList=t[3:] )
    else: printc("@You used the at sign syntax wrong.@red@")
#printc('@test@red@uncollored@color@blue@@color@yellow@')

# formats text in ways besides color. only bold and underline and reverse seem to work in my vs code terminal
def formatText(text, format):
    if format == "bold" or format == "b":
        s = '<b>' + text + '</b>'
        print_formatted_text(HTML(s))
    elif format == "blink":
        s = '<blink>' + text + '</blink>'
        print_formatted_text(HTML(s))
    elif format == "italic" or format == "i":
        s = '<i>' + text + '</i>'
        print_formatted_text(HTML(s))
    elif format == "reverse" or format == "r": # swap text color and background color
        s = '<reverse>' + text + '</reverse>'
        print_formatted_text(HTML(s))
    elif format == "underline" or format == "u":
        s = '<underline>' + text + '</underline>'
        print_formatted_text(HTML(s))
    elif format == "hidden" or format == "h":
        s = '<hidden>' + text + '</hidden>'
        print_formatted_text(HTML(s))

# tests
# formatText("bold", "bold")
# formatText("blink", "blink") # doesnt work for me
# formatText("italic", "italic") # doesnt work for me
# formatText("reverse", "reverse") 
# formatText("underline", "underline") 
# formatText("hidden", "hidden") # still visible

# returns true if lowercase of input == choice or first char of choice
def checkInput(inp, choice):
    choice = choice.strip().lower()
    if inp == choice or inp == choice[0]:
        return True
    else: return False

def wait(seconds): # accepts floats
    ''' printOnSecond is a string btw'''
    sys.stdout.flush()
    time.sleep(seconds)
    sys.stdout.flush()
    
class printSlowly():
    def __init__(self, text, secondsBetweenChars=.03, newline=True, pause=.7, initialWait=True, skipable=True, addParenthesis=True):
        # .03 is a pretty good talking speed
        # you no longer need to have parenthesis around dialogue when addparanthesis=true
        self.text = text
        self.secondsBetweenChars=secondsBetweenChars
        self.newline=newline
        self.pause=pause
        self.initialWait=initialWait
        self.skipable=skipable    
        self.finished=False    
        self.finishNow=False
        self.i = 0
        if addParenthesis and len(self.text)>0:
            firstChar = self.text[0]
            #check if first char is ' or "
            if firstChar != "'" and firstChar != '"':
                self.text = '"' + self.text + '"'

        t1 = threading.Thread(target=self.go, args=())
        t2 = threading.Thread(target=self.handleUserInput, args=())
        t2.start()  
        t1.start() 
        t1.join()  # waits here until thread is finished
    
    def go(self):
        pausePoints = ['.', ',', '!', '?', ':', '\n']
        skipThese = ['"', "'"]
        waitOnNextChar=False
        if self.initialWait: wait(self.pause)
        for self.i in range(len(self.text)):
            if self.finishNow:
                self.secondsBetweenChars = 0
                self.pause = 0
            print(str(self.text[self.i]), end='')
            if waitOnNextChar: 
                wait(self.pause)
                waitOnNextChar=False
            if str(self.text[self.i]) in pausePoints: # wait longer conditionally
                waitOnNextChar=True
            if str(self.text[self.i]) not in skipThese: # dont wait if printing quotes
                wait(self.secondsBetweenChars)
        if self.newline:print('')
        self.finished=True

    def handleUserInput(self):
        while True:
            if self.finished==True:
                return
            else:              # FIXME this isnt perfect
                while msvcrt.kbhit(): # try not to let user type while printing
                    x = getpass.getpass('')
                    print('\033[{}C\033[1A'.format(self.i+1) , end ='') # go back to where current printing char is and don't insert a newline
                    if x == '' and self.skipable:
                        self.finishNow=True
                

    

def preventUserInput():
    while msvcrt.kbhit(): # try not to let user type while printing
        x = getpass.getpass('')
        if x == '':
            print("test")

def thread(targetFunction, numberOfThreads=1,): # not used
    threads = []
    for i in range(numberOfThreads):
        t = threading.Thread(target=targetFunction, args=(i,))
        threads.append(t)
        t.start()

def yesno(player):
    #  Returns True if user input is yes, returns False if no.
    while True:
        userinput = getInput(player)
        if userinput == "yes" or userinput == "y":
            return True
        elif userinput == "no" or userinput == "n":
            return False
        else:
            printc("@'yes'@yellow@ or @'no'@yellow@.")

def dichotomy(option1, option2):
    # Returns True if user input is option1, returns False if option2.
    # Make sure the options are in stripped lowercase form
    while True:
        userinput = input("> ").lower().strip()
        if userinput == option1:
            return True
        elif userinput == option2:
            return False
        else:
            print("You must choose @'yes'@yellow@ or @'no'@yellow@.")

def getInput(player, oneTry=False, prompt='> '): # lowers and strips input
    while True:
        inp = input(prompt).lower().strip()

        if player.devmode and inp == "debug damage":
            player.takeDamage(int(input("How much damage? : ")))
        elif player.devmode and inp == "debug level up":
            player.levelUp()
        elif player.devmode and inp == "debug add xp":
            player.gainXp(int(input("How much XP?: ")), input("Scale? (True or False): "))
        elif inp == "hp":
            print("You have " + str(player.hp) + " out of " + str(player.maxhp) +  " HP. "),
            print("("),
            print(str(int(round(float(player.hp)/float(player.maxhp), 2) * 100))),
            print("% )")
        elif inp == "inv" or inp == "inventory":
            player.openInventory()
            return inp
        elif inp == "me":
            print("You are a level " + str(player.level) + " " + player.aspect['occ'] + " with " + str(player.money) + " money to your name.")
        elif inp == "save":
            pickle.dump(player, open("AdventureQuestSave.meme", "w"))
            show("@Game saved!@green@")
        elif inp == "load":
            player = pickle.load(open("AdventureQuestSave.meme", "r"))
            show("@Game loaded!@green@")
        elif inp == '':
            continue
        else:
            return inp
        if oneTry:
            return inp

def checkForCancel(inp):
    if  'back' in inp or  'cancel' in inp or  'return' in inp or  'bye' in inp or  'leave' in inp or  'exit' in inp:
        return True
    else:
        return False

# the only reason i made this was so that it would preserve newlines because the textwrap module doesnt do that
def wrap(text, limit=40, padding=True):
    text = str(text)
    if padding: pad = " "
    else: pad = ""
    out = ''
    l = text.split("\n")
    for s in l: # for each line
        if s == "":
            out += "\n"
            continue
        out += pad
        w=0 
        for d in s.split(): # for each word
            if w + len(d) + 2 < limit: # if fits in limit
                out += d + " "
                w += len(d) + 1 
            else: # if goes over limit
                out += "\n "
                out += d + " "
                w = len(d)
        if l[len(l)-1] != s: out += "\n" # only add newline if not on last line
    return out

#### dev #############################################

def bug(player):
    if player.devmode:
        show("@Well you hit a bug... You should probably fix that@red@")
    else:
        show("Oh my god. No. Not now.")
        show("A bug like this!? At a time like this!?")
        show("This can't be happening!")
        show("Quick! Save your game before it's too late!")
        show("Hurry!")
        show("What is happening?! WHAT IS HAPPENING!?")
        show("NOOOOOOOOOOOOO!!!!!!!!!!!")
        assert False

def log(text = "log!", warning=False):
    if warning:
        logging.warning(text)
    else:
        logging.info(text)

#### misc #############################################

# takes an array returns a random index
def getRandomIndex(arr):
    return arr[random.randint(0, len(arr)-1)]

def getRandInt(min = 1, max= 10): # return random int between 1 and max
    return random.randint(1, max)

def getOtherHand(player):
    if 'hand' not in player.aspect:
        return 'right' # just guess instead of crashing
    if player.aspect['hand']=='right':
        return 'left'
    else:
        return 'right'

def endDemo(player):
    show("Suddenly you don't feel right.")
    show("There's something wrong here.")
    show("Wait a minute, is that...")
    printSlowly('The end of the demo?', secondsBetweenChars=.1)
    show("Yes.")
    show("It is.")
    show("You jolt upright in bed.")
    show("Huh, what a strange dream.")
    show("You walk down stairs and eat a piece of toast.")
    # TODO peieo fo toasta
    show("Deciding you better start your day, you make your way outside.")
    return maintown(player)

#### UI stuff ############################################

def getStats(player):
    s = ''
    s += "Health:   " + str(player.hp) + " / " + str(player.maxhp) + "\n"
    s += "Level:    " + str(player.level) + "\n"
    s += "XP:       " + str(player.xp) + " / " + str(player.levelupxp) +"\n"
    s += "Money:    $ " + str(player.money) + "\n"
    s += "Strength: " + str(player.strength) + "\n"
    s += "Damage:   " + str(player.getTotalAttackPower()) + "\n"
    s += "Block:    " + str(player.getTotalBlock())
    return s

#### sounds #####################################################

class Sound(): 
    # to play a sample: Sound('low piano G sharp.wav')
    # FIXME: this probably has a lot of bugs yet to be discovered
    # TODO: add channels for better handling of sounds (might not be necessary)
    # more fun functions https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Channel.queue
    # NOTE: make loop -1 to loop forever
    # NOTE: volume adjustments (fade in out) only work with wav files
    def __init__(self, fileName, playNow=True, waitUntilFinished=False, queue=True, volume=1, loop=1):
        self.fileName = "source/audio/" + fileName
        self.loop = loop
        # initialize
        self.mixer = pygame.mixer # make a new mixer for each sound. seems easier that way
        self.mixer.init()
        if '.wav' in self.fileName:
            self.format = 'wav'
            self.sound = self.mixer.Sound(self.fileName) # sound method only supports wav files
            self.sound.set_volume(volume)
            if playNow:
                self.sound.play(self.loop)
        elif '.mp3' in self.fileName:
            self.format = 'mp3'
            self.sound = self.mixer.music.load(self.fileName)
            if playNow:
                self.mixer.music.play(self.loop)

    def getLength(self): # returns duration of wav file in seconds
        import wave
        import contextlib
        with contextlib.closing(wave.open(self.fileName,'r')) as f:
            frames = f.getnframes()
            rate = f.getframerate()
            return frames / float(rate)

    def stopSound(self): # stops all sounds
        if self.format == 'wav':
            self.sound.stop()
        elif self.format == 'mp3':
            self.mixer.music.stop()
        self.mixer.quit()

        #log("stopped playing " + self.fileName)

