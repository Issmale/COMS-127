# <Issmale Bekri>             <10/29/2022>
# <Assignment 4>


import random
import sys

START_ROOM = 1
FINAL_ROOM = 9999
currentRoom = START_ROOM
visited_room1 = False
visited_room2 = False
visited_room3 = False
visited_room4 = False
visited_room5 = False
visited_room6 = False
visited_room7 = False
playerHealth = 10
maxHealth = 10
playerAccuracy = 2

def combat(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth,goldAmount):
    enemyName = ""
    enemyHealth = 0
    enemyAccuracy = 0
    enemyDamage = 0
    halloweencharacter = random.randint(0,2)
    playerDamage = random.randint(0,3)
    print("You have entered a room with combat, HAHAHAHAHAHAHA!")
    print()
    if halloweencharacter == 0: 
        enemyName = "Michael Myers"
        maxEnemyHealth = 2
        enemyHealth = maxEnemyHealth
        enemyAccuracy = 5
        enemyDamage = 1
        print("You have encountered {0}...".format(enemyName))
        print()
        print("{0} has {1} HP and {2} ATTACK strength...".format(enemyName,enemyHealth, enemyDamage))
        print()
        print("Player has {} HP and {} attack strength...".format(playerHealth,playerAccuracy))

    elif halloweencharacter == 1:
        enemyName = "Chucky"
        maxEnemyHealth = 4
        enemyHealth = maxEnemyHealth
        enemyAccuracy = 6
        enemyDamage = 2
        print("You have encountered {0}...".format(enemyName))
        print()
        print("{0} has {1} HP and {2} ATTACK strength...".format(enemyName,enemyHealth, enemyDamage))
        print()
        print("Player has {} HP and {} attack strength...".format(playerHealth,playerAccuracy))

    elif halloweencharacter == 2: 
        enemyName = "IT"
        maxEnemyHealth = 6
        enemyHealth = maxEnemyHealth 
        enemyAccuracy = 7
        enemyDamage = 3
        print("You have encountered {0}...".format(enemyName))
        print()
        print("{0} has {1} HP and {2} ATTACK strength...".format(enemyName,enemyHealth, enemyDamage))
        print()
        print("Player has {} HP and {} attack strength...".format(playerHealth,playerAccuracy))


    else:
        print("Error - 'combat' function: 'halloween character' value is invalid:", halloweencharacter)

    
    currentTurn = random.randint(0, 1)
    if currentTurn == 0:
        print("It is the player's turn!")
        print()
    else:
        print("{0} has struck first!".format(enemyName))
    print()

    
    while playerHealth > 0 and enemyHealth > 0:
        if currentTurn == 0: 
            
            action = input("COMBAT choice: [a]ttack, [f]lee: ")
            while action != "a" and action != "f":
                print("Invalid combat choice...")
                action = input("COMBAT choice: [a]ttack, [f]lee: ")
            print()

            
            if action == "a":
                if random.randint(0, 9) < playerAccuracy:
                    enemyHealth -= playerDamage
                    print("You have HIT {0}! Its HP is: {1} / {2}".format(enemyName,enemyHealth, maxEnemyHealth))
                    print()
                else:
                    print("You have MISSED {}...".format(enemyName))
                    print()
            elif action == "f":
                
                print("Smart choice! You have escaped the combat")
                break
    

            else:
                print("Error - 'combat' function: 'action' value is invalid:", action)

        else: 
            if random.randint(0, 9) < enemyAccuracy:
                playerHealth -= enemyDamage
                print("You have been HIT by {0}. Your HP is: {1} / {2}".format(enemyName, playerHealth, maxHealth))
                print()
            else:
                print("{0} has MISSED you...".format(enemyName))
                print()
        
        currentTurn += 1
        currentTurn %= 2
        
    
    if playerHealth > 0 and enemyHealth <= 0:
        print("Congratulations! You have defeated {0}...".format(enemyName))
        
       
    elif playerHealth > 0 and enemyHealth > 0:
        print("That was a close one! {0} almost got you!".format(enemyName))
       
        
    else:
        print("Sadly, {0} was victorious...".format(enemyName))
        print()
        currentRoom = FINAL_ROOM
        
    return halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount, action

    
    

