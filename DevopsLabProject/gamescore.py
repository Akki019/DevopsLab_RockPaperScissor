import random

# Used when starting a new game and writing name and rounds in gamescore.txt file

def newgame(name,rounds):
    f = open("gamescore.txt", "w")
    f.write(name+'\n'+rounds+'\n'+'0 0 0')
    f.close()

def gamescoreupdate(winner):
    f = open("gamescore.txt", "r")

    data = f.readlines()

    scorecard=list(map(int,data[2].split()))
    scorecard[0]+=1
    if winner=='AI':
        scorecard[2]+=1
    elif winner=='Player':
        scorecard[1]+=1
    data[2]=str(scorecard[0])+' '+str(scorecard[1])+' '+str(scorecard[2])

    f.close()

    with open('gamescore.txt', 'w') as file:
        file.writelines(data)

def AI():
    options=['rock','paper','scissor']
    return random.choice(options)

def winner(selected,AI):
    if selected==AI:
        return 'Draw'
    elif ((selected=='rock' and AI=='scissor') or (selected=='scissor' and AI=='paper') or (selected=='paper' and AI=='rock')):
        return 'Player'
    else:
        return 'AI'
    