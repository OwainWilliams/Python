# Increment 2 numbers by 1. If user presses 1 add 1 to player one's score
# If user presses 2, add 1 to player two's score

 
def main():
    print('Welcome to Table Tennis Scoreboard V1.0')
    startSinglesGame()

def playerScores(whoScored):
    if whoScored == '1':
        global playerOneScore
        playerOneScore += 1
    elif whoScored == '2':
        global playerTwoScore
        playerTwoScore += 1
        
    print('The score is: '+ str(playerOneScore) + ' / ' + str(playerTwoScore))


def startSinglesGame():
    global playerOneScore
    global playerTwoScore
    gameStarter = False


    while True:
        prompt = input('Press 1 when Player 1 scores, Press 2 when Player 2 scores :')
        if prompt == '1' or prompt == '2':
            if playerOneScore < 11 or playerTwoScore < 11:
                playerScores(prompt)
            else:
                if playerOneScore == 11:
                    print('Playe One Wins!!!')
                else:
                    print('Player Two Wins!!!')  
        else:
            break
    

playerOneScore = 0
playerTwoScore = 0

main()
