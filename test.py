#!/usr/bin/env LC_ALL=en_US.UTF-8 /usr/local/bin/python3

# import os
# from source.utils import wait
# os.system("start G:/Code/AdventureQuest/source/audio/paper.wav")
# wait(2)
# os.system("start G:/Code/AdventureQuest/source/audio/paper.wav")

# from playsound import playsound
# playsound('G:/Code/AdventureQuest/source/audio/paper.wav', bl)

# import pygame
# pygame.mixer.pre_init(44100, -16,2,2048)
# pygame.init()

# pygame.mixer.music.load('paper.wav')
# pygame.mixer.music.play()

# import contextlib
# with contextlib.redirect_stdout(None): # prevents console ouput during import
#     import pygame
# import pygame.mixer
# pygame.mixer.init()
# sound1 = pygame.mixer.Sound('source/audio/low piano G sharp.wav')
# sound2 = pygame.mixer.Sound('source/audio/splash.wav')
# chan1 = pygame.mixer.find_channel()
# chan1.queue(sound1)
# chan2 = pygame.mixer.find_channel()
# chan2.queue(sound2)


# from source.utils import *
# s = Sound('low piano G sharp.wav', loop=2)
# # s2 = Sound('paper.wav')
# wait(1)
# s.stopSound()
# s = Sound('etheral_unlock_1.mp3', loop=2)
# # s2 = Sound('paper.wav')
# wait(1)
# s.stopSound()
# print("t")

# import os, os.path

# # simple version for working with CWD
# print(len([name for name in os.listdir('.saves') if os.path.isfile(name)])
# )
# # path joining version for other paths
# DIR = '.saves'
# print (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# from source.utils import *

# def rollNumbers(start, end, speed=1.5):
#     r = start-end # range
#     maxSpeed = .01
#     if r < 0: r *= -1
#     s = ''
#     startTime = .5
#     for t in range(r):
#         startTime /= speed
#     time = startTime
#     for c in range(r+1):
#         s = str(start - c )
#         print(s)
#         if time < maxSpeed:
#             wait(maxSpeed)
#         else:
#             wait(time)
#         time *= speed 

# rollNumbers(100, 3)











# from source.utils import *
# import random
# LISTOFANSWERS = [
#     'What the fuck why would you ask me that.',
#     "I can't tell if you're joking or if you're serious.",
#     "Yeah. Sure.",
#     "Absolutely not.",
#     "Yes. It is destined to be so.",
#     "Sometimes.",
#     "I wouldn't count on it.",
#     "Probably!",
#     "It could be so.",
#     "You'll know soon enough.",
#     "Not sure."
# ]
# def punchJacksonInTheFace(stealth=True):
#     clear()
#     x = input("Ask me a question: ")
#     printSlowly(LISTOFANSWERS[random.randint(0,len(LISTOFANSWERS))])

# while True: punchJacksonInTheFace()
from __future__ import unicode_literals
import unicodedata
s=''
# s = str(s)
print('aaaàçççñññ'.decode('unicode-escape'))

# s = unicodedata.normalize('NFKD', s).encode('ascii','ignore')

# print(s)

# print(u'█'.encode('utf-8'))























