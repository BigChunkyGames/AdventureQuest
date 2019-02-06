# coding=utf-8
# above is a 'magic comment' which specifies the ascii encoding type

# The purpose of this file is to hold lists like a list of all dank memes
# TODO im prety sure all of these lists would be better (faster) as tuples but i dont really care enough to change it right now

import random
from source.utils import *
# from colorama import Fore
# from colorama import Style

def getWeaponPrefix():
    pass
    # TODO

def getRandomMemePeople():
    return getRandomIndex(DANKNAMES)

def getRandomDankAdjective():
    return getRandomIndex(DANKADJECTIVES)

def getRandomPainNoise():
    return getRandomIndex(PAIN_NOISES)

def getRandomDankClothing():
    return getRandomIndex(DANKCLOTHING)

def getMotherlyPlattitude():
    return getRandomIndex(MOTHERLYPLATITUDES)

def getRandomEnemyName(biome):
    if random.randint(1, 100) >= 95: # 5% chance you battle a pokeymon
        return getRandomIndex(ALL_POKEYMON)
    if biome == "plains":
        return getRandomIndex(ENEMYNAMES_PLAINS)
    if biome == "forest":
        return getRandomIndex(ENEMYNAMES_FOREST)
    if biome == "desert":
        return getRandomIndex(ENEMYNAMES_DESERT)
    if biome == "mountain":
        return getRandomIndex(ENEMYNAMES_MOUNTAIN)
    if biome == "spooky":
        return getRandomIndex(ENEMYNAMES_SPOOKY)
    else:
        return "Void Creature" # couldnt find a biome 

def getRandomWeaponName(extreme=False):
    if extreme: return getRandomIndex(WEAPON_EXTREME)
    else: return getRandomIndex(WEAPON)

def getRandomArmourName(slot=None):
    if slot == None: slot = getRandomArmourSlot()
    if slot == "head":
        return getRandomIndex(ARMOUR_HEAD)
    if slot == "chest":
        return getRandomIndex(ARMOUR_CHEST)
    if slot == "offhand":
        return getRandomIndex(ARMOUR_OFFHAND)
    if slot == "legs":
        return getRandomIndex(ARMOUR_LEGS)
    if slot == "feet":
        return getRandomIndex(ARMOUR_FEET)

def getRandomItemPrefix(goodness = 3):
    ''' 1=shitty, 2=bad, 3=ok, 4=good, 5=really good '''
    if goodness <= 1:
        return getRandomIndex(ITEM_PREFIX_SHITTY)
    elif goodness == 2:
        return getRandomIndex(ITEM_PREFIX_BAD)
    elif goodness == 3:
        return getRandomIndex(ITEM_PREFIX_OK)
    elif goodness == 4:
        return getRandomIndex(ITEM_PREFIX_GOOD)
    elif goodness >= 5:
        return getRandomIndex(ITEM_PREFIX_REALLYGOOD)

def getRandomAttackVerb():
    return getRandomIndex(ATTACK_VERBS)

def getRandomExtremeAttackVerb(): # not used yet
    return getRandomIndex(ATTACK_VERBS_EXTREME)

def getReaction(reactionlevel): # FIXME not currently used i dont think
    reaction = []
    if reactionlevel == 1:
        reaction = ["ehh", "pff"]
    elif reactionlevel == 2:
        reaction = ["oh cool", "neat"]
    elif reactionlevel == 3:
        reaction = ["whoa dude", "that was sick"]
    return reaction[random.randint(0, len(reaction)-1)]

def getInvalidOptionText(traveling=False):
    if not traveling: return getRandomIndex(INVALID_OPTION)
    else: return getRandomIndex(INVALID_OPTION_TRAVELING)
    
def getRandomDogNoise():
    return getRandomIndex(DOG_NOISES)

def getConversationResponse(responses = 1):
    response='"'
    for i in range(responses):
        response += getRandomIndex(CONVERSATION)+" "
    return response + '"'

def getRandomTVShow():
    return getRandomIndex(TV_SHOWS)

def getRandomArmourSlot():
    return getRandomIndex(ARMOUR_SLOTS)

def getDifficulty(index):
    if index >= len(DIFFICULTIES):
        return 'Lose'
    return DIFFICULTIES[index]

