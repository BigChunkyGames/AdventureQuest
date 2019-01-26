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
from source.customBase import RadioList2 
#from pygments.lexers.html import HtmlLexer
from prompt_toolkit.layout.margins import ScrollbarMargin, NumberedMargin
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.formatted_text import FormattedText

from source.lists import getRandomAttackVerb
from source.utils import wait, wrap, log
import random

class ShopUI():

    def __init__(self, player, nameOfShop, shopInventory, shopKeeperAsciiArt=None, customCurrency=None):
        '''shopInventory is a list of items'''
        self.player = player
        self.name = nameOfShop
        self.shopInventory = shopInventory
        self.shopKeeperAsciiArt = shopKeeperAsciiArt
        if self.shopKeeperAsciiArt == None:
            self.shopKeeperAsciiArt ='''
     _\|/^
      (_oo     what can i get for ya
       |     
      /|\\
       |
       LL
            '''
          
        self.playerClans = ' '.join(self.player.clantags)
        if len(self.player.clantags) > 0 : 
            self.playerName = FormattedText([
                ('#ffffff', player.aspect['name']),
                ('', ' '),
                ('#cc00cc', self.playerClans, "utf-8"),
            ]) 
        else: 
            self.playerClans =  self.playerName = FormattedText([
                ('#ffffff', player.aspect['name']),
            ]) 
        if customCurrency == None: self.currency = "dollars"
        else: self.currency = customCurrency
        self.result = None

        self.buySellRadiosRows = []
        self.listOfItems = []
        self.populateBuySellRadios() # declares self.buySellRadios
        self.currentRadios = self.buySellRadios
        self.rightWindowDescription = self.buySellRadios.description # description is whataver is in the description box on the right
        self.requestingConfirmation = False
        self.playerIs = "at buy/sell menu"
        
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
                self.getShopContainer(),
                focused_element=self.buySellRadios,
            ),
            key_bindings=self.bindings,
            style=self.style,
            mouse_support=True,
            full_screen=True,
            )

    def handleEscape(self, event):
        self.requestingConfirmation = False
        if self.currentRadios == self.buySellRadios:
            self.done()
        else: # return to main page
            self.playerIs = "at buy/sell menu"
            self.populateBuySellRadios()
            self.currentRadios = self.buySellRadios
            # self.description = self.buySellRadios.description
            self.refresh()

    def handleEnter(self, event):
        if self.requestingConfirmation:
            self.requestingConfirmation = False
            if self.playerIs == "buying":
                self.buy()
                self.listOfItems = self.shopInventory
            elif self.playerIs == "selling":
                self.sell()
                self.listOfItems = self.player.getAllInventoryItemsAsObjectList()
            if self.handleEmptiness(self.listOfItems): return
            self.makeListCurrentRadios(self.listOfItems) 
            # TODO sound music, sound effect of eating a consumable
            return

        elif self.currentRadios == self.buySellRadios: # if on main page
            if self.currentRadios._selected_index == 0: # BUY, show shops inventory
                self.playerIs = "buying"
                self.listOfItems = self.shopInventory
            elif self.currentRadios._selected_index == 1: # SELL, show player inventory
                self.playerIs = "selling"
                self.listOfItems = self.player.getAllInventoryItemsAsObjectList()
            else:log("what the fuck")
            if self.handleEmptiness(self.listOfItems): return
            self.makeListCurrentRadios(self.listOfItems) 
        elif self.currentRadios == self.selectedRadios: # if not on main page
            self.requestingConfirmation = True
            price = self.getCurrentlySelectedItem().sellValue
            if price == 1 and self.currency.endswith('s'): currency = 'dollar'
            else: currency = self.currency
            nameOfItem = self.getCurrentlySelectedItem().name
            if self.playerIs == "buying":
                self.refresh(setDescription="Purchase " + str(nameOfItem) +" for " + str(price) + " " + currency + "?")
            elif self.playerIs == "selling":
                self.refresh(setDescription="Sell " + str(nameOfItem) +" for " + str(price) + " " + currency + "?")

    def buy(self):
        item = self.getCurrentlySelectedItem()
        if item.sellValue > self.player.money:
            self.refresh(setDescription="You can't afford that.")
        else:
            self.player.money = self.player.money - item.sellValue # subtract funds
            self.player.money = round(self.player.money, 2) # round to cents
            item.sellValue = item.sellValue /2 # half the worth of the item after buying
            self.shopInventory.remove(item)
            self.player.addToInventory(item, printAboutIt=False)

    def sell(self):
        item = self.getCurrentlySelectedItem()
        if item.equipped == True: self.player.unequip(item=item)
        self.player.inventory.remove(item) # remove item from player inventory
        self.player.money = self.player.money + item.sellValue # get paid
        self.player.money = round(self.player.money, 2) # round just in case
        self.shopInventory.append(item) # give item to shop owner

    def getCurrentlySelectedItem(self):
        return self.listOfItems[self.currentRadios._selected_index]

    def handleEmptiness(self, lis):
        if len(self.listOfItems) == 0:
            self.currentRadios = self.buySellRadios
            if self.playerIs == "buying":
                self.playerIs = "at buy/sell menu"
                self.refresh(setDescription="Sold out!")
            elif self.playerIs == "selling":
                self.playerIs = "at buy/sell menu"
                self.refresh(setDescription="You've got nothing left!")
            return True

    def makeListCurrentRadios(self, lisp, selectedIndex=0):
        lisp = self.refreshItemDescriptions(lisp)
        self.listOfItemsTupled = self.tuplify(lisp)
        self.selectedRadios = RadioList2(
            values=self.listOfItemsTupled,
            app = self)    
        self.selectedRadios._selected_index = selectedIndex
        self.currentRadios = self.selectedRadios 
        # self.description = self.currentRadios.values[selectedIndex]
        self.refresh()

    def refreshItemDescriptions(self, lis):
        for i in lis:
            i.description = i.buildItemDescriptionString()
        return lis

    def tuplify(self, listt):
        if len(listt) == 0:
            return [] # should never see this
        newlist=[]
        for i in range(len(listt)):
            l = []
            l.append(self.unicodify(listt[i].description))
            l.append(self.unicodify(self.colorBasedOnRarity(listt[i], useGetName=True))) # colors
            newlist.append( tuple(l) )
        return newlist

    def makeFormattedText(self, text, color='#ffffff'):
        return FormattedText([
            (color, str(text) )# this shit is shit
        ])
        
    def colorBasedOnRarity(self, item, useGetName=False): # also colors consumables, returns name
        if useGetName: name = item.getName()
        else: name = item.name
        if item.type == 'consumable':
            color = '#99ff66'
        elif item.rarity == "None" or item.rarity == None or item.rarity == "common":
            color = '#ffffff'
        elif item.rarity == "rare":
            color = '#0066ff' # blue
        elif item.rarity == 'epic':
            color = '#cc3300' # orange
        elif item.rarity == 'legendary':
            color = '#9900cc'
        return self.makeFormattedText(name, color=color)

    def refresh(self, setDescription=False):
        index = self.currentRadios._selected_index
        if setDescription:
            self.rightWindowDescription = setDescription
        else:
            self.rightWindowDescription = self.currentRadios.values[index][0]
        
        self.application.layout=Layout(
            self.getShopContainer(),
            focused_element=self.currentRadios)
            
        
    def populateBuySellRadios(self):
        self.buySellRadiosRows = []
        self.populateBuySellRadiosHelper('Buy')
        self.populateBuySellRadiosHelper('Sell')
        self.buySellRadios = RadioList2(
            values=self.buySellRadiosRows,
            app = self)

    def populateBuySellRadiosHelper(self, category):
        desc = self.shopKeeperAsciiArt
        tup = []
        tup.append(desc)
        tup.append(category.capitalize())
        self.buySellRadiosRows.append( tuple(tup) )

    def unicodify(self, text):
        if isinstance(text, str):
            return str(text)
        else:
            return text

    def getShopContainer(self):
        width = 60
        smallerWidth = 40
        height = 10
        if self.playerIs == "at buy/sell menu":
            leftWindowTitle = ""
            rightWindowTitle = self.makeFormattedText(self.name)
            desc = self.rightWindowDescription
        elif self.playerIs == "buying":
            leftWindowTitle = self.makeFormattedText(self.name)
            rightWindowTitle = self.colorBasedOnRarity(self.getCurrentlySelectedItem())
            desc = wrap(self.rightWindowDescription, width-2)
        elif self.playerIs == "selling":
            leftWindowTitle = self.makeFormattedText(self.player.aspect["name"])
            rightWindowTitle = self.colorBasedOnRarity(self.getCurrentlySelectedItem())
            desc = wrap(self.rightWindowDescription, width-2)
        root_container = VSplit([
            HSplit([
                Dialog(
                    title=leftWindowTitle,
                    body=HSplit([
                        self.currentRadios,
                    ], )
                ),
            ], padding=0, width = smallerWidth, ),
            HSplit([
                Dialog(
                    title = rightWindowTitle,
                    body=Label(desc),
                ),
            ], padding=0, width = width,),
        ])
        return root_container 

    def run(self):
        self.application.run()

    def done(self):
        self.result = "hit escape"
        get_app().exit(result="hit escape")
 
# TODO:
# colors