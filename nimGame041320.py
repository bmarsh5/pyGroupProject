
from random import randint

def main():

    whoseTurn = 1
    ballCount = 0
    mode = 0

    whoseTurn = turnFunction()

    ballCount = ballCountFunction()

    mode = computerMode()


    while ballCount >= 2 :
        if whoseTurn == 0 :
            #PC turn
            if mode == 0 or ballCount == 3 or ballCount == 7 or ballCount == 15 or ballCount == 31 or ballCount == 63 :
                print("computer acting in dumb mode")
                ballCount = computerDumbMode(ballCount)
                print("The ball count is now",ballCount, "\n")
                whoseTurn = 1
            else :
                print("computer acting in smart mode")
                ballCount = computerSmartMode(ballCount)
                whoseTurn = 1
                print("Computer removed balls to make the pile:", ballCount,"balls\n")
        else :
            #Player turn
            print("Player's turn")
            ballCount = playerTurn(ballCount)
            print("The ball count is now:",ballCount,"balls\n")
            whoseTurn = 0
            
    if ballCount == 1 :
        if whoseTurn == 0 :
            print("Computer loses and Player wins!!!!")
        else :
            print("Player loses and Computer wins")
                  

def turnFunction() :
    turn = randint(0,1)
    print("Turn =", turn)
    return turn


def ballCountFunction() :
        result = randint(10,100)
        print("Ball count is ",result)
        return result

def computerMode() :
    computerMode = randint(0,1)
    print("Computer =", computerMode)
    return computerMode

def computerDumbMode(ballCount): 
    ##Bryan
    halfOfBalls = ballCount//2     
    dumbBallCount = randint(1,halfOfBalls)    
    result = ballCount - dumbBallCount    
    print("the computer takes away", dumbBallCount)    #Prints the random value to be subtracted from the pile    
    return result     
    result = computerDumbMode(ballCount)

def computerSmartMode(ballCount) :
    if  10 <= ballCount <= 28:
        return 7
    elif 29 <= ballCount <= 46:
        return 15
    elif 47 <=  ballCount <= 64:
        return 31
    elif 65 <= ballCount <= 100:
        return 63
    elif ballCount == 2 :
        return 1
    else :
        return 3

# @ballCount Takes the current pile size.
# @return Returns the new calculated ball count
# Bryan    
def playerTurn (ballCount):
    playerTurn = False
    while not playerTurn:
        print("The size of the ball pile is currently:", ballCount,"balls")
        allowableChoice = ballCount//2
        print("How many balls would you like to remove?  Half of the pile size is: ", allowableChoice)
        playerChoice = input("Player chooses to remove: ")
        if playerChoice.isdigit() != True:   
           print("Your input was either negative or was not a number.  Try again :(" ) 
        else:
            playerChoice = int(playerChoice)
            if ballCount/2 < playerChoice or playerChoice == 0:
                print("Dude.  Seriously.  Follow directions.")
            else:
                ballCount -= playerChoice
                playerTurn = True
                return ballCount

main()
