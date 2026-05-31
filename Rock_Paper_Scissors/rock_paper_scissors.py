import random

CHOICES = ["rock", "paper", "scissors"]
WINNING_MOVES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_player_choice():
    """Ask the player for rock, paper, scissors, or quit."""
    while True:
        choice = input("Choose rock, paper, scissors, or q to quit: ").lower().strip()

        if choice == "q":
            return "quit"

        if choice in CHOICES:
            return choice

        print("Invalid choice. Please type rock, paper, scissors, or q.")


def get_round_winner(player_choice, computer_choice):
    """Return the winner of one round."""
    if player_choice == computer_choice:
        return "tie"

    if WINNING_MOVES[player_choice] == computer_choice:
        return "player"

    return "computer"


def print_score(score):
    """Show the current score."""
    print("\nScore")
    print(f"Player: {score['player']}")
    print(f"Computer: {score['computer']}")
    print(f"Ties: {score['tie']}\n")


def play_game():
    """Play Rock Paper Scissors against the computer."""
    score = {
        "player": 0,
        "computer": 0,
        "tie": 0,
    }

    print("Welcome to Rock Paper Scissors!")
    print("Try to beat the computer. Your score is tracked after every round.\n")

    while True:
        player_choice = get_player_choice()

        if player_choice == "quit":
            print("Thanks for playing!")
            print_score(score)
            break

        computer_choice = random.choice(CHOICES)
        winner = get_round_winner(player_choice, computer_choice)

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if winner == "tie":
            print("It is a tie!")
        elif winner == "player":
            print("You win this round!")
        else:
            print("Computer wins this round!")

        score[winner] += 1
        print_score(score)


if __name__ == "__main__":
    play_game()
