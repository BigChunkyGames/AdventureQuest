from source.utils import show, input
from source.lists import getInvalidOptionText

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
        show("The enterence to DogeTown leads to a courtyard were digdogs of all sizes wag their tails run inbetween the strucutrers. ")
        show("Around you are a few buildings with doors large enough for you to enter.")
        show("There is one called @'party'@yellow@ puppo's puppy palace.")
        show("Another is @'Bony'@yellow@s Convenience Store.")
        show("On your left rests a towering structure that looks like a @'church'@yellow@. You hear howling from inside. ")
        show("There is also a path to what looks to be the @'king'@yellow@s quarters.")
        show("Or you can @'leave'@yellow@.")
        x = input(player)
        if (x == "party" or x == "p"):
            show("Party puppo's puppy palace prick's your fancy so you prop open the door and walk inside.")
            show("The club music blasts and the dance floor is crowded with floofers and doges getting down to the hip hop beat.")
            show("")
# sub woofer
            pass
        elif (x == "bony" or x == "b" or x == "bony's"):
            # TODO shop
            # treat, healing item
            # 
            pass
        elif (x == "king" or x == "k" or x == "king's"):

            pass
        elif (x == "church" or x == "c"):
            if player.getVisits("dogetownChurch", "add") == 1 :
                show("The soulful doggos inside are howling a hymn in unison. It sounds beautiful and you're touched knowing it's even  possible for diggies to sound this good. ")
                show("The church has massive stained glass windows of grand grizlords, slippery tube dudes, and big scary teeth doggos. ")
                show("Though threatened by the colossal artistry, you slowly creek open the mighty door and enter.")
                show("As you open the door the entire doggo quire stops singing and looks directly at you.")
                show("It is completely silent.")
                show("At the end of the chancel and behind the alter stands a duggo holding it's paws to the sky as if to cast his radiance around the room.  ")
                show("It is no ordinary duggo.")
                show("It is...")
                show("DOG")
                show("The entire quire of doogles starts growling and barking at the sight of you.")
                show("You exit the building.")
            else:
                show("Though the sound of the doggos singing sounds amazing from outside, you don't want to go back in there.")
        elif (x == "leave" or x == "l"):
            show("Because you are insane, you decide to leave Dogetown. After all, the rest of the world can't be that much worse.")
            show("Can it?")
            break
        else:
            print(getInvalidOptionText())



