from source.item import generateRandomArmourOrWeapon, Item, Consumable,generateRandomConsumable


def devMode(player):

    player.aspect['name'] = "Jim Johnson"
    player.aspect['hand'] = 'right'
    player.aspect['town'], player.aspect['land'] = "Maintown", "Flat Earth"
    player.aspect['age'] = 21

    #change some more values
    player.money = 8000
    player.maxhp = 3000
    player.hp = 3000
    player.devmode = True



    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)
    player.levelUp(printAboutIt=False, sound=False)

    player.clantags.append('[test1]')
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
    
    player.inventory.append(Item(player, 'Tea', customDescription="Andy Worm Poet gave you this cup of tea. It's still warm and smells delicious.", _type='consumable', sellValue=5, consumable=Consumable(player, heal=3)))

    for i in range(50):
        player.inventory.append(generateRandomConsumable(player))












    return