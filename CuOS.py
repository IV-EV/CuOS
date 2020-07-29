import time, os, shelve

#Define saving function
def savegame(savenum):
    #save file(s) i/o
    with shelve.open('PlayerSave') as save:
        save['Progress'] = savenum

#Auto i/o
def poscheck():
    with shelve.open('PlayerSave') as save:
        gamepos = save['Progress']
        return gamepos

#Define start ASCII art as a function for later call if needed
def startMessage():
    #Clear screen
    os.system("cls")
    #Print ASCII art
    print("""                               /\\
                              /  \\
                             /    \\
                            /      \\
                           /        \\
                     _____/__________\______
                    /                        \\
                   |     Are you one of us?   |
                    \________________________/
                          \          /
                           \        /
                            \      /
                             \    /
                              \  /
                               \/
                                                    """)

#Define check for when user is inputting for the first time
def falseCheck():
    #Return input in lowercase
    return input("[Y/N] ").lower()

#Define check for when user is inputting again after an invalid input
def trueCheck():
    #Return input in lowercase
    return input("Invalid input.\n[Y/N] ").lower()

#Definition of starting choice
def startGame(again):

    #Perform either falseCheck or trueCheck depending on
    #whether user is going again
    if again == False:
        #Assign user response to variable "usrInput"
        usrInput = falseCheck()
    if again == True:
        #Assign user response to variable "usrInput"
        usrInput = trueCheck()

    #Display message based on user input
    if usrInput == "y":
        print("You're not alone. Welcome to the rebellion."
        " Follow the White Rabbit.")
        exit()
    elif usrInput == "n":
        print("""The system doesn't need you.
        [Preparing to eject Drive A: BrnFnct]
        [Drive Ejected]""")
        exit()
    if usrInput == "restart":
        startMessage()
        startGame(False)
    else:
        #If input is not "y" or "n", startGame with again set to True
        startGame(True)

try:
    if poscheck() == 0:
        #Show start message
        startMessage()

        #Start game by calling first choice
        startGame(False)
    else:
        print('yeet')
except:
    print('failed ya fuck')
    exit()