def getRandomFinalThought():
    return "*" + getRandomIndex(FINALTHOUGHTS) + "...*"


# these are constants. thats why they're all caps
### misc ##############################################################################

DANKADJECTIVES = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
DANKNAMES = ["Caillou", "Gabe Newell", "Batman", "Sanic", "Peppa Pig", "Pepe", "Famous Basketball Player Shaquille O'Neal", "Big Man Tyrone", "Voiceover Pete", "Shrek", "Neil deGrasse Tyson", "Bill Nye the Science Guy", "xXx_Sinpars_xXx", "Nicholas Cage", "Sergei Rachmaninoff"]
DANKCLOTHING = ["dick sock", "red bandana", "blue bandana", "single sock", "ski mask", "Christmas stocking"]
INVALID_OPTION = ["That is not a good choice." ,"Pick something else.", "I'm really going to need you to input a valid option.",
 "Try that again.", "Try that again but this time choose a valid option.", "THROW EXCEPTION: \"User chose an option that wasn't one of the options surrounded by single quotes like they should have\"", "raise AssertionError(\"User can't type.\")", 
 "I'm really sorry but that's just not a valid option", "I like what you're thinking but choose an option that is valid.", "The words with 'single quotes' around them are the ones that can be chosen so make sure to type one of those.", "The yellow words. Pick one of those.", "There is no need to do that right now.", "After considering that option, you decide to pick something else."  ]
INVALID_OPTION_TRAVELING = ["You tried to go that way but it didn't make any sense.", "You tried to go there but ended up right back where you started.", "That is no place you should be going right now.", "Sorry, that is off-limits.", "You thought about going that way but changed your mind.", "There is no need to do that right now.", "After considering that option, you decide to pick something else."]
TV_SHOWS = ["Commercials", 'Soap Opera', 'The News', 'Jeopardy', 'Wheel of Fortune', 'Spongebob', 'Emotionally Intense Drama', 'Cops', 'Reruns of your least favorite show', 'Oprah', 'Ellen', 'Static']
DIFFICULTIES = ['Easy','Cheesy','Grandma','Baby','Veteran','Veterinarian','Constant','Linear','Polynomial','Exponential','Double Exponential','Triple Exponential','Quadruple Exponential','Quintuple Exponential','Sextuple Exponential','Septuple Exponential','Octuple Exponential','Chaitin Omega Number','Random','Normal','Abnormal','Very Easy','Win Instantly','Difficult','Ultra-Difficult','Impossible', 'Easy-Hard', 'Baby-X', 'Brutal', 'Minority', 'Dandelion', 'Starts easy but gets harder later', "Enemys always deal damage equal to twice your health", 'Starts easy, gets harder in the middle but gets easier towards the end', 'Starts hard then gets harder until it\'s impossibly hard but then gets easier', 'Starts normal then gets hard then gets easier then gets baby-X then gets easier then gets harder', 'Come on this is only the second choice in the game you\'ve got to choose something', 'If you don\'t choose this one it\'s just going to be set to very hard', "I'm warning you. You're just going to have to restart because of how hard it's going to be", "Seriously, you won't even want to keep playing because the first enemy will always insta-kill you", "Each time you say no the difficulty only gets harder", "The difficulty is getting so hard you're going to lose before you're even introduced to the concept of health", "That's it. Say no again. I dare you", "Last chance", 
]
FINALTHOUGHTS = ['I think I left the oven on at home',"I wonder what was going to be for dinner tonight", 'How can this be!', 'I am in excruciating pain!', 'Am I dying, or is this my birthday?', 'This is the last of Earth! I am content!', 'Fuuuuuuuuuuuuuuuuck', 'Oh noooooooo', 'How could I let this happen', 'So I put my hands up, they\'re playing my song, butterflys fly away', 'In west Philadelphia, born and raised', "What is love, baby don't hurt me", "Who let the dogs out", "I wonder if I'll lose XP for this", "Not Again!", "They never made a garfield 3"] # TODO more

### NPC's #############################################################################

