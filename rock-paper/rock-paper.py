import random

def play():
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    user = input("\nWhat's your choice? 'r' for Rock, 'p' for Paper, 's' for Scissors: ").lower()
    while user not in choices:
        user = input("Invalid input! Please enter 'r', 'p', or 's': ").lower()

    computer = random.choice(['r', 'p', 's'])

    print(f"\nYou chose {choices[user]}.")
    print(f"The computer chose {choices[computer]}.")

    if user == computer:
        return "It's a tie!"
    
    if is_win(user, computer):
        return "You won! 🎉"
    
    return "You lost! 😢"

def is_win(player, opponent):
    # r > s, s > p, p > r
    return (player == "r" and opponent == "s") or \
           (player == "s" and opponent == "p") or \
           (player == "p" and opponent == "r")

# Run the game
print(play())
