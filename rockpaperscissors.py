# Issmale Bekri        11/30/2022
# Rock Paper Scissors Game


import random

#Global Variables
human_score = 0
computer_score = 0



def winnerannounce(human_score,computer_score):
    if human_score > computer_score:
        print("Congratulations you have won!")
        print()
    elif human_score < computer_score:
        print("Unfortunately computer has won...better luck next time!")
        print()
    elif human_score == computer_score:
        print("HAHA you and the computer have tied!")
        print()
    

def gameplay(user_choice,random_computer_choice):
    global human_score
    global computer_score
    if user_choice == random_computer_choice:
        print("It is a tie! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        human_score+=1
        computer_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "rock" and random_computer_choice == "paper":
        print("Computer won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        computer_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "rock" and random_computer_choice == "scissor":
        print("Human won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        human_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "paper" and random_computer_choice == "rock":
        print("Human won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        human_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "paper" and random_computer_choice == "scissor":
        print("Computer won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        computer_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "scissor" and random_computer_choice == "rock":
        print("Computer won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        computer_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    elif user_choice == "scissor" and random_computer_choice == "paper":
        print("Human won! COMPUTER CHOICE: {0} HUMAN CHOICE: {1}".format(random_computer_choice,user_choice))
        print()
        human_score+=1
        print("SCOREBOARD | HUMAN: {0} | COMPUTER: {1}".format(human_score,computer_score))
        print()
    
    return human_score,computer_score
    


def startgame(computer_choice,num_rounds):
    global human_score
    global computer_score
    count = 1
    currentTurn = 0 

    
    while count <= num_rounds:
        if currentTurn == 0:
            currentTurn+= 1
            user_choice = input("What would you like to choose? \"rock\", \"paper\", \"scissor\": ")
            print()
            while user_choice != "rock" and user_choice != "paper" and user_choice != "scissor":
                print("Invalid input...")
                print()
                user_choice = input("What would you like to choose? \"rock\", \"paper\", \"scissor\": ")
                print()
        if currentTurn == 1:
            random_computer_choice = random.choice(computer_choice)
            currentTurn//=2
        
        human_score,computer_score = gameplay(user_choice,random_computer_choice)

        count+=1
    
    winnerannounce(human_score,computer_score)





def main():
    global human_score
    global computer_score
    print("Welcome to Rock, Paper, Scissors Game")
    print()
    print("By: <Issmale Bekri>")
    print("[COM S 127 <Section B>]")
    print()
    gameOver =  False
    computer_choice = ["rock","paper","scissor"]
    

    while gameOver == False: 
        human_score = 0
        computer_score = 0
        gameChoice = input("MAIN MENU: [p]lay, [i]nstructions, or [q]uit: ")
        print()
        
        while gameChoice != "p" and gameChoice != "i" and gameChoice != "q":

            print("Invalid input...")
            print()
            gameChoice = input("MAIN MENU: p[lay], [i]nstructions, or [q]uit: ")
            print()
       
        if gameChoice == "p":
            while True:
                try:
                    num_rounds = int(input("How many rounds would you like to play (1-12): "))
                    while num_rounds < 0 or num_rounds > 12:
                        print()
                        print("Please make sure the number is between 1 and 12.")
                        print()
                        num_rounds = int(input("How many rounds would you like to play (1-12): "))
                    print()
                    break
                except Exception as e:
                    print("An error occured {0}".format(e))
                    print()
            
            
            
            startgame(computer_choice,num_rounds)

        elif gameChoice == "i":
            print("This is the game of rock, paper, and scissors.")
            print("The user will be playing against the computer to win!")
            print("Rock smashes scissors, paper folds the rock and scissors cut paper.")
            print("This means that if it is rock vs scissors winner will be rock, if it is paper vs rock winner will be paper and if it is scissors vs paper winner will be scissors.")
            print("If the computer and user choose the same choice, then it will be a tie.")
            print("Enjoy and Good Luck!")
            print()
        
        elif gameChoice == "q":
            gameOver = True
            print("GOODBYE :/")



if __name__ == "__main__":
    main()