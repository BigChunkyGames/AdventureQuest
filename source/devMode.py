def devMode(player):
    player.aspect['name'] = "name"
    player.aspect['gender'] = "boi"
    player.aspect['heshe'], player.aspect['HeShe'], player.aspect['hisher'] = "he", "He", "his"
    player.aspect['occ'], player.aspect['viverb'], player.aspect['skill1'], player.aspect['skill2'] = "fireman", "stab", "sewing", "rubiks cube solving"
    player.aspect['town'], player.aspect['hills'] = "Swagsburgh", "Peak's Hills"
    player.aspect['adj1'], player.aspect['adj2'], player.aspect['adj3'], player.aspect['adj4'], player.aspect['adj5'] = "cool", "neato", "sick nasty", "wiggity wiggity whack", "excellent"

    #change some more values
    player.maxhp = 9999999
    player.hp = 9999999
    player.dogecoin = 8000
    player.devmode = True

    

    # teleport player - make sure to import that place
    # from places.maintown import *
    # maintown(player)
    # teleporting disabled - instead just modify game.py and change what debug mode skips

    return