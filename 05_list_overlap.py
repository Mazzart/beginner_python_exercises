"""
Take two lists and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

Extras:

1) Randomly generate two lists to test this
2) Write this in one line of Python
"""
import random

# Random generation of two lists
length_first_list = int(input("Please enter the length of the first list (<101): "))
length_second_list = int(input("Please enter the length of the second list (<101): "))
first_list = random.sample(range(100), length_first_list)
second_list = random.sample(range(100), length_second_list)


def common_in_list(list_1: 'list', list_2: 'list') -> 'list':
    """Returns a list that contains common elements in two lists"""
    if len(list_1) >= len(list_2):
        new_list = [item for item in list_1 if item in list_2]
    else:
        new_list = [item for item in list_2 if item in list_1]
    return new_list


if __name__ == "__main__":
    print(common_in_list(first_list, second_list))
