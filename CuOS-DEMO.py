import time, os

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
    return input("[Y/N] ")

#Define check for when user is inputting again after an invalid input
def trueCheck():
    return input("Invalid input.\n[Y/N] ")

#Definition of starting choice
def startGame(again):

    #Perform either falseCheck or trueCheck depending on whether user is going again
    if again == False:
        #Assign user response to variable "usrInput"
        usrInput = falseCheck()
    if again == True:
        #Assign user response to variable "usrInput"
        usrInput = trueCheck()

    #Display message based on user input
    if usrInput == "y":
        print("You're not alone. Welcome to the rebellion. Follow the White Rabbit.")
        exit()
    elif usrInput == "n":
        print("""The system doesn't need you.
        [Preparing to eject Drive A: BrnFnct]
        [Drive Ejected]""")
        exit()
    else:
        #If input is not "y" or "n", startGame with again set to True
        startGame(True)


#Show start message
startMessage()

#Start game by calling first choice
startGame(False)