def shop(playerHealth,maxHealth,playerAccuracy,goldAmount):
    print("You have entered a room which have a shop inside of it!")
    print()
    shop = input("Please enter [Y]es if you want to shop or [N]o to leave the shop: ")
    while shop != "Y" and shop != "N":
        print()
        print("Please enter [Y]es if you want to shop or [N]o to leave the shop: ")
    if shop == "Y":
        shop_option = input("Enter [MHP]- for Max Health, [PH]- for Player Health or [PA]- for Player Accuracy, to boost it up: ")
        print()
        while shop_option != "MH" and  shop_option != "PH" and shop_option!= "PA":
            print("Invalid input.")
            print()
            shop_option = input("Please input [MH]-maxHealth, [PH]-player health or [PA]- player Accuracy to boost it up:  ")
            print()
        if shop_option == "MH":
            shop_optionMH = input("Pay 5 golds to boost your max health by 5: [Y]es or [N]o?: ")
            while shop_optionMH != "Y" and shop_optionMH != "N":
                print("Invalid...")
                shop_optionMH = input("Pay 5 golds to boost your max health by 5: [Y]es or [N]o?(make sure they are in uppercase): ")
                print()
            if shop_optionMH == "Y":
                if (goldAmount-5) < 0:
                    print("You do not have enough gold.")
                    print()
                
                else:
                    goldAmount-=5
                    maxHealth+=5
                    print("After purchasing, you currently have", goldAmount , "gold pieces in your posession and your maxHealth is: {}".format(maxHealth))
                    print()
                
            elif shop_optionMH == "N":
                print()
                print("Good luck on your adventure!")
                print()
            
            
        elif shop_option == "PH":   
            shop_optionPH = input("Pay 10 golds to boost your health by 5: [Y]es or [N]o?: ")
            print()
            while shop_optionPH != "Y" and shop_optionPH != "N":
                print("Invalid...")
                print("Invalid...")
                shop_optionPH = input("Pay 10 golds to boost your health by 5: [Y]es or [N]o?(make sure they are in uppercase): ")
                print()
            if shop_optionPH == "Y":
                if (playerHealth + 5) > maxHealth:
                    print("Error. Your player health exceeds your max health.")
                    print()
                
                elif (goldAmount-10)<0:
                    print("You do not have enough gold.")
                
                else:
                    playerHealth+=5
                    goldAmount-=10      
                    print("After purchasing, you currently have", goldAmount , "gold pieces in your posession and your playerhealth is: {}".format(playerHealth))
                    print()
                
            elif shop_optionPH == "N":
                print()
                print("Good luck on your adventure")
            
        elif shop_option == "PA":
            shop_optionPA = input("Pay 5 golds to boost your player accuracy by 1: [Y]es or [N]o?: ")
            print()
            while shop_optionPA != "Y" and shop_optionPA != "N":
                print("Invalid...")
                print()
                shop_optionPA = input("Pay 5 golds to boost your player accuracy by 1: [Y]es or [N]o?(make sure they are in uppercase): ")
                print()
            if shop_optionPA == "Y":
                if (goldAmount-5) < 0:
                    print("You do not have enough gold.")
                    print()
                else:
                    goldAmount-=5
                    playerAccuracy+=1 
                    print("After purchasing, you currently have", goldAmount , "gold pieces in your posession and your playerAccuracy is: {}".format(playerAccuracy))
                    print()

            elif shop_optionPA == "N":
                print()
                print("Good luck on your adventure!") 
                print()

    elif shop == "N":
        print()
        print("Good luck on your adventure!")
        
        print()

    return playerHealth,maxHealth,playerAccuracy,goldAmount

