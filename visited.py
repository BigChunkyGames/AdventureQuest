visitedareas = {}

def visited():
    try:
        if visitedareas['tavern']:  # If 'tavern' is in 'visitedareas' dictionary
            pass
        return True
    except KeyError:  # If 'tavern' is not in 'visitedareas' dictionary
        visitedareas['tavern'] = True
        return False

print(visited())
print(visited())
print(visited())