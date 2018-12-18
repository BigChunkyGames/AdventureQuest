# coding=utf-8
# above is a 'magic comment' which specifies the ascii encoding type

# The purpose of this file is to hold lists like a list of all dank memes


import random
from utils import *
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
    else:
        return "Void Creature" # couldnt find a biome 

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

def getInvalidOptionText():
    return getRandomIndex(INVALID_OPTION)
    

#################### lists #############################################################
# these are constants. thats why they're all caps

### misc ##############################################################################

DANKADJECTIVES = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
DANKNAMES = ["Caillou", "Gabe Newell", "Batman", "Sanic", "Peppa Pig", "Pepe", "Famous Basketball Player Shaquille O'Neal", "Big Man Tyrone", "Voiceover Pete", "Shrek", "Neil deGrasse Tyson", "Bill Nye the Science Guy", "xXx_Sinpars_xXx", "Nicholas Cage", "Sergei Rachmaninoff"]
DANKCLOTHING = ["dick sock", "red bandana", "blue bandana", "single sock", "ski mask", "Christmas stocking"]
MOTHERLYPLATITUDES = ["There's no 'I' in 'Team'!", "Everybody makes mistakes. Don't forget to save often!", "Time heals all wounds. If you're injured, find a place to sleep!", "Work smarter, not harder. A lot of times, you can just type the first letter of a choice instead of the whole word."]
INVALID_OPTION = ["That is not a good choice." ,"Pick something else.", "I'm really going to need you to input a valid option.",
 "Try that again.", "Try that again but this time choose a valid option.", "THROW EXCEPTION: \"You suck.\"", "raise AssertionError(\"User can't type.\")", 
 "I'm really sorry but that's just not a valid option", ]
### enemies ##############################################################################

