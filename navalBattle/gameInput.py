# Issmale Bekri             11-28-2022
# Assignment #6 Naval Battle

import random
import gameBoard

def getHumanInput():
    loop = True
    while loop == True:
        try:
            row = int(input("Enter an integer value for the row between (0-9): "))
            while row < 0 or row > (gameBoard.GAME_BOARD_HEIGHT-1):
                print("Invalid Input: ")
                row = int(input("Enter an integer value for the row between (0-9): "))
            loop = False
        except Exception as e:
            print("Invalid Input...")
            print("An error occured:",e)
    
    loop2 = True
    while loop2 == True:
        try:
            col = int(input("Enter an integer value for the col between (0-9): "))
            while col < 0 or col > gameBoard.GAME_BOARD_HEIGHT-1:
                print("Invalid Input: ")
                col = int(input("Enter an integer value for the col between (0-9): "))
            loop2 = False
        except Exception as e:
            print("Invalid Input...")
            print("An error occured:",e) 
    
    return row, col

def getComputerInput():
  
    row = random.randint(0,(gameBoard.GAME_BOARD_WIDTH - 1))

    col = random.randint(0,(gameBoard.GAME_BOARD_WIDTH - 1))

    return row, col