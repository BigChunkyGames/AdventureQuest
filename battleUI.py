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
from prompt_toolkit.widgets import TextArea, Label, Frame, Box, Checkbox, Dialog, Button, MenuContainer, MenuItem, ProgressBar
from customBase import RadioList # had to make some changes
from pygments.lexers.html import HtmlLexer

class BattleUI():

    def __init__(self):
        self.playerHPBar = ProgressBar()
        self.setHealthProgressBar(self.playerHPBar, 100) #TODO make actual current health
        self.enemyHPBar = ProgressBar()
        self.setHealthProgressBar(self.enemyHPBar, 100) 

        self.battleLog = 'jiggles'

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
            full_screen=True)


    # TODO call when escape successful or enemy dies
    def do_exit(self):
        get_app().exit(result=False)

    # call this function to change the value a progress bar (prog) to a percent
    def setHealthProgressBar(self,prog, percent):
        prog._percentage = percent
        prog.container = FloatContainer(
            content=Window(height=1),
            floats=[
                Float(left=0, top=0, right=0, bottom=0, content=VSplit([
                    Window(style='bg:#00cc00', # health, green
                            width=lambda: D(weight=int(prog._percentage))),
                    Window(style='bg:#ff0000', # damage, red
                            width=lambda: D(weight=int(100 - prog._percentage))),
                ])),
            ])

    # returns new root container (updates text and stuff)
    def getRootContainer(self):
        root_container = VSplit([
            HSplit([
                Dialog(
                    title='Actions',
                    body=HSplit([
                        self.radios,
                        Label(
                            text="text", 
                            dont_extend_height=False)])),
                Frame(
                    body=self.playerHPBar,
                    title='Health'), # TODO get name of player
            ], padding=1),
            HSplit([
                Dialog(
                    title = 'Battle Log',
                    body=Label(
                        text=self.battleLog, 
                        dont_extend_height=False)),
                Frame(
                    body=self.enemyHPBar,
                    title='Progress bar'), # TODO get name of enemy
            ], padding=1),
        ])
        return root_container

    def handleEnter(self, event):
        self.radios.current_value = self.radios.values[self.radios._selected_index][0] # show change to selection with *
        choice = self.radios.current_value
        #TODO do something depending on current value
        if choice == "Attack":
            self.battleLog += "\nYou tried to attack..."
        elif choice == "Dodge":
            self.battleLog += "\nYou tried to dodge..."
        elif choice == "Item":
            self.battleLog += "" #TODO item selection
        elif choice == "Run":
            self.battleLog += "\nYou tried to run..." # TODO run
        else:
            pass
        self.refresh()
        
    def refresh(self):
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.radios)

    style = Style.from_dict({
        'window.border': '#888888',
        'shadow': 'bg:#222222',

        'menu-bar': 'bg:#aaaaaa #888888',
        'menu-bar.selected-item': 'bg:#ffffff #000000',
        'menu': 'bg:#888888 #ffffff',
        'menu.border': '#aaaaaa',
        'window.border shadow': '#444444',

        'focused  button': 'bg:#880000 #ffffff noinherit',

        'dialog':             'bg:#88ff88',
        'dialog frame-label': 'bg:#ffffff #000000',
        'dialog.body':        'bg:#000000 #ffcccc', #background color, text color
        'dialog shadow':      'bg:#00aa00',
    })

    def run(self):
        self.application.run()

if __name__ == '__main__': # i think this means, if this is the file that was run, do this
        b = BattleUI()
        b.run()   