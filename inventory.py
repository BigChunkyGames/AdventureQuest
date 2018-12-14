from utils import *

class Inventory:

    def __init__(self, player):
        self.items = []
        self.player = player
        self.THE_UI = [
"+-------------------------------------------------------------------+" "\n"
"| ", player.getAspect("name"), "                                                         |" "\n"
"|XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX|" "\n"
"|                                              X                    |" "\n"
"|                                              X  hp    xx / xx     |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"|                                              X                    |" "\n"
"+-------------------------------------------------------------------+" 
        ]

    def getItemNames(self):
        for items in self.items:
            pass #TODO

    def open(self):
        for s in self.THE_UI:
            print(s),
        raw_input("press enter to leave ").lower().strip()


#i = Inventory("1")
#i.open()
