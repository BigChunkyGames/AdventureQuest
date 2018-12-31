from source.utils import show, input, checkInput, yesno, printc
from source.lists import getInvalidOptionText
from source.enemy import *
from source.combat import *

#TODO QUEST get information from dogetown (but its funny because they only say bark)
# TODO the rest of this
def dogeTown(player):
    if player.getVisits("dogeTown", "add") == 1 :
        show("You approach what seems to be a town completely inhabited by polite and playful doggos.")
        show("It's magnificent. You have never seen anything like it. There are puggos and long boys and shoobos and wrinklers... All types of doge boys run about playing fetch and chase through the streets and in the open fields around the town.")
        show("Yappers are yipping from rooftops and floofers woof from below.")
        show("A smol baby doge pupper runs by you at hecking fast speeds and zooms through a doggie door.")
        show("You continue to a white marble staircase and begin to climb.")
        show("The town is surrounded by a pearly white wall bolstering multicolored flags all with the same paw print emblem.")
        show("Marveling at the beautiful architecture, you wonder how such a place has been only 5 distances away from your home town all this time.")
        show("You reach the top of the staircase and are halted by 2 shoobers armed with spears crossed to block your path.")
        show("Another doggo approaches. This doge, a shibe, greets you with the grandeur of a king. He is surely the doggest. ")
        show('"Bork."')
        x = input(player)
        show('"Woof bork!"')
        x = input(player)
        show('"Yip yip bark boof woof, bork yip bark boof?"')
        x = input(player)
        show("The doge nods his head to the shoober soliders and they uncross their spears. It seems that thanks to your cunning choice of words you have been granted access into Dogetown.")
        
        # gabe

    while True:
        print("The entrance to DogeTown leads to a courtyard were digdogs of all sizes wag their tails and run in between the structures. ")
        print("Around you are a few buildings with doors large enough for you to enter.")
        printc("There is one called @'party'@yellow@ puppo's puppy palace.")
        printc("Another is @'Bony'@yellow@s Convenience Store.")
        printc("On your left rests a towering structure that looks like a @'church'@yellow@. You hear howling from inside. ")
        printc("There is also a path to what looks to be the @'king'@yellow@s quarters.")
        printc("Or you can @'leave'@yellow@.")
        x = input(player)
        if (x == "party" or x == "p"):
            show("Party puppo's puppy palace prick's your fancy so you prop open the door and walk inside.")
            show("The club music blasts and the dance floor is crowded with floofers and doges getting down to the hip hop beat.")
            party(player)    
        elif (x == "bony" or x == "b" or x == "bony's"):
            show("Feeling like you don't have enough in your pockets, you decide to purchase some poochmerch.")
            show("Inside the quaint shop, a diggy sploot leans up against the counter.")
            print('"Bow bow."')
            x = input(player)
            print('"Gruph."')
            print("Look at his wares?")
            if yesno(player):
                # TODO shop
                # treat, healing item
                # frizbee, weapon
                # bone, chew to gain 3 xp
                # doge collar, 2 defense
                # rolled up piece of paper, unroll to find missing dog poster for your dog that you lost a long time ago
                pass
            show("That was fun, but now it's time to leave.")
        elif (x == "king" or x == "k" or x == "king's"):
            show("You approach an impractically large marble door at the top of another set of white marble steps.")
            print "Open?"
            if yesno(player):
                print "It's locked. Knock?"
                if yesno(player):
                    show("You give the door a few knocks and it opens.")
                    show("King Dogedog III, ruffled and majestic, peers from behind the gigantic door.")
                    count = 0
                    while True:
                        count = count +1
                        words = random.randint(1,10)
                        s = ""
                        for i in range(words):
                            if i == 0:
                                s += str(getRandomDogNoise().capitalize())
                            else:
                                s += str(", " + getRandomDogNoise())
                        s += "."
                        print s
                        if count == 4 or count > 10:
                            printc ("(if you ever get tired of talking you can always type @'leave'@yellow@)")
                        x = input(player)
                        if checkInput(x,"leave"):
                            break
                        elif checkInput(x,"bork bork bork woof bork"): # TODO find this code somewhere
                            # TODO accesss granted
                            show("The king opens the door wide and allows you to enter.")
                            show("Then he slams it shut in your face because this part of the game is unfinished.")
                            break
                        

            show("You head back down the stairs to the courtyard.")
        elif (x == "church" or x == "c"):
            if player.getVisits("dogetownChurch", "add") == 1 : # TODO inventory has to not have costume equuiped
                show("The soulful doggos inside are howling a hymn in unison. It sounds beautiful and you're touched knowing it's even possible for diggies to sound this good. ")
                show("The church has massive stained glass windows of grand grizlords, slippery tube dudes, and big scary teeth doggos. ")
                show("Though threatened by the colossal artistry, you slowly creek open the mighty door and enter.")
                show("As you open the door the entire doggo quire stops singing and looks directly at you.")
                show("It is completely silent.")
                show("At the end of the chancel and behind the alter stands a duggo holding his paws to the sky as if to cast his radiance around the room.  ")
                show("It is no ordinary duggo.")
                show("It is...")
                show("It must be...")
                show("Buddhog")
                show("The entire quire of doogles starts growling and barking at the sight of you.")
                show("You exit the building.")
                show("There was something oddly familiar about that dog.")
            elif 1: # TODO if you have the costume equipped
                show("Fitting right in, you crawl to the nearest pew and take a seat.")
                print "Sing along?"
                if yesno(player):
                    show("You try to sing along to the hymns but they are completely unpredictable.")
                show("The song finishes and all of the soulful diggums look towards the front of the chapel.")
                show("The room erupts in grrfles as Buddhog lowers his paws and clears his throat.")
                show('"My children, thank you all for being here today."')
                show('"Please bow with me in prayer."')
                show("The room erupts into bows of praise.")
                show("Bow wow wow bow bow wow bow...")
                show('"We praise you, almighty DOG. We lift our paws to you."')
                show('"Now please turn to page bork-hundred and 3."')
                show("You pick up a book from under the seat in front of you.")
                show("You have acquired 'The Sacred Texts of Buddhogism'.") # TODO inventory
                print "Read it?"
                if yesno(player):
                    show("The entire book is written using dog words that you cannot understand.")
                    print "Continue reading?"
                    if yesno(player):
                        show("You pretend to continue reading the book.")
                show('The doggos begin chanting.')
                for j in range(3):
                    count = count +1
                    words = 3
                    s = ""
                    for i in range(words):
                        if i == 0:
                            s += str(getRandomDogNoise().capitalize())
                        else:
                            s += str(", " + getRandomDogNoise())
                    s += "."
                    show(s) 
                show("This chanting continues for several minutes, but you cannot leave. Something about Buddhog captivates you.")
                show("The sermon finishes and all of the dogles leave.")
                show("You can talk to @'Buddhog'@yellow@ or @'leave'@yellow@.")
                x = input(player)
                if checkInput(x, "Buddhog"):
                    show("You approach the holy dog.")
                    show("You're nervous, something about him makes your heart beat fast.")
                    show("He turns to face you, and you realize what you've been missing all along.")
                    show('"' + player.aspect["name"] + '?!"')
                    show("You both embrace in a hug that lasts a lifetime.")
                    show("Tears roll down your face as you realize that you are now reunited with your childhood dog, Bud.")
                    show('"It has been so long, ' + player.aspect["name"] + '".')
                    printc("@Bud has joined the party!@cyan@") # TODO party members, also do if bud in party then entering church is different
                    raw_input("... ")
                    show("Bud will aid you in your quest. With your efforts combined, you are one step closer to defeating your greatest enemy.")
            else:
                show("Though the sound of the doggos singing sounds amazing from outside, you don't want to go back in there.")
        elif (x == "leave" or x == "l"):
            show("Because you are insane, you decide to leave Dogetown. After all, the rest of the world can't be that much worse.")
            show("Can it?")
            break
        else:
            print(getInvalidOptionText())

