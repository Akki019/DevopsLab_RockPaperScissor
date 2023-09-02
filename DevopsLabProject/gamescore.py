import random

# Used when starting a new game and writing name and rounds in gamescore.txt file

def newgame(name,rounds):
    f = open("gamescore.txt", "w")
    f.write(name+'\n'+rounds+'\n'+'0 0 0'+'\n'+'player AI winner')
    f.close()

def gamescoreupdate(selected,AI,winner):
    f = open("gamescore.txt", "r")

    data = f.readlines()

    scorecard=list(map(int,data[2].split()))
    scorecard[0]+=1
    if winner=='AI':
        scorecard[2]+=1
    elif winner=='Player':
        scorecard[1]+=1
    data[2]=str(scorecard[0])+' '+str(scorecard[1])+' '+str(scorecard[2])+'\n'

    record=data[3].split()
    record[0]=selected+'.jpg'
    record[1]=AI+'.jpg'
    record[2]=winner
    data[3]=record[0]+' '+record[1]+' '+record[2]

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
    

def getresult():
    f = open("gamescore.txt", "r")

    data = f.readlines()
    record=data[3].split()
    if record[2]!='AI' and record[2]!='Draw':
        record[2]=data[0]
    scorecard=data[2].split()
    f.close()
    return {'player':record[0],'AI':record[1],'winner':record[2],'playername':data[0],'playerwins':scorecard[1],'aiwins':scorecard[2]}

def ismoreround():
    f = open("gamescore.txt", "r")

    data = f.readlines()
    roundsplayed=data[2].split()[0]
    print(roundsplayed)
    print(data[1])
    if int(roundsplayed)==int(data[1]):
        return False
    else:
        return True
    

def getfinalresult():
    f = open("gamescore.txt", "r")

    data = f.readlines()
    record=data[3].split()
    scorecard=data[2].split()
    if scorecard[1]>scorecard[2]:
        winner=data[0]+' wins'
    elif scorecard[1]<scorecard[2]:
        winner='AI wins'
    else:
        winner='Draw'
    f.close()
    return {'winner':winner,'playername':data[0],'playerwins':scorecard[1],'aiwins':scorecard[2]}