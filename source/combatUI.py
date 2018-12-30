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
from utilities.customBase import RadioList, ProgressBar # had to make some changes
from pygments.lexers.html import HtmlLexer
from prompt_toolkit.layout.margins import ScrollbarMargin, NumberedMargin
from prompt_toolkit import print_formatted_text, HTML

from lists import getRandomAttackVerb
import random

class CombatUI():

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

        self.playerGoesNext = False # by default, enemy always gets first strike
        self.playerJustDodged = False
        self.battleLog = ''
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
                # inventory - opens the inventory manager (instead of item)
            ]
        )
        
        self.bindings = KeyBindings()
        self.bindings.add('right' )(focus_next)
        self.bindings.add('tab' )(focus_next)
        self.bindings.add('s-tab')(focus_previous)
        self.bindings.add('left')(focus_previous)
        self.bindings.add('c-m')(self.handleEnter)
        # TODO escape key tries to flee
        # TODO: make secret easter egg key bindings # self.bindings.add('a', 'a')(self.test)  

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
        if self.enemy.hp == 0: # check if he dead
            self.result = "win"
            get_app().exit(result="win")
            return
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
            self.battleLog += "You tried to run..." 
            if 20 > random.randint(0,100): # chance to escape is always 20% i guess
                self.battleLog += " and escaped the combat!"
                self.result = "escaped"
                get_app().exit(result="escaped")
                return
            else:
                self.battleLog += " but failed to escape!\n"
        else:
            self.battleLog += "How did you do that!?"
        self.refresh()

    def enemyTurn(self):
        # for now, always try to attack TODO
        self.playerGoesNext = True
        self.battleLog += self.enemy.name + " tried to " 
        attack = getRandomAttackVerb() 
        if attack[-1] == "*": # if attack finishes the sentence
            self.battleLog += attack[:-1] # remove *
        else :
            self.battleLog += str(attack)
            self.battleLog += " you... "
            
        # calculate hit chance and handle
        dodgeModifier = 0
        if self.playerJustDodged == True:
            dodgeModifier = 30
            self.playerJustDodged = False
        if self.enemy.missChancePercent + dodgeModifier > random.randint(0,100):
            # missed
            if not attack[-1] == "*": self.battleLog += " but missed!\n"
            else: self.battleLog += " It missed!\n"
        else:
            # hit
            damage = self.enemy.attack
            if not attack[-1] == "*": self.battleLog += " and dealt " + str(damage) + " damage!\n"
            else: self.battleLog += " It dealt " + str(damage) + " damage!\n"
            self.player.hp = self.player.hp - damage
            if self.player.hp < 0:
                self.player.hp = 0
            self.setHealthProgressBar(self.playerHPBar, self.toPercent(self.player.hp, self.player.maxhp))
            if self.player.hp == 0: #dead
                self.result = "lose"
                get_app().exit(result="lose")
                return
        self.refresh()
        
    def refresh(self):
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.radios)

    # returns new root container (updates text and stuff)
    def getRootContainer(self):
        root_container = VSplit([
            HSplit([
                Dialog(
                    title='Actions',
                    body=HSplit([
                        self.radios,
                        Label(
                            text="this text changes depending on what action is highlighted #TODO ", 
                            dont_extend_height=False)])),
                Frame(
                    body=self.playerHPBar,
                    title='Health'), # TODO get name of player
            ], padding=1),
            HSplit([
                Dialog(
                    title = 'Battle Log',
                    body=TextArea(
                        scrollbar=True,
                        line_numbers=False,
                        wrap_lines=True,
                        dont_extend_height=False,
                        dont_extend_width=False,
                        focusable=True,
                        focus_on_click=True,
                        read_only=False,
                        text=self.battleLog,  
                        ),
                    ),
                Frame(
                    body=self.enemyHPBar,
                    title='Progress bar'), # TODO get name of enemy
                
            ], padding=1)
        ])
        return root_container

    style = Style.from_dict({
        'textarea':           'bg:#66ff99',

        'dialog':             'bg:#88ff88',
        'dialog frame-label': 'bg:#ffffff #000000',
        'dialog.body':        'bg:#000000 #ffcccc', #background color, text color
        'dialog shadow':      'bg:#00aa00',
    })

    def run(self):
        self.application.run()

# if __name__ == '__main__': # i think this means, if this is the file that was run, do this
#     from player import *
#     from enemy import *
#     b = CombatUI(Player(),Enemy(Player(), "forest"))
#     b.run()   


# STILL TODO
# fix scrolling issue in battelog
# fix color of battlelog
# description of selection text
# hpbar names, might just skip