def party(player):
    show("On your left you see the @'bar'@yellow@ where doggers are getting crank. ")
    show("Straight ahead is the @'dance'@yellow@ floor.")
    show("Towards the right you notice a picture of a fire hydrant and an arrow pointing towards the end of a @'hallway'@yellow@.")
    while (True):
        print("Where will you go now?")
        x = input(player)
        if x == 'bar' or x == 'b':
            show("You decide that it's about time to get a drink and take a seat at the bar.")
            show("The barktender, a plump bulldoger, grunts and gestures to his selection of doogie booze.")
            print("Consider his selection?")
            if yesno(player):
                # TODO buy things at bar
                pass
            show("The pulsing of the sudwoofers shakes the room.")
            print("Ask for rumors?")
            if yesno(player):
                show('"Bork bark. Roof bork riffity bork ruff.')
                show("A quest has been added to your quest log.") #TODO quests
        elif x == 'dance' or x == 'd':
            if player.getVisits("dogetown dance", "add") == 1:
                show("The dance floor is packed with sweating grinding bitches, so you dive in.")
                show("Just when you think you've got your boogy on, you find yourself in the middle of the mosh pit.")
                show("You realize a bit too late what you've gotten yourself into. There's no way out!")
                show("The bitches are grinding too hard!")
                show("You're being attacked!")
                e = Enemy(player, "forest")
                e.setName("Doge Pit")
                e.setListOfAttacks([
                    "scratch you with a wall of claws... *",
                    "bork you over...*",
                    "get nippy with you...*",
                    "soak you in slobber...*",
                    "jump on you and lick your face...*",
                    "gnaw on your hair...*"])
                c = Combat(player, alert=False, enemy=e)
                show("You finally thrash your way out of the mosh pit.")
            else:
                show("You don't really want to go back in there.")
        elif x == 'leave' or x == 'l':
            return
        elif x == 'hallway' or x == 'h':
            if player.getVisits("dogetown hallway", "add") >1 :
                show("You don't have to go to the bathroom anymore.")
                continue
            show("You make your way down the hallway and come to a set of two doors each with their own sign.")
            show( "The door on the @'left'@yellow@ has a symbol that looks like this:")
            s="""                                                        
                @@@@@@@             
                   @@@@             
     @@@@@@@@@@@ @@@ @@             
   @@           @@.  @@             
 @@%@@            @@                
@@    @@           @@               
@       @@@         @               
@         @@@       @               
@@          @@@    @@               
 @@           @@@ @@                
  @@             @@                 
    @@@       @@@                   
         @@@                        
"""
            print(s)
            raw_input("... ")
            show("The door on the @'right'@yellow@ has a symbol that looks like this:")
            s = """                                      
                         ,.. 
                       ,...  
                     ,..,.   
                    ....     
                  ,..*       
           ((   #...         
         ((#((&%#            
       (((#(&& ,(            
    /((((((&&(&&&&(          
   (((#(((#&&&&&             
  ((#(((#&&&&&               
  (((##%&&&,                 
  ####%&,                                       
  """
            print(s)
            raw_input("... ")
            while True:
                print("Which door will you choose?")
                x = input(player)
                if checkInput(x, "left"):
                    if player.getVisits("dogeTown boy's bathroom"):
                        show("You probably want to choose the other door.")
                    if player.aspect["gender"] == "girl" or player.aspect["gender"] == "gril":
                        show("The doogs inside the bathroom bork angrily at you and you are forced to leave.")
                        player.getVisits("dogeTown boy's bathroom", "add")
                        continue
                    bathroom(player)
                    break
                elif checkInput(x, "right"):
                    if player.getVisits("dogeTown girls's bathroom"):
                        show("You probably want to choose the other door.")
                    if player.aspect["gender"] == "boy" or player.aspect["gender"] == "boi":
                        show("The doogettes inside the bathroom birk angrily at you and you are forced to leave.")
                        player.getVisits("dogeTown girls's bathroom", "add")
                        continue
                    bathroom(player)
                    break
            party(player)
            return
        else:
            print(getInvalidOptionText())
        
def bathroom(player):
    show("Inside the bathroom there is one open stall.")
    show("You enter the stall and close the door.")
    show("In front of you is a very dirty fire hydrant.")
    show("You take a seat.")
    show("You notice, hanging on the back of the door, a kinky doggy-style costume.")
    show("You acquired the doggy-style costume.") #TODO inventory
    print("Put it on?")
    if yesno(player):
        #TODO inventory
        show("You put on the costume.")
    show("Having finished your business, you prepare to leave.")
    print "Wash your hands first?"
    if yesno(player):
        show("You wipe your hands on the grassy countertop and check yourself out in the mirror.")
        show("At the sight of yourself, you are fullfilled with confidence.")
        show("Damn, you look fine.") 
        player.addExperience(1)
        # TODO different reaction depending on if constume was equipped
    show("You walk back into the club.")

    
    

