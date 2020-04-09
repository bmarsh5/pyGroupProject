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

Bryan- Bartender
Jim- Meeting Organizer
Kiara- Coding expert

Sources
"""
from random import randint

def main():
    # variables 
    turn = 0
    computerMode = 0
    ballCount = 0
   
            
    # input
    #Generate a random integer between 10 and 100 for ball size. 
                #### Jim
    
    def ballCountFunction(ballCount) :
        #Jim Terry
        result = randint(10,100)
        return result

        #ballCount = ballCountFunction(ballCount)
        #print("The original pile size is", ballCount) # can be deleted when proof is there
    
    '''Generate a random integer of 0 or 1 for first turn. '''
                #### Bryan
    def turnFunction() :
        turn = randint(0,1)
        print("Turn=", turn)
        return turn

    '''Generate a random integer of 0 or 1 for computer mode (smart or stupid). '''
                #### Bryan
    def computerMode(computerMode) :
        computerMode = randint(0,1)
        print("Computer=", computerMode)
        return computerMode
    
    '''User input code to decide how many marble user chooses to take. '''
                #### Kiara


    # process formulas
    
    
    ''' Smart Mode process '''
    # In smart mode the computer takes off enough marbles to make
    # the size of the pile a power of two minus 1óthat is, 3, 7, 15, 31, or 63.
            #### Jim
    def computerSmartMode(ballCount) :

        '''Jim Terry'''
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
    
    # That is always a legal move, except when the size of the pile is currently one less than a power of two.
    # In that case, the computer makes a random legal move
            #### Kiara

    ''' Stupid Mode process '''
    def computerDumbMode(ballCount): 
        ##Bryan
        halfOfBalls = ballCount//2     
        dumbBallCount = randint(1,halfOfBalls)    
        result = ballCount - dumbBallCount    
        print("the value is dumb ball count", dumbBallCount)    #Prints the random value to be subtracted from the pile    
        return result     
        result = computerDumbMode(ballCount)

    '''User turn process '''
            #### Bryan
    def playerTurn(ballCount):
        print("The value of balls is currently:", ballCount)
        playerChoice = int(input("please enter a number to remove:"))
        ballCount -= playerChoice
        return ballCount

    
    ''' Size of pile calculation '''
    # Run the script which chooses whose turn this is, and either asks for user input or

   
    
    computerMode = computerMode(computerMode)
    ballCount = ballCountFunction(ballCount) 
    turn = turnFunction()
    
    while ballCount >= 1 :


        if turn == 0 :
            
            if computerMode == 0 and ballCount != 7 and ballCount != 15 and ballCount != 31 and ballCount != 63 : 
                ballCount = computerSmartMode(ballCount)   # smart mode
                
            else :   # dumb mode
                
                ballCount = computerDumbMode(ballCount)  
        else :
            ballCount = playerTurn(ballCount)
        print("The new ball count is:", ballCount)
            


    ####  Bryan can write an outline, based on our code, and help with logic
            #### W/ Jim & Kiara helping to code
    
    # output
    print("The size of the pile is now:", ballCount)

main()


