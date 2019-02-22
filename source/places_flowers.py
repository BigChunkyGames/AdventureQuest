
from source.utils import *
from source.enemy import Enemy
from source.combat import Combat
from source.item import Item, Consumable
from source.places_wormHome import wormHome, tea

# this file and wormhome sort of go together

def flowers(player):
    if player.registerVisit("flowers")==1:
        while True:
            show("Daffodils, irises, daisies, larkspurs, dahlias, sunflowers, carnations, and amaryllis sprawl for miles around.")
            show("They are so densly arranged and neatly packed that they block your path.")
            show("There is no other way across the field.")
            show("There is only one way to get through the flowers.")
            print ("Attack the flowers?")
            if yesno(player):
                player.karma = player.karma - 1
                if not attackFlowers(player): #if escaped
                    continue # TODO combat advanced: disable escape and dodge
                else: break
            else:
                show("You decide to wait.")
                s = ''
                for i in range(30):
                    s +=". "
                printSlowly(s, secondsBetweenChars=.5, pause=0, skipable=False, quotes=False)
                print("Are you sure you don't want to attack the flowers?")
                if not yesno(player):
                    if not attackFlowers(player): #if escaped
                        continue
                    else: break
                else:
                    show("You continue waiting.")
                    printSlowly(s, secondsBetweenChars=.5, pause=0, skipable=False, quotes=False)
                    player.history.append("waited for flowers")
                    show("The flowers, appreciating your patience, slowly part, revealing a path.")
                    show("You continue to the end of the field.")
                    break
        show("You notice a little scrap of paper protruding from a tiny hole in the dirt.")
        print("Pick it up?")
        if yesno(player):
            word = "like"
            show("Scrawled on the old tattered paper is a poem written in extremely small handwriting. It is nearly impossible to read. You can just barely make out what it says...")
            print('')
            show('Song of a Worm', dots=False) # TODO italisize
            print('')
            show('My lonely home is a hole in the soil', dots=False)
            show("I've exhausted my thoughts", dots=False)
            show('And now gladly recoil.', dots=False)
            print('')
        else: 
            word = "read"
        shoe = player.equippedArmourFeet
        if shoe == None: shoe = "shoe"
        else: 
            shoe = shoe.name
        show("You hear a faint, angry squeaking coming from a hole near your "+shoe+".") 
        show("You bend down and investigate the noise...")
        show('Angry Worm Poet is angry that you didn\'t ' + word + ' his poem.')
        show('Fuming with artistic despair, he musters the strength to squeak:')
        printSlowly('"Nobody ever gets me!"', secondsBetweenChars=.03)
        printSlowly('"Nobody likes my poem!"', secondsBetweenChars=.03)
        printSlowly('"I can\'t take it anymore!"', secondsBetweenChars=.03)
        while(True):
            printc("@'Smash'@yellow@ him under your foot or @tell him that you really loved his poem@yellow@?" )
            x = getInput(player)
            if checkInput(x, "smash"):
                show('You prepare to stomp the pesky worm.')
                e = Enemy(player, "plains")
                e.name = "Angry Worm Poet"
                e.attack = 1
                e.hp = 3
                e.setListOfAttacks(["slime on your shoe...*"])
                c = Combat(player, alert=False, enemy=e)
                clear()
                if c.result == 'win':
                    player.karma = player.karma - 3
                    player.history.append("killed angry worm poet")

                    show("Angry Worm Poet is smashed into the dust and drops the deed to Worm Home. ")
                    description = "Tiny tattered legal document. It says:\nWhomst ever holds    this deed has rightful ownshership over 'Worm Home'."
                    i = Item(player, "Deed to 'Worm Home'", customDescription=description,      _type='Quest', )
                    player.history.append("owns worm home")
                    player.addToInventory(i) # FIXME inventory
                    print("Enter Worm Home?")
                    if yesno(player):
                        show("You open the tiny door to the worm's underground abode and walk inside.")
                        show("However small it looked from the outside, Worm Home is    surprisingly spacious.")
                        show("There are pictures hanging on the dirt walls of the entryway.")
                        show("The pictures is a family photo of Angry Worm Poet and his loving  parents.")
                        show("He was an even smaller wormling then.")
                        show("A happy wormling with joyfilled cherub cheeks.")
                        show("A family tree is knitted into a tapestry on the far wall above a  quaint table supporting a bouquet of freshly picked flowers.")
                        show('"Angry Worm Poet" is the last worm on the family tree.')
                        show("A freshly baked pie lays uneaten on the windowsill.")
                        show("There is a note next to the pie.")
                        show('"Here\'s your pie for the week, my little Angry Worm Poet.')
                        show("It's strawberry rhubarb, your favorite!")
                        show("I hope you think of me with every scrumptious bite.")
                        show("I'll have a new one for you next week.")
                        print("")
                        show("So, how are things with Beautiful Worm Girlfriend?")
                        show("Did you pop the question yet?")
                        show("She is just going to love Worm Grandmother's old wedding ring.")
                        show("You two were made for each other!")
                        show("I can't wait to see you and hear all about it.")
                        show("I've just been so lonely after your father died.")
                        show("If anything were to ever happen to you...")
                        show("You're all I have...")
                        show("We just won't think about that!")
                        print("")
                        show("Your loving mother,")
                        show('Loving Worm Mom "')
                        show("You return the note to the windowsill.")
                        print("Take the pie?")
                        if yesno(player): takeThePie(player)
                        return wormHome(player) 
                     
                    else: # dont enter worm home
                        show("You've had enough of this.")
                        return
                else: # didnt win combat
                    show("You rethink fighting the worm.")

            elif 'love' in x or 'like' in x or 'enjoy' in x:
                player.karma = player.karma + 1
                show("The worm stops and looks at you.")
                show("A single tear wells in his eye.")
                printSlowly('"No one has ever complimented my poem before..."', secondsBetweenChars=.03)
                printSlowly('"Please... Would you like to come in and have some tea?"', secondsBetweenChars=.03)
                print("Enter the tiny hole in the ground?")
                if yesno(player):
                    show("Andy Worm Poet opens the door to his underground abode and you walk inside.")
                    show("However small it looked from the outside, Andy's home is surprisingly spacious.")
                    show("Andy offers you some tea.")
                    tea(player)
                    printSlowly('"You know, this ol\' home is just too big for a small guy like me."')
                    printSlowly('"I wish I lived closer to some kind people that liked my poem."')
                    show("@Andy is really starting to open up to you@cyan@.")
                    printSlowly('"If only there where a way that I could show my poem to the world..."')
                    printSlowly('"Why don\'t you keep it. You obviously love it even more than I do."')
                    recievePoem(player)
                    printSlowly('"I was actually going to throw it away."')
                    printSlowly('"That\'s why it was laying discarded like that in the dirt outside my hole."')
                    printSlowly("\"I just can't find it within myself to appreciate my own work.\"")
                    printSlowly("\"It's different when you've experienced the countless hours that went into each word of the poem.\"")
                    printSlowly('"What a wonderful conversation we\'ve been having."')
                    printSlowly('"You are a true friend."')
                    printSlowly('"You can come back if you\'d like."')
                    printSlowly('"To have some more tea."')
                    printSlowly('"And talk."')
                    printSlowly('"I have holes near every major city in ' + player.aspect['land'] + '"')
                    printSlowly('"Though some of them need attention before they can be used."')
                    printSlowly('"You can always travel through my worm holes if you don\'t feel like walking."')
                    printSlowly('"They are surprisingly fast."')
                    printSlowly('"See you again soon!"')
                    show('You shuffle back out of the worm hole and resume your quest.')
                    show("That was weird.")
                    return 
                else: # chose not to go inside
                    printSlowly("I understand...")
                    printSlowly("Well...")
                    printSlowly("I want you to have this.")
                    recievePoem(player)
                    printSlowly('"I was actually going to throw it away."')
                    printSlowly('"That\'s why it was laying discarded like that in the dirt outside my hole."')
                    printSlowly("\"I just can't find it within myself to appreciate my own work.\"")
                    printSlowly("\"It's different when you've experienced the countless hours that went into each word of the poem.\"")
                    printSlowly('"Well anyway... I hope to see you again soon!"')
                    return

            else: # fail to respond correctly
                print("If you liked his poem, just tell him.")

    else: # youve already been to flowers
        if 'attacked flowers' in player.history:
            show("You come to a field of destoyed and uprooted flowers and find Worm Home.")
        elif 'waited for flowers' in player.history:
            show("You come to a field of flowers that part away from you wherever you walk and find Worm Home.")
        else:
            bug(player)
        show("Go inside?")
        if yesno(player):
            wormHome(player)
            return
        else:
            show("Better get going.")
            return