#(hints)
MOTHERLYPLATITUDES = ["There's no 'I' in 'Team'!", "Everybody makes mistakes. Don't forget to save often!", "Time heals all wounds. If you're injured, find a place to sleep!", "Work smarter, not harder. A lot of times, you can just type the first letter of a choice instead of the whole word.", "Sometimes you can choose options that aren't listed, like 'back' to cancel what you're doing."]# TODO more
CONVERSATION = ["Oh wow!", "That sounds incredible.", "No way!"," You are so amazing.", "I can't even believe how great that is.", "Of course!", "Tell me more!", "More!", "WHAT.", "You're fearless.", "JEALOUS!", "You didn't."]
DOG_NOISES = ["bark", "woof", "scrrf","yarrar","boof","birf","huuurg","ruff","rough","yip","yip yip", "bark bark","gruph","bow", "bow wow", "grrrrr"]
CURSES = ['fuck', 'shit', 'bitch', 'hoe', 'ho', 'cunt', 'wretch', 'whore', 'ass', 'dick', 'prick', 'cock', 'peener', 'vag', 'pussy', 'asshole', 'bastard', 'damn', 'bollocks', 'christ', 'hell', 'motherfucker', 'mother fucker', 'shitass', 'twat', 'jesus', 'song of a bitch', 'omg']

### items ##############################################################################
WEAPON = ['Great Sword', 'Claymore', 'Dagger', 'Staff', 'Hatchet', 'Nunchucks', 'Ninja Stars', 'Switchblade', 'Butterfly Knife', 'Mace', 'Club', 'Boomerang', 'Trident', 'Spear', 'Sickle', 'Bow and Arrow', 'Sheers', 'Sling',  'Whip', 'Spade', 'Hammer', "Boxing Gloves", "Gardening Gloves", "Shovel", "Pick Axe", "Blender", "Paper Airplane", "Banjo", "Drum Stick", "Throwing Knife", "Battle Toaster", "Chef Knife", 'Cheese Knife', 'Piece of Bark', 'Crab', 'Scissors', 'Envelope Opener', 'Cat Food Can Lid', 'Staple Gun', 'Nail Gun', 'Boomerang', 'Halberd', 'Finger Nail Clipper', 'Bubble Gun', 'Lawn Flamingo', 'Syringe', 'Sickle', 'Khopesh', 'Spork', 'Darts', 'Knitting Needle', 'Trident' ]
WEAPON_EXTREME = ['Pirate Ship Cannon', 'Trebuchet', 'Flame Thrower', 'Bazooka', 'Javelin Missile Launcher', 'Harpoon'] # TODO advanced combat
WEAPON_SPECIAL = ["Vampire Teeth", 'Light Sabor', 'Broken Light Sabor'] # TODO advanced combat (dont have prefix)
ARMOUR_SLOTS=['head', 'offhand', 'chest', 'legs', 'feet'] 
ARMOUR_HEAD = ['Army Helmet', 'Gas Mask', 'Beanie', 'Top Hat', 'Knight Helmet', "Straw Hat", "Ski Mask", "Conical Party Hat", "Propeller Cap", 'Shower Cap', 'Hair Net', '10 Gallon Hat', 'Toupee', 'Head Crab', 'Tiara', "Jack O'Lantern", "Wig", 'Hijab', "Smitty Werbenjegermanjensen's Hat", 'Bonnet', 'Turban', 'Umbrella Hat', ]
ARMOUR_OFFHAND = ['Shield', 'Gauntlet', 'Japanese Fan', "Frying Pan", 'Pizza Box', 'Amulet', 'Ring', 'Umbrella', 'Dictionary', 'Trashcan Lid', 'Musical Triangle',  'Ball of Yarn', 'Loose Change', 'Flip Phone', 'Prescription Medication', ]
ARMOUR_CHEST = ["Sleeveless T-Shirt", "Chainmail Cuirass", "Sweat Shirt", "Bikini Top", 'Sweatshirt', 'Saran Wrap', 'T-Shirt', 'Blouse', 'Tuxedo', 'Bra', 'Life Vest', 'Parka', 'Plaid Button-Up', 'Bullet-Proof Vest', 'Tie', 'Blazer', 'Corset', 'Oxygen Tank',  ]
ARMOUR_LEGS = ["Ripped Jeans", "Short Shorts", "Skort", "Ballerina Tutu", "Hip Joggers", "Jeggings", 'Dress Pants', 'Joggers', 'Cargo Shorts', 'Swim Trunks', 'Bikini Bottoms', 'Spanks', 'Capris', 'Overalls', 'Yoga Pants', 'Highwasted Jeans', 'Speedo', 'Bike Shorts', 'Gym Shorts', 'Slacks', 'Kilt', 'School Uniform Skirt', 'Bell Bottoms', 'Fig Leaf', 'Mermaid Tail', ]
ARMOUR_FEET = ["Fresh Kicks", "Pair of the Newest Air-Jordan's", 'Sandles', 'Crocks', 'Knee Socks', 'Socks', 'Converse', 'Dress Shoes', 'Water Shoes', 'Flippers', 'Ballet Point Shoes', 'Linen Wraps', 'Tap Shoes', 'Moon Boots', 'Heelys', 'Clown Shoes', 'Hiking Boots', 'Baseball Cleats', 'Ice Climbing Boots', 'Loafers', 'Boat Shoes', 'Stilettos', 'Compression Socks', 'Light-up Sketchers', ]

