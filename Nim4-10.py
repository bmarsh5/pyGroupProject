
"""
Name:
CSC 119-001
Date:040220
Program Name:nimGame
Description:
            From a pile of marbles, a player or the computer may take up to
            half of the marbles on each turn.  The player who takes the last
            marble loses.

            You will note that the computer cannot be beaten in smart mode when it has the
            first move, unless the pile size happens to be 15, 31, or 63. 
            Of course, a human player who has the first turn and knows the winning strategy
            can win against the computer.
Members:
    Bryan
    Jim
    Kiara

Sources-
    general knowledge
    
"""

from random import randint

def main():
    # variables 
    turn = 0
    computerMode = 0
    ballCount = 0
    playerChoice = 0
    halfOfBalls = 0
    dumbBallCount = 0


## Computes the size of the pile of balls after the user makes a choice.
# @ballCount Takes the current pile size.
# @return Returns the new calculated ball count
# Bryan    
def playerTurn (ballCount):
    playerTurn = False
    while not playerTurn:
        print("The size of the ball pile is currently:", ballCount,"balls")
        allowableChoice = ballCount//2
        print("How many balls would you like to remove?  Half of the pile size is: ", allowableChoice)
        playerChoice = input("Player removes: ")
        if playerChoice.isdigit() != True:   
           print("Your input was either negative or was not a number.  Try again :(" ) 
        else:
            playerChoice = int(playerChoice)
            if ballCount/2 <= playerChoice or playerChoice == 0:
                print("Dude.  Seriously.  Follow directions.")
            else:
                ballCount -= playerChoice
                playerTurn = True
                return ballCount

## Computes the ball count.
# @ballCount is randomly generated between 10 and 100
# @return Returns the new calculated ball count
# Jim
def ballCountFunction(ballCount) :
        result = randint(10,100)
        return result

##Generate a random integer of 0 or 1 for first turn.
# @turn is the random 0 or 1.
# @return Returns a 0 or 1
def turnFunction() :
    turn = randint(0,1)
    print("Turn=", turn)
    return turn

## Computes a 0 or 1 to determine dumb or smart mode.
# @computerMode is a random 0 or 1
# @return the computer mode
# 
def computerMode(computerMode) :
    computerMode = randint(0,1)
    print("Computer=", computerMode)
    return computerMode

## Computes the smart mode and ballcount
# @ballCount - previously calculated
# @return Returns the new calculated ball count
#Jim
def computerSmartMode(ballCount) :
    if  10 <= ballCount <= 28:
        return 7
    elif 29 <= ballCount <= 46:
        return 15
    elif 47 <=  ballCount <= 64:
        return 31
    elif 65 <= ballCount <= 100:
        return 63
    else :
        return 3

## Computes 
# 
# @return
# Bryan

def computerDumbMode(ballCount): 
    ##Bryan
    halfOfBalls = ballCount//2     
    dumbBallCount = randint(1,halfOfBalls)    
    result = ballCount - dumbBallCount    
    print("the value is dumb ball count", dumbBallCount)    #Prints the random value to be subtracted from the pile    
    return result     
    result = computerDumbMode(ballCount)

##
#    
#
# Bryan
def playerChoice() :
    return result

main()    

