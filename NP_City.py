import random
from building import Building
from building import Residential
from building import Industry
from building import Commercial
#from building import Park
from building import Building
from map import Map
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

            

def buildBuilding(choices, turn, map):
    bType = choices[0]
    if bType == "R":
        bPlace = Residential()
        pass
        
    elif bType == "I":
        pass
    elif bType == "C":
        pass
    elif bType == "O":
        pass
    elif bType == "*":
        pass
    else:
        print("Error!")
    return



def selectBuilding(buildingDict, map):
    choices = []
    buildErrorMsg = "Please type in a valid position map!"
    while(True): #Check building type
        print("\n(R) Residential\n(I) Industry\n(C) Commercial\n(O) Park\n(*) Road")
        bChoice = input("\nYour choice: ")
        bChoice = bChoice.upper()
        if bChoice in buildingDict:
            map.draw_map()
            print("You have selected: " + buildingDict[bChoice])
            while(True): # Check position              
                pChoice = input("Select a position: ")
                if len(pChoice) == 2:
                    if pChoice[0].isalpha() and pChoice[1].isdigit():
                        break
           
                if len(pChoice) == 3:
                    if pChoice[0].isalpha() and pChoice[1].isdigit() and pChoice[2].isdigit():
                        break
                    else:
                        print(buildErrorMsg)
                        continue
                else:
                    print(buildErrorMsg)
                    continue
            
            pChoice = pChoice[0].upper() + pChoice[1] + pChoice[2]
            choices.append(bChoice)
            choices.append(pChoice)
            return choices 
        else:
            print("Please type in a valid building!")


            
def playGame(turn):  
    turn = 1
    # 2.3.1. Initialize game variables - Put running numbers in here
    buildingDict = { # I have no idea what this is for but i feel like it can be used for something, delete and turn the keys into a list if needed
        "R": "Residential",
        "I": "Industry",
        "C": "Commercial",
        "O": "Park",
        "*": "Road"
    }                      
    # 2.3.2. Display game menu
    map = Map(20, 20)
    while(True):
        map.draw_map()
        print("Turn Number: " + str(turn))
        print("\n1 Build a building\n2 Save Game\n3 See High Scores\n0 Exit Game")
         
    # 2.3.3. Process game menu choice (You can use a function here)
        sgChoice = input("\nYour choice: ")
        if sgChoice.isdigit() and len(sgChoice) == 1:
            sgChoice = int(sgChoice)
            
            if sgChoice == 1:
                #First function validates user input
                choices = selectBuilding(buildingDict, map) # I dont want do everything in one function legit headache , break it up
                print(choices)
                #Second function builds the building on the map
                buildBuilding(choices, turn, map)
                turn += 1
               
            # 2.3.8. Save game
            elif sgChoice == 2:
                turn += 1
                pass
            # 2.3.7. Display high scores
            elif sgChoice == 3:
                turn += 1
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
    playGame() #Pass parameters in


    
    
def highScores():
    # 4.1. Display high scores menu  
    # 4.2. Display high scores
    print("\nHigh scores\n-----------")
    
  
    
    
# Main Flow Of The Game----------------------------------------------------------------------------
turn = 1

while (True):
    mmChoice = mainmenu()
    if mmChoice == 1:
        playGame(turn)
    elif mmChoice == 2:
        loadGame()
    elif mmChoice == 3:
        highScores()
        continue
    elif mmChoice == 0:
        break
    else:
        print("Invalid choice!")


