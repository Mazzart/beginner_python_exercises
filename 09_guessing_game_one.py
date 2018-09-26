"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random


def guessing_number(l, h):
    """
    Find the secret number generated randomly between l and h.
    :param l: start number
    :param h: stop number
    :return: int - secret_number between l and h
    """
    secret_number = random.randrange(l, h)
    count = 0
    while True:
        guess = int(input(f"Please guess number between {l} and {h}: "))
        count += 1
        if guess > secret_number:
            print("Secret number is lower then your number.")
        elif guess < secret_number:
            print("Secret number is higher then your number.")
        else:
            print(f"You are right. The secret number is {guess}.")
            print(f"You took {count} guesses.")
            game_status = input("Enter 'exit' to finish the game: ")
            if game_status == 'exit':
                break
            else:
                secret_number = random.randrange(l, h)
                count = 0


guessing_number(1, 9)
