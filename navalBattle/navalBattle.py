# <Issmale Bekri>             <11/26/2022>
# Assignment #6 Naval Battle

import gameBoard
import gamePlay

def main():
    
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None
    
    numHumanTargets = 0
    numComputerTargets = 0
    
    print("Welcome to Naval Battle!")
    print()
    
    
    print("By: <Issmale Bekri>")
    print("[COM S 127 <section B>]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            
            gameboardChoice = gameBoard.chooseHumanGameBoard()
            
            humanGameBoard, numHumanTargets = gameBoard.loadGameBoard(gameboardChoice)
            
            gameboardChoice = gameBoard.chooseComputerGameBoard()
            
            computerGameBoard, numComputerTargets = gameBoard.loadGameBoard(gameboardChoice)
            
            targetBoard = gameBoard.loadTargetBoard()
            
            gamePlay.runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            print("Welcome to the battle ship game!")
            print("You will be playing against the computer and trying to destroy the enemy's battle ship.")
            print("You will be swapping turns with the computer and the first one to destory the whole battle ship wins.")
            print("Good Luck!")
        elif choice == "q":
            gameOver = True
            print("Goodbye!")
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()

if __name__ == "__main__":
    main()