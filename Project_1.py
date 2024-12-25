"""Snake, water, Gun Game 

project 1 """



"""
1 = snake
2 = water
3 = gun
"""
import random


computer = random.choice([1, 2, 3])
youstr = input("Enter your choise: ")
youdict = {"snake": 1, "water": 2, "gun": 3}

reversedict = {1: "snake", 2: "water", 3: "gun"}
you = youdict[youstr]

print(f"computer choose: {reversedict[computer]} \n you choose: {reversedict[you]}")

if (computer == you):
    print("Macth draw!")
else:
    # Series 1
    if (computer == 1 and you == 2):
        print("You lose!")

    elif (computer == 1 and you == 3):
        print("You win!")

    # Series 2
    elif (computer == 2 and you == 1):
        print("You win!")

    elif (computer == 2 and you == 3):
        print("You lose!")

    # series 3

    elif (computer == 3 and you == 1):
        print("You lose!")

    elif (computer == 3 and you == 2):
        print("you win!")

    else:
        print("Something went wrong!")