ITEM_PREFIX_SHITTY = ["Ugly", 'Shitty', 'Dirty', "Really Dull", "Damaged", "Fake", "Cardboard" ,"Holographic", "Awkward", "Uncomfortable", "Disgusting", "Wobbly", "Hairy", "Wet", ]
ITEM_PREFIX_BAD = ["Bad", "Rusty", "Hardy", "Unwieldy", "Dull", "Poor", "Stupid", "Corroded","Sticky", "Wooden",  "Plastic", "Uniquely Shaped", "Vintage", "Jiggly", "Average"]
ITEM_PREFIX_OK = ["Wieldy", "Nice", "Decent", "Cool", "Pokey", "Kinda Sharp", "Real", "Freaky", "Metal", "Croche", "Hand Knitted", "Dwarven", "Ancient", "Squishy", "Firm", "Solid", "Golden", "Bronze", "Silver", "Black", "White", "Transparent",  "Neat", ]
ITEM_PREFIX_GOOD = ["Good", "Pretty Good", "Swift", "Near-mint", "Sharp",'Like-new', "Elven", "Holy", "Blessed", getRandomDankAdjective(), "Glass", "Comfortable", "Stylish", "Grass", "Electromagnetic", "Sacred", "Chrome", "Spring Loaded", "Sexy", "Sneaky", "Flamboyant", "Romantic", "Swanky", ]
ITEM_PREFIX_REALLYGOOD = ["Really Good", "Excellent", "Prestine", "Very Sharp", "Executive", "Diamond","Beautiful", "Pristine", ]
ITEM_PREFIX_SPECIAL = ["Fire", "Ice", "Electrified", ] # TODO
ITEM_PREFIX_ADVERBS = ["Uncomfortably", "Straight-Up", "Ridiculously", "Really", "Very", "Intensely"] # TODO
### enemies ##############################################################################

