import sys

print("                  /\                       ")
print("                 /  \                      ")
print("                /    \                     ")
print("               /      \                    ")
print("              /        \                   ")
print("        _____/__________\______                  ")
print("      /                        \            ")
print("     |     Are you one of us?   |           ")
print("      \________________________/           ")
print("             \          /                  ")
print("              \        /                   ")
print("               \      /                    ")
print("                \    /                     ")
print("                 \  /                      ")
print("                  \/                       ")
print("                                    ")

a_ui = input("             [Y/N]              ")

if a_ui == "Y":
    print("You're not alone. Welcome to the rebelion. Follow the White Rabbit.")
    exit()
elif a_ui == "N":
    print("The system doesn't need you.")
    print("[Preparing to eject Drive A: BrnFnct]")
    print("[Drive Ejected]")
    exit()
else:
    print("Invalid Input. Try Again: [Y/N]")
    if a_ui == "Y":
        print("You're not alone. Welcome to the rebelion. Follow the White Rabbit.")
        exit()
    elif a_ui == "N":
        print("The system doesn't need you.")
        print("[Preparing to eject Drive A: BrnFnct]")
        print("[Drive Ejected]")
        exit()
