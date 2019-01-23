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
from source.utils import wait
import re
import random

class CombatUI():

    def __init__(self, player, enemy):
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

        self.playerGoesNext = False # by default, enemy always gets first strike
        self.playerJustDodged = False
        self.battleLog = ''
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
                # inventory - opens the inventory manager (instead of item)
            ]
        )

        self.maxHeightOfBattleLogWindow = 11 # FIXME find a way to fit text inside battle log
        
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

        self.enemyTurn() # enemy goes first

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
        #TODO do something depending on current value
        if choice == "Attack":
            self.battleLog += "You tried to attack..."
            damage = 2 #TODO
            self.battleLog += " and did " 
            self.battleLog += str(damage)
            self.battleLog += " damage!\n" # TODO color
            self.enemy.hp = self.enemy.hp - damage
            if self.enemy.hp < 0:
                self.enemy.hp = 0
            self.setHealthProgressBar(self.enemyHPBar, self.toPercent(self.enemy.hp, self.enemy.maxhp))
        elif choice == "Dodge":
            self.battleLog += "You tried to dodge...\n"
            # dodging increases chance for enemy to miss by 30%
            self.playerJustDodged = True
        elif choice == "Item":
            self.battleLog += "" #TODO item selection
        elif choice == "Run":
            self.tryToEscape()
            self.refresh()
            return
        else:
            self.battleLog += "How did you do that!?"
            
        if self.enemy.hp == 0: # check if he dead
            self.result = "win"
            get_app().exit(result="win")
            return
        self.refresh()
        self.enemyTurn()
    
    def tryToEscape(self, event=None):
        self.battleLog += "You tried to run..." 
        if self.escapeChancePercent> random.randint(0,100): # chance to escape is always 20% i guess
            self.battleLog += " and escaped the combat!"
            self.result = "escaped"
            get_app().exit(result="escaped")
            return
        else:
            self.battleLog += " but failed to escape!\n"
            self.refresh()
            self.enemyTurn()

    def enemyTurn(self):
        # for now, always try to attack TODO
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
        dodgeModifier = 0
        if self.playerJustDodged == True:
            dodgeModifier = 30
            self.playerJustDodged = False
        if self.enemy.missChancePercent + dodgeModifier > random.randint(0,100):
            # missed
            if not attack[-1] == "*": s += " but missed!\n"
            else: s += " But missed!\n"
        else:
            # hit
            damage = self.enemy.attack
            if not attack[-1] == "*": s += " and dealt " + str(damage) + " damage!\n"
            else: 
                s += " It dealt " + str(damage) + " damage!\n"
            self.player.hp = self.player.hp - damage
            if self.player.hp < 0:
                self.player.hp = 0
            self.setHealthProgressBar(self.playerHPBar, self.toPercent(self.player.hp, self.player.maxhp))
            if self.player.hp == 0: #dead
                self.result = "lose"
                get_app().exit(result="lose")
                return
        self.battleLog += s
        self.refresh()

    def refresh(self):
        #self.application.style=self.style
        #self.battleLog += "changing color to " + str(self.currentStyle)
        slicedBattleLog = self.battleLog.split('\n')
        if len(slicedBattleLog) >= self.maxHeightOfBattleLogWindow: # dont let battlelog get too long
            self.battleLog = self.battleLog[self.battleLog.index('\n')+1:]
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.radios)

    def makeFormattedText(self, text, color='#ffffff'):
        return FormattedText([
            (color, str(text)) 
        ])

    # returns new root container (updates text and stuff)
    def getRootContainer(self):
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
        root_container = VSplit([
            HSplit([
                Dialog(
                    title=actionsTitle,
                    body=HSplit([
                        self.radios,
                    ], height= 10)
                ),
                Frame(
                    body=self.playerHPBar,
                    title=self.playerName,
                ),
            ], padding=0, width = 100 ),
            HSplit([
                Dialog(
                    title = battleLogTitle,
                    body=t,
                ),
                Frame(
                    body=self.enemyHPBar,
                    title=enemyName
                ), 
            ], padding=0, width = 100)
        ])
        return root_container

    def run(self):
        self.application.run()
 
# STILL TODO
# fix scrolling issue in battelog
# fix color of battlelog
# description of selection text
# what the hell is this dumb line at the bottom of the battlelog
