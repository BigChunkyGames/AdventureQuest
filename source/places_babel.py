from source.utils import *




def babel(player):
    show("You stand before an immense hexagonal structure that seems to go on endlessly into the sky.")
    show("A poster on the front door advertises a poetry contest.")
    print("Read the poster?")
    if yesno(player):
        show("The poster says:")
        show("This contest is for", dots=False)
        show("poets who can't ignore", dots=False)
        show("the poster on this door", dots=False)
        show("if you would like to learn more,", dots=False)
        show("talk to a librarian.", dots=False)
    print("Open the solid oak doors and walk inside?")
    if yesno(player):
        show("For as far as you can see there are enormous adjacent hexagonal rooms, each lined with shelves of books containing every possible combination of words and characters.")
        show("Overwhelmed at the thought of finding a book about the illuminati by browsing, you decide to ask the librarian.")
        show("A tall librarian is standing behind the front desk.  ")
        show("She is reading a book that appears to be entirely gibberish.")
        show("She looks up at you from above her glasses.")
        printSlowly("Can I help you?")
        x = player.getInput()
        if 'illum' in x or 'book' in x:
            show("Her eyes widen in shock")
            printSlowly("You want a book about one of the most infamous groups ever to grace the planet?")
            printSlowly("You're quite bold to be asking about them in a place like this.")
            show("She looks around to make sure nobody else is watching, and then types something into her computer")
            printSlowly("It looks like all of our books on the subject have been checked out by the developers.")
            printSlowly("Try coming back next release, maybe they'll be back by then.")
            show("She looks back at her book as if you weren't there.")
            show("What 'developers' is she even talking about?")
        elif 'poet' in x or 'contest' in x:
            printSlowly("Oh, here for the poetry contest, are you?")
            printSlowly("Sorry, but the developers haven't implemented that yet.")
            printSlowly("Come back a few releases from now, maybe then it will be ready.")
            show("She goes back to reading her book.")
            show("Well that's dissapointing.")
        elif 'no' in x or checkForCancel(x):
            show("Try not to waste my time in the future. I'm clearly a busy woman.")
        show("Having had your fill of this librarian, you decide to head back into the world.")

    else:
        show("Yeah you don't really like books anyway.")
        show("You decide to leave the grandiose library behind you.")
        return
    








BOOKSHELF = '''
 _________________________________________________________
||-------------------------------------------------------||
||.--.    .-._                        .----.             ||
|||==|____| |H|___            .---.___|""""|.-------.___ ||
|||  |====| | |xxx|_          |+++|=-=|_  _| -=++=- |---|||
|||==|    | | | B | \         |   |   |_\/_| Health | ^ |||
|||  |    | | | I |\ \   .--. |   |=-=|_/\_| -=++=- | ^ |||
|||  |    | | | O |_\ \_( oo )|   |   |    |  Diet  | ^ |||
|||==|====| |H|xxx|  \ \ |''| |+++|=-=|""""| -=++=- |---|||
||`--^----'-^-^---'   `-' ""  '---^---^----^--------^---^||
||-------------------------------------------------------||
||-------------------------------------------------------||
||               ___                   .-.__.-----. .---.||
||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
||      _a'{ / (|===|+|   |++|  |==|   | |  |@Illum@yellow@| | R |||
||      '/\\\/ _(|===|-|   |  |''|  |:x:|=|  |@inati@yellow@| | Y |||
||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | Z |||
||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
||-------------------------------------------------------||
||_______________________________________________________||
'''




SHARK = '''    
              ,^;
             . /
         .-'`  {
       ,`  -'-. `\\_
      ;  /      " -'
      |  \       ,^,
      \   '-.__,/ _`'._
       .     ```      ``'--._
      <.`                      `'-.
         '`-._       ,   (((   o _,,,>
        jgs   `'""----\   ,--..--"""
                       '-' '''
                       
# listOfRows = SHARK.splitlines()
# for i in listOfRows:

#     printc(i)