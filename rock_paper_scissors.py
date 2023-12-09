import random

user_wins=0
computer_wins=0

options = ["rock","paper","scissors"]



while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    #Here we take a random number that takes an input value and assigns 0,1,2 to rock, paper and scissors respectively

    computer_pick = options[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        continue

    else:
        print("You Lost!")
        computer_wins += 1



print("You Won", user_wins, "times.")
print("the computer", computer_wins, "times.")

print("Goodbye!")