# these can have duplicate names for different biomes and even duplicates within biome
# format like... "A wild [Shrek] appeared!" or "[Big huge rat monster] attacked and did 3 damage!"
ENEMYNAMES_PLAINS = ["FaZe Fanboy", "Sonic", "Tails", "Knuckles", "Ciallou", "Creeper", "some dude with a riot shield", 
'Gary "Roach" Sanderson', 'Brutus the Buckeye', "Chad", "Angry Cat" ]
ENEMYNAMES_FOREST = ["Shrek", "Donkey", "Big Huge Rat Monster", "Forest Squidward", "Treant", "Murloc", "Huge Bear", "The SnapChat Ghost",
"Dragonfly"  ]
ENEMYNAMES_DESERT = ["Huge Fucking Scorpion", "Bobcat", "Agent 008"]
ENEMYNAMES_MOUNTAIN = ["Baby Dinosour", "Dwayne 'The Rock' Johnson", "Possessed Rock"]
ENEMYNAMES_SPOOKY = ["Zombie", "Skeleton", "Ghost", "Count Spookula",] # FIXME not currently used
ENEMYNAMES_BIG_GUYS = ["Deadra", "Mr. Skeltal"] # FIXME not currently used
ALL_POKEYMON = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Rattata","Raticate","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Raichu","Sandshrew","Sandshrew","Sandslash","Sandslash","Nidoran","Nidorina","Nidoqueen","Nidoran","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Vulpix","Ninetales","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Diglett","Dugtrio","Dugtrio","Meowth","Meowth","Persian","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Geodude","Graveler","Graveler","Golem","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd,""Doduo","Dodrio","Seel","Dewgong","Grimer","Grimer","Muk","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Exeggutor","Cubone","Marowak","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr., Mime""Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium","Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl","Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff","Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo","Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire","Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress","Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel","Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird","Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle","Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune","Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh,""Celebi","Treecko","Grovyle","Sceptile","Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone","Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry","Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain","Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja","Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye","Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun","Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt","Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria","Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol","Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Castform","Castform","Castform","Kecleon","Shuppet","Banette","Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein","Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum","Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza","Jirachi","Deoxys","Turtwig","Grotle","Torterra","Chimchar","Monferno","Infernape","Piplup","Prinplup","Empoleon","Starly","Staravia","Staraptor","Bidoof","Bibarel","Kricketot","Kricketune","Shinx","Luxio","Luxray","Budew","Roserade","Cranidos","Rampardos","Shieldon","Bastiodon","Burmy","Burmy","Burmy","Wormadam","Wormadam","Wormadam","Mothim","Combee","Vespiquen","Pachirisu","Buizel","Floatzel","Cherubi","Cherrim","Shellos","Shellos","Gastrodon","Gastrodon","Ambipom","Drifloon","Drifblim","Buneary","Lopunny","Mismagius","Honchkrow","Glameow","Purugly","Chingling","Stunky","Skuntank","Bronzor","Bronzong","Bonsly","Mime Jr,." "Happiny","Chatot","Spiritomb","Gible","Gabite","Garchomp","Munchlax","Riolu","Lucario","Hippopotas","Hippowdon","Skorupi","Drapion","Croagunk","Toxicroak","Carnivine","Finneon","Lumineon","Mantyke","Snover","Abomasnow","Weavile","Magnezone","Lickilicky","Rhyperior","Tangrowth","Electivire","Magmortar","Togekiss","Yanmega","Leafeon","Glaceon","Gliscor","Mamoswine","Porygon","Gallade","Probopass","Dusknoir","Froslass","Rotom","Uxie","Mesprit","Azelf","Dialga","Palkia","Heatran","Regigigas","Giratina","Giratina","Cresselia","Phione","Manaphy","Darkrai","Shaymin","Shaymin","Arceus","Victini","Snivy","Servine","Serperior","Tepig","Pignite","Emboar","Oshawott","Dewott","Samurott","Patrat","Watchog","Lillipup","Herdier","Stoutland","Purrloin","Liepard","Pansage","Simisage","Pansear","Simisear","Panpour","Simipour","Munna","Musharna","Pidove","Tranquill","Unfezant","Unfezant","Blitzle","Zebstrika","Roggenrola","Boldore","Gigalith","Woobat","Swoobat","Drilbur","Excadrill","Audino","Timburr","Gurdurr","Conkeldurr","Tympole","Palpitoad","Seismitoad","Throh","Sawk","Sewaddle","Swadloon","Leavanny","Venipede","Whirlipede","Scolipede","Cottonee","Whimsicott","Petilil","Lilligant","Basculin","Basculin","Sandile","Krokorok","Krookodile","Darumaka","Darmanitan","Darmanitan","Maractus","Dwebble","Crustle","Scraggy","Scrafty","Sigilyph","Yamask","Cofagrigus","Tirtouga","Carracosta","Archen","Archeops","Trubbish","Garbodor","Zorua","Zoroark","Minccino","Cinccino","Gothita","Gothorita","Gothitelle","Solosis","Duosion","Reuniclus","Ducklett","Swanna","Vanillite","Vanillish","Vanilluxe","Deerling","Sawsbuck","Emolga","Karrablast","Escavalier","Foongus","Amoonguss","Frillish","Frillish","Jellicent","Jellicent","Alomomola","Joltik","Galvantula","Ferroseed","Ferrothorn","Klink","Klang","Klinklang","Tynamo","Eelektrik","Eelektross","Elgyem","Beheeyem","Litwick","Lampent","Chandelure","Axew","Fraxure","Haxorus","Cubchoo","Beartic","Cryogonal","Shelmet","Accelgor","Stunfisk","Mienfoo","Mienshao","Druddigon","Golett","Golurk","Pawniard","Bisharp","Bouffalant","Rufflet","Braviary","Vullaby","Mandibuzz","Heatmor","Durant","Deino","Zweilous","Hydreigon","Larvesta","Volcarona","Cobalion","Terrakion","Virizion","Tornadus","Thundurus","Reshiram","Zekrom","Landorus","Kyurem","Keldeo","Meloetta","Meloetta","Genesect","Chespin","Quilladin","Chesnaught","Fennekin","Braixen","Delphox","Froakie","Frogadier","Greninja","Bunnelby","Diggersby","Fletchling","Fletchinder","Talonflame","Scatterbug","Spewpa","Vivillon","Litleo","Pyroar","Flabébé","Floette","Florges","Skiddo","Gogoat","Pancham","Pangoro","Furfrou","Espurr","Meowstic","Honedge","Doublade","Aegislash","Spritzee","Aromatisse","Swirlix","Slurpuff","Inkay","Malamar","Binacle","Barbaracle","Skrelp","Dragalge","Clauncher","Clawitzer","Helioptile","Heliolisk","Tyrunt","Tyrantrum","Amaura","Aurorus","Sylveon","Hawlucha","Dedenne","Carbink","Goomy","Sliggoo","Goodra","Klefki","Phantump","Trevenant","Pumpkaboo","Gourgeist","Bergmite","Avalugg","Noibat","Noivern","Xerneas","Yveltal","Zygarde","Diancie","Hoopa","Hoopa","Volcanion","Rowlet","Dartrix","Decidueye","Litten","Torracat","Incineroar","Popplio","Brionne","Primarina","Pikipek","Trumbeak","Toucannon","Yungoos","Gumshoos","Grubbin","Charjabug","Vikavolt","Crabrawler","Crabominable","Oricorio","Oricorio","Oricorio","Oricorio","Cutiefly","Ribombee","Rockruff","Lycanroc","Wishiwashi","Mareanie","Toxapex","Mudbray","Mudsdale","Dewpider","Araquanid","Fomantis","Lurantis","Morelull","Shiinotic","Salandit","Salazzle","Stufful","Bewear","Bounsweet","Steenee","Tsareena","Comfey","Oranguru","Passimian","Wimpod","Golisopod","Sandygast","Palossand","Pyukumuku","Silvally","Minior","Komala","Turtonator","Togedemaru","Mimikyu","Bruxish","Drampa","Dhelmise","Cosmog","Cosmoem","Solgaleo","Lunala","Nihilego","Buzzwole","Pheromosa","Xurkitree","Celesteela","Kartana","Guzzlord","Necrozma","Magearna","Marshadow","Poipole","Naganadel","Stakataka","Blacephalon","Zeraora","Meltan","Melmetal"]

