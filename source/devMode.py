from source.item import generateRandomArmourOrWeapon, Item


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
    player.level = 10

    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')
    player.clantags.append('[test]')

    i = generateRandomArmourOrWeapon(player)
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, rarity='common')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, rarity='rare')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, rarity='epic')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, rarity='legendary')
    i = generateRandomArmourOrWeapon(player, _type='weapon', rarity='common')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, _type='weapon', rarity='rare')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, _type='weapon', rarity='epic')
    player.inventory.append(i)
    i = generateRandomArmourOrWeapon(player, _type='weapon', rarity='legendary')
    player.inventory.append(i)
    player.getInitialItems()
    
    i1 = Item(player, 'Tea', customDescription="Andy Worm Poet gave you this cup of tea. It's still warm and smells delicious.", _type='consumable', sellValue=5)
    i1.customActivationFunction = lambda:i1.consume(heal=3)
    player.inventory.append(i1)

    



    return