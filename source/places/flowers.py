
from source.utils import *
from source.enemy import Enemy
from source.combat import Combat
from source.item import Item


def flowers(player):
    if player.getVisits("flowers", "add") == 1 :
        show("Anemones, daffodils, irises, daisies, larkspurs, dahlias, sunflowers, carnations, and amaryllis sprawl for miles around.")
        show("They are so densly arranged and neatly packed that they block your path.")
        show("There is no other way across the field.")
        show("There is only one way to get through the flowers.")
        print ("Attack the flowers?")
        if yesno(player):
            player.karma = player.karma - 1
            attackFlowers(player) # TODO disable escape and dodge
        else:
            show("You decide to wait.")
            wait(30, '. ')
            print("Are you sure you don't want to attack the flowers?")
            if not yesno(player):
                attackFlowers(player)
            else:
                show("You continue waiting.")
                wait(30, '. ')
                player.choices.append("waited for flowers")
                show("The flowers, appreciating your patience, slowly part, revealing a path.")
                show("You continue to the end of the field.")
        show("You notice a little scrap of paper protruding from a tiny hole in the dirt.")
        print("Pick it up?")
        if yesno(player):
            word = "like"
            show("Scrawled on the old tattered paper is a poem written in extremely small handwriting. It is nearly impossible to read. You can just barely make out what it says...")
            show('Song of a Worm')
            show('')
            show('My lonely home is a hole in the soil')
            show("I've exhausted my thoughts")
            show('And now gladly recoil.')
            show('')
        else: 
            word = "read"
        show("You hear a faint, angry squeaking coming from a hole near your shoe.") # TODO say     what shoe armour is
        show("You bend down and investigate the noise...")
        show('Angry Worm Poet is angry that you didn\'t ' + word + ' his poem.')
        show('Fuming with artistic despair, he musters the strength to cry, "I will destroy you!"')
        while(True):
            printc("@'Smash'@yellow@ him under your foot or @tell him that you really loved his poem@yellow@?" )
            x = getInput(player)
            if checkInput(x, "smash") or checkInput(x, 'Smash'):
                player.karma = player.karma - 3
                show('You prepare to stomp the pesky worm.')

                e = Enemy(player, "plains")
                e.name = "Angry Worm Poet"
                e.attack = 1
                e.hp = 1
                e.setListOfAttacks(["slime on your shoe...*"])
                Combat(player, alert=False, enemy=e)
                clear()
                show("Angry Worm Poet is smashed into the dust and drops the deed to Worm Home. ")
                description = "Tiny tattered legal document. It says:\nWhomst ever holds this deed has rightful ownshership over 'Worm Home'."
                i = Item(player, "Deed to 'Worm Home'", customDescription=description,  _type='Quest', )
                player.addToInventory(i) # FIXME inventory
                show("Enter Worm Home?")
                if yesno(player):
                    show("You open the tiny door to the worm's underground abode and walk inside.")
                    show("However small it looked from the outside, Worm Home is surprisingly spacious.")
                else:
                    show("You've had enough of this.")
                    return

            elif 'love' in x or 'like' in x or 'enjoy' in x:
                player.karma = player.karma + 1
                show("The worm stops and looks at you.")
                show("A single tear wells in his eye.")
                show('"No one has ever complimented my poem before..."')
                show('"Please... Would you like to come in and have some tea?"')
                print("Enter the tiny hole in the ground?")
                if yesno(player):
                    show("Andy Worm Poet opens the door to his underground abode and you walk inside.")
                    show("However small it looked from the outside, Andy's home is surprisingly spacious.")
                    show("Andy offers you some tea.")
                    while(True):
                        printc("@'Chamomile'@yellow@ or @'lavender'@yellow@?")
                        x = getInput(player)
                        if checkInput(x, "chamomile"):
                            show("Andy pours you a cup of chamomile tea")
                            tea = 'Chamomile'
                        elif checkInput(x, "lavender"):
                            show("Andy pours you a cup of lavender tea")
                            tea = 'Lavender'
                        else:
                            print("Which tea do you want?")
                    receiveTea(player, tea)
                else:
                    show("I understand...")
                    show("Well...")
                    show("I want you to have this poem.")
                    receivePoem(player)

            else:
                print("If you liked his poem, just tell him.")

    else: # youve already been here
        if 'attacked flowers' in player.choices:
            show("You come to a field of destoyed and uprooted flowers and find Worm Home.")
        elif 'waited for flowers' in player.choices:
            show("You come to a field of flowers that part away from you wherever you walk and find Worm Home.")
        else:
            show("How did you do that?!")

            
def receiveTea(player, tea):
    i = Item()




def attackFlowers(player):
    player.choices.append("attacked flowers")
    player.map.getTile(8,5).description = "a field of destoyed flowers."
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
    Combat(player, alert=False, enemy=e)
    clear()
    show("Having just ripped all of the flowers from the ground, you finally make it to the other side of the field.")
