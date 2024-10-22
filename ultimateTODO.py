# <Issmale Bekri>             <11/2/2022>
# <Assignment 5>


import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for key, value in todoList.items():
        checking_items = item in todoList[key]
        if checking_items == True:
            itemFound = True
            keyName = key
            index = todoList[key].index(item)
    
    return itemFound, keyName, index   

def addItem(item,toList, todoList):
    itemFound,keyName,index = checkItem(item, todoList)
    if itemFound == False:
        todoList[toList].append(item)
    elif itemFound == True:
        print("{0} is already in {1} and in {2} index.".format(item,keyName,index))
        print()
    

    return todoList

def deleteItem(item, todoList):
    itemFound,keyName,index = checkItem(item, todoList)
    if itemFound == True:
        todoList[keyName].pop(index)
    elif itemFound == False:
        print("Error {0} is not found.".format(item))

    

    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound == True:
        addItem(item,toList, todoList)
    
    
    return todoList

def printTODOList(todoList):
    
    print(todoList)


    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":
            item = input("Enter an item: ")
            print()
            toList = "backlog"

            addItem(item, toList, todoList)
           
            printTODOList(todoList)

        
        elif choice == "m":
                
            length_backlog = len(todoList["backlog"])
            length_todo = len(todoList["todo"])
            length_in_progress= len(todoList["in_progress"])
            length_in_review = len(todoList["in_review"])
            length_done = len(todoList["done"])
            if length_backlog == 0 and length_todo == 0 and length_in_progress == 0 and length_in_review == 0 and length_done == 0:
                print()
                print("Error, No items to move!")
                print()
            else: 
                item = input("Enter an item: ")
                print()
                itemFound,keyName,index = checkItem(item, todoList)
                if itemFound == False:
                    print("The item does not exist...")
                    print()
                    item = input("Enter an item: ")
                    print()
                    itemFound,keyName,index = checkItem(item, todoList)
                toList = input("Choose a key: \"backlog\", \"todo\", \"in_progress\", \"in_review\", or \"done\": ")
                print()
                while toList != "backlog" and toList != "todo" and toList != "in_progress" and toList != "in_review" and toList != "done":
                    print("Invalid input...")
                    print()
                    toList = input("Choose a key: \"backlog\", \"todo\", \"in_progress\", \"in_review\", or \"done\": ")
                    print()
                moveItem(item, toList, todoList)
            
            printTODOList(todoList)


        
            
        elif choice == "d":
            item = input("Enter an item: ")
            
            deleteItem(item, todoList)
            
            printTODOList(todoList)
            
            
        elif choice == "s":
            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
            
        elif choice == "q":
            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    
    print("By: <Issmale Bekri>")
    print("[COM S 127 <B>]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()
