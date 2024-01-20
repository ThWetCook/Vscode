from getpass import getpass

user1_wins, user2_wins = 0, 0

options = ["rock", "paper", "scissors", "lizard", "spock"]

while True:
    user1_input = getpass("User 1, type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user1_input == "q":
        break

    if user1_input not in options:
        continue

    user2_input = getpass("User 2, type Rock/Paper/Scissors/Lizard/Spock or Q to quit: ").lower()
    if user2_input == "q":
        break

    if user2_input not in options:
        continue

    print(f"User 1 chose {user1_input}")
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

        print("User 1 won!")
        user1_wins += 1

    elif user1_input == user2_input:
        print("It's a tie!")

    else:
        print("User 2 won!")
        user2_wins += 1

print(f"User 1 won {user1_wins} times.")
print(f"User 2 won {user2_wins} times.")
print("Goodbye!")
