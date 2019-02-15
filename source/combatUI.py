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
from source.utils import wait, wrap, Sound
from source.inventoryUI import InventoryUI

import re
import random

class CombatUI():

    def __init__(self, player, enemy, song='worry 1.mp3'):
        self.song = Sound(song, loop=-1)
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
        if self.player.equippedWeapon.name != None: self.weaponName = self.player.equippedWeapon.name
        else: self.weaponName = "Bare Hands"

        self.enemy = enemy

        self.playerGoesNext = True # by default, enemy always gets first strike
        self.playerJustDodged = False
        self.battleLog = '\n\n\n\n\n\n\n'
        self.maxHeightOfBattleLogWindow = 8
        self.width = 90
        self.smallWidth = 30

        self.selectedIndexText = ''
        self.result = None
        self.escapeChancePercent = 20

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
            weaponName = self.weaponName)
        
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
            self.enemyTurn()
            return
        self.playerGoesNext = False

        # handle choice
        self.radios.current_value = self.radios.values[self.radios._selected_index][0] # show change to selection with *
        choice = self.radios.current_value
        s = ''
        if choice == "Attack":
            s +=  "You tried to attack... "
            damage = self.player.getTotalAttackPower()
            s += " and did " 
            s += str(damage)
            s += " damage!" # TODO color
            self.enemy.hp = self.enemy.hp - damage
            if self.enemy.hp < 0:
                self.enemy.hp = 0
            self.setHealthProgressBar(self.enemyHPBar, self.toPercent(self.enemy.hp, self.enemy.maxhp))
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
            
        if self.enemy.hp == 0: # check if he dead
            self.done("win")
            return
        self.enemyTurn(s)
    
    def tryToEscape(self, event=None):
        s = ''
        s += "You tried to run..." 
        if self.escapeChancePercent> random.randint(0,100): # chance to escape is always 20% i guess
            s += " and escaped the combat!" # #TODO advanced combat: isnt ever visible
            self.done("escaped")
        else:
            s += " but failed to escape!"
        return s

    def enemyTurn(self, textOfPlayerTurn=False):
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
            self.player.hp = self.player.hp - damage
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

    def refresh(self):
        self.fillBattleLogWithNewlines()
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.radios)

    def fillBattleLogWithNewlines(self):
        self.battleLog = wrap(self.battleLog, limit=self.width-self.smallWidth)
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
        t = TextArea(
            scrollbar=False,
            line_numbers=False,
            wrap_lines=True,
            dont_extend_height=True,
            dont_extend_width=True,
            focusable=True,
            focus_on_click=True,
            read_only=False,
            text=self.battleLog,  
            style='bg:#000000',
            height=10,
            )
        root_container = HSplit([
            VSplit([
                Dialog(
                    title=actionsTitle,
                    body=HSplit([
                        self.radios,
                    ], height= height),
                    width=self.smallWidth
                ),
                Dialog(
                    title = battleLogTitle,
                    body=Label(self.battleLog),
                    width=self.width-self.smallWidth
                ),
            ], padding=0, width = self.smallWidth, height=height+2 ),
            VSplit([
                Frame(
                    body=self.playerHPBar,
                    title=self.playerName,
                    width=int(self.width/2)
                ),
                Frame(
                    body=self.enemyHPBar,
                    title=enemyName,
                    width=int(self.width/2)
                ), 
            ], padding=0, width = self.width, height=height)
        ])
        return root_container

    def run(self):
        self.application.run()

    def done(self, result='?'):
        self.result = result
        if self.result != 'inventory':
            self.song.stopSound()
        get_app().exit(result=result)
 
# STILL TODO
# fix scrolling issue in battelog
# fix color of battlelog
# description of selection text
# what the hell is this dumb line at the bottom of the battlelog
