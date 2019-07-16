
class Player:
    def __init__(self, score):
        self.score = score



def main():
    print('Welcome to Table Tennis Scoreboard V1.0')
    playerone = Player(0)
    playertwo = Player(0)

    startsinglesgame(playerone, playertwo)


def startsinglesgame(playerone, playertwo):
    while True:
        if playerone.score < 11 and playertwo.score < 11:
            if playerone.score == 10 and playertwo.score == 10:
                tiebreak()
            else:
                prompt = input('Press 1 when Player 1 scores, Press 2 when Player 2 scores :')
                if prompt == '1' or prompt == '2':
                    playerscores(prompt, playerone, playertwo)
                else:
                    break
        else:
            if playerone.score == 11:
                print('Player One wins!')
                break
            else:
                print('Player Two wins!')
                break
            

def playerscores(whoscored, playerone, playertwo):
    global pointsPlayed
    if whoscored == '1':
        playerone.score += 1
    elif whoscored == '2':
        playertwo.score += 1
    
    pointsPlayed += 1
    print('The score is: '+ str(playerone.score) + ' / ' + str(playertwo.score))
    
    changeService = checkService(pointsPlayed)
    if changeService == 'change':
        print('Change service')


def tiebreak():
    print('Tie break!')
    temp = 0


def reset():
    playerOneScore = 0
    playerTwoScore = 0



def checkService(pointsPlayed):
    if pointsPlayed % 2 == 0:
        return('change')
    else:
        return ()


pointsPlayed = 0
main()
