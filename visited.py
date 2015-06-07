visitedareas = {}

def visited(area):
    try:
        if visitedareas[area]:  # If 'tavern' is in 'visitedareas' dictionary
            pass
        return True
    except KeyError:  # If 'tavern' is not in 'visitedareas' dictionary
        visitedareas[area] = True
        return False

print(visited("Tavern"))  # False
print(visited("Tavern"))  # True
print(visited("Blacksmith"))  # False
print(visited("Tavern"))  # True