# these can have duplicate names for different biomes and even duplicates within biome
# format like... "A wild [Shrek] appeared!" or "[Big huge rat monster] attacked and did 3 damage!"
ENEMYNAMES_PLAINS = ["FaZe Fanboy", "Sonic", "Tails", "Knuckles", "Ciallou", "Creeper", "some dude with a riot shield", 
'Gary "Roach" Sanderson', 'Brutus the Buckeye', "Chad", "Angry Cat" ]
ENEMYNAMES_FOREST = ["Shrek", "Donkey", "Big Huge Rat Monster", "Forest Squidward", "Treant", "Murloc", "Huge Bear", "The SnapChat Ghost",
"Dragonfly"  ]
ENEMYNAMES_DESERT = ["Huge Fucking Scorpion", "Bobcat", "Agent 008"]
ENEMYNAMES_MOUNTAIN = ["Baby Dinosour", "Dwayne 'The Rock' Johnson", "Possessed Rock"]
ENEMYNAMES_SPOOKY = ["Zombie", "Skeleton", "Ghost", "Count Spookula", "Big Spider", 'Colony of Bats', 'Floating Skull', 'Tarantula', 'Mr. Spooks', 'Spook-o-Johnson'] 
ENEMYNAMES_BIG_GUYS = ["Deadra", "Mr. Skeltal"] # FIXME not currently used
ALL_POKEYMON = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Rattata","Raticate","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Raichu","Sandshrew","Sandshrew","Sandslash","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Vulpix","Ninetales","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Diglett","Dugtrio","Dugtrio","Meowth","Meowth","Persian","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Geodude","Graveler","Graveler","Golem","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd,""Doduo","Dodrio","Seel","Dewgong","Grimer","Grimer","Muk","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Exeggutor","Cubone","Marowak","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr., Mime""Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh,""Celebi","Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Castform","Castform","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys","Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Burmy","Burmy","Wormadam","Wormadam","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Shellos","Gastrodon","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr,." "Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina","Giratina","Cresselia","Phione","Manaphy","Darkrai","Shaymin","Shaymin","Arceus","Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Frillish","Jellicent","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Meloetta","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Hoopa","Volcanion","Rowlet","Dartrix","Decidueye","Litten","Torracat","Incineroar","Popplio","Brionne","Primarina","Pikipek","Trumbeak","Toucannon","Yungoos","Gumshoos","Grubbin","Charjabug","Vikavolt","Crabrawler","Crabominable","Oricorio","Oricorio","Oricorio","Oricorio","Cutiefly","Ribombee","Rockruff","Lycanroc","Wishiwashi","Mareanie","Toxapex","Mudbray","Mudsdale","Dewpider","Araquanid","Fomantis","Lurantis","Morelull","Shiinotic","Salandit","Salazzle","Stufful","Bewear","Bounsweet","Steenee","Tsareena","Comfey","Oranguru","Passimian","Wimpod","Golisopod","Sandygast","Palossand","Pyukumuku","Silvally","Minior","Komala","Turtonator","Togedemaru","Mimikyu","Bruxish","Drampa","Dhelmise","Cosmog","Cosmoem","Solgaleo","Lunala","Nihilego","Buzzwole","Pheromosa","Xurkitree","Celesteela","Kartana","Guzzlord","Necrozma","Magearna","Marshadow","Poipole","Naganadel","Stakataka","Blacephalon","Zeraora","Meltan","Melmetal"]

### biome descriptors used in map.py ##############################################################################

FOREST_SYNONYMS = ["a forest", "some trees", "a woods" ,"an aesthetic arberetum of luscious shrubbery"]
PLAINS_SYNONYMS = ["some plains" , "a vast expanse of grass ;)", "a flowing green field", "the open expanse of nature", "an open prairie", "wide lowlands"]
DESERT_SYNONYMS = ["an expanse of dunes", "a desert", "naked golden fields of sand", ]
MOUNTAINS_SYNONYMS = ["a specious assortment of unbridled peaks", "some mountains", "shimmering peaks of aestitic rapture", "huge rocks", "just a fucking ton of huge gigantic fucking rocks"]
TRANSIT_SYNONYMS = ["You walk past" ,"You stroll your way toward", "You thought there was nothing but when you turned around you saw", "On your left you see",    "Enjoying the nice weather, you suddenly come accross", "Half asleep, you notice", "Not paying attention, you almost fail to take notice of", "You hear someone say, \"" + getMotherlyPlattitude() + "\" but when you turn around it was only" ]

### verbs ##############################################################################

# if ends with * , the sentence reads without trailing "you!" ex. the monster is attempting to critisize your outfit!
# else, sentence reads with trailing you ex. the monster is trying to strike you!
ATTACK_VERBS = ["scratch", "bite", "punch", "insult", "kick", "lick", "attack", "assult", "elbow", "curb-stomp", "stab", "spin-kick", "charge", "strike", "pounce upon", "rush", "seduce", "tickle", "roundhouse-kick", "combo", 
"abuse", "rangle", "criticize your outfit!*", "destroy", "deconstruct", "direct unfavorable criticism against","argue about political matters with", "assail", "gossip about you behind your back!*" , "take you on a one way trip to pain town!*","engage",]
ATTACK_VERBS_EXTREME = ["nuke", "fireblast", "falcon punch", "no-scope", "ult"]

### onomatopoeia ##############################################################################

PAIN_NOISES = ["Youch!", "Oof!", "Ouch!", "Owwee!", "That has got to hurt.", "Should have dodged that.", "That looked like it hurt!", "Dang!", "Ooch!", "Ow!", "~ouch~"]

# ex.
#print "look out! here comes a " + getRandomDankAdjective() + " " + getRandomEnemyName("forest")
