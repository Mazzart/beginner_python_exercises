import random


# Task 1
# To make game easier - a random number will be in range from 0 to 100

secret_number = random.randint(0, 100)
checker_1 = True

print("You are playing a guessing game.\n"
      "You need to guess a secret number (from 0 to 100)\n")

while checker_1:
    try:
        guess_number = int(input("Please enter your initial guess: "))
        checker_1 = False
    except ValueError:
        print("Please enter an integer number")

while guess_number != secret_number:
    if guess_number < secret_number:
        print("Your number is lower than secret number. Try again.")
        guess_number = int(input("Please enter your guess again: "))
    elif guess_number > secret_number:
        print("Your number is higher than secret number. Try again.")
        guess_number = int(input("Please enter your guess again: "))
                           
print(f"Finally. The secret number was: {guess_number}")


# Task 2 - Fibonacci numbers
# Completed exercise in previous homework assignment
# https://github.com/Mazzart/beginner_python_exercises/blob/master/fibonacci_numbers.py


# Task 3 - Bubble sort

checker_3 = True

while checker_3:
    try:
        n = int(input('Enter the length of the list: '))
        checker_3 = False
    except ValueError:
        print('Please enter positive integer for the length')

items_list = random.sample(range(n*10), n)


def bubble_sort(rand_list: list) -> list:
    for i in range(len(rand_list)):
        swapped = False
        for j in range(len(rand_list)-1):
            if rand_list[j] > rand_list[j+1]:
                rand_list[j], rand_list[j+1] = rand_list[j+1], rand_list[j]
                swapped = True
        if not swapped:
            break
    return rand_list


bubble_sort(items_list)
print(items_list)


# Task 4 - Selection sort
# Completed exercise in previous homework assignment
# https://github.com/Mazzart/beginner_python_exercises/blob/master/selection_sort.py
