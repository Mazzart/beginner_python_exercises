"""There are four tasks in this program:
Task 1: Fast sorting
Task 2: Closest sum of 2 numbers in the list to the entered number
Task 3: Smallest sum of 2 numbers that are formed from the list of digits
Task 4: Heap sort
"""

import random

# ---------------------------------------------------------------------
# Task 1 - Fast sorting
# ---------------------------------------------------------------------
# create list with 10 items in the range from 1 to 100 using random module
L_1 = random.sample(range(1, 100), 10)
print("Task 1 answer:\nInput list L_1:", L_1)


def quick_sort_growing(list_num: list) -> list:
    """Return the sorted list in growing order"""

    if len(list_num) < 2:  # if length of the list is less than 2
        return list_num  # return input list
    else:
        # randomly choose a number from list_num and write it to the variable pivot
        pivot = list_num[random.choice(range(len(list_num)))]
        # create list where all numbers is less than pivot
        less_part = [i for i in list_num[:] if i < pivot]
        # create list where all numbers is greater than pivot
        greater_part = [i for i in list_num[:] if i > pivot]
        # recursive call of the function with less part (greater part) until base case
        return quick_sort_growing(less_part) + [pivot] + quick_sort_growing(greater_part)


print("Output list L_1:", quick_sort_growing(L_1))
# ---------------------------------------------------------------------
# Task 2 - Closest sum of two numbers in the list to the entered number
# ---------------------------------------------------------------------
sum_of_two, closest_num = 0, 0
position_i = None
position_j = None
checker = True

while checker:
    # check whether there are list_length and number integers
    try:
        list_length = int(input("\nEnter the length of the list: "))
        number = int(input("Enter your number: "))
        checker = False
    # if not, print the message and repeat until the list_length and number are integer numbers
    except ValueError:
        print("Enter positive integer.")

# create list with list_length items in the range from 0 to list_length * 10 using random module
L_2 = random.sample(range(list_length * 10), list_length)
L_2.sort()
i, j = 0, list_length-1

while i < j:
    sum_of_two = L_2[i] + L_2[j]
    if sum_of_two > number:
        j -= 1
    else:
        if sum_of_two > closest_num:
            closest_num = sum_of_two
            position_i = i
            position_j = j
        i += 1

# if statement for cases when sum_of_two always greater then number
if closest_num == 0:
    print("The sum of two closest numbers is not found.")
# otherwise print result
else:
    print("\nTask 2 answer:\nInput list:", L_2)
    print("Closest number is:", closest_num,
          "which is the sum of two numbers:",
          (L_2[position_i], L_2[position_j]))
# ---------------------------------------------------------------------
# Task 3 - Find the smallest sum of two numbers that are formed from
# the list of digits. [4, 3, 8, 6, 1] -> 184 (148 + 36)
# ---------------------------------------------------------------------
lst = [random.choice(range(10)) for i in range(5)]
example_lst = [4, 3, 8, 6, 1]
print("\nTask 3 answer:")
print(f"Input lists: {lst, example_lst}")


def min_sum(array):
    """Return smallest sum of 2 numbers
       that are formed from the list of digits"""

    array.sort()

    x = y = 0
    for num in range(len(array)):
        if num % 2 != 0:
            x = x * 10 + array[num]
        else:
            y = y * 10 + array[num]

    print(f"First number: {x}")
    print(f"Second number: {y}")
    return x + y


print(f"Sum for the lst: {min_sum(lst)}")
print(f"Sum for the example_lst: {min_sum(example_lst)}")
# ---------------------------------------------------------------------
# Task 4 - Heap sort
# ---------------------------------------------------------------------
# create list with 10 items in the range from 1 to 100 using random module
L_4 = random.sample(range(1, 100), 11)
print("\nTask 4 answer:\nInput list L_4:", L_4)


def heap_sort(array: list) -> list:
    """Return sorted list using heap sort"""

    def down_heap(array, k, n):
        """Build the heap in array so that largest value is at the root"""
        new_elem = array[k]
        while k <= n / 2:
            child = 2 * k
            if child < n and array[child] < array[child + 1]:
                child += 1
            if new_elem >= array[child]:
                break
            array[k] = array[child]
            k = child
        array[k] = new_elem

    size = len(array)
    for i in range(round(size / 2 - 1), -1, -1):
        down_heap(array, i, size - 1)
    for i in range(size - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        down_heap(array, 0, i - 1)

    return array


print("Output list L_4:", heap_sort(L_4))
