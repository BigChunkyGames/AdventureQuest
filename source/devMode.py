from source.item import generateRandomWeapon


def devMode(player):
    player.aspect['name'] = "devMode"
    player.aspect['gender'] = "boi"
    player.aspect['heshe'], player.aspect['HeShe'], player.aspect['hisher'] = "he", "He", "his"
    player.aspect['hand'] = 'right'
    player.aspect['occ'], player.aspect['viverb'], player.aspect['skill1'], player.aspect['skill2'] = "fireman", "stab", "sewing", "rubiks cube solving"
    player.aspect['town'], player.aspect['land'] = "Swagsburgh", "Skyrim"
    player.aspect['adj1'], player.aspect['adj2'], player.aspect['adj3'], player.aspect['adj4'], player.aspect['adj5'] = "cool", "neato", "sick nasty", "wiggity wiggity whack", "excellent"

    #change some more values
    player.maxhp = 9999999
    player.hp = 10
    player.money = 8000
    player.devmode = True
    
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')

    player.getInitialItems()
    player.inventory.append(generateRandomWeapon(player))
    player.inventory.append(generateRandomWeapon(player))
    player.inventory.append(generateRandomWeapon(player))
    #print player.getAllInventoryItems()

    



    return