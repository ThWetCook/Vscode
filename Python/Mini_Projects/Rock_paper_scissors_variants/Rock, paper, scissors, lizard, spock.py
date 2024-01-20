from ast import While
import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user_input = input("Type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 4)
    # rock 0, paper, 1, scissors 2, lizard 3, spock 4
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if (
        (user_input == "rock" and computer_pick == "scissors") or
        (user_input == "paper" and computer_pick == "rock") or
        (user_input == "scissors" and computer_pick == "paper") or
        (user_input == "lizard" and computer_pick == "spock") or
        (user_input == "spock" and computer_pick == "scissors") or
        (user_input == "scissors" and computer_pick == "lizard") or
        (user_input == "lizard" and computer_pick == "paper") or
        (user_input == "paper" and computer_pick == "spock") or
        (user_input == "spock" and computer_pick == "rock") or
        (user_input == "rock" and computer_pick == "lizard")):

        print("You won!")
        user_wins += 1
        
    elif user_input == computer_pick:
        print("It's a tie!")

    else:
        print("You lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Goodbye!")