def takeThePie(player):
    i = Item(player, "Angry Worm Poet's Pie", customDescription="It's strawberry rhubarb, his favorite.", _type='consumable', sellValue=8, consumable=Consumable(consumeText="You're not really a big fan of rhubarb.", heal=3))
    player.addToInventory(i)            

def recievePoem(player):
    i = Item(player, 'Song of a Worm by Andy Worm Poet', customDescription="Song of a Worm\n\nMy lonely home is a hole in the soil\nI've exhausted my thoughts\nAnd now gladly recoil.", _type='quest', sellValue=0 )
    player.addToInventory(i)

def attackFlowers(player):
    show("You roll up your sleeves and prepare to engage!")
    e = Enemy(player, "plains")
    e.name = "Beautiful Field of Flowers"
    e.attack = 0
    e.setListOfAttacks([
        "gently caress your ankles with their petals...*",
        "sway from side to side...*",
        "drop a few petals...*",
        "smell beautiful...*",
        "swing back and forth in the wind...*",
        'just live a peaceful life...*'
    ])
    c = Combat(player, alert=False, enemy=e)
    if c.result == 'win':
        player.history.append("attacked flowers")
        player.map.getTile(8,5).description = "a field of destoyed flowers."
        clear()
        show("Having just ripped all of the flowers from the ground, you finally make it to the other side of the field.")
        return True
    else:
        show("You rethink attacking these flowers.")
        return False

