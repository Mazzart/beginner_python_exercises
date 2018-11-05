import random

# ---------------------------------------------------------------------
# Task 1 - Program calculates n! recursively
# ---------------------------------------------------------------------
n_1 = int(input("Enter positive integer: "))  # write the number from the user to the variable


def factorial(n: int) -> int:  # create function to calculate factorial which takes as input integer number
    """Return factorial of a number."""
    if n == 0:  # the base case
        return 1  # returns a value without making any subsequent recursive calls
    else:
        return n * factorial(n - 1)  # recursive call of factorial function until base case


fact_of_n_1 = factorial(n_1)
print(f"Factorial of {n_1}! is {fact_of_n_1}")
# ---------------------------------------------------------------------
# Task 2 - Merge sort, first odd numbers then even
# ---------------------------------------------------------------------
# https://github.com/Mazzart/beginner_python_exercises/blob/master/merge_sort_odd_even.py
# ---------------------------------------------------------------------
# Task 3 - Sorting in the form of waves (a1 >= a2 <= a3 >= a4 <= ...)
# ---------------------------------------------------------------------
L_3 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("Input list L_3:", L_3)
L_3.sort()  # list L_3 is sorted using method sorts

wavy_L_3 = []  # create empty list
i, j = 0, -1  # initialize variables

while i != len(L_3) // 2:  # condition (when i is equal half the length of the list) to exit the while loop
    wavy_L_3.append(L_3[j])  # add to the wavy_L_3 elements by one from second half of the L_3
    wavy_L_3.append(L_3[i])  # add to the wavy_L_3 elements by one from first half of the L_3
    i += 1  # increase variable i by one
    j -= 1  # reduce variable j by one

print("Output list L_3:", wavy_L_3)
# ---------------------------------------------------------------------
# Task 4
# ---------------------------------------------------------------------
L_4 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("Input list L_4:", L_4)

even_part = [i for i in L_4 if i % 2 == 0]  # create list with even numbers from L_4
odd_part = [i for i in L_4 if i % 2 == 1]  # create list with odd numbers from L_4


def quick_sort_growing(list_num: list) -> list:
    """Return the sorted list in growing order"""

    if len(list_num) < 2:  # if length of the list is less than 2
        return list_num  # return input list
    else:
        pivot = list_num[0]  # write the first element of the input list to the variable
        less_part = [i for i in list_num[1:] if i < pivot]  # create list where all numbers is less than pivot
        greater_part = [i for i in list_num[1:] if i > pivot]  # create list where all numbers is greater than pivot
        # recursive call of the function with less part (greater part) until base case
        return quick_sort_growing(less_part) + [pivot] + quick_sort_growing(greater_part)


def quick_sort_descending(list_num: list) -> list:
    """Return the sorted list in descending order"""

    if len(list_num) < 2:  # if the length of the list is less than 2
        return list_num  # return input list
    else:
        pivot = list_num[0]  # write the first element of the input list to the variable
        greater_part = [i for i in list_num[1:] if i > pivot]  # create list where all numbers is greater than pivot
        less_part = [i for i in list_num[1:] if i < pivot]  # create list where all numbers is less than pivot
        # recursive call of the function with greater part (less part) until base case
        return quick_sort_descending(greater_part) + [pivot] + quick_sort_descending(less_part)


print("Output list L_4:", quick_sort_descending(even_part) + quick_sort_growing(odd_part))
# ---------------------------------------------------------------------
# Task 5 - Median of two sorted lists
# ---------------------------------------------------------------------
