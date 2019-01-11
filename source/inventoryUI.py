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
from utilities.customBase import RadioList2 
#from pygments.lexers.html import HtmlLexer
from prompt_toolkit.layout.margins import ScrollbarMargin, NumberedMargin
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText

from lists import getRandomAttackVerb
from utils import wait
import re
import random

class InventoryUI():

    def __init__(self, player):
        self.player = player
        self.playerClans = ' '.join(self.player.clantags)
        if len(self.player.clantags) > 0 : 
            self.playerName = FormattedText([
                ('#ffffff', unicode(player.aspect['name'], "utf-8")),
                ('', ' '),
                ('#cc00cc', self.playerClans, "utf-8"),
            ]) 
        else: 
            self.playerClans =  self.playerName = FormattedText([
                ('#ffffff', unicode(player.aspect['name'], "utf-8")),
            ]) 
        self.result = None

        self.radiosCategoriesContents = []
        t = self.getItemText('weapon')
        if not t == '': 
            tup = []
            tup.append(t)
            tup.append('Weapons')
            self.radiosCategoriesContents.append( tuple(tup) )

        t = self.getItemText('armour')
        if not t == '': 
            tup = []
            tup.append(t)
            tup.append('Armour')
            self.radiosCategoriesContents.append( tuple(tup) )

        t = self.getItemText('consumable')
        if not t == '': 
            tup = []
            tup.append(t)
            tup.append('Consumable')
            self.radiosCategoriesContents.append( tuple(tup) )
            
        t = self.getItemText('quest')
        if not t == '': 
            tup = []
            tup.append(t)
            tup.append('Quest')
            self.radiosCategoriesContents.append( tuple(tup) )

        self.radiosCategories = RadioList2(
            values=self.radiosCategoriesContents,
            app = self)

        self.currentRadios = self.radiosCategories
        self.description = self.radiosCategories.description
        
        self.bindings = KeyBindings()
        self.bindings.add('right' )(focus_next)
        self.bindings.add('tab' )(focus_next)
        self.bindings.add('s-tab')(focus_previous)
        self.bindings.add('left')(focus_previous)
        self.bindings.add('c-m')(self.handleEnter)
        self.bindings.add('escape')(self.handleEscape)

        self.style = Style.from_dict({
            'dialog.body':        'bg:#000000 #ffcccc', #background color, text color
        })

        self.application = Application(
            layout=Layout(
                self.getRootContainer(),
                focused_element=self.radiosCategories,
            ),
            key_bindings=self.bindings,
            style=self.style,
            mouse_support=True,
            full_screen=True,
            )

    def getItemText(self, _type):
        return self.unicodify(self.player.getAllInventoryItemsAsString(_type=_type))

    def handleEscape(self, event):
        if self.currentRadios == self.radiosCategories:
            self.done()
        else: # return to main page
            self.currentRadios = self.radiosCategories
            self.description = self.radiosCategories.description
            self.refresh()

    def handleEnter(self, event):
        if self.currentRadios == self.radiosCategories: # if on main page
            if self.radiosCategories._selected_index == 0:
                radiosList = self.player.getAllInventoryItemsAsObjectList(_type='weapon')
            if self.radiosCategories._selected_index == 1:
                radiosList = self.player.getAllInventoryItemsAsObjectList(_type='armour')
            if self.radiosCategories._selected_index == 2:
                radiosList = self.player.getAllInventoryItemsAsObjectList(_type='consumable')
            if self.radiosCategories._selected_index == 3:
                radiosList = self.player.getAllInventoryItemsAsObjectList(_type='quest')
            # radiosList = self.showEquipped(radiosList)
            radiosList = self.tuplify(radiosList)
            self.selectedRadios = RadioList2(
                values=radiosList,
                app = self)       
            self.currentRadios = self.selectedRadios  
        elif self.currentRadios == self.selectedRadios:
            pass
        self.refresh()

    # def showEquipped(self, l):
    #     ''' adds *'s to a weapon's name if it is equipped'''
    #     for i in range(len(l)):
    #         if l[i] == self.player.equippedWeapon or l[i] == self.player.equippedArmourChest or l[i] == self.player.equippedArmourHead or l[i] == self.player.equippedArmourLegs or l[i] == self.player.equippedArmourFeet:
    #             l[i].name = '*' + l[i].name + '*'
    #     return l

    def tuplify(self, listt):
        if len(listt) == 0:
            return [('Nothing here!', 'empty')]
        newlist=[]
        for i in range(len(listt)):
            l = []
            l.append(self.unicodify(listt[i].description))
            l.append(self.unicodify(listt[i].name))
            newlist.append( tuple(l) )
        return newlist

    def done(self):
        self.result = "hit escape"
        get_app().exit(result="")

    def refresh(self):
        self.description = self.currentRadios.description
        self.application.layout=Layout(
            self.getRootContainer(),
            focused_element=self.currentRadios)
        
        

    def makeFormattedText(self, text, color='#ffffff'):
        return FormattedText([
            (color, unicode(text, "utf-8")) # this shit is shit
        ])

    def unicodify(self, text):
        return unicode(text,"utf-8")

    # returns new root container (updates text and stuff)
    def getRootContainer(self):
        descriptionText = FormattedText([
            ('#ffffff', "Description") # this shit is shit
        ])
        actionsTitle = FormattedText([
            ('#ffffff', "Inventory") # this shit is shit
        ])
        root_container = VSplit([
            HSplit([
                Dialog(
                    title=actionsTitle,
                    body=HSplit([
                        self.currentRadios,
                    ], height= 10)
                ),
            ], padding=0, width = 100 ),
            HSplit([
                Dialog(
                    title = descriptionText,
                    body=TextArea(
                        text=self.description, 
                        style='bg:#000000',
                        height=10,
                    ),
                ),
            ], padding=0, width = 100 ),
        ])
        return root_container 

    def run(self):
        self.application.run()
 

