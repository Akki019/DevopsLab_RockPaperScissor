# Used when starting a new game and writing name and rounds in gamescore.txt file

def newgame(name,rounds):
    f = open("gamescore.txt", "w")
    f.write(name+'\n'+rounds)
    f.close()