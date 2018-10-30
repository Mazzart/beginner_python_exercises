import random

checker = True

while checker:
    try:
        n = int(input('Enter the length of the list (positive integer): '))
        rand_list = random.sample(range(n * 10), n)
        checker = False
    except ValueError:
        print('Please, try again...')


# Solution 1


def binary_search(array: list, value: int) -> str:
    """Search algorithm that finds the positions of a target value"""
    array.sort()  # binary search works for sorted list
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > value:
            high = mid - 1
        else:
            if array[mid] < value:
                low = mid + 1
            else:
                return f"The number you are looking for is in position {mid} in the list."
    return "Number is not found in the list."


# Solution 2 (is number in list)


def bisect_search(array: list, e: int) -> bool:
    array.sort()  # binary search works for sorted list

    def bisect_search_helper(arr: list, val: int, low: int, high: int) -> bool:
        if high == low:
            return arr[low] == val
        mid = (low + high) // 2
        if arr[mid] == val:
            return True
        elif arr[mid] > val:
            if low == mid:  # nothing left to search
                return False
            else:
                return bisect_search_helper(arr, val, low, mid-1)
        else:
            return bisect_search_helper(arr, val, mid+1, high)

    if len(array) == 0:
        return False
    else:
        return bisect_search_helper(array, e, 0, len(array)-1)
