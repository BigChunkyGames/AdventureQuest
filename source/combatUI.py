#!/usr/bin/env python
"""
https://github.com/prompt-toolkit/python-prompt-toolkit/blob/master/examples/full-screen/full-screen-demo.py
"""
from __future__ import unicode_literals

from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout.containers import Window, VSplit, HSplit, FloatContainer, Float, WindowAlign, is_container, ConditionalContainer, DynamicContainer
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.lexers import PygmentsLexer
from prompt_toolkit.layout.menus import CompletionsMenu
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import TextArea, Label, Frame, Box, Checkbox, Dialog, Button, MenuContainer, MenuItem
from source.customBase import RadioList, ProgressBar # had to make some changes
#from pygments.lexers.html import HtmlLexer
from prompt_toolkit.layout.margins import ScrollbarMargin, NumberedMargin
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText

from source.lists import getRandomAttackVerb
from source.utils import wait, wrap, Sound, getStats
from source.inventoryUI import InventoryUI
import threading

import re
import random

class CombatUI():

    def __init__(self, player, enemy, song='worry 2.wav'):
        self.song = Sound( player,fileName = song, loop=-1)
        self.player = player
        self.playerClans = ' '.join(self.player.clantags)
        if len(self.player.clantags) > 0 : 
            self.playerName = FormattedText([
                ('#ffffff', str(player.aspect['name'])),
                ('', ' '),
                ('#cc00cc', str(self.playerClans)),
            ]) 
        else: 
            self.playerClans =  self.playerName = FormattedText([
                ('#ffffff', str(player.aspect['name'])),
            ]) 
        self.enemy = enemy

        self.playerGoesNext = True # by default, enemy always gets first strike
        self.playerJustDodged = False
        self.escapeTries = 0
        self.escapeChance = .3

        self.battleLog = '\n\n\n\n\n\n'
        self.maxHeightOfBattleLogWindow = 7
        self.totalWidth = 90
        self.actionsWidth = 30
        self.statsWidth = 20 

        self.selectedIndexText = ''
        self.result = None

        self.playerHPBar = ProgressBar()
        self.setHealthProgressBar(self.playerHPBar, self.toPercent(self.player.hp, self.player.maxhp)) 
        self.enemyHPBar = ProgressBar()
        self.setHealthProgressBar(self.enemyHPBar, 100) 

        self.radios = RadioList(
            values=[ #value, lable
                ('Attack', 'Attack'), # use eqipped weapon
                ('Dodge', 'Dodge'), # icrease miss chance for enemy
                ('Item', 'Item'),
                ('Run', 'Run') # try to escape
                # more options could be:
                # check - returns text about enemy potentially indicating weaknessess
            ],
            player = self.player,
            width = self.actionsWidth)
        
        self.bindings = KeyBindings()
        self.bindings.add('right' )(focus_next)
        self.bindings.add('tab' )(focus_next)
        self.bindings.add('s-tab')(focus_previous)
        self.bindings.add('left')(focus_previous)
        self.bindings.add('c-m')(self.handleEnter)
        self.bindings.add('escape')(self.tryToEscape)
        # self.bindings.add('up')(self.setSelectedIndexTextUp)
        # TODO: make secret easter egg key bindings # self.bindings.add('a', 'a')(self.test)  
        self.style = Style.from_dict({
            'dialog.body':        'bg:#000000 #ffcccc', #background color, text color
        })

        self.application = Application(
            layout=Layout(
                self.getRootContainer(),
                focused_element=self.radios,
            ),
            key_bindings=self.bindings,
            style=self.style,
            mouse_support=True,
            full_screen=True,
            )

    

    # call this function to change the value a progress bar (prog) to a percent
    def setHealthProgressBar(self,progbar, percent):
        if percent < 0: # should never happen but for safety
            percent = 0
        progbar.container = FloatContainer(
            content=Window(height=1),
            floats=[
                Float(left=0, top=0, right=0, bottom=0, content=VSplit([
                    Window(style='bg:#00cc00', # health, green
                            width=lambda: D(weight=int(percent))),
                    Window(style='bg:#ff0000', # damage, red
                            width=lambda: D(weight=int(100 - percent))),
                ])),
            ])

    def toPercent(self, value, max):
        return int(100*(float(value)/float(max)))

    def handleEnter(self, event):
        if not self.playerGoesNext: # check if it's actually your turn
            return
        self.playerGoesNext = False

        choice = self.radios.values[self.radios._selected_index][0] 
        s = ''
        if choice == "Attack":
            self.attackEnemy()
            return # return early so attackEnemy can go to enemy turn so damaging consunmables work
        elif choice == "Dodge": # dodging increases chance for enemy to miss by 30% SCALING
            s += "You tried to dodge... "
            self.playerJustDodged = True 
        elif choice == "Item": # doesnt take your turn
            self.playerGoesNext = True
            self.done(result='inventory')
            return
        elif choice == "Run":
            s += self.tryToEscape()
        else:
            s += "How did you do that!?"
        
        self.enemyTurn(s)

    def attackEnemy(self, alwaysHit=True, consumableDamage=None, consumableName=None ):
        s = ''
        if not consumableDamage == None: # if has consumable damage
            damage = consumableDamage # better also have a name
            s += "You threw the " + str(consumableName) + "... "
        else:
            s +=  "You tried to attack... "
            damage = self.player.getTotalAttackPower()
        s += " and did " 
        s += str(damage)
        s += " damage!" # TODO color
        self.enemy.hp = self.enemy.hp - int(damage)
        if self.enemy.hp < 0:
            self.enemy.hp = 0
        self.setHealthProgressBar(self.enemyHPBar, self.toPercent(self.enemy.hp, self.enemy.maxhp))
        self.enemyTurn(s)
    
    def tryToEscape(self, event=None):
        s = ''
        s += "You tried to run..." 
        randomChance = random.uniform(0,1) - (self.escapeTries-1) *.1 # each try makes it 10 percent easier to escape after first try
        if self.escapeChance > randomChance and self.escapeTries>0: #has to have already tried to escape once
            s += " and escaped the combat!" # TODO advanced combat: isnt ever visible
            self.done("escaped")
        else:
            s += " but failed to escape!"
        self.escapeTries += 1
        return s

    def enemyTurn(self, textOfPlayerTurn=False):
        if self.enemy.hp == 0: # check if he dead
            self.done("win")
            return
        # for now, always try to attack TODO advanced combat
        self.playerGoesNext = True
        s=''
        s += self.enemy.name + " tried to " 
        attack = self.enemy.getRandomAttack() 
        if attack[-1] == "*": # if attack finishes the sentence
            s += attack[:-1] # remove *
        else :
            s += str(attack)
            s += " you... "
            
        # calculate hit chance and handle
        dodgeModifier = 0 # TODO advanced combat dodge modifier
        if self.playerJustDodged == True:
            dodgeModifier = 30
            self.playerJustDodged = False
        if self.enemy.missChancePercent + dodgeModifier > random.randint(0,100):
            # missed
            if not attack[-1] == "*": s += " but missed!"
            else: s += " But missed!"
        else:
            # hit
            damage = self.enemy.attack
            if not attack[-1] == "*": s += " and dealt " + str(damage) + " damage!"
            else: 
                s += " It dealt " + str(damage) + " damage!"
            self.player.hp = self.player.hp - damage # lose health
            #t1 = threading.Thread(target=self.rollNumbers(self.player.hp, self.player.hp - damage), args=())
            #t1.start()
            # self.rollNumbers(self.player.hp, self.player.hp - damage)

            if self.player.hp < 0:
                self.player.hp = 0
            self.setHealthProgressBar(self.playerHPBar, self.toPercent(self.player.hp, self.player.maxhp))
            if self.player.hp == 0: #dead
                # TODO make death less awkwawrd
                self.done("lose")
                return
        if textOfPlayerTurn: 
            self.battleLog = textOfPlayerTurn + '\n\n' + s 
        else:
            self.battleLog = s 
        self.refresh()

    def rollNumbers(self, start, end, speed=1.5):
        r = start-end # range
        maxSpeed = .01
        if r < 0: r *= -1
        startTime = .5
        for t in range(r):
            startTime /= speed
        time = startTime
        for c in range(r+1):
            s = int(start - c )
            self.player.hp = s
            self.refresh()
            if time < maxSpeed:
                wait(maxSpeed)
            else:
                wait(time)
            time *= speed 

    def refresh(self):
        self.fillBattleLogWithNewlines()
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.radios)

    def fillBattleLogWithNewlines(self):
        self.battleLog = wrap(self.battleLog, limit=self.totalWidth-self.actionsWidth-self.statsWidth)
        slicedBattleLog = self.battleLog.split('\n') # list of rows of the battlelog
        while True:
            if len(slicedBattleLog) < self.maxHeightOfBattleLogWindow: 
                slicedBattleLog.append('\n') 
            else:
                break
        self.battleLog = '\n'.join(slicedBattleLog)

    # def suspense(self): # doesnt work because ui updates on run method, not during other methods
    #     for i in range(3):
    #         wait(.5)
    #         self.battleLog += '.'
    #         self.refresh()

    def makeFormattedText(self, text, color='#ffffff'):
        return FormattedText([
            (color, str(text)) 
        ])

    # returns new root container (updates text and stuff)
    def getRootContainer(self):
        height = self.maxHeightOfBattleLogWindow
        enemyName = self.makeFormattedText(self.enemy.name) 
        battleLogTitle = FormattedText([
            ('#ffffff', "Battle Log") 
        ])
        actionsTitle = FormattedText([
            ('#ffffff', "Actions") 
        ])
        statsTitle = FormattedText([
            ('#ffffff', "Stats") 
        ])
        root_container = HSplit([
            VSplit([
                Dialog( # actions
                    title=actionsTitle,
                    body=HSplit([
                        self.radios,
                    ], height= height),
                    width=self.actionsWidth
                ), # battlelog 
                Dialog(
                    title = battleLogTitle,
                    body=Label(self.battleLog),
                    width=self.totalWidth-self.actionsWidth - self.statsWidth
                ),
                Dialog( # stats
                    title = statsTitle,
                    body=Label(getStats(self.player)),
                    width=self.statsWidth ,
                ),
            ], padding=0, width = self.actionsWidth, height=height+2 ),
            # health bars #
            VSplit([ 
                Frame(
                    body=self.playerHPBar,
                    title=self.playerName,
                    width=int(self.totalWidth/2)
                ),
                Frame(
                    body=self.enemyHPBar,
                    title=enemyName,
                    width=int(self.totalWidth/2)
                ), 
            ], padding=0, width = self.totalWidth)
        ])
        return root_container

    def run(self):
        self.application.run()

    def done(self, result='?'):
        self.result = result
        if self.result != 'inventory':
            self.song.stopSound()
        get_app().exit(result=self.result)
 
# STILL TODO
# fix color of battlelog
# description of selection text
