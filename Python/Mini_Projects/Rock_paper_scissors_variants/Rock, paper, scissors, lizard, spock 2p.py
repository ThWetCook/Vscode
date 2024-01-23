import os

def get_input_and_clear(prompt=""):
    print(prompt, end='', flush=True)
    user_input = input()
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen after Enter is pressed
    return user_input

user1_wins = 0
user2_wins = 0

options = ["rock", "paper", "scissors", "lizard", "spock", "100%"]

while True:
    user1_input = get_input_and_clear("Player 1, type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        continue

    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before prompting user2

    user2_input = get_input_and_clear("Player 2, type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user2_input == "q":
        break

    if user2_input not in options:
        continue

    print("\nPlayer 1 picked", user1_input + ".")
    print("Player 2 picked", user2_input + ".")

    if (
        (user1_input == "rock" and user2_input == "scissors") or
        (user1_input == "paper" and user2_input == "rock") or
        (user1_input == "scissors" and user2_input == "paper") or
        (user1_input == "lizard" and user2_input == "spock") or
        (user1_input == "spock" and user2_input == "scissors") or
        (user1_input == "scissors" and user2_input == "lizard") or
        (user1_input == "lizard" and user2_input == "paper") or
        (user1_input == "paper" and user2_input == "spock") or
        (user1_input == "spock" and user2_input == "rock") or
        (user1_input == "rock" and user2_input == "lizard")):
        print("\nPlayer 1 won!")
        user1_wins += 1

    elif user1_input == user2_input:
        print("\nIt's a tie! Nobody earns a point.")

    elif user1_input == "100%" and user2_input != "100%":
        print("\nPlayer 1 won!")
        user1_wins += 1

    elif user2_input == "100%" and user2_input != "100%":
        print("\nPlayer 2 won!")
        user2_wins += 1
    
    elif user1_input == "100%" and user2_input == "100%":
        print("\nIt's a tie! Nobody earns a point.")

    else:
        print("\nPlayer 2 won!")
        user2_wins += 1

    input("\nPress Enter to continue...")

print(f"\nPlayer 1 won {user1_wins} times.")
print(f"Player 2 won {user2_wins} times.")
print("Goodbye!")