def navigation(currentRoom):
    if currentRoom == 1:
        direction = input("Choose a path [n]orth, [s]outh, [e]ast, [w]est?: ")
        print()
        while direction != "n" and direction != "s" and direction != "e" and direction != "w":
            print("Invalid input...")
            direction = input("Please input [n]orth, [s]outh, [e]ast, [w]est? (make sure they are lowercase): ")
    
        if direction == "n":
            currentRoom = 4
        elif direction == "s":
            currentRoom = 7
        elif direction == "e":
            currentRoom = 6
        elif direction == "w":
            currentRoom = 3
    elif currentRoom == 2:
        direction = input("Choose a path [s]outh, [w]est: ")
        print()
        while direction != "s" and direction != "s":
            print("Invalid input...")
            direction = input("Please input [s]outh, [w]est? (make sure they are lowercase): ")
    
        if direction == "s":
            currentRoom = 6
        elif direction == "w":
            currentRoom = 4

    elif currentRoom == 3:
        direction = input("Choose a path [n]orth, [e]ast: ")
        print()
        while direction != "n" and direction != "e":
            print("Invalid input...")
            direction = input("Please input [n]orth, [e]ast? (make sure they are lowercase): ")
    
        if direction == "n":
            currentRoom = 5
        elif direction == "e":
            currentRoom = 1
    
    elif currentRoom == 4:
        direction = input("Choose a path [e]ast, [w]est, [s]outh?: ")
        print()
        while direction != "e" and direction != "w" and direction != "s":
            print("Invalid input...")
            direction = input("Please input [e]ast, [w]est, [s]outh? (make sure they are lowercase): ")
    

        if direction == "e":
            currentRoom = 2
        elif direction == "w":
            currentRoom = 5
        elif direction == "s":
            currentRoom = 1

    elif currentRoom == 5:
        direction = input("Choose a path [s]outh, [e]ast?: ")
        print()
        while direction != "s" and direction != "e":
            print("Invalid input...")
            direction = input("Please input [s]outh, [e]ast? (make sure they are lowercase): ")
 
        if direction == "s":
            currentRoom = 3
        elif direction == "e":
            currentRoom = 4

    elif currentRoom == 6:

        direction = input("Choose a path [n]orth, [w]est?: ")
        print()
        while direction != "w" and direction != "n":
            print("Invalid input...")
            direction = input("Please input [n]orth, [w]est? (make sure they are lowercase): ")
    
    
        if direction == "w":
            currentRoom = 1
        if direction == "n":
            currentRoom = 2

    elif currentRoom == 7:

        direction = input("Choose a path [n]orth, [e]ast?: ")
        print()
        while direction != "n" and direction != "e":
            print("Invalid input...")
            direction = input("Please input [n]orth, [e]ast? (make sure they are lowercase): ")
    
        if direction == "n":
            currentRoom = 1
        elif direction == "e":
            currentRoom = FINAL_ROOM

    return currentRoom
        
    

