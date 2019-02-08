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

import contextlib
with contextlib.redirect_stdout(None): # prevents console ouput during import
    import pygame
import pygame.mixer
pygame.mixer.init()
sound1 = pygame.mixer.Sound('source/audio/low piano G sharp.wav')
sound2 = pygame.mixer.Sound('source/audio/splash.wav')
chan1 = pygame.mixer.find_channel()
chan1.queue(sound1)
chan2 = pygame.mixer.find_channel()
chan2.queue(sound2)