"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

secret_number = random.randrange(1, 9)


def guessing_number(secret, l, h):
    count = 0
    while True:
        guess = int(input("Please guess number between {} and {}: ".format(l, h)))
        count += 1
        if guess > secret:
            print("Secret number is lower then your number.")
        elif guess < secret:
            print("Secret number is higher then your number.")
        else:
            print(f"You are right. The secret number is {guess}.")
            print(f"You took {count} guesses.")
            game_status = input("Enter 'exit' to finish the game: ")
            if game_status == 'exit':
                break
            else:
                secret = random.randrange(1, 9)
                count = 0


guessing_number(secret_number, 1, 9)
