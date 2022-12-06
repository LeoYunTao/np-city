import random
# Display Welcome statement

# 1. Display main menu
def mainmenu():
    print("Welcome, mayor of NP City!\n--------------------------\n1 Start new game\n2 Load saved game\n3 Show high scores\n \n0 Exit Game")
    while True: # Validation if user does not input an integer, the program will continually prompt the user until he gives a valid input
        mmChoice = input("\nYour choice: ") # Ask user for choice
        if mmChoice.isdigit() and len(choice) == 1:# Check if user input a string that can be converted into integer and has a length of one
            choice = int(choice)# Convert the user input into integer
            return choice# Return it to the main program
        else:
            print("Please type in an integer!")# Tell the user what he needs to input if he does not know
            
def startGame():
    # 2.1. Display start game menu
    print("You have selected: Start new game")
    
    # 2.2. Process start game menu choice
   
    # 2.3. Start game
    # 2.3.1. Initialize game variables
    
    # 2.3.2. Display game menu
    while True:
        print("\n ") #Insert display options here like line 6
        sgChoice = input("\nYour choice: ")
        if sgChoice.isdigit() and len(choice) == 1:
            choice = int(choice)
            return choice
        else:
            print("Please type in an integer!")
    # 2.3.3. Process game menu choice (You can use a function here)
    if sgChoice == 1:
        pass
    elif sgChoice == 2:
        pass
    elif sgChoice == 3:
        pass
    elif sgChoice == 0:
        pass
    else:
        print("Invalid choice!")
    # 2.3.4. Repeat 2.3.2. and 2.3.3. until game over
    # 2.3.5. Display game over message
    # 2.3.6. Display game statistics
    # 2.3.7. Display high scores
    # 2.3.8. Ask if user wants to save game
    # 2.3.9. If yes, ask for file name
    # 2.3.10. Save game
    # 2.3.11. Display main menu

def loadGame():
    # 3.1. Display load game menu
    # 3.3. Ask for file name
    # 3.4. Load game
    # 3.5. Display game menu
    print("\n") # Display options like line 6
    while True:
        lgChoice = input("\nYour choice: ")
        if lgChoice.isdigit() and len(choice) == 1:
            choice = int(choice)
            return choice
        else:
            print("Please type in an integer!")
    # 3.2. Process load game menu choice (You can use same function as 2.3.3.)
    if lgChoice == 1:
        startGame()
    elif lgChoice == 2:
        loadGame()
    elif lgChoice == 3:
        highScores()
    elif lgChoice == 0:
        exitGame()
    else:
        print("Invalid choice!")
    # 3.6. Process game menu choice
    # 3.7. Repeat 3.5. and 3.6. until game over
    # 3.8. Display game over message
    # 3.9. Display game statistics
    # 3.10. Display high scores
    # 3.11. Ask if user wants to save game
    # 3.12. If yes, ask for file name
    # 3.13. Save game
    # 3.14. Display main menu

def highScores():
    # 4.1. Display high scores menu
    print("\nHigh scores\n-----------")
    # 4.2. Display high scores
    # 4.3. Display main menu
    

def processMmChoice(mmChoice):
    if mmChoice == 1:
        startGame()
    elif mmChoice == 2:
        loadGame()
    elif mmChoice == 3:
        highScores()
    elif mmChoice == 0:
        exitGame()
    else:
        print("Invalid choice!")
            
# Main Flow Of The Game----------------------------------------------------------------------------
while (True):
    mmChoice = mainmenu()
    processMmChoice(mmChoice)


