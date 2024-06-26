
import random

response = "y"

while response == "y":
    num = random.randint(1, 6)  # Generate a random number between 1 and 6

    print("You rolled a dice...")
    print("---------")
    if num == 1:
        print("|       |")
        print("|   o   |")
        print("|       |")
    elif num == 2:
        print("| o     |")
        print("|       |")
        print("|     o |")
    elif num == 3:
        print("| o     |")
        print("|   o   |")
        print("|     o |")
    elif num == 4:
        print("| o   o |")
        print("|       |")
        print("| o   o |")
    elif num == 5:
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
    elif num == 6:
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
    print("---------")

    response = input("Do you want to roll again? (y/n): ")
    print()
