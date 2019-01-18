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

def wait(seconds, printThisStringEachSecond=False): # accepts floats
    ''' printOnSecond is a string btw'''
    if printThisStringEachSecond == False:
        time.sleep(seconds)
    else:
        for s in range(seconds):
            print(printThisStringEachSecond),
            time.sleep(1)

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
            print("You must choose 'yes' or 'no'.")

def getInput(player):
    while True:
        inp = input("> ").lower().strip()
        if player.devmode and inp == "debug damage":
            player.takeDamage(int(input("How much damage? : ")))
        elif player.devmode and inp == "debug level up":
            player.levelUp()
        elif player.devmode and inp == "debug add xp":
            player.addExperience(int(input("How much XP?: ")), input("Scale? (True or False): "))
        elif inp == "hp":
            print("You have " + str(player.hp) + " out of " + str(player.maxhp) +  " HP. "),
            print("("),
            print(str(int(round(float(player.hp)/float(player.maxhp), 2) * 100))),
            print("% )")
        elif inp == "i" or inp == "inventory":
            player.openInventory()
        elif inp == "me":
            print("You are a level " + str(player.level) + " " + player.aspect['occ'] + " with " + str(player.money) + " money to your name.")
        elif inp == "save":
            pickle.dump(player, open("AdventureQuestSave.meme", "w"))
            show("Game saved!")
        elif inp == "load":
            player = pickle.load(open("AdventureQuestSave.meme", "r"))
            show("Game loaded!")
        else:
            return inp

def checkForCancel(input):
    if checkInput(input, 'back') or checkInput(input, 'cancel') or checkInput(input, 'return'):
        return True
    else:
        return False

# the only reason i made this was so that it would preserve newlines because the textwrap module doesnt do that
def wrap(text, limit=40, padding=True):
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
