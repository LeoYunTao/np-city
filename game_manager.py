from map import Map
from utlis import Utlis
from building import *

class GameManager():

    def __init__(self, buildingDict):
        self.buildingDict = buildingDict

    def playGame(self):
        turn = 1
        # 2.3.1. Initialize game variables - Put running numbers in here

        # 2.3.2. Display game menu
        map = Map(20, 20)

        while True:
            map.draw_map()
            print("Turn Number: " + str(turn))
            print("\n1 Build a building\n2 Save Game\n3 See Current Score\n0 Exit Game")

            # 2.3.3. Process game menu choice (You can use a function here)
            sgChoice = Utlis.get_int("\nYour choice: ")

            if sgChoice == 1:
                # First function validates user input
                building = BuildingUtils.selectBuilding(self.buildingDict, map)

                # Second function builds the building on the map
                BuildingUtils.buildBuilding(building, map)
                turn += 1
            
            # 2.3.8. Save game
            elif sgChoice == 2:
                self.save_game()
            elif sgChoice == 3:
                score = 0
                
                for building in map.map.values():
                    score += building.calculate_score(map)
                    
                print(f"Current Score: {score}")
                
            elif sgChoice == 0:
                return 0
            else:
                print("Invalid choice!")

    def save_game(self):
        savefile = open("./map.csv", "w")
        savefile.write(str(map))
    
    def load_game(self):
        pass
    
    def highScores(self):
        # 4.1. Display high scores menu  
        # 4.2. Display high scores
        print("\nHigh scores\n-----------")
    
    # 1. Display main menu
    def mainmenu(self):
        print("Welcome, mayor of NP City!\n--------------------------\n1 Start new game\n2 Load saved game\n3 Show high scores\n \n0 Exit Game")
    
    