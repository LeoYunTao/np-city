import random
from building import *
from utlis import Utlis
from game_manager import GameManager


# Main Flow Of The Game----------------------------------------------------------------------------
buildingDict = {
    "R": Residential,
    "I": Industry,
    "C": Commercial,
    "O": Park,
    "*": Road
}

game_manager = GameManager(buildingDict)

while (True):
    game_manager.mainmenu()

    mmChoice = Utlis.get_int(input_messge="\nYour choice: ")

    if mmChoice == 1:
        game_manager.playGame()

    elif mmChoice == 2:
        game_manager.load_game()

    elif mmChoice == 3:
        game_manager.highScores()

    elif mmChoice == 0:
        break

    else:
        print("Invalid choice!")


