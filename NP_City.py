import random
# Display Welcome statement

# 1. Display main menu
def mainmenu():
    print("Welcome, mayor of NP City!\n--------------------------\n1 Start new game\n2 Load saved game\n3 Show high scores\n \n0 Exit Game")
    while True: # Validation if user does not input an integer, the program will continually prompt the user until he gives a valid input
        mmChoice = input("\nYour choice: ") # Ask user for choice
        if mmChoice.isdigit() and len(mmChoice) == 1:
            mmChoice = int(mmChoice)
            return mmChoice
        else:
            print("Please type in an integer!")
            
def startGame():
    # 2.3.1. Initialize game variables - Put running numbers in here
    #generateList()
    #generateMap()
    # 2.3.2. Display game menu
    while(True):
        print("\n1 Build a building\n2 Save Game\n3 See High Scores\n0 Exit Game")
        
    # 2.3.3. Process game menu choice (You can use a function here)
    # 2.3.4. Repeat 2.3.2. and 2.3.3. until game over
        sgChoice = input("\nYour choice: ")
        if sgChoice.isdigit() and len(sgChoice) == 1:
            sgChoice = int(sgChoice)
            
            if sgChoice == 1:
                pass
            # 2.3.8. Save game
            elif sgChoice == 2:
                pass
            # 2.3.7. Display high scores
            elif sgChoice == 3:
                pass
            elif sgChoice == 0:
                return 0
            else:
                print("Invalid choice!")
            
        else:
            print("Please type in an integer!")

def loadGame():
    # 3.1. Display load game menu
    # 3.3. Ask for file name
    # 3.4. Load game
    # 3.5. Display game menu
    startGame() #Pass parameters in

def highScores():
    # 4.1. Display high scores menu  
    # 4.2. Display high scores
    print("\nHigh scores\n-----------")
    
            
# Main Flow Of The Game----------------------------------------------------------------------------

while (True):
    mmChoice = mainmenu()
    if mmChoice == 1:
        startGame()
    elif mmChoice == 2:
        loadGame()
    elif mmChoice == 3:
        highScores()
        continue
    elif mmChoice == 0:
        break
    else:
        print("Invalid choice!")


