# Guess the number (computer)

import random


username = input("Enter your name: ")

print(f"\nHello {username}! Welcome to the Guessing Number Game🔢🤔\n")
print("____________________________")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 to {x}: "))
        if guess < random_number:
            print(f"Sorry {username}, guess again. Too Low!")
        elif guess > random_number:
            print(f"Sorry {username}, guess again. Too High!")

    print(f"Yay congrats {username}. You guess the number {random_number} correctly!!")      

guess(100)