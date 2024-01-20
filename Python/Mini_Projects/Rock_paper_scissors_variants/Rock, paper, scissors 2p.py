from ast import While
from getpass import getpass as input

user1_wins = 0
user2_wins = 0

options = ["rock", "paper", "scissors", "100%"]

while True:
    user1_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        continue

    user2_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        continue

    if user1_input == user2_input:
        print("Tie! No one earns a point!")

    elif user1_input == "100%":
        print("User 1 won!")
        user1_wins += 1

    elif user2_input == "100%":
        print("User 2 won!")

    elif((user1_input == "rock" and user2_input == "scissors") or
        (user1_input == "paper" and user2_input == "rock") or
        (user1_input == "scissors" and user2_input == "paper")):
        print("User 1 won!")
        user1_wins += 1

    else:
        print("User 2 won!")
        user2_wins += 1


print(f"User 1 won {user1_wins} times.")
print(f"User 2 won {user2_wins} times.")
print("Goodbye!")