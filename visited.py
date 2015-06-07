def visited():
    try:
        if visited:
            print("This is your second time here.")
    except NameError:
        print("This is your first time here.")
        visited = True

visited()
visited()