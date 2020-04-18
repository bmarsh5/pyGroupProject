    
## Computes the size of the pile of balls after the user makes a choice.
# @ballCount Takes the current pile size.
# @return Returns the new calculated ball count
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
