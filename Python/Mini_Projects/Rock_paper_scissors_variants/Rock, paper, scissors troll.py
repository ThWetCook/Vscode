from ast import While
import random

user_wins = 0
computer_wins = 0

computer_pick = "none"

options = ["rock", "paper", "scissors"]

number = 0

# Functions
def computer_lose_pick():
    global computer_pick  # Declare to use the global variable
    if user_input == "rock":
        computer_pick = "scissors"

    elif user_input == "paper":
        computer_pick = "rock"
    elif user_input == "scissors":

        computer_pick = "paper"

def computer_win_pick():
    global computer_pick  # Declare to use the global variable
    if user_input == "rock":
        computer_pick = "paper"

    elif user_input == "paper":
        computer_pick = "scissors"

    elif user_input == "scissors":
        computer_pick = "rock"

def computer_random_pick():
    global computer_pick
    random_number = random.randint(0, 2)
    # rock 0, paper 1, scissors 2
    computer_pick = options[random_number]

# Ask name
name = input("Type your name to begin: ").lower()

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    # Fun begins 😁
    if name == "yanneke":
        if number == 0:
            computer_lose_pick()
        elif number >= 2:
            computer_win_pick()

        number += 1
        if number > 2:
            number = 0
    
    elif name == "isolde":
        computer_win_pick()

    elif name == "lennert":
        computer_lose_pick()

    else:
        computer_random_pick()

    print("Computer picked", str(computer_pick) + ".")

    if (user_input == "rock" and computer_pick == "scissors") or \
       (user_input == "paper" and computer_pick == "rock") or \
       (user_input == "scissors" and computer_pick == "paper"):
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

if name == "yanneke":
    print(f"{name}, I had expected more of you :) You won {user_wins} times. Get good")
    print(f"The computer won {computer_wins} times.")  

elif name == "isolde":
    print("Idiot. Get better. You didn't even win once.")
    print(f"The computer won {computer_wins} times.")

elif name == "lennert":
    print(f"I had expected no less of you. You're the best at playing against a bot. You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")

else:
    print(f"{name}, you won {user_wins} times.")
    print(f"Goodbye {name}!")
