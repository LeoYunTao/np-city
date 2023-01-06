from map import Map
from utlis import Utlis
from building import *

class GameManager():

    def __init__(self, buildingDict):
        self.buildingDict = buildingDict
        self.starting_coins = 16
        self.current_coins = self.starting_coins
        self.map = Map(20, 20)
        self.score = 0

    def playGame(self):
        # 2.3.1. Initialize game variables - Put running numbers in here
        # 2.3.2. Display game menu
        
        turn = 0
        while self.current_coins > 0 and (self.map.column * self.map.row) >= turn:
            turn = len(self.map.map) + 1
            
            self.map.draw_map()
            print(f"Turn Number: {turn}")
            print(f"Coins: {self.current_coins}")
            print("\n1 Build a building\n2 Save Game\n3 See Current Score\n0 Exit Game")

            # 2.3.3. Process game menu choice (You can use a function here)
            sgChoice = Utlis.get_int("\nYour choice: ")

            if sgChoice == 1:
                # First function validates user input
                building = BuildingUtils.selectBuilding(self.buildingDict, self.map)

                # Second function builds the building on the map
                BuildingUtils.buildBuilding(building, self.map)
                
                self.current_coins = self.calculate_coins()
            
            # 2.3.8. Save game
            elif sgChoice == 2:
                self.save_game()
            elif sgChoice == 3:
                self.score = sum([building.calculate_score(self.map) for building in self.map.map.values()])
                    
                print(f"Current Score: {self.score}")
                
            elif sgChoice == 0:
                return 0
            else:
                print("Invalid choice!")
        
        #Endgame
        #Calculate finale score

        name = input("Please enter your name (Max 20 characters) : ")
        while len(name) > 20:
            print("Name exceeded 20 characters!")
            name = input("Please enter your name (Max 20 characters) : ")

        with open('leaderboard.csv','a') as csv_file:
            csv_file.write(name + "," + str(self.score) + "," + "\n")
            csv_file.close()

        self.displayhighScores()

        
    def calculate_coins(self):
        # starting coins - number of turns + sum of coins generated by the building
        return self.starting_coins - len(self.map.map) + sum([building.calculate_coins(self.map) for building in self.map.map.values()])

    def save_game(self):
        savefile = open("./map.csv", "w")
        savefile.write(str(map))
    
    def load_game(self):
        pass
    
    def displayhighScores(self):
        # 4.1. Display high scores menu  
        # 4.2. Display high scores

        highscores = [] # in format (score, playername)
        leaderboard = open("leaderboard.csv", "r")
        
        for line in leaderboard:
            line = line.strip().split(",")
            
            if line == '':
                break
                        
            highscores.append((line[1], line[0]))
            
        leaderboard.close()
        
        highscores = sorted(highscores, reverse=True)

        print("--------- HIGH SCORES ---------")
        print("{:<3} {:<22} {:<5}".format("Pos", "Player", "Score"))
        print("{:<3} {:<22} {:<5}".format("---", "------", "-----"))
        for i in range(len(highscores)):
            if i >= 10:
                break
            print("{:>2}. {:<22} {:>5}".format(i + 1, highscores[i][1] , highscores[i][0] ))

        print("-------------------------------")

            #for line in f:
                #print(line.strip())

    
    # 1. Display main menu
    def mainmenu(self):
        print("Welcome, mayor of NP City!\n--------------------------\n1 Start new game\n2 Load saved game\n3 Show high scores\n \n0 Exit Game")
    
    