def status(goldAmount, visited_room, currentRoom):
    if currentRoom == 1:
        if visited_room == False:
            gold = 10 
            print("You have entered room 1, fortunatelty there is no combat or shop in this room!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
            
        elif visited_room == True:
            print()
            print("You have already visited room 1 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 2:
        if visited_room == False:
            gold = 10 
            print("You have entered room 2!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
    
        elif visited_room == True:
            print()
            print("You have already visited room 2 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 3:
        if visited_room == False:
            gold = 10 
            print("You have entered room 3!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
    
    
        elif visited_room == True:
            print()
            print("You have already visited room 3 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 4:
        if visited_room == False:
            gold = 10 
            print("You have entered room 4!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
    
        elif visited_room == True:
            print()
            print("You have already visited room 4 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 5:
        if visited_room5 == False:
            gold = 10 
            print("You have entered room 5!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
    
        elif visited_room == True:
            print()
            print("You have already visited room 5 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 6:
        if visited_room == False:
            gold = 10 
            print("You have entered rooom 6!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room
    
        elif visited_room == True:
            print()
            print("You have already visited room 6 before...")
            print()
            return goldAmount, visited_room

    if currentRoom == 7:
        if visited_room == False:
            gold = 10 
            print("You have entered room 7!")
            print()
            print("The room has", gold, "gold pieces in it...")
            print()
            goldAmount += gold
            print("After taking the gold, you currently have", goldAmount, "gold pieces in your posession...")
            print()
            visited_room = True
            return goldAmount, visited_room

        elif visited_room == True:
            print()
            print("You have already visited room 7 before...")
            print()
            return goldAmount, visited_room



def room1(goldAmount, visited_room1, currentRoom):
    if currentRoom == 1:
       goldAmount, visited_room1 = status(goldAmount, visited_room1, currentRoom)
       currentRoom = navigation(currentRoom)
    return currentRoom, goldAmount, visited_room1

def room2(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth ,goldAmount,visited_room2,currentRoom):
    if currentRoom == 2:
        goldAmount,visited_room2 = status(goldAmount, visited_room2, currentRoom)
        halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount, action = combat(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth,goldAmount)
        if action == "f":
            currentRoom = navigation(currentRoom)
        elif playerHealth <= 0:
            currentRoom = FINAL_ROOM
        else:
            currentRoom = navigation(currentRoom)

    return currentRoom, halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth ,goldAmount,visited_room2

def room3(goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room3,currentRoom):
    if currentRoom == 3:
        goldAmount,visited_room3 = status(goldAmount, visited_room3, currentRoom)
        playerHealth,maxHealth,playerAccuracy,goldAmount = shop(playerHealth,maxHealth,playerAccuracy,goldAmount)
        currentRoom = navigation(currentRoom)
        
    return currentRoom, goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room3

def room4(goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room4,currentRoom):
    if currentRoom == 4:
        goldAmount,visited_room4 = status(goldAmount, visited_room4, currentRoom)
        playerHealth,maxHealth,playerAccuracy,goldAmount = shop(playerHealth,maxHealth,playerAccuracy,goldAmount)
        currentRoom = navigation(currentRoom)
        
    return currentRoom, goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room4

def room5(halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room5,currentRoom):
    if currentRoom == 5:
        goldAmount,visited_room5 = status(goldAmount, visited_room5, currentRoom)
        halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,action = combat(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth,goldAmount)
        if playerHealth <= 0:
            currentRoom = FINAL_ROOM
        elif action == "f":
            currentRoom = navigation(currentRoom)
        else:
            currentRoom = navigation(currentRoom)

    return currentRoom, halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room5

def room6(goldAmount,visited_room6,currentRoom):
    if currentRoom == 6:   
        goldAmount,visited_room6 = status(goldAmount, visited_room6, currentRoom)
        currentRoom = navigation(currentRoom)

    return currentRoom, goldAmount,visited_room6

def room7(halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room7,currentRoom):
    if currentRoom == 7:
        goldAmount,visited_room7 = status(goldAmount, visited_room7, currentRoom)
        halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,action = combat(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth,goldAmount)
        if playerHealth <= 0:
            currentRoom = FINAL_ROOM
        else:
            currentRoom = navigation(currentRoom)
   
    return currentRoom, halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room7


def main():
    gameOver = False
    START_ROOM = 1
    FINAL_ROOM = 9999
    START_GOLD = 0 
    goldAmount = START_GOLD
    currentRoom = START_ROOM
    visited_room1 = False 
    visited_room2 = False
    visited_room3 = False
    visited_room4 = False
    visited_room5 = False
    visited_room6 = False
    visited_room7 = False
    playerHealth = 10
    maxHealth = 10
    playerAccuracy = 2
    halloweencharacter = 0
    playerDamage = 0
    print("Welcome to Dungeon Crawl...")
    print()
    print("By: <Issmale Bekri>")
    print("[COM S 127 <B>]")
    print()

    while gameOver == False:
        choice = input("DUNGEON CRAWL GAME MENU: [p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p": 
            while currentRoom != FINAL_ROOM: 
                if currentRoom == 1:
                    currentRoom, goldAmount,visited_room1 = room1(goldAmount, visited_room1, currentRoom)
                elif currentRoom == 2:
                    currentRoom, halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth ,goldAmount,visited_room2 = room2(halloweencharacter,playerHealth, playerAccuracy, playerDamage, maxHealth ,goldAmount,visited_room2,currentRoom)
                elif currentRoom == 3:
                    currentRoom, goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room3 = room3(goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room3,currentRoom)
                elif currentRoom == 4:
                    currentRoom, goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room4 = room4(goldAmount,playerHealth,maxHealth,playerAccuracy,visited_room4,currentRoom)
                elif currentRoom == 5:
                    currentRoom, halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room5 = room5( halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room5,currentRoom)
                elif currentRoom == 6:
                    currentRoom, goldAmount,visited_room6 = room6(goldAmount,visited_room6,currentRoom)
                elif currentRoom == 7:
                    currentRoom, halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room7 = room7(halloweencharacter,playerHealth, maxHealth, playerAccuracy, playerDamage,goldAmount,visited_room7,currentRoom)
                else:
                    print("Error - currentRoom number", currentRoom, "does not correspond with available rooms")
                    sys.exit()
            
            if playerHealth > 0:
                print("Congrats! You are the winner of the Dungeon Crawl game!")
                print("You have escaped with", goldAmount, "gold from the dungeon!")
                print("Thanks for playing with us!")
            else:
                print("You have died while trying to escape the dungeon, therefore you've lost the game!")
                
            gameOver = False
            START_ROOM = 1
            FINAL_ROOM = 9999
            START_GOLD = 0 
            goldAmount = START_GOLD
            currentRoom = START_ROOM
            visited_room1 = False 
            visited_room2 = False
            visited_room3 = False
            visited_room4 = False
            visited_room5 = False
            visited_room6 = False
            visited_room7 = False 
            playerHealth = 10
            maxHealth = 10
            playerAccuracy = 2    

        elif choice == "i": 
            print("HELLO THERE! Welcome to spooky season.")
            print()
            print("This is the dungeon game, some rooms have shops, some rooms have combats and other have neither.")
            print()
            print("Player can go to each room and hopefully find their way out.")
            print()
            print("Use the navigation buttons to guide you through the dungeon crawl game. Good Luck!!!")
            print()

        elif choice == "q": 
            gameOver = True
            print("We are sad to see you leave...Goodbye :(")
            break
        
        else:
            print()
            print("Please enter [p], [i], or [q] (make sure they are lowercase)...")
            print()

if __name__ == "__main__":
    main()