### biome descriptors used in map.py ##############################################################################

FOREST_SYNONYMS = ["a forest", "some trees", "a woods" ,"an aesthetic arberetum of luscious shrubbery"]
PLAINS_SYNONYMS = ["some plains" , "a vast expanse of grass ;)", "a flowing green field", "the open expanse of nature", "an open prairie", "wide lowlands"]
DESERT_SYNONYMS = ["an expanse of dunes", "a desert", "naked golden fields of sand", ]
MOUNTAINS_SYNONYMS = ["a specious assortment of unbridled peaks", "some mountains", "shimmering peaks of aestitic rapture", "huge rocks", "just a fucking ton of huge gigantic fucking rocks"]
TRANSIT_SYNONYMS = ["You walk past" ,"You stroll your way toward", "You thought there was nothing but when you turned around you saw", "On your left you see",
         "Enjoying the nice weather, you suddenly come accross", "Half asleep, you notice", "Not paying attention, you almost fail to take notice of", "You hear someone say,\"" + getMotherlyPlattitude() + "\" but when you turn around it was only" ]

### verbs ##############################################################################

# if ends with * , the sentence reads without trailing "you!" ex. the monster is attempting to critisize your outfit!
# else, sentence reads with trailing you ex. the monster is trying to strike you!
ATTACK_VERBS = ["scratch", "bite", "punch", "insult", "kick", "lick", "attack", "assult", "elbow", "curb-stomp"
, "stab", "spin-kick", "charge", "strike", "pounce upon", "rush", "seduce", "tickle", "roundhouse-kick", "combo", 
"abuse", "rangle", "criticize your outfit!*", "destroy", "deconstruct", "direct unfavorable criticism against",
"argue about political matters with", "assail", "gossip about you behind your back!*" , "take you on a one way trip to pain town!*",
"engage",]
ATTACK_VERBS_EXTREME = ["nuke", "fireblast", "falcon punch", "no-scope", "ult"]

### onomatopoeia ##############################################################################

PAIN_NOISES = ["Youch!", "Oof!", "Ouch!", "Owwee!", "That has got to hurt.", "Should have dodged that.", 
    "That looked like it hurt!", "Dang!", "Ooch!", "Ow!", "~ouch~"]



# ex.
#print "look out! here comes a " + getRandomDankAdjective() + " " + getRandomEnemyName("forest")
