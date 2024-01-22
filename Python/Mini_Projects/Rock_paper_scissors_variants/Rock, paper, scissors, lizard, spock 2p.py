from getpass import getpass

user1_wins, user2_wins = 0, 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

# Functions
def get_user_input(user):
    while True:
        user_input = getpass(f"{user}, type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
        if user_input == "q":
            break

        if user_input in options:
            return user_input
        else:
            print(f"Invalid input for {user}. Please try again.")

# Main game loop
while True:
    user1_input = get_user_input("User 1")
    if user1_input == "q":
        break

    user2_input = get_user_input("User 2")
    if user2_input == "q":
        break

    print(f"\nUser 1 chose {user1_input}")
    print(f"User 2 chose {user2_input}")

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

        print("\nUser 1 won!")
        user1_wins += 1

    elif user1_input == user2_input:
        print("\nIt's a tie!")

    else:
        print("\nUser 2 won!")
        user2_wins += 1

# Print statements
print(f"User 1 won {user1_wins} times.")
print(f"User 2 won {user2_wins} times.")
print("Goodbye!")
