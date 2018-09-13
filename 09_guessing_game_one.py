"""
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right.

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
import random

low = 1
high = 9
secret_number = random.randrange(low, high+1)


def guessing_number(secret, l, h):
    while True:
        guess = int(input("Please guess number between {} and {}: ".format(l, h)))
        if guess > secret:
            print("Secret number is lower then your number.")
        elif guess < secret:
            print("Secret number is higher then your number.")
        else:
            print("You are right. The secret number is {}".format(guess))
            break


guessing_number(secret_number, low, high)
