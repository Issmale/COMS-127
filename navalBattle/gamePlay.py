# Issmale             11-28-2022
# Assignment #6 Naval Battle

import gameBoard
import gameInput

def _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets):
    print("Human's Turn")
    print()
    gameBoard.printBoard(targetBoard,len(targetBoard[0]),len(targetBoard)-1)
    print()
    gameBoard.printBoard(humanGameBoard, len(humanGameBoard[0]), len(humanGameBoard))
    print()
    
    while True:
        try: 
            row, col = gameInput.getHumanInput()
        except Exception as e:
            print("Error Occured:",e)
            continue
        if targetBoard[row][col] == "X" or targetBoard[row][col] == "O":
            print("Please input different coordinates...")
        else:
            break
    print("The HUMAN targets coordinates ({0}, {1})".format(row,col))
    
    
    if computerGameBoard[row][col] == "@":
        computerGameBoard[row][col] = "X"
        targetBoard[row][col] = "X"
        print("Hit")
        numComputerTargets-=1
    else:
        computerGameBoard[row][col] = "O"
        targetBoard[row][col] = "O"
        print("MISS")
    

    
    return humanGameBoard, targetBoard, computerGameBoard, numComputerTargets

def _computerTurn(humanGameBoard, numHumanTargets):
   
    print("Computer's Turn")
    
    while True:
        try: 
            row, col = gameInput.getComputerInput()
        except Exception as e:
            print("Error Occured:",e)
            continue
        if humanGameBoard[row][col] == "X" or humanGameBoard[row][col] == "O":
            print("Please input different coordinates...")
        else:
            break

    
    print("The COMPUTER targets coordinates ({0}, {1})".format(row,col))
    

    
    
    if humanGameBoard[row][col] == "@":
        humanGameBoard[row][col] = "X"
        humanGameBoard[row][col] = "X"
        print("Hit")
        numHumanTargets-=1
    else:
        humanGameBoard[row][col] = "O"
        humanGameBoard[row][col] = "O"
        print("MISS")
    
    
    
    
    return humanGameBoard, numHumanTargets

def _printWinner(numComputerTargets, computerGameBoard):
    
    if numComputerTargets == 0:
        print("Human has won!")
    else:
        print("Computer Has Won")
    
    gameBoard.printBoard(computerGameBoard,len(computerGameBoard[0]),len(computerGameBoard))
    print()
    
    

    return

def runGame(humanGameBoard, targetBoard, computerGameBoard, numHumanTargets, numComputerTargets):
    
  
    currentTurn = 0 

   
    while numHumanTargets > 0 and numComputerTargets > 0:
        if currentTurn == 0:
            humanGameBoard, targetBoard, computerGameBoard, numComputerTargets = _humanTurn(humanGameBoard, targetBoard, computerGameBoard, numComputerTargets)
        else:
            humanGameBoard, numHumanTargets = _computerTurn(humanGameBoard, numHumanTargets)

        
        currentTurn += 1
        currentTurn %= 2
    
    
    _printWinner(numComputerTargets, computerGameBoard)

    return