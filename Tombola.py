import random

def generate_game_numbers():
    # Generate 10 unique random numbers between 1 and 50
    return random.sample(range(1, 51), 10)

def create_players(n):
    players = {}
    for i in range(1, n + 1):
        # Each player gets 10 unique random numbers
        players[f"Player_{i}"] = {
            "numbers": set(random.sample(range(1, 51), 10)),
            "marked": set()
        }
    return players

def play_game(players, game_numbers):
    print("\nGame Numbers to be Called:")
    print(game_numbers)
    print("\nStarting Number Calling...\n")

    winner_found = False

    # Call all 10 numbers
    for number in game_numbers:
        print(f"Number Called: {number}")

        for player_name, data in players.items():
            if number in data["numbers"]:
                data["marked"].add(number)
                print(f"{player_name} marked {number}")

                # Check if all 10 numbers are matched
                if data["marked"] == data["numbers"]:
                    print(f"\n🎉 {player_name} is the WINNER! 🎉")
                    winner_found = True

        print("-" * 40)

    if not winner_found:
        print("\nNo player matched all 10 numbers.")

def main():
    n = int(input("Enter number of players: "))

    game_numbers = generate_game_numbers()
    players = create_players(n)

    print("\nPlayers and Their Numbers:")
    for name, data in players.items():
        print(f"{name}: {sorted(data['numbers'])}")

    play_game(players, game_numbers)

if __name__ == "__main__":
    main()
