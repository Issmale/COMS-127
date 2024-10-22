# Issmale Bekri          <9-26-22>
# <Assignment 3>

import random 

print("Welcome to NIMGRAB!")
print()


print("By: Issmale Bekri")
print("[COM S 127 B")
print()

# Constant values
NUM_ITEMS_LOW = 4
NUM_ITEMS_HIGH = 8
NUM_TO_TAKE_LOW = 1
NUM_TO_TAKE_HIGH = 3

# Game flow variables
gameOver = False
currentTurn = 0 


while(gameOver == False):
    start = input("[p]lay, [i]nstructions, or [q]uit?: ")
    if(start == "p"):
        number_of_items = random.randint(NUM_ITEMS_LOW,NUM_ITEMS_HIGH)
        while(number_of_items > 0): 
            if(currentTurn == 0):
                currentTurn+=1
                print("Human's Turn")
                counter1 = 0
                while(number_of_items > counter1):
                    print("|",end =" ")
                    counter1+=1 
                print()
                takeaway =int(input("Enter a integer between 1 and 3: "))
                if(takeaway >= NUM_TO_TAKE_LOW and takeaway<= NUM_TO_TAKE_HIGH):
                    print("Human has taken {0} from the pool.".format(takeaway))
                    number_of_items-=takeaway   
                else:
                    print("Wrong input please input a number between 1 and 3.") 
                        
            elif(currentTurn == 1):
                currentTurn = currentTurn // 2
                print("Computer's Turn")
                counter2 = 0
                while(number_of_items > counter2):
                    print("|",end =" ")
                    counter2+=1
                print()
                takeaway2 = random.randint(NUM_TO_TAKE_LOW,NUM_TO_TAKE_HIGH)
                if(number_of_items > 1):
                    while(takeaway2 > number_of_items):
                        takeaway2 = random.randint(NUM_TO_TAKE_LOW,NUM_TO_TAKE_HIGH)
                    print("Computer has taken {0} from the pool.".format(takeaway2))
                    number_of_items-=takeaway2
                elif(number_of_items == 2):
                    takeaway2 = 1
                    print("Computer has taken {0} from the pool.".format(takeaway2))
                    number_of_items-=takeaway2
                elif(number_of_items == 1):
                    takeaway2 = 1
                    print("Computer has taken {0} from the pool.".format(takeaway2))
                    number_of_items-=takeaway2
                elif(number_of_items == 3):
                    takeaway2 = random.randint(1,2)
                    print("Computer has taken {0} from the pool.".format(takeaway2))
                    number_of_items-=takeaway2

            else:
                print("Wrong Input.")
            
            
        if(currentTurn == 0):
            print("The COMPUTER has taken the last item... Therefore, the HUMAN Has Won!")
        else:
            print("he HUMAN has taken the last item... Therefore, the COMPUTER Has Won!")
        currentTurn = 0

    elif(start == "i"):
        print("The instructions of the game are thus: Each player, the human and the computer,take turns removing objects from a pool.")
        print("Each player can remove between NUM_TO_TAKE_LOW and NUM_TO_TAKE_HIGH items total.")          
        print("The game progresses until the last item is removed from the pool. The player to take the last item loses the game.")  

    elif(start == "q"):
        gameOver == True
        print("Goodbye!")
    else:
        print("Wrong in put please input [p]lay, [i]nstructions, or [q]uit?.")

    














