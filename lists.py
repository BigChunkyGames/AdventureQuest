# The purpose of this file is to hold lists like a list of all dank memes

def getRandomDankAdjective():
    adjs = ["Dank", "Sick", "MLG", "Nice", "Dope", "Swiggity" ]
    return adjs[random.randint(0, len(adjs)-1)]