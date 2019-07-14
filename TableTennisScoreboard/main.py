
def main():
    print('Welcome to Table Tennis Scoreboard V1.0')
    startSinglesGame()


def startSinglesGame():
    global playerOneScore
    global playerTwoScore
   
    while True:
        if playerOneScore < 11 and playerTwoScore < 11:
            if playerOneScore == 10 and playerTwoScore == 10:
                tiebreak()
            else:
                prompt = input('Press 1 when Player 1 scores, Press 2 when Player 2 scores :')
                if prompt == '1' or prompt == '2':
                    playerScores(prompt)
                else:
                    break
        else:
            if playerOneScore == 11:
                print('Player One wins!')
                break
            else:
                print('Player Two wins!')
                break
            

def playerScores(whoScored):
    global pointsPlayed
    global playerOneScore
    global playerTwoScore

    if whoScored == '1':
        playerOneScore += 1
    elif whoScored == '2':
        playerTwoScore += 1
    
    pointsPlayed += 1
    print('The score is: '+ str(playerOneScore) + ' / ' + str(playerTwoScore))
    
    changeService = checkService(pointsPlayed)
    if changeService == 'change':
        print('Change service')


def tiebreak():
    print('Tie break!')
    temp = 0


def reset():
    global playerOneScore
    global playerTwoScore
    playerOneScore = 0
    playerTwoScore = 0



def checkService(pointsPlayed):
    if pointsPlayed % 2 == 0:
        return('change')
    else:
        return ()


playerOneScore = 0
playerTwoScore = 0
pointsPlayed = 0
main()
