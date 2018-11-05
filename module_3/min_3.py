import random

# ----------------------------------------------------------------------
# Task 1 - Merge sort recursive
# ----------------------------------------------------------------------
L_1 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("Input list L_1:", L_1)


def merge_sort(array: list) -> list:  # create function which takes as input list
    """Return sorted list using merge sort."""
    if len(array) > 1:
        middle = len(array) // 2  # find the middle point to divide the list into two parts
        left = array[:middle]  # left part of the list
        right = array[middle:]  # right part of the list

        merge_sort(left)  # recursive call of merge_sort function with new input
        merge_sort(right)  # recursive call of merge_sort function with new input

        i = j = k = 0
        # condition for sorting
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # adding remaining items
        if i < len(left):
            array[k: k + len(left[i:])] = left[i:]
        # adding remaining items
        if j < len(right):
            array[k: k + len(right[j:])] = right[j:]

    return array


print("Output list L_1:", merge_sort(L_1))
# ----------------------------------------------------------------------
# Task 2 - Merge sort recursive reversed
# ----------------------------------------------------------------------
L_2 = random.sample(range(1, 100), 10)  # create list with 10 items in the range from 1 to 100 using random module
print("Input list L_2:", L_2)


def merge_sort_reversed(array: list) -> list:  # create function which takes as input list
    """Return reversed sorted list using merge sort."""
    if len(array) > 1:
        middle = len(array) // 2  # find the middle point to divide the list into two parts
        left = array[:middle]  # left part of the list
        right = array[middle:]  # right part of the list

        merge_sort_reversed(left)  # recursive call of merge_sort function with new input
        merge_sort_reversed(right)  # recursive call of merge_sort function with new input

        i = j = k = 0
        # condition for sorting
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        # adding remaining items
        if i < len(left):
            array[k: k + len(left[i:])] = left[i:]
        # adding remaining items
        if j < len(right):
            array[k: k + len(right[j:])] = right[j:]

    return array


print("Output list L_2:", merge_sort_reversed(L_2))
# ----------------------------------------------------------------------
# Task 3
# ----------------------------------------------------------------------
n_3 = int(input("Enter positive integer: "))  # write the number from the user to the variable
# create two lists then concatenate them and sort one list
L_3 = sorted([x for x in range(n_3) if x % 2 == 0 and x % 3 == 0] +  # list with even numbers that are divided by 3
             [x for x in range(n_3) if x % 2 == 1 and x % 5 == 0])  # list with odd numbers that are divided by 5
print("Output list L_3:", L_3)
# ----------------------------------------------------------------------
# Task 4 - Reverse list using recursion
# ----------------------------------------------------------------------
L_4 = random.sample(range(1, 20), 10)  # create list with 10 items in the range from 1 to 20 using random module
print("Input list L_4:", L_4)


def reversed_list_recur(array: list) -> list:  # create function which takes as input list
    """Return list in reversed order."""
    if len(array) < 2:  # base case
        return array  # returns a list without making any subsequent recursive calls
    # last element of the list + recursive call of the function until base case
    return [array[-1]] + reversed_list_recur(array[:-1])


print("Output list L_4:", reversed_list_recur(L_4))
# ----------------------------------------------------------------------
# Task 5 - Fibonacci using recursion
# ----------------------------------------------------------------------
n_5 = int(input("Enter positive integer: "))  # write the number from the user to the variable


def fib(number: int, dictionary: dict):
    """Return Fibonacci numbers."""
    if number in dictionary:  # if the number already in the dictionary
        return dictionary[number]  # return the corresponding value
    else:
        ans = fib(number-1, dictionary) + fib(number-2, dictionary)  # recursively find Fibonacci number
        dictionary[number] = ans  # write Fibonacci number to the dictionary
        return ans  # return Fibonacci number


d = {1: 1, 2: 2}  # initial dictionary with Fibonacci numbers
fib_list = [1]  # initial Fibonacci sequence
for item in range(1, n_5):  # iteration through items in range from 1 to user input
    if fib_list[-1] <= n_5:  # if the last element in the Fibonacci sequence is less than or equal to the user input
        fib_list.append(fib(item, d))  # append Fibonacci number to the Fibonacci sequence

print("Fibonacci sequence:", fib_list[:-1])
