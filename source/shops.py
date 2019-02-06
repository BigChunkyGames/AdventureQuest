from source.shopUI import ShopUI
from source.item import Item



class Shop():
    def __init__(self, player, nameOfShop, preset=True, openNow=False, currency='Money'):
        '''
        preset will create a shop from a list of premade shops
        '''
        self.player = player
        self.shopName = nameOfShop
        self.shopAsciiArt = None
        self.visitedOnDay = player.day
        self.currency = currency
        self.originalInventory = []
        self.currentInventory = []
        self.player.shops.append(self) # add to list of shops
        self.UI = self.setUI()
        if openNow: self.UI.run()

    def setUI(self):
        return ShopUI(self.player, self.shopName, self.currentInventory, shopKeeperAsciiArt=self.shopAsciiArt, customCurrency=self.currency )

    def openUI(self):
        self.UI = self.setUI() # keep updated
        return self.UI.run()

    def restock(self):
        self.currentInventory = self.originalInventory
        
def openIfExists(player, name):
    for s in player.shops:
        if s.name==name:
            return s.openUI()
    return False
