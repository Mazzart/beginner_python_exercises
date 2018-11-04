import random

# ----------------------------------------------------------------------
# Task 1 - Merge sort recursive
# ----------------------------------------------------------------------
L_1 = random.sample(range(1, 100), 10)
print("Input list L_1:", L_1)


def merge_sort(array: list) -> list:
    """Returns sorted list using merge sort."""
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        if i < len(left):
            array[k: k + len(left[i:])] = left[i:]
        if j < len(right):
            array[k: k + len(right[j:])] = right[j:]

    return array


print("Output list L_1:", merge_sort(L_1))
# ----------------------------------------------------------------------
# Task 2 - Merge sort recursive reversed
# ----------------------------------------------------------------------
L_2 = random.sample(range(1, 100), 10)
print("Input list L_2:", L_2)


def merge_sort(array: list) -> list:
    """Returns reversed sorted list using merge sort."""
    if len(array) > 1:
        middle = len(array) // 2
        left = array[:middle]
        right = array[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        if i < len(left):
            array[k: k + len(left[i:])] = left[i:]
        if j < len(right):
            array[k: k + len(right[j:])] = right[j:]

    return array


print("Output list L_2:", merge_sort(L_2))
# ----------------------------------------------------------------------
# Task 3
# ----------------------------------------------------------------------
n_3 = int(input("Enter positive integer: "))
L_3 = sorted([x for x in range(n_3) if x % 2 == 0 and x % 3 == 0] +
             [x for x in range(n_3) if x % 2 == 1 and x % 5 == 0])
print("Output list L_3:", L_3)
# ----------------------------------------------------------------------
# Task 4 - Reverse list using recursion
# ----------------------------------------------------------------------
L_4 = random.sample(range(1, 20), 10)
print("Input list L_4:", L_4)


def reversed_list_recur(array: list) -> list:
    """Returns list in reversed order."""
    if len(array) < 2:
        return array
    return [array[-1]] + reversed_list_recur(array[:-1])


print("Output list L_4:", reversed_list_recur(L_4))
# ----------------------------------------------------------------------
# Task 5 - Fibonacci using recursion
# ----------------------------------------------------------------------
n_5 = int(input("Enter positive integer: "))


def fib(number: int, dictionary: dict):
    if number in dictionary:
        return dictionary[number]
    else:
        ans = fib(number-1, dictionary) + fib(number-2, dictionary)
        dictionary[number] = ans
        return ans


d = {1: 1, 2: 2}
fib_list = [1]
for item in range(1, n_5):
    if fib_list[-1] <= n_5:
        fib_list.append(fib(item, d))

print("Fibonacci sequence:", fib_list[:-